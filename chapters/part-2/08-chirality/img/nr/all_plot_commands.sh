#!/bin/bash

# All plots for thesis
# Run from geno

#. /home/regruber/g-2/openQxD-devel/01-dev/python-venv/bin/activate

PYTHON="/scratch/rgruber/67bc5d6d049e882b8a262db6/myvenv/bin/python3"
PPATH="/scratch/rgruber/67bc5d6d049e882b8a262db6/"


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 3 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-25T02:27:37.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson/num_range/fine_free/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-26T22:22:22.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/nr/fine_nr.pdf \
	--names "Wilson" "Wilson-Clover" "free Wilson" \
	--ylim -2.8 2.8 --xlim -0.5 7.8 --conjugate yes yes yes --methods IoU

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns1/*num_range*.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns1/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-21T00\:42\:30.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns1/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-23T16:09:31.log \
	-n3 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/nr/wc_Nc20_Ns1_nr.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--inset 0.65 0.05 0.4 0.4 --xlim -0.5 7.8 --xlim -0.02 0.02 --ylim -2.5 2.5 --ylim -0.02 0.02 \
	#--title 'Numerical range: $N_s=1$, $N_c=20$.' \

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns2/*num_range*.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-21T02\:26\:06.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns2/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-23T16:09:31.log \
	-n3 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/nr/wc_Nc20_Ns2_nr.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate yes yes yes yes --inset 0.65 0.05 0.4 0.4 --xlim -0.5 7.8 --xlim -0.2 0 --ylim -2.5 2.5 --ylim -0.1 0.1 \
	#--title 'Numerical range: $N_s=2$, $N_c=20$.' \

${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/Ns4/*num_range*.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-21T08\:06\:39.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/Ns4/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-28T21:52:32.log \
	-n3 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/nr/wc_Nc20_Ns4_nr.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--conjugate yes yes yes yes --inset 0.65 0.05 0.4 0.4 --xlim -0.5 7.8 --xlim -0.2 0 --ylim -2.5 2.5 --ylim -0.1 0.1 \
	#--title 'Numerical range: $N_s=4$, $N_c=20$.' \


${PYTHON} ${PPATH}/scripts/num_range.py -v -N 4 \
	-n0 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/48x24x24x24/Nc20/P02P13/*num_range*.log \
	-n1 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/6x6x6x6/Nc20/P02P13/*num_range*.log \
	-n2 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/coarse/4x4x4x4/Nc20/P02P13/*num_range*.log \
	-n3 /home/regruber/g-2/openQxD-devel/01-dev/log/wilson_clover/num_range/fine/48x24x24x24b5.30k0.13625c1.90952id2_n10_f0_num_range_2025-06-19T19:16:05.log \
	-o ${PPATH}/chapters/part-2/07-chirality/img/nr/wc_Nc20_P02P13_nr.pdf \
	--names "LMA" 'MG $6^4$' 'MG $4^4$' "fine" \
	--inset 0.65 0.05 0.4 0.4 --xlim -0.5 7.8 --xlim -0.02 0.02 --ylim -2.5 2.5 --ylim -0.02 0.02 \
	#--title 'Numerical range: $N_s=2$, $N_c=20$.' \

