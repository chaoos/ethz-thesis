#!/bin/bash

# All plots for thesis
# Run from geno

. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/python3"
PPATH="/home/regruber/g-2/openQxD-devel/01-dev/"

${PYTHON} ${PPATH}/corr_var.py -v -N5 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/07-chirality/img/chirality.pdf \
	-i0 /home/hpcp/rgruber/F7/final '{regular,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/F7/2nd_run/Ns50 '*_rem2.dat' \
	-i2 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
	-i3 /home/hpcp/rgruber/F7/2nd_run/Ns50_B6x6x6x6 '*_rem2.dat' \
	-i4 /home/hpcp/rgruber/F7/final 'str2_run2/*_L0.dat' \
	--plot-together 0 1 2 --plot-together 0 3 4 \
	--plot-titles 'LMA' '2-level MG LMA' \
	--names 'Stochastic estimator' 'L0: $i=1 \; (N_s=1)$' 'L0: $i=3 \; (N_s=2)$' 'L0: $i=1 \; (N_s=1)$' 'L0: $i=3 \; (N_s=2)$' \
	-a 0.0658 --nsrc 1 --ylim 1e-15 1e-6 #--nconfigs 3

