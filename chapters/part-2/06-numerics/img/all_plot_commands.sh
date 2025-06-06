#!/bin/bash

# All plots for thesis
# Run from geno

. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/python3"
PPATH="/home/regruber/g-2/openQxD-devel/01-dev/"

# ${PYTHON} ${PPATH}/plot_contributions.py -v -N4 --fold \
# 	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/H7/H7_rel_variance.pdf \
# 	-i0 /home/hpcp/rgruber/H7/final/trad '*_L0.dat' \
# 	-i1 /home/hpcp/rgruber/H7/final/4lvl '*_regular.dat' \
# 	-i2 /home/hpcp/rgruber/H7/final/3lvl '*_L0.dat' \
# 	-i3 /home/hpcp/rgruber/H7/final/4lvl '*_regular.dat' \
# 	-n 'L0: rest-rest + rest-eigen' REG 'L0: Fine grid' REG \
# 	--nsrc 1 1 1 1 -c 'G[1]-G[0]' 'L1: eigen-eigen' \
# 	-c 'G[3]-G[2]' 'L1: Coarse grid' --contributions 0 c0 1 'LMA' \
# 	--contributions 2 c1 3 '2-level MG LMA' \
# 	--plot-grid 2 1 --plot-var --construct-early --variant 1 \
# 	--ylim 0 1 -a 0.0658 --name-as-title --plot-sum

# ${PYTHON} ${PPATH}/plot_contributions.py -v -N4 --fold \
# 	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/G7/G7_rel_variance.pdf \
# 	-i0 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
# 	-i1 /home/hpcp/rgruber/G7/final/both '*_regular.dat' \
# 	-i2 /home/hpcp/rgruber/G7/final 'str2_run2/*_L0.dat' \
# 	-i3 /home/hpcp/rgruber/G7/final 'str2_run2/*_regular.dat' \
# 	-n 'L0: rest-rest + rest-eigen' REG 'L0: Fine grid' REG \
# 	--nsrc 1 1 1 1 -c 'G[1]-G[0]' 'L1: eigen-eigen' \
# 	-c 'G[3]-G[2]' 'L1: Coarse grid' --contributions 0 c0 1 'LMA' \
# 	--contributions 2 c1 3 '2-level MG LMA' \
# 	--plot-grid 2 1 --plot-var --construct-early --variant 1 \
# 	--ylim 0 1 -a 0.0658 --name-as-title --plot-sum


# ${PYTHON} ${PPATH}/plot_contributions.py -v -N4 --fold \
# 	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/F7/F7_rel_variance.pdf \
# 	-i0 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
# 	-i1 /home/hpcp/rgruber/F7/final/both '*_regular.dat' \
# 	-i2 /home/hpcp/rgruber/F7/final 'str2_run2/*_L0.dat' \
# 	-i3 /home/hpcp/rgruber/F7/final 'str2_run2/*_regular.dat' \
# 	-n 'L0: rest-rest + rest-eigen' REG 'L0: Fine grid' REG \
# 	--nsrc 1 1 1 1 -c 'G[1]-G[0]' 'L1: eigen-eigen' \
# 	-c 'G[3]-G[2]' 'L1: Coarse grid' --contributions 0 c0 1 'LMA' \
# 	--contributions 2 c1 3 '2-level MG LMA' \
# 	--plot-grid 2 1 --plot-var --construct-early --variant 1 \
# 	--ylim 0 1 -a 0.0658 --name-as-title --plot-sum


# ${PYTHON} ${PPATH}/plot_contributions.py -v -N4 --fold \
# 	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/E7/E7_rel_variance.pdf \
# 	-i0 /home/hpcp/rgruber/E7/final/trad '*_L0.dat' \
# 	-i1 /home/hpcp/rgruber/E7/final/trad '*_regular.dat' \
# 	-i2 /home/hpcp/rgruber/E7/final 'str2/*_L0.dat' \
# 	-i3 /home/hpcp/rgruber/E7/final 'str2/*_regular.dat' \
# 	-n 'L0: rest-rest + rest-eigen' REG 'L0: Fine grid' REG \
# 	--nsrc 1 1 1 1 -c 'G[1]-G[0]' 'L1: eigen-eigen' \
# 	-c 'G[3]-G[2]' 'L1: Coarse grid' --contributions 0 c0 1 'LMA' \
# 	--contributions 2 c1 3 '2-level MG LMA' \
# 	--plot-grid 2 1 --plot-var --construct-early --variant 1 \
# 	--ylim 0 1 -a 0.0658 --name-as-title --plot-sum

${PYTHON} ${PPATH}/corr_var.py -v -N8 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/E7/E7_abs_variance.pdf \
	-i0 /home/hpcp/rgruber/E7/final '{4lvl/*_s{0..11}_,3lvl/,str2/,trad/}*_regular.dat' \
	-i1 /home/hpcp/rgruber/E7/final '{str2,3lvl}/*_L0.dat' \
	-i2 /home/hpcp/rgruber/E7/final '{str2,str2_run3lvl,str2_run4lvl}/*_L1.dat' \
	-i3 /home/hpcp/rgruber/E7/final '{trad,trad_run3lvl}/*_L0.dat' \
	-i4 /home/hpcp/rgruber/E7/final/trad '*_L1.dat' \
	-i5 /home/hpcp/rgruber/E7/final/3lvl '*_L0.dat' \
	-i6 /home/hpcp/rgruber/E7/final/3lvl '*_L1.dat' \
	-i7 /home/hpcp/rgruber/E7/final/trad '*_L1.dat' \
	--plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 \
	--plot-titles LMA '2-level MG LMA' '3-level MG LMA' \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid (exact)' \
	-a 0.0658 --nsrc 1 --ylim 1e-13 1e-6 #--nconfigs 3

${PYTHON} ${PPATH}/corr_var.py -v -N8 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/F7/F7_abs_variance.pdf \
	-i0 /home/hpcp/rgruber/F7/final '{regular,both,trad,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/F7/final/str2_run2 '*_L0.dat' \
	-i2 /home/hpcp/rgruber/F7/final/str2_run2 '*_L1.dat' \
	-i3 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
	-i4 /home/hpcp/rgruber/F7/final/trad '*_L1.dat' \
 	-i5 /home/hpcp/rgruber/F7/final/both '*_L0.dat' \
 	-i6 /home/hpcp/rgruber/F7/final/both '*_L1.dat' \
 	-i7 /home/hpcp/rgruber/F7/final/both '*exact_L2.dat' \
	--plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 \
	--plot-titles LMA '2-level MG LMA' '3-level MG LMA' \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid (exact)' \
	-a 0.0658 --nsrc 1 --ylim 1e-15 1e-6 #--nconfigs 3

${PYTHON} ${PPATH}/corr_var.py -v -N9 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/G7/G7_abs_variance.pdf \
	-i0 /home/hpcp/rgruber/G7/final '{regular{,_t003_run{1,2}},str2,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/G7/final 'str2_run2/*_L0.dat' \
	-i2 /home/hpcp/rgruber/G7/final 'str2_run2/*_L1.dat' \
	-i3 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
	-i4 /home/hpcp/rgruber/G7/final/trad '*exact_L1.dat' \
	-i5 /home/hpcp/rgruber/G7/final/4lvl '*_L0.dat' \
	-i6 /home/hpcp/rgruber/G7/final/4lvl '*_L1.dat' \
	-i7 /home/hpcp/rgruber/G7/final/4lvl '*_L2.dat' \
	-i8 /home/hpcp/rgruber/G7/final/trad '*exact_L1.dat' \
	--plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 8 \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid' 'L3: eigen-eigen (exact)' \
	-a 0.0658 --plot-titles LMA '2-level MG LMA' '4-level MG LMA' \
	--ylim 1e-17 1e-6 --nsrc 1 #--nconfigs 3

${PYTHON} ${PPATH}/corr_var.py -v -N9 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/H7/H7_abs_variance.pdf \
	-i0 /home/hpcp/rgruber/H7/final/4lvl '*_regular.dat' \
	-i1 /home/hpcp/rgruber/H7/final/trad '*_L0.dat' \
	-i2 /home/hpcp/rgruber/H7/final/trad '*_L1.dat' \
	-i3 /home/hpcp/rgruber/H7/final/str2 '*_L0.dat' \
	-i4 /home/hpcp/rgruber/H7/final/str2 '*_L1.dat' \
	-i5 /home/hpcp/rgruber/H7/final/4lvl '*_L0.dat' \
	-i6 /home/hpcp/rgruber/H7/final/4lvl '*_L1.dat' \
	-i7 /home/hpcp/rgruber/H7/final/4lvl '*_L2.dat' \
	-i8 /home/hpcp/rgruber/H7/final/trad '*_L1.dat' \
	--plot-together 0 1 2 --plot-together 0 3 4 --plot-together 0 5 6 7 8 \
	-a 0.0658 --plot-titles LMA '2-level MG LMA' '4-level MG LMA' \
	--names 'Stochastic estimator' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid' 'L3: Coarse grid (exact)' \
	--ylim 1e-17 1e-6 --nsrc 1

${PYTHON} ${PPATH}/gauge_noise.py -v -N9 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/G7/G7_var_vs_srcs.pdf \
	-i0 /home/hpcp/rgruber/G7/final '{regular{,_t003_run{1,2}},str2,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/G7/final 'str2_run2/*_L0.dat' \
	-i2 /home/hpcp/rgruber/G7/final 'str2_run2/*_L1.dat' \
	-i3 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
	-i4 /home/hpcp/rgruber/G7/final/trad '*exact_L1.dat' \
	-i5 /home/hpcp/rgruber/G7/final/4lvl '*_L0.dat' \
	-i6 /home/hpcp/rgruber/G7/final/4lvl '*_L1.dat' \
	-i7 /home/hpcp/rgruber/G7/final/4lvl '*_L2.dat' \
	-i8 /home/hpcp/rgruber/G7/final/trad '*exact_L1.dat' \
	--times 20 --nsrc 1 2 4 8 16 32 64 128 256 512 1024 \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid' 'L3: eigen-eigen (exact)' \
	-l 4 8 --plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 8 \
	--plot-titles 'LMA' '2-level MG LMA' '4-level MG LMA' \
	-a 0.0658 --ylim 1e-15 1e-9 #--nconfigs 3

${PYTHON} ${PPATH}/gauge_noise.py -v -N7 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/G7/G7_var_vs_srcs2.pdf \
	-i0 /home/hpcp/rgruber/G7/final '{regular{,_t003_run{1,2}},str2,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
	-i2 /home/hpcp/rgruber/G7/final/trad '*_L1.dat' \
	-i3 /home/hpcp/rgruber/G7/final/4lvl '*_L0.dat' \
	-i4 /home/hpcp/rgruber/G7/final/4lvl '*_L1.dat' \
	-i5 /home/hpcp/rgruber/G7/final/4lvl '*_L2.dat' \
	-i6 /home/hpcp/rgruber/G7/final/trad '*_L1.dat' \
	--times 20 --nsrc 1 2 4 8 16 32 64 128 256 512 1024 \
	-a 0.0658 --names 'Stochastic estimator' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid' 'L3: Coarse grid (exact)' \
	-l 2 6 --plot-together 0 1 2 --plot-together 0 3 4 5 6 \
	--plot-titles LMA '4-level MG LMA' --ylim 1e-15 1e-9 #--nconfigs 3

${PYTHON} ${PPATH}/gauge_noise.py -v -N8 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/E7/E7_var_vs_srcs.pdf \
	-i0 /home/hpcp/rgruber/E7/final '{4lvl/*_s{0..11}_,3lvl/,str2/,trad/}*_regular.dat' \
	-i1 /home/hpcp/rgruber/E7/final '{str2,3lvl}/*_L0.dat' \
	-i2 /home/hpcp/rgruber/E7/final '{str2,str2_run3lvl,str2_run4lvl}/*_L1.dat' \
	-i3 /home/hpcp/rgruber/E7/final '{trad,trad_run3lvl}/*_L0.dat' \
	-i4 /home/hpcp/rgruber/E7/final/trad '*_L1.dat' \
	-i5 /home/hpcp/rgruber/E7/final/3lvl '*_L0.dat' \
	-i6 /home/hpcp/rgruber/E7/final/3lvl '*_L1.dat' \
	-i7 /home/hpcp/rgruber/E7/final/trad '*_L1.dat' \
	--times 20 --nsrc 1 4 16 64 256 1024 4096 \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid (exact)' \
	-l 4 7 --plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 \
	--plot-titles LMA '2-level MG LMA' '3-level MG LMA' \
	-a 0.0658 --ylim 1e-14 1e-8 #--nconfigs 3


${PYTHON} ${PPATH}/gauge_noise.py -v -N8 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/F7/F7_var_vs_srcs.pdf \
	-i0 /home/hpcp/rgruber/F7/final '{regular,both,trad,str2_run2}/*_regular.dat' \
	-i1 /home/hpcp/rgruber/F7/final/str2_run2 '*_L0.dat' \
	-i2 /home/hpcp/rgruber/F7/final/str2_run2 '*_L1.dat' \
	-i3 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
	-i4 /home/hpcp/rgruber/F7/final/trad '*_L1.dat' \
 	-i5 /home/hpcp/rgruber/F7/final/both '*_L0.dat' \
 	-i6 /home/hpcp/rgruber/F7/final/both '*_L1.dat' \
 	-i7 /home/hpcp/rgruber/F7/final/both '*exact_L2.dat' \
	--plot-together 0 3 4 --plot-together 0 1 2 --plot-together 0 5 6 7 \
	--times 20 --nsrc 1 2 4 8 16 32 64 128 256 512 1024 \
	--names 'Stochastic estimator' 'L0: Fine grid' 'L1: Coarse grid' 'L0: rest-rest + rest-eigen' 'L1: eigen-eigen (exact)' 'L0: Fine grid' 'L1: Coarse grid' 'L2: Coarse grid (exact)' \
	-l 4 7 \
	--plot-titles LMA '2-level MG LMA' '3-level MG LMA' \
	-a 0.0658 --ylim 1e-14 1e-9 #--nconfigs 3

${PYTHON} ${PPATH}/vvv.py -v -N20 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/volume.pdf \
	-i0 /home/hpcp/rgruber/E7/final '{4lvl/*_s{0..11}_,3lvl/,str2/,trad/}*_regular.dat' \
	-i1 /home/hpcp/rgruber/F7/final '{regular,str2_run2}/*_regular.dat' \
	-i2 /home/hpcp/rgruber/G7/final '{regular{,_t003_run{1,2}},str2,str2_run2}/*_regular.dat' \
	-i3 /home/hpcp/rgruber/H7/final '4lvl/*_regular.dat' \
	-i4 /home/hpcp/rgruber/E7/final/str2 '*_L1.dat' \
	-i5 /home/hpcp/rgruber/F7/final/str2_run2 '*_L1.dat' \
	-i6 /home/hpcp/rgruber/G7/final '{str2,str2_run2}/*_L1.dat' \
	-i7 /home/hpcp/rgruber/H7/final 'str2/*_L1.dat' \
	-i8 /home/hpcp/rgruber/E7/final/trad '*_L1.dat' \
	-i9 /home/hpcp/rgruber/F7/final/trad '*_L1.dat' \
	-i10 /home/hpcp/rgruber/G7/final/trad '*_L1.dat' \
	-i11 /home/hpcp/rgruber/H7/final/trad '*_L1.dat' \
	-i12 /home/hpcp/rgruber/E7/final/str2 '*_L0.dat' \
	-i13 /home/hpcp/rgruber/F7/final/str2_run2 '*_L0.dat' \
	-i14 /home/hpcp/rgruber/G7/final '{str2,str2_run2}/*_L0.dat' \
	-i15 /home/hpcp/rgruber/H7/final 'str2/*_L0.dat' \
	-i16 /home/hpcp/rgruber/E7/final/trad '*_L0.dat' \
	-i17 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
	-i18 /home/hpcp/rgruber/G7/final/trad '*_L0.dat' \
	-i19 /home/hpcp/rgruber/H7/final/trad '*_L0.dat' \
	--xticks 2 4 8 --times 20 --nsrc 1 -g 0 1 2 3 \
	-g 4 5 6 7 -g 8 9 10 11 -g 12 13 14 15 -g 16 17 18 19 \
	--plot-together 0 4 2 --plot-together 0 3 1 \
	--group-names 'Stochastic estimator' 'L1: Coarse-grid' 'L1: eigen-eigen (exact)' 'L0: Fine-grid' 'L0: rest-rest + rest-eigen' \
	--gauge-variance 0 1 2 --plot-oox 0 1 3 4 \
	-a 0.0658 --ylim 1e-13 1e-8 \
	--plot-titles LMA '2-level MG LMA' #--nconfigs 3

${PYTHON} ${PPATH}/gauge_noise.py -v -N1 --fold \
	-o /scratch/rgruber/67bc5d6d049e882b8a262db6/chapters/part-2/06-numerics/img/gauge_variance.pdf \
	-i0 /home/hpcp/rgruber/E7/final '{4lvl/*_s{0..11}_,3lvl/,str2/,trad/}*_regular.dat' \
	--times 20 --nsrc 1 4 16 64 256 1024 4096 \
	--xticks 1 4 16 64 256 1024 4096 -a 0.0658 \
	-n 'Stochastic estimator $\sigma^2_G$' \
	--plot-together 0 --plot-titles 'E7: at $t = {fm_time}\,fm\,(t/a = {time})$' \
	--ylim 1e-12 1e-8 #--nconfigs 3

# ${PYTHON} corr_var.py -v -N5 --fold -o /home/regruber/plots/thesis/figure_09.pdf \
# 	-i0 /home/hpcp/rgruber/F7/final '{regular,str2_run2}/*_regular.dat' \
# 	-i1 /home/hpcp/rgruber/F7/2nd_run/Ns50 '*_rem2.dat' \
# 	-i2 /home/hpcp/rgruber/F7/final/trad '*_L0.dat' \
# 	-i3 /home/hpcp/rgruber/F7/2nd_run/Ns50_B6x6x6x6 '*_rem2.dat' \
# 	-i4 /home/hpcp/rgruber/F7/final 'str2_run2/*_L0.dat' \
# 	--plot-together 0 1 2 --plot-together 0 3 4 \
# 	--plot-titles LMA 'MG LMA: $8^4$ block size' \
# 	--names Stochastic 'L0: $N_s=1$' 'L0: $N_s=2$' 'L0: $N_s=1$' 'L0: $N_s=2$' \
# 	-a 0.0658 --nsrc 1 --ylim 1e-15 1e-6 ##--nconfigs 3

