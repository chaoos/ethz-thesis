OLD
---

a) (missing physics motivation)
b) exponential StN ratio problem of the correlator (Parisi-Lepage)
c) mini-review of variance reduction methods: multi-level, distillation, Hutchinson, probing, FS, ...)
d) sketch of LMA


Intro Part II
-------------


a) physics: we need precise correlators -> little recap on what I already said
	* motivation for variance reduction methods
	* g-2 HVP and so on (short)
	* total: 1-2p maximal

b) translation averaging suppresses the gauge noise ~ 1/sqrt{V} but exact translation averaging costs V^2 => estimate
	* definintion of translation averaging on an n-point function -> see our PRD
	* follow this intro: https://arxiv.org/pdf/2401.14724
	* use correlator expression from intro -> g-2 > HVP -> final few eqs
	* total 1-3p

c) stochastic estimators (Hutchinson) add extra variance which can be large
	* we want translation average, but it's V^2 with point sources -> estimate
	* standard hutchinson 1p
	* maybe dilution here 1p

d) existing solutions: probing/freq. splitting/LMA => motivation for next chapter
	* connected
		* LMA 4p -> 1p
	* disconnected
		* HP 1p
		* FS 1p
		* MLMC 1p
		* MG MLMC 1p

e) other problems/related literature (distillation, Parisi-Lepage StN, ...) what this thesis doesn't cover but you want to acknowledge
	* StN, 2p
	* multilevel sampling 2p
	* (smearing 1p) (evtl. remove details, but leave the refs)
	* (distillation 1p) (evtl. remove details, but leave the refs)
	* (end smearing 1p) (evtl. remove details, but leave the refs)
	* dilution 1p (evtl. after hutchinson)

f) remainder of this part
	* last paragraph 1p
	* (Add LMA chapter)

Alternative:
------------

* In the intro above: LMA 4p -> 1p maximal, and mention it will be discussed in its own chapter
* Remove spectral propagator from 2pt
* Remove 4p from intro
* Separate chapter LMA
	* 4p from intro
	* spectral prop from 2pt
	* V2 problem
	* X-term problem


