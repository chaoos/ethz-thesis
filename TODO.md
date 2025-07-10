# TODO

* [x] methodology of part2 measurements
* [ ] strong scaling with many RHS
* [x] abstracts
* [x] declaration of originality
* [x] ackowledgements
* [x] appendix: data availability
* [x] dual lattice cleanup with shared memory and process block grid
* [ ] asynch solver is a bit scattered around
* [x] part1 intro end
* [ ] consistency in notation of lattice size TxL^3 or L_0 L_1 ...
* [x] chirality: numerical range plots
* [ ] overall summary?
* [ ] publish zenodo
* [x] caption of figures in part 2: add ref to MGLMA paper, where they are taken.
* [x] read through once, add \readit{n} to chapter headers, where n is the number of times read through it; continue at "Exact estimator on coarsest level"
* [ ] "full correlator" -> "Euclidean time correlator" everywhere
* [ ] Ns, \hat{Ns}, same for Nc
* [ ] "MG-LMA" -> "MG LMA"
* [x] check evans and steves presentations
* [x] cheryls corrections, continue at chapter 7
* [ ] i.e -> \ie, and others
* [ ] Fix ordering of publications and references [P1] to [P11], but then the refs start at [12]
* [ ] For all figures: check font sizes relative to main text font size
* [ ] Longer chapter titles, like "Performance" --> "Performance plot of GPU stuff blabla"
* [ ] `openQ*D` or `openQxD`
* [ ] Go through refs and check if they look correct
* [ ] Search for "section" and check if it should be "chapter"


## Final things to check

* [ ] No more red things -> no red last page
* [ ] Line break layout of \code{} fragments
* [ ] Captions and their figures on the same page
* [ ] No unmet references
* [ ] check all \code{} parts, also in captions, footnotes, figures, etc
* [ ] Also in images/schemes!
* [ ] Table of contents: only depth 2
* [ ] Remove TLDRs
* [ ] Check crefs in clover picture

<!-- Funny quote
// If this code works, it was written by Paul DiLascia. If not, I don't know
// who wrote it
 -->

Funny quote
// I'm sorry.
-- Anonymous programmer

Funny quote
from "about vectors" book preface

# Redo all plots

## On chaos

```bash
./scripts/plot_dual_tpn.py -v -i '/home/roman/mnt/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/*/numa/dual/shm/ideal_tpn/*/r*/*.log' -o chapters/part-1/08-performance/img/dual_tpn_numa_shm.pdf --plot 'D300=D300, 2 Nodes' 'A400=A400, 2 Nodes' 'G8=G8, 1 Node'
./scripts/plot_dual_nodes.py -v -i '/home/roman/mnt/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/*/dual/ideal_nodes/*/*run*.log' -o chapters/part-1/08-performance/img/dual_nodes.pdf --plot G8=G8 D300=D300 A400=A400
./scripts/plot_dual_bar.py -v -i '/home/roman/mnt/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/*/numa/dual/shm/fraction/*/r*/*.log' -o chapters/part-1/08-performance/img/dual_bar_numa_shm.pdf --plot 'G8=G8 todo' 'D300=D300 todo' 'A400=A400 todo'
```

## On geno

```bash
./scripts/plot_overlaps.py -v -i /home/hpcp/rgruber/thesis/perf/leo/test/quda/gpu/leo/F7/async -o chapters/part-1/08-performance/img/async_leo_F7 -t 'F7 @ Leonardo (tuned)'
./scripts/plot_overlaps.py -v -i /home/hpcp/rgruber/thesis/perf/new/test/quda/gpu/daint-alps/F7/async -o chapters/part-1/08-performance/img/async_daint_alps_F7 -t 'F7 @ Daint (tuned)' --glob '/NPROC*overlap{0}_*/'
./scripts/plot_metrics.py -v -i plots/mrhs.py
./scripts/plot_metrics.py -v -i plots/coarse.py
./scripts/scaling_plot.py -v -i plots/daint-alps.py
```

And the variance plots (on geno?):

```bash
all_plot_commands.sh
```
