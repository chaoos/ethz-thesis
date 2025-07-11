#!/bin/bash

# All plots for thesis
# Run from geno

#. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/scratch/rgruber/67bc5d6d049e882b8a262db6/myvenv/bin/python3"
PPATH="/scratch/rgruber/67bc5d6d049e882b8a262db6/"


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 1 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-26T22:22:22.log \
	-c0 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T18:26:32.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/both/fine_wf.pdf \
	--names "{type} free Wilson" --labels "Numerical range" "Spectral hull" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 1 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-25T02:27:37.log \
	-c0 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T11\:57\:27.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/both/fine_w.pdf \
	--names "{type} Wilson" --labels "Numerical range" "Spectral hull" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 1 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-c0 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull.*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/both/fine_wc.pdf \
	--names "{type} Wilson-Clover" --labels "Numerical range" "Spectral hull" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 3 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-25T02:27:37.log \
	-c0 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T11\:57\:27.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-c1 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull.*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-26T22:22:22.log \
	-c2 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T18:26:32.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/both/fine_wf.pdf \
	-o ${PPATH}/chapters/part-2/07-chirality/img/both/fine.pdf \
	--names "{type} Wilson" "{type} Wilson-Clover" "{type} free Wilson" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes yes yes

