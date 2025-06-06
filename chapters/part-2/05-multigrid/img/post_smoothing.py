#!/usr/bin/env python3

import matplotlib.pyplot as plt
import os
import sys
import numpy as np
import math 
from scipy.ndimage import gaussian_filter1d
from pathlib import Path

rpath = "../../../../preamble/colors.py"
apath = os.path.abspath(f"{os.path.dirname(__file__)}/{rpath}")
sys.path.append(os.path.dirname(apath))
import colors as col

def smooth(X):
  return np.sin(X)

def smoothed_staircase_sin(x, xmax=2*math.pi, bins=10, alpha=0.5):
    step = xmax/bins

    x = np.asarray(x)
    y = smooth(x)

    step_indices = np.floor(x / step)
    midpoints = (step_indices + 0.5) * step
    step_values = np.sin(midpoints)

    Y = (1 - alpha) * step_values + alpha * y
    Y[0] = smooth(x[0])
    Y[-1] = smooth(x[-1])

    return Y

def sine_with_sharpness(x, alpha=0.0, steps=10):
    # Validate alpha parameter.
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be between 0 and 1 (inclusive)")
    
    sin_val = math.sin(x)
    
    # Normalize phase to [0, 1) over a period of 2π.
    phase = (x % (2 * math.pi)) / (2 * math.pi)
    
    if alpha == 1.0:
      # Hard staircase: quantize phase and compute sine exactly at the quantized phase.
      quant_phase = round(phase * steps) / steps
      stair_val = math.sin(quant_phase * 2 * math.pi)
      return stair_val
    else:
      # For 0 < alpha < 1, create a soft staircase using a sigmoid transition.
      scaled_phase = phase * steps
      i = math.floor(scaled_phase)
      t = scaled_phase - i  # fractional part in [0, 1)
      
      # Define the sigmoid's steepness k.
      # When alpha is small the transition is very smooth (small k),
      # and as alpha increases it approaches a hard step.
      k = 5 + 20 * alpha
      
      # Compute a sigmoid (logistic) interpolation weight.
      smooth_t = 1 / (1 + math.exp(-k * (t - 0.5)))
      
      # Compute the quantized angles at lower and upper bins.
      lower_phase = (i % steps) / steps
      upper_phase = (((i + 1) % steps)) / steps
      lower_angle = lower_phase * 2 * math.pi
      upper_angle = upper_phase * 2 * math.pi
      
      # Sine values at the bin boundaries.
      sin_lower = math.sin(lower_angle)
      sin_upper = math.sin(upper_angle)
      
      # Soft staircase value: smoothly interpolated sine value between the two bins.
      soft_stair_val = (1 - smooth_t) * sin_lower + smooth_t * sin_upper
      
      # Blend between the smooth sine and the soft staircase version.
      return (1 - alpha) * sin_val + alpha * soft_stair_val

def smoothen(sharp, sigma=12):
  smoothened = gaussian_filter1d(sharp, sigma)
  return smoothened

def main():
  xmax = 2*math.pi
  X = np.linspace(-1, xmax+1, num=1000)

  fig, axes = plt.subplots(1, 2, sharey=True, figsize=(11, 5))

  Y_smooth = smooth(X)
  Y_sharp = smoothed_staircase_sin(X, alpha=0)
  Y_conv = smoothen(Y_sharp)

  axes[0].plot(X, Y_smooth, '--', color="mygray", label="alpha=0")
  axes[0].plot(X, Y_sharp, '-', color="plot0", label="alpha=1")
  axes[1].plot(X, Y_smooth, '--', color="mygray", label="alpha=0")
  axes[1].plot(X, Y_conv, '-', color="plot1", label="alpha=0.85")

  for ax in axes:
    ax.axhline(y=0, linewidth=0.75, color='k')
    ax.set_xticks(np.linspace(0, 1, num=11)*xmax)
    ax.set_xticklabels([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    ax.set_xlim(0, xmax)
    ax.set_xlabel(r"$x/L$")
  
  axes[0].set_ylabel(r"$\psi(x)$")

  #for ax, t in zip(axes, ["a)", "b)", "c)"]):
  #  ax.title.set_text(t)

  plt.yticks([-1, 0, 1], labels=[])
  filename = Path(__file__)
  outfile = filename.with_suffix('.pdf')
  print(f"{outfile = }")
  plt.savefig(outfile)

if __name__ == '__main__':
  main()
