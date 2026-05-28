# Lagrangian Ellipsoid Scheme: figures for http://arxiv.org/abs/2605.27606 

This directory contains a self-contained post-processing notebook for regenerating the paper figures from the saved empirical and reduced-model data products.

## Contents

- `paper_figures_lagrangian_ellipsoid_scheme.ipynb` — main figure-generation notebook.
- `data/empirical_train_mavg_out_v10b_enriched.npz` — empirical MEE train and derived variables.
- `data/sde_calibration_mavg_out_v10_results.npz` — marginal-OU null-model output.
- `data/stationary_alignment_closure_v14_results.npz` — stationary-alignment closure output retained for provenance.
- `data/sigma_residual_closure_v15_results.npz` — final residual-closure comparison output.
- `paper_figure_captions.md` — draft captions.

## How to run

Install the small Python stack:

```bash
pip install numpy scipy matplotlib jupyter
```

Then open and run:

```bash
jupyter notebook paper_figures_lagrangian_ellipsoid_scheme.ipynb
```

The notebook writes figures to `figures_paper/` and summary tables to `tables_paper/`.

## Reproducibility note

This is a self-contained figure-regeneration package: it includes the saved NPZ data products needed to reproduce the paper figures. It does not rerun the expensive particle-advection simulation by default. The simulation/calibration notebooks can be provided separately as the full provenance chain.
