from plot_metrics import extract, mean_sem
import numpy as np
import re

def ncalls(r):
  secs = extract(r.file, r'QUDA \(rank=0\):\s+secs\s+= ([\d\.e\+\-]+)', 1, mapping=np.float64)
  return len(secs)

def nrhs(r):
  return extract(r.file, r'\_nrhs(\d+)\/check3[\_,\.]', 1, mapping=int, file_reduce=lambda x: [x[0]]*ncalls(r))

def time(r):
  return extract(r.file, r'QUDA \(rank=0\):\s+secs\s+= ([\d\.e\+\-]+)', 1, mapping=np.float64)

def time_per_rhs(r):
  nr = nrhs(r)[0]
  return [t/nr for t in time(r)]

def gpu_energy(r):
  pre_solv = extract(r.file, r'pre_solv\(j=(\d+)\): /sys/cray/pm_counters/accel0_energy: (\d+) J', 2, mapping=np.float64)
  post_solv = extract(r.file, r'post_solv\(j=(\d+)\): /sys/cray/pm_counters/accel0_energy: (\d+) J', 2, mapping=np.float64)
  return np.array(post_solv) - np.array(pre_solv)

def node_energy(r):
  pre_solv = extract(r.file, r'pre_solv\(j=(\d+)\): /sys/cray/pm_counters/energy: (\d+) J', 2, mapping=np.float64)
  post_solv = extract(r.file, r'post_solv\(j=(\d+)\): /sys/cray/pm_counters/energy: (\d+) J', 2, mapping=np.float64)
  return np.array(post_solv) - np.array(pre_solv)

  # pre  = extract(r.file, r'init: /sys/cray/pm_counters/energy: (\d+) J', 1, mapping=np.float64)
  # post = extract(r.file, r'finalize: /sys/cray/pm_counters/energy: (\d+) J', 1, mapping=np.float64)
  # return np.array(post) - np.array(pre)

def node_energy_per_rhs_per_gpu(r):
  nr = nrhs(r)[0]
  return [x/(4*nr) for x in node_energy(r)]

def node_energy_per_rhs(r):
  nr = nrhs(r)[0]
  return [x/(4*nr) for x in node_energy(r)]

def gpu_energy_per_rhs(r):
  nr = nrhs(r)[0]
  return [x/(4*nr) for x in gpu_energy(r)]

def gpu_power(r):
  nr = nrhs(r)[0]
  return [e/(1000*t) for e,t in zip(gpu_energy(r), time(r))]

def node_power(r):
  nr = nrhs(r)[0]
  return [e/(1000*t) for e,t in zip(node_energy(r), time(r))]

def speedup(d):
  first = next(iter(d))
  first_v = d.get(first, 1.0)
  return {k:first_v/v for k,v in d.items()}

def non_zero(f, sub_f=None):
  def g(r):
    fr = np.array(f(r))
    sub_fr = np.array(fr if sub_f is None else sub_f(r))
    return fr[sub_fr.astype(bool)]
  return g

plots = [
  {
    "active": True,
    "hostname": ["geno"],
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/mrhs_tts.pdf",
    "properties": {
      "xlabel": r"Number of RHS'",
      "ylabel": "Speedup",
      "xlim": [0, 33],
      #"xticks": [1, 2, 4, 8, 12, 16, 24, 32],
      #"yscale": "log",
    },
    "lines": [
      {
        "plot_args": {"label": "D300 (16 GH200 nodes)", "marker": "x", "linewidth": 1.5, "alpha": 1},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300/mrhs/*_nrhs*/*.check3.log",
        "x": [nrhs],
        "y": [time_per_rhs],
        "postprocess": speedup,
      },
      {
        "plot_args": {"label": "A400 (2 GH200 nodes)", "marker": "x", "linewidth": 1.5, "alpha": 1},
        "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/A400/mrhs/*_nrhs*/*.check3.log",
        "x": [nrhs],
        "y": [time_per_rhs],
        "postprocess": speedup,
      },
    ]
  },

  {
    "active": True,
    "hostname": ["geno"],
    "name": "A400 (2 GH200 nodes)",
    "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/mrhs_energy.pdf",
    "properties": [
      {"xlabel": r"Number of RHS'", "ylabel": "Energy/Node/RHS [Joule]"},
      {"ylabel": "Power [KW]"},
    ],
    "lines": [
      {
        "plot_args": {"label": "Energy", "color": "tab:blue", "marker": "x", "linewidth": 1.5, "alpha": 1},
        "glob": r"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/A400/mrhs_energy/*/*/*.log",
        "x": [non_zero(nrhs, node_energy_per_rhs)],
        "y": [non_zero(node_energy_per_rhs)],
      },
      {
        "axis": "twinx",
        "plot_args": {"label": "Power/Node", "color": "tab:orange", "marker": "x", "linewidth": 1.5, "alpha": 1},
        "glob": r"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/A400/mrhs_energy/*/*/*.log",
        "x": [non_zero(nrhs, node_power)],
        "y": [non_zero(node_power)],
      },
    ]
  },

  # {
  #   "active": True,
  #   "hostname": ["geno"],
  #   "filename": "/scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-1/08-performance/img/mrhs_gflops.pdf",
  #   "properties": {
  #     "xlabel": "Number of RHS",
  #     "ylabel": "TFLOPS",
  #     "xlim": [0,17],
  #     "xticks": np.arange(1, 17).tolist(),
  #   },
  #   "lines": [
  #     {
  #       "plot_args": {"label": "D300", "marker": "x", "linewidth": 1.5, "alpha": 1},
  #       "glob": f"/home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/D300/mrhs/*_nrhs*/*.check3.log",
  #       "x": [nrhs],
  #       "y": [
  #         lambda r: extract(r.file, r'QUDA \(rank=0\):\s+gflops\s+= ([\d\.e\+\-]+)', 1,
  #           mapping=lambda x: np.float64(x)/1000)
  #         ],
  #     },
  #   ]
  # },

]