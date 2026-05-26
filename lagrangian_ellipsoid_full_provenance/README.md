# Lagrangian ellipsoid scheme: full provenance notebooks

This directory contains the full computational provenance for the paper figures and reduced-model results.

## What is included

There are two reproducibility modes.

### Fast path

The directory includes the NPZ data products used in the paper.  You can run notebooks 02--07 immediately to reproduce diagnostics, model fits, and figures.

### Full path from scratch

Run notebook 01 first:

```text
01_generate_empirical_train_from_scratch.ipynb
```

This constructs the synthetic incompressible Gaussian--Holder flow, advects the particle clouds, fits the minimum-volume enclosing ellipsoid, computes the ellipsoid-averaged gradient, and writes

```text
empirical_train_mavg_out_v10.npz
```

This is the expensive data-generating step.

Then run:

```text
02_enrich_empirical_train.ipynb
03_null_sde_calibration.ipynb
04_generator_diagnostics_source_sink.ipynb
05_stationary_alignment_closure.ipynb
06_sigma_residual_final_closure.ipynb
07_paper_figures_lagrangian_ellipsoid_scheme.ipynb
```

## Conceptual order

1. Generate the empirical train $(M(t),g(t))$.
2. Enrich it with intrinsic variables $(v,\sigma,A,\omega,\alpha)$.
3. Fit the marginal-gradient null model and show why it fails.
4. Diagnose the source--sink balance.
5. Fit the stationary alignment closure.
6. Fit the final affine residual closure.
7. Generate paper figures.

## Notes

The full simulation step may take several minutes.  The included NPZ files are provided so that readers can reproduce the paper figures without rerunning the expensive particle-advection simulation.
