#!/bin/bash

# All plots for thesis
# Run from geno

#. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/scratch/rgruber/67bc5d6d049e882b8a262db6/myvenv/bin/python3"
PPATH="/scratch/rgruber/67bc5d6d049e882b8a262db6/"


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 3 \
	-c0 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T11\:57\:27.log \
	-c1 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull.*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-c2 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2.spec_hull.2025-06-25T18\:26\:32.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/fine_sh.pdf \
	--names "Wilson" "Wilson-Clover" "free Wilson" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes yes yes --points yes

# ${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
# 	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns1/*conv_hull_evals*.log \
# 	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns1/*conv_hull_evals*.log \
# 	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns1/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-24T03:37:02.log \
# 	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
# 	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
# 	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns1_sh_old.pdf \
# 	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" --title 'Spectral hull: $N_s=1$, $N_c=20$.' \
# 	--aspect auto --points no yes --xscale log --xlim 1e-4 10 --ylim -1.8 1.8 \
# 	--inset 0.05 0.05 0.4 0.4 --xlim 4e-3 1e-2 --ylim -0.025 0.025 --conjugate no no no yes # --only-visible no no no yes

# ${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
# 	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns2/*conv_hull_evals*.log \
# 	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-20T17\:06\:00.log \
# 	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-24T03:37:03.log \
# 	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
# 	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
# 	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns2_sh_old.pdf \
# 	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" --title 'Spectral hull: $N_s=2$, $N_c=20$.' \
# 	--aspect auto --points no yes --xscale log --xlim 1e-4 10 --ylim -1.8 1.8 \
# 	--inset 0.05 0.05 0.4 0.4 --xlim 4e-3 1e-2 --ylim -0.025 0.025 --conjugate yes yes yes yes

# ${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
# 	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns4/*conv_hull_evals*.log \
# 	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-20T17:05:55.log \
# 	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T18:05:21.log \
# 	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
# 	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
# 	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns4_sh_old.pdf \
# 	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" --title 'Spectral hull: $N_s=4$, $N_c=20$.' \
# 	--aspect auto --points no yes --xscale log --xlim 1e-4 10 --ylim -1.8 1.8 \
# 	--inset 0.05 0.05 0.4 0.4 --xlim 4e-3 1e-2 --ylim -0.025 0.025 --conjugate yes yes yes yes

# ${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
# 	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/P02P13/*conv_hull_evals*.log \
# 	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/P02P13/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T03:04:26.log \
# 	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/P02P13/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T08:30:31.log \
# 	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
# 	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
# 	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_P02P13_sh_old.pdf \
# 	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" --title 'Spectral hull: $i=4$, $N_s=1$, $N_c=20$.' \
# 	--aspect auto --points no yes --xscale log --xlim 1e-4 10 --ylim -1.8 1.8 \
# 	--inset 0.05 0.05 0.4 0.4 --xlim 4e-3 1e-2 --ylim -0.025 0.025 --conjugate no no no yes


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/P02P13/*conv_hull_evals*.log \
	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/P02P13/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T03:04:26.log \
	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/P02P13/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T08:30:31.log \
	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log\
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-i3 /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_P02P13_sh.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate no no no yes --ylim -4 2 --xlim -0.25 7.25 --points no yes \
	--only-visible no no no no --only-visible no no no yes \
	--inset 0.1 0.1 0.5 0.4 --xscale linear log --aspect equal 15 --ylim -0.05 0.05 --xlim 1e-3 0.1 \
	#--title 'Spectral hull: $N_s=2$, $N_c=20$.' \

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns1/*conv_hull_evals*.log \
	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns1/*conv_hull_evals*.log \
	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns1/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-24T03:37:02.log \
	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-i3 /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns1_sh.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate no no no yes --ylim -4 2 --xlim -0.25 7.25 --points no yes \
	--only-visible no no no no --only-visible no no no yes \
	--inset 0.1 0.1 0.5 0.4 --xscale linear log --aspect equal 15 --ylim -0.05 0.05 --xlim 1e-3 0.1 \
	#--title 'Spectral hull: $N_s=1$, $N_c=20$.' \


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns2/*conv_hull_evals*.log \
	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-20T17\:06\:00.log \
		/home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-05T04\:52\:57.log \
	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-24T03:37:03.log \
	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-i3 /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns2_sh.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate no no no yes --ylim -4 2 --xlim -0.25 7.25 --points no yes \
	--only-visible no no no no --only-visible no no no yes \
	--inset 0.1 0.1 0.5 0.4 --xscale linear log --aspect equal 15 --ylim -0.05 0.05 --xlim 1e-3 0.1 \
	#--title 'Spectral hull: $N_s=2$, $N_c=20$.' \

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-c0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns4/*conv_hull_evals*.log \
	-c1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-06-20T17:05:55.log \
		/home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-04T11:05:54.log \
		/home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-06T12\:26\:21.log \
	-c2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_conv_hull_evals_2025-07-01T18:05:21.log \
	-c3 /scratch/rgruber/openqxd_quda_build/01-work/log/wilson_clover/num_range/fine/*spec_hull*.log \
	    /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-i3 /scratch/rgruber/openqxd_quda_build_old/01-work/log/48x24x24x24b5.30k0.13625c1.90952id2.check4_450modes.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/sh/wc_Nc20_Ns4_sh.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate no no no yes --ylim -4 2 --xlim -0.25 7.25 --points no yes \
	--only-visible no no no no --only-visible no no no yes \
	--inset 0.1 0.1 0.5 0.4 --xscale linear log --aspect equal 15 --ylim -0.05 0.05 --xlim 1e-3 0.1 \
	#--title 'Spectral hull: $N_s=4$, $N_c=20$.' \

