from scaling_plot import extract
import numpy as np
import math


nproc = lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) process grid', (1,2,3,4), lambda x: np.prod(list(map(int, x))))
lvol = lambda r: extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) lattice,', (1,2,3,4), lambda x: np.prod(list(map(int, x))))

def nproc_divided_by(ranks_per_node):
  return lambda r: math.ceil(nproc(r)/ranks_per_node)

def ignore_first(x):
  return np.mean(x[1:])

def time_per_rhs(r):
  time = extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction = lambda x: x[1:])
  N_rhs = extract(r.file, r'\((\d+) RHS\'\)', 1, reduction = lambda x: x[0])
  #print(f"{time = }")
  #print(f"{N_rhs = }")
  return time/N_rhs


plots = [

  {
    "active": False,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_dw_strong_old.pdf",
    "name": "CSCS Alps system (GH200) Dirac operator, avg over 10k applications, NVSHMEM=off",
    "properties": {"xlabel": "Nodes"},
    "todo": "5 indep runs",
    "lines": [
      {
        "plot_args": {"label": "GPU periodic GDR=off", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/strong/128x64x64x64/*gdr0*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },

      {
        "plot_args": {"label": "GPU periodic GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/strong/128x64x64x64/*gdr1*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },

      {
        "plot_args": {"label": "GPU C* GDR=off", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/strong/128x128x64x64/*gdr0*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },

      {
        "plot_args": {"label": "GPU C* GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/strong/128x128x64x64/*gdr1*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },

    ]
  },

  {
    "active": False,
    "scaling": 1, # weak
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_dw_weak_old.pdf",
    "name": "CSCS Alps system (GH200) Dirac operator, avg over 10k applications, NVSHMEM=off",
    "todo": "5 indep runs",
    "properties": [
      {"xlabel": "Nodes"},
      {"xlabel": "Nodes"}
    ],
    "lines": [

      {
        "plot_args": {"label": "GPU periodic GDR=off", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/*gdr0*/*run*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

      {
        "plot_args": {"label": "GPU periodic GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/*gdr1*/*run*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
          "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

      {
        "plot_args": {"label": "GPU cstar GDR=off", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/weak/be128x128x128x64/*gdr0*/*run*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

      {
        "plot_args": {"label": "GPU cstar GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/weak/be128x128x128x64/*gdr1*/*run*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
          "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

    ]
  },

  {
    "active": False, # still running on Daint
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_dw_strong.pdf",
    "name": "CSCS Alps system (GH200) Dirac operator, NVSHMEM=off",
    "properties": {"xlabel": "Nodes"},
    #"todo": "all fine with this plot!",
    "lines": [
      # {
      #   "plot_args": {"label": "GPU periodic GDR=off", "alpha": 1, "fmt": ""},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/strong/128x64x64x64/*gdr0*/r*/*.log",
      #   "x": nproc_divided_by(4),
      #   "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
      #   "extract": {
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #   },
      # },
      {
        "plot_args": {"label": "GPU periodic GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/strong/128x64x64x64/*gdr1*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },
      # {
      #   "plot_args": {"label": "GPU C* GDR=off", "alpha": 1, "fmt": ""},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/strong/128x128x64x64/*gdr0*/r*/*.log",
      #   "x": nproc_divided_by(4),
      #   "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
      #   "extract": {
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #   },
      # },
      {
        "plot_args": {"label": "GPU C* GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/strong/128x128x64x64/*gdr1*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
        },
      },
      {
        "plot_args": {"label": "CPU C* (256 ranks per node)", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/openqxd/cpu/todi/Dop/cstar/strong/*/*.log",
        "x": nproc_divided_by(256),
        "time": lambda r: extract(r.file, r'Time per lattice point for Dw_dble\(\):\n+([\d\.e\+\-]+) micro sec', 1, np.float64)*extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) local lattice', (1,2,3,4), lambda x: np.prod(list(map(int, x))))/1.0e6,
      },
    ]
  },

  {
    "active": False,
    "scaling": 1, # weak
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_dw_weak.pdf",
    "name": "CSCS Alps system (GH200) Dirac operator, NVSHMEM=off",
    #"todo": "outliers, +10 runs on daint >=32 nodes",
    "properties": [
      {"xlabel": "Nodes", "ylim": [-0.05, 1.05]},
      {"xlabel": "Nodes"}
    ],
    "lines": [

      # {
      #   "plot_args": {"label": "GPU periodic GDR=off", "alpha": 1, "fmt": ""},
      #   #"glob": "/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/*gdr0*/r*/*.log",
      #   "glob": "/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/{NPROC{4,2}x{4,2}x{2,1}x{2,1}_*_ngpu10000,*64}_gdr0/r*/*.log",
      #   "x": nproc_divided_by(4),
      #   "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
      #   "extract": {
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
      #     "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
      #   },
      # },

      {
        "plot_args": {"label": "GPU periodic GDR=on", "alpha": 1, "fmt": ""},
        #"glob": "/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/*gdr1*/r*/*.log",
        "glob": "/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/periodic/weak/b128x64x64x64/{NPROC{4,2}x{4,2}x{2,1}x{2,1}_*_ngpu10000,*64}_gdr1/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
          "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

      # {
      #   "plot_args": {"label": "GPU cstar GDR=off", "alpha": 1, "fmt": ""},
      #   "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/weak/be128x128x128x64/*gdr0*/r*/*.log",
      #   "x": nproc_divided_by(4),
      #   "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
      #   "extract": {
      #     "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
      #     "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
      #     "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
      #   },
      # },

      {
        "plot_args": {"label": "GPU cstar GDR=on", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/Dop/cstar/weak/be128x128x128x64/*gdr1*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'openQCD_qudaDw_NoLoads\(...\)\:\s+([\d\.e\+\-]+) sec \((\d+) times', (1,2), reduction = lambda x: x[0][0]/x[0][1]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "random_ud": lambda r: extract(r.file, r'random_ud\(...\)\: ([\d\.e\+\-]+) sec', 1),
          "Dw_dble": lambda r: extract(r.file, r'Dw_dble\(mu\, ...\)\: ([\d\.e\+\-]+) sec', 1),
        },
      },

      {
        "plot_args": {"label": "CPU cstar (256 rank per node)", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/openqxd/cpu/todi/Dop/cstar/weak/*/*.log",
        "x": nproc_divided_by(256),
        "time": lambda r: extract(r.file, r'Time per lattice point for Dw_dble\(\):\n+([\d\.e\+\-]+) micro sec', 1, np.float64)*extract(r.file, r'(\d+)x(\d+)x(\d+)x(\d+) local lattice', (1,2,3,4), lambda x: np.prod(list(map(int, x))))/1.0e6,
      },

    ]
  },

  {
    "active": True,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_inv_strong.pdf",
    "name": "CSCS Alps system (GH200) Solver, NVSHMEM=off, GDR=on",
    "properties": {"xlabel": "Nodes"},
    #"todo": "all fine with this plot!",
    "lines": [
      {
        "plot_args": {"label": "G8", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/G8/solver/strong/*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:5]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:5]),
        },
      },
      {
        "plot_args": {"label": "D300", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300/solver/strong/*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:5]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:5]),
        },
      },
      {
        "plot_args": {"label": "D300x16", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300x16/solver/strong/*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:5]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:5]),
        },
      },
    ]
  },

  {
    "active": False,
    "scaling": 1, # weak
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_inv_weak_mrhs.pdf",
    "name": "CSCS Alps system (GH200) Solver, NVSHMEM=off, GDR=on",
    "properties": [
      {"xlabel": "Nodes/Nrhs"},
      {"xlabel": "Nodes/Nrhs"},
    ],
    "todo": "weak/strong? mg_mrhs_list=16",
    "lines": [
      {
        "plot_args": {"label": "G8", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/G8/solver/weak_mrhs/*/r*/*.log",
        "x": nproc_divided_by(4),
        #"time": time_per_rhs,
        "time": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:]),
        },
      },

      {
        "plot_args": {"label": "D300", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300/solver/weak_mrhs/*/r*/*.log",
        "x": nproc_divided_by(4),
        #"time": time_per_rhs,
        "time": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+secs\s+\= ([\d\.e\+\-]+)', 1, reduction=lambda x: x[1:]),
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:]),
        },
      },

    ]
  },

  {
    "active": True,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/daint_alps_inv_strong_mrhs.pdf",
    "name": "CSCS Alps system (GH200) Solver, NVSHMEM=off, GDR=on",
    "properties": [
      {"ylabel": "Speedup per RHS", "xlabel": "Nodes/Nrhs"},
      {"ylabel": "Average time per RHS [s]", "xlabel": "Nodes/Nrhs"},
    ],
    "todo": "weak/strong? mg_mrhs_list=16",
    "lines": [

      {
        "plot_args": {"label": "G8", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/G8/solver/weak_mrhs/*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": time_per_rhs,
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:]),
        },
      },

      {
        "plot_args": {"label": "D300", "alpha": 1, "fmt": ""},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300/solver/weak_mrhs/*/r*/*.log",
        "x": nproc_divided_by(4),
        "time": time_per_rhs,
        "extract": {
          "GPU memory usage": lambda r: extract(r.file, r'QUDA \(rank\=0\)\: Device memory used = ([\d\.e\+\-]+) MiB', 1),
          "Iteration count": lambda r: extract(r.file, r'QUDA \(rank\=0\)\:\s+iter\s+= (\d+)', 1, reduction=lambda x: x[1:]),
        },
      },

    ]
  },

]