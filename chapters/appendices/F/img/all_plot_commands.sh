#!/bin/bash

# All plots for thesis
# Run from geno

. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/python3"
PPATH="/home/regruber/g-2/openQxD-devel/01-dev/"

${PYTHON} ${PPATH}/var_vs_x.py -v -N6 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/appendices/F/img/var_vs_pion_mass.pdf \
	-i0 /home/hpcp/rgruber/G8/final 'regular/*_regular.dat' \
	-i1 /home/hpcp/rgruber/G7/final '{str2,str2_run2}/*_regular.dat' \
	-i2 /home/hpcp/rgruber/G8/final/trad '*_L0.dat' \
	-i3 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
	-i4 /home/hpcp/rgruber/G8/final '2lvl/*_L0.dat' \
	-i5 /home/hpcp/rgruber/G7/final '{str2,str2_run2}/*_L0.dat' \
	--times 20 --nsrc 1 -g 0 1 -g 2 3 -g 4 5 \
	--group-names 'Stochastic estimator' 'LMA: L0 (rest-rest + rest-eigen)' 'MG LMA: L0 (fine-grid)' \
	--gauge-variance 0 1 --plot-together 0 1 2 \
	--title '' --plot-titles '' \
	--xlabel 'Pion mass [MeV]' --xticks 180 270 --xticklabels '{tick} (G8)' '{tick} (G7)' \
	-a 0.0658 --ylim 1e-13 1e-8 #--nconfigs 3
