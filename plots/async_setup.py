import math
import textwrap
import os
import shutil
import hashlib

def file_equal(file1, file2):
  return hashlib.md5(open(file1,'rb').read()).hexdigest() == hashlib.md5(open(file2,'rb').read()).hexdigest()

def lattice_equal(s):
  good = True
  for setup in s.setups:
    if "!QUDA_NPROC" in setup:
      N0 = setup['!QUDA_NPROC'][0]*setup['!QUDA_L'][0]
      N1 = setup['!QUDA_NPROC'][1]*setup['!QUDA_L'][1]
      N2 = setup['!QUDA_NPROC'][2]*setup['!QUDA_L'][2]
      N3 = setup['!QUDA_NPROC'][3]*setup['!QUDA_L'][3]

      good = good and s.lattice_size[0] == N0 and s.lattice_size[1] == N1 and s.lattice_size[2] == N2 and s.lattice_size[3] == N3
      good = good and setup['!QUDA_NPROC'][3] == setup['NPROC'][3]

  return good


setup = {
  "work_dir": "__work",
  "templates": [
    {
      "template": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/global.h.template",
      "file": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/global.h",
      "bak": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/global.h.bak",
    },
    {
      "template": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/quda_global.h.template",
      "file": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/quda_global.h",
      "bak": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/include/quda_global.h.bak",
    },
    {
      "template": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/devel/quda/check5.c.template",
      "file": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/devel/quda/check5.c",
      "bak": "/scratch/rgruber/openqxd_quda_build/src/openQxD-devel/devel/quda/check5.c.bak",
    },
  ],
  # "substitute": {
  #   "work": "/scratch/rgruber/openqxd_quda_build/01-work/",
  # },
  "env": {
    "QUDA_REORDER_LOCATION": "CPU",
    "QUDA_DETERMINISTIC_REDUCE": 1, # 1=enabled, 0=disabled
    "QUDA_RESOURCE_PATH": "/tmp/tunecache/{{tune_cache_subdir}}/{{setup_str}}",
  },
  "checks": [
    {
      "test": lattice_equal,
      "fail": lambda s: f"Lattices not compatible!"
    },
  ],
  "runs": [

    {
      "run_name": "quda/gpu/geno/A360/async", # QXD-32-2
      "lattice_size": [64,64,32,32],
      "input_file_template": "/scratch/rgruber/openqxd_quda_build/01-work/input/A360_template.in",
      "sbatch_template": "/scratch/rgruber/openqxd_quda_build/01-work/sbatch/run.sh",
      "setups": [
        #{"NPROC":[1,2,2,2], "!overlap": 0, "!ncalls": 0}, # check3, sync, basecase, done
        #{"NPROC":[1,2,2,2], "overlap": 0, "ncalls": 432}, # check5, sleep, done
        {"NPROC":[1,2,2,2], "overlap": 1, "ncalls": 79}, # check5, pure IO
        {"NPROC":[1,2,2,2], "overlap": 2, "ncalls": 10}, # check5, MPI+IO
        {"NPROC":[1,2,2,2], "overlap": 3, "ncalls": 126}, # check5, Dop
        {"NPROC":[1,2,2,2], "overlap": 4, "ncalls": 623055}, # check5, allreduce
        {"NPROC":[1,2,2,2], "overlap": 5, "ncalls": 6812}, # check5, pure MEM
      ],
      "progs": [
        #"../openqxd_quda_build/src/openQxD-devel/devel/quda/check3",
        "../openqxd_quda_build/src/openQxD-devel/devel/quda/check5",
      ],
      "substitute": {
        "NPROC_BLK0":1,"NPROC_BLK1":1,"NPROC_BLK2":1,"NPROC_BLK3":1,
        "QUDA_NPROC0":"NPROC0","QUDA_NPROC1":"NPROC1","QUDA_NPROC2":"NPROC2","QUDA_NPROC3":"NPROC3",
        "QUDA_L0":"L0","QUDA_L1":"L1","QUDA_L2":"L2","QUDA_L3":"L3",
        "ninversions": 10, #TODO: set appropriately
        "log_dir": "/home/hpcp/rgruber/thesis/perf/new/test/{{run_name}}/{{setup_str}}", #TODO
        "log_file": "{{log_dir}}/64x32b3.24a0.05ku0.135560kds0.134617kc0.129583r001.{{binary}}.log", # TODO: set to run name
        #"tune_cache_subdir": "A360",
      },
      "env": {
        "QUDA_ENABLE_TUNING": 1, # TODO: 0=disable, 1=enable tuning
        "QUDA_DETERMINISTIC_REDUCE": 1, # enables MPI_Gather instead of MPI_Allreduce
        "QUDA_RESOURCE_PATH": "/tmp/tunecache/A360/NPROC1x2x2x2/",
      },
      "cleanup": False,
      "build_cmd": "make -j {{binary}}",
      "cmd": "sh {{sbfile}}",
    },

  ]
}
