#!/bin/bash

# All plots for thesis
# Run from geno

. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/python3"
PPATH="/home/regruber/g-2/openQxD-devel/01-dev/"

${PYTHON} ${PPATH}/corr_var.py -v -N5 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/08-chirality/img/chirality.pdf \
	-i0 /home/hpcp/rgruber/F7/final '{regular,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/F7/2nd_run/Ns50 '*_rem2.dat' \
	-i2 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
	-i3 /home/hpcp/rgruber/F7/2nd_run/Ns50_B6x6x6x6 '*_rem2.dat' \
	-i4 /home/hpcp/rgruber/F7/final 'str2_run2/*_L0.dat' \
	--plot-together 0 1 2 --plot-together 0 3 4 \
	--plot-titles 'LMA' '2-level MG LMA' \
	--names 'Stochastic estimator' \
	        'L0: $N_s=1$, case (1)' \
	        'L0: $N_s=2$, case (2sc)' \
	        'L0: $N_s=1$, case (1)' \
	        'L0: $N_s=2$, case (2sc)' \
	-a 0.0658 --nsrc 1 --ylim 1e-15 1e-6 #--nconfigs 3

${PYTHON} ${PPATH}/plot_eigenvalues.py -v --Nc 20 \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/08-chirality/img/eigenvalues_Nc20.pdf \
	-i ${PPATH}/log/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_eigen_g5D_20241010_18:05.log \
	   ${PPATH}/log/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_eigen_g5coarseD_bs6666_Nc20_Ns1.log \
	   ${PPATH}/log/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_eigen_g5coarseD_bs6666_Nc20_Ns2.log \
	-m "|" "|" "|" \
	-l 'Fine grid: $Q$' \
	   'Coarse grid: $\hat{Q}: N_s=1$, case (1)' \
	   'Coarse grid: $\hat{Q}: N_s=2$, case (2sc)'

