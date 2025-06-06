from scaling_plot import extract
import numpy as np
import math


nproc = lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) process grid', (1,2,3,4), lambda x: np.prod(list(map(int, x))))
lvol = lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) lattice,', (1,2,3,4), lambda x: np.prod(list(map(int, x))))

def nproc_divided_by(ranks_per_node):
  return lambda r: math.ceil(nproc(r)/ranks_per_node)

def ignore_first(x):
  return np.mean(x[1:])

plots = [

  {
    "active": True,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img//todi_inv_strong2.pdf",
    "name": "CSCS Alps testing system (GH200) multigrid GDR=off, NVSHMEM=off",
    "properties": {"xlabel": "GPUs"},
    "lines": [
      {
        "plot_args": {"label": "C380", "alpha": 1},
        "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/quda/gpu/todi/C380/test/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
        "x": nproc_divided_by(1),
        "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
        "extract": {
          "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
          "Gflops": lambda r: extract(r.file, r'QUDA \(rank=0\):   gflops      = ([\d\.e\+\-]+)', 1, reduction=lambda x: x),
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
        },
      },
      {
        "plot_args": {"label": "G8", "alpha": 1},
        "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/quda/gpu/todi/G8/test/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
        "x": nproc_divided_by(1),
        "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
        "extract": {
          "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
          "Gflops": lambda r: extract(r.file, r'QUDA \(rank=0\):   gflops      = ([\d\.e\+\-]+)', 1, reduction=lambda x: x),
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
        },
      },
      {
        "plot_args": {"label": "D300", "alpha": 1},
        "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/benchmarks/quda/gpu/todi/D300/strong/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
        "x": nproc_divided_by(1),
        "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
        "extract": {
          "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
          "Gflops": lambda r: extract(r.file, r'QUDA \(rank=0\):   gflops      = ([\d\.e\+\-]+)', 1, reduction=lambda x: x),
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
        },
      },
      # {
      #   "plot_args": {"label": "B400", "alpha": 1},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/benchmarks/quda/gpu/todi/B400/strong/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
      #   "x": nproc_divided_by(1),
      #   "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
      #   "extract": {
      #     "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
      #   },
      # },

      # {
      #   "plot_args": {"label": "A400a00b324", "alpha": 1},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/benchmarks/quda/gpu/todi/A400a00b324/strong/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
      #   "x": nproc_divided_by(1),
      #   "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
      #   "extract": {
      #     "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
      #   },
      # },
      # {
      #   "plot_args": {"label": "D400a00b324/", "alpha": 1},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/benchmarks/quda/gpu/todi/D400a00b324//strong/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
      #   "x": nproc_divided_by(1),
      #   "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
      #   "extract": {
      #     "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
      #   },
      # },
      # {
      #   "plot_args": {"label": "D400a00b343//", "alpha": 1},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/old/log/benchmarks/quda/gpu/todi/D400a00b343///strong/*_GDR0_NVSHMEM0/*check3*.log", # where are the log files?
      #   "x": nproc_divided_by(1),
      #   "time": lambda r: extract(r.file, r'QUDA \(rank=0\):   secs        = ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
      #   "extract": {
      #     "iteration count": lambda r: extract(r.file, r'QUDA \(rank=0\):   iter        = (\d+)', 1, reduction=lambda x: x),
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     #"tuning": lambda r: extract(r.file, r'Tuned block', 0, mapping = str, reduction = lambda x: x.size),
      #   },
      # },
    ]
  },

]
