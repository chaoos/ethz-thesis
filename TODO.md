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
* [x] consistency in notation of lattice size TxL^3 or L_0 L_1: Choose: L_0, L_1, L_2, L_3 everywhere!
* [x] chirality: numerical range plots
* [ ] overall summary?
* [ ] publish zenodo
* [x] caption of figures in part 2: add ref to MGLMA paper, where they are taken.
* [x] read through once, add \readit{n} to chapter headers, where n is the number of times read through it; continue at "Exact estimator on coarsest level"
* [ ] "full correlator" -> "Euclidean time correlator" everywhere
* [x] "MG-LMA" -> "MG LMA"
* [x] check evans and steves presentations
* [x] cheryls corrections, continue at chapter 7
* [x] i.e. -> \ie
* [ ] c.f. -> \cf and add command
* [ ] Fix ordering of publications and references [P1] to [P11], but then the refs start at [12]
* [ ] For all figures: check font sizes relative to main text font size
* [x] Longer chapter titles, like "Performance" --> "Performance plot of GPU stuff blabla"
* [ ] `openQ*D` or `openQxD`? -> `openQxD`
* [ ] Go through refs and check if they look correct
* [x] Search for "section" and check if it should be "chapter"
* [x] Add "publications" to ToC
* [ ] Maybe have a separation between chapters and appendices and page indicating "Appendices" or so
* [x] The doctoral students must clearly declare their own achievements according to article 13 of the (https://ethz.ch/content/dam/ethz/special-interest/phys/department/doctoral/documents/Detailed%20Stipulations_D-PHYS_2022.pdf). It is recommended that this declaration be summarised in a separate section. -> Currently I have "Summary of contributions" in the overall intro ...
* [x] "Muon" or "muon" -> "muon"
* [x] Chirality figures: check if i=1 -> ID (1) and so on
* [x] The little intros with section references, like the "structure of the thesis" but for the chapter
* [ ] Thesis feedback Tim: v1 overall intro
* [ ] Thesis feedback Tim: v2 p2intro
* [ ] Thesis feedback Tim: v2 chirality
* [ ] Thesis feedback Tim: v2 conclusions + summary
* [x] Thesis feedback Letizia: step1
* [x] Thesis feedback Letizia: step2
* [ ] Thesis feedback Marina 1
* [ ] Thesis feedback Marina 2
* [ ] Tim: For the abstract, I would add 2 sentences of “motivation”
* [x] "Proposal for Field Memory Management in Heterogeneous Architectures" title is a bit too long
* [x] Summary of the thesis: its bullet point in the overview (left in firefox) should have less intendation
* [x] Summary in the TOC: before and after 10pt vertical space
* [x] fix "Motivation of this thesis" with Letizias comments -> streamline it
* [x] Notation: add cardinality | A |.
* [x] Part 1: All summaries: add critical discussion, limits, summary
* [x] Part 2: All summaries: add critical discussion, limits, summary
* [x] Part 1: overall summary: add critical discussion, limits, summary
* [x] Part 2: overall summary: add critical discussion, limits, summary
* [x] Part 1: Always tease the next chapter in summaries
* [x] Part 2: Always tease the next chapter in summaries
* [x] Ada Lovelace quote
* [ ] \Ns, N_s -> \cNs (for coarse spins)
* [ ] \Nc, N_c -> \cNc (for coarse colors)
* [ ] In all plots: \Ns, N_s -> \cNs (for coarse spins)
* [ ] In all plots: \Nc, N_c -> \cNc (for coarse colors)
* [x] Zitat Schulthess
* [x] Pion mass scaling appendix

## TODO for Monday (14.07.25):

* [x] check if LMA chapter has all I want to say about it -> variants, AMA, V2, X-term probs, ...
* [x] read Part 2 intro, 2pt, LMA, subspace deflation and check if it makes sense now.

## Final read through:

* [x] Title pages
* [x] Abstract
* [x] Zusammenfassung
* [x] DoO
* [x] Ackn
* [x] ToC
* [ ] Overall Intro
* [x] Part 1
	* [x] Part 1: Intro
	* [x] Part 1: openqxd
	* [x] Part 1: quda
	* [x] Part 1: interface
	* [x] Part 1: develop
	* [x] Part 1: performance
	* [x] Part 1: CI/CD
	* [x] Part 1: mem manager
	* [x] Part 1: Conclusions
* [x] Part 2
	* [x] Part 2: Intro
	* [x] Part 2: 2pt
	* [x] Part 2: LMA
	* [x] Part 2: subspace deflation
	* [x] Part 2: local coherence
	* [x] Part 2: Multigrid
	* [x] Part 2: Numerics
	* [x] Part 2: Chirality
	* [x] Part 2: Conclusions
* [x] Overall Summary
* [ ] Appendices
	* [ ] Appendix A: Building
	* [ ] Appendix B: Running
	* [ ] Appendix C: NR and SH
	* [ ] Appendix D: Symmetries
	* [ ] Appendix E: Notation
	* [ ] Appendix F: Physical Pion Masses
	* [ ] Appendix G: License
* [ ] Bibliography
* [ ] List of Figures
* [ ] List of Tables
* [ ] Publications


## Final things to check at Sunday (20.07.25)

* [x] TODOs in overall intro
* [x] No more red things
* [x] No red last page
* [x] Line break layout of \code{} fragments
* [x] Captions and their figures/code listings on the same page
* [x] No unmet references -> from log output
* [x] check sizes of all \code{} parts, also in captions, footnotes, figures, etc
* [x] Also in images/schemes!
* [x] Table of contents: only depth 2
* [x] Remove TLDRs
* [x] Remove "proof-read" indications
* [x] Check crefs in clover picture
* [x] Search for "?" and the turned around one "¿"
* [x] All eqs have a space before comma or full stop
* [x] ToC: are the vertical spaces correct? before part 1 and 2, before and after summary, before bib
* [x] Last section before appendix: add \addtocontents{toc}{\protect\vspace{10pt}} after \section{blabla}
* [x] Check all quotes (no duplicates, etc.)
* [ ] Push to github, add tag, add permalink to tagged PDF

## TODO after hand-in of the thesis

* [ ] Get Diss. No. from doctoral office


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
