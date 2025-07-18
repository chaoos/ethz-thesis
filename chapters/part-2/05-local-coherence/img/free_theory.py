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
import colors

def mom_space(X, Gamma=1, midpoint=0):
  return np.exp(-((X-midpoint)/Gamma)**2)/(np.abs(Gamma)*np.sqrt(math.pi))
  #return 1/((X-midpoint)**2 + Gamma**2)

def pos_space(X, Gamma=1, midpoint=0):
  return np.exp(-((X-midpoint)/Gamma)**2)/(np.abs(Gamma)*np.sqrt(math.pi))
  #return np.exp(-Gamma*np.abs(X-midpoint))*np.exp(1j*midpoint*X)

def staircase(X, xmax=1, bins=10, Gamma=1):
  step = (2*xmax)/bins
  step_indices = np.floor(X/step)
  midpoints = (step_indices + 0.5)*step
  Y = pos_space(midpoints, Gamma=Gamma)
  Y[0] = pos_space(X[0], Gamma=Gamma)
  Y[-1] = pos_space(X[-1], Gamma=Gamma)
  return Y

def main():
  xmax = 1
  X = np.linspace(-xmax, xmax, num=1000)

  fig, axes = plt.subplots(1, 3, figsize=(15, 5))

  Y_mom = mom_space(X, Gamma=0.05)
  #Y_pos = pos_space(X)
  Y_pos = staircase(X, bins=64, Gamma=2)
  Y_stc = staircase(X, bins=8, Gamma=2)

  axes[0].plot(X, Y_mom, '-', color="plot0", label="momentum")
  axes[1].plot(X, Y_pos, '-', color="plot1", label=r"$L_{\mu}=64$")
  axes[2].plot(X, Y_stc, '-', color="plot2", label=r"$b_{\mu}=8$")

  #for g in [2, 3, 4, 5]:
  #  axes[1].plot(X, staircase(X, bins=64, Gamma=g), '-', label=f"{g = }")
  #  axes[2].plot(X, staircase(X, bins=8, Gamma=g), '-', label=f"{g = }")

  for ax in axes:
    ax.axhline(y=0, linewidth=0.75, color='k')
    ax.set_xlim(-xmax, xmax)

  kwargs = {
    "fontsize": "xx-large",
  }

  axes[0].set_xticks([-1, 1]*xmax)
  axes[0].set_xticklabels([r"$-\pi/a$", r"$\pi/a$"], **kwargs)
  axes[0].set_xlabel(r"$p$", **kwargs)
  axes[0].set_ylabel(r"$\psi(p)$", **kwargs)

  axes[1].set_xticks([-1, 1]*xmax)
  axes[1].set_xticklabels([r"$-L_{\mu} a/2$", r"$L_{\mu} a/2$"], **kwargs)
  axes[1].set_xlabel(r"$x$", **kwargs)
  axes[1].set_ylabel(r"$\psi(x)$", **kwargs)
  axes[1].set_ylim(0, 2*max(Y_pos))
  axes[1].legend(**kwargs)

  axes[2].set_xticks([-1, 1]*xmax)
  axes[2].set_xticklabels([r"$-L_{\mu} a/2$", r"$L_{\mu} a/2$"], **kwargs)
  axes[2].set_xlabel(r"$x$", **kwargs)
  axes[2].set_ylabel(r"$\psi(x)$", **kwargs)
  axes[2].set_ylim(0, 2*max(Y_pos))
  axes[2].legend(**kwargs)

  for ax, t in zip(axes, ["a)", "b)", "c)"]):
    ax.title.set_text(t)
    ax.title.set_fontsize(20)
    ax.set_yticks([])

  plt.tight_layout()

  outfile = Path(__file__).with_suffix('.pdf')
  print(f"{outfile = }")
  plt.savefig(outfile)

if __name__ == '__main__':
  main()
