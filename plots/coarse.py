from plot_metrics import extract
import numpy as np


def dim_Dw(lvol, Nc=3, Ns=4, Nrhs=1):
  return lvol*Nc*Ns

def dim_Aw(cvol, Nc=3, Ns=4, Nrhs=1):
  return dim_Dw(cvol, Nc, Ns)

def mem_fine_spinor(lvol, Nc=3, Ns=4, Nrhs=1, ibytes=16):
  return dim_Dw(lvol, Nc, Ns)*ibytes

def mem_coarse_spinor(cvol, Nc=3, Ns=4, Nrhs=1, ibytes=16):
  return dim_Aw(cvol, Nc, Ns)*ibytes

def mem_Dw(L, gauge=1, clover=1, D=4, Nc=3, Ns=4, Nrhs=1, ibytes=16):
  return ((gauge+clover)*np.prod(L)*D*Nc*Nc*ibytes + Nrhs*4*mem_fine_spinor(np.prod(L), Nc, Ns, ibytes))/(1024*1024*1024)

def mem_Aw(cvol, D=4, Nc=3, Ns=4, Nrhs=1, ibytes=16):
  return ((2*D+1)*cvol*Nc*Nc*Ns*Ns*ibytes + Nrhs*4*mem_coarse_spinor(cvol, Nc, Ns, ibytes))/(1024*1024*1024)

def coarse(r):
  Nc = extract(r.file, r'\[lma_new\] lma\(0\)\.Ns = (\d+)', 1, mapping=int)[0]/2
  NPROC = extract(r.file, r'\[lma_new\] NPROC = (\d+)', 1, mapping=int)[0]
  nb = extract(r.file, r'\[lma_new\] lma\((\d+)\).nb = (\d+)', (1,2), mapping=int)
  return [ mem_Aw(NPROC*nb[0][1], Nc=Nc, Ns=2), mem_Aw(NPROC*nb[1][1], Nc=Nc, Ns=2), mem_Aw(1, Nc=Nc, Ns=2) ]


plots = [
  {
    "active": True,
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/07-numerics/img/coarse_condition.pdf",
    #"name": "Solvers",
    "figsize": (6.0, 5.0),
    "subplots_adjust": {
      "bottom": 0.15,
      "left": 0.15,
    },
    "ax": ["ax.tick_params(axis='both', labelsize=14)"],
    "legend": {"fontsize": 14},
    "properties": {
      "xlabel": r'$\mathbb{C}$-dimension of Dirac operator',
      "xaxis.label.fontsize": 16,
      "yaxis.label.fontsize": 16,
      "yscale": "log",
      "xscale": "log",
      "position": [0.15, 0.1, 0.8, 0.85],
      #"xticks": [100, 819200, 13107200, 402653184],
      #"xticklabels": ["LMA", r"MG: $8^4$", r"MG: $4^4$", "Fine-grid"],
    },
    "lines": [
      {
        "active": True,
        "plot_args": {"label": "G7 - Condition number", "fmt": "-x", "linewidth": 1.5, "alpha": 1},
        "glob": f"/home/hpcp/rgruber/G7/cond/*/*.log", # where are the log files?
        "x": [
          lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) lattice', (1,2,3,4), mapping=int, grp_reduce=lambda x: 12*np.prod(x)),
          lambda r: extract(r.file, r'lma\((\d+)\)\.dim = (\d+)', 2, mapping=int),
        ],
        "y": [
          lambda r: [extract(r.file, r'\n Est\. highest magitude EV = ([\d\.e\+\-]+) ', 1, mapping=np.float64, file_reduce=lambda x: [x[0]])[0]/extract(r.file, r'k =  0, \|D\*psi\|/\|psi\| = ([\d\.e\+\-]+), ', 1, mapping=np.float64, file_reduce=lambda x: [x[0]])[0]],
          lambda r: extract(r.file, r'\[L(\d+)\]  Est\. condition number\s+= ([\d\.e\+\-]+)', 2, mapping=np.float64),
        ],
      },
      {
        "plot_args": {"label": "G7 - BICGSTAB #iteration steps", "fmt": "-+", "linewidth": 1.5, "alpha": 1},
        # "model": {
        #   "function": lambda x, k, n: k*x**n,
        #   "plot_args": {"label": r"model $f(x) = k x^n$"},
        # },
        "glob": f"/home/hpcp/rgruber/G7/time/NPROC8x8x8x8_nconfig*/time2.log", # where are the log files?
        "x": [
          lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) lattice', (1,2,3,4), mapping=int, grp_reduce=lambda x: 12*np.prod(x)),
          lambda r: extract(r.file, r'lma\((\d+)\)\.dim = (\d+)', 2, mapping=int),
        ],
        "y": [
          lambda r: extract(r.file, r'time2\.bicgstab\(level\=(\d+)\)\.status\.avg\s+= ([\d\.e\+\-]+)', 2, mapping=np.float64),
        ],
      },
    ]
  },

  {
    "active": True,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/07-numerics/img/coarse_tts_vs_memory.pdf",
    "figsize": (6.0, 5.0),
    "subplots_adjust": {
      "bottom": 0.15,
      "left": 0.15,
    },
    "ax": ["ax.tick_params(axis='both', labelsize=14)"],
    "legend": {"fontsize": 14},
    "properties": {
      "xlabel": "Dirac operator size in memory [GB]",
      "xaxis.label.fontsize": 16,
      "yaxis.label.fontsize": 16,
      "ylabel": "time [sec]",
      "position": [0.15, 0.1, 0.8, 0.85],
    },
    "lines": [
      {
        "plot_args": {"label": "G7 - Dirac operators", "marker": "x", "linewidth": 1.5, "alpha": 1},
        "model": {
          "function": lambda x, a: a*x,
          "plot_args": {"label": r"Fit $f(x) = a x$", "marker": "", "linewidth": 1.5, "alpha": 1},
        },
        "glob": f"/home/hpcp/rgruber/G7/time/NPROC8x8x8x8_nconfig*/time1.log", # where are the log files?
        "x": [
          lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) lattice', (1,2,3,4), mapping=int, grp_reduce=mem_Dw),
          lambda r: coarse(r),
        ],
        "y": [
          lambda r: extract(r.file, r'lma\(0\)\.stats\.Dop\.time\.avg    = ([\d\.e\+\-]+) sec', 1, mapping=np.float64),
          lambda r: extract(r.file, r'lma\((\d+)\)\.stats\.Aop\.time\.avg    = ([\d\.e\+\-]+) sec', 2, mapping=np.float64),
        ],
      },
    ]
  },

]