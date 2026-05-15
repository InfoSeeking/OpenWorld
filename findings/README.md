We used openworld to evaluate three flagship world models — V-JEPA 2, VideoMAE v2, and DreamerV3 — on the IntPhys2 physical reasoning benchmark.

A world model with genuine physical understanding should represent a physically impossible event — say, a ball passing through a solid wall — differently from a physically plausible one. We tested whether current models do this. They do not.

**Preliminary findings:**

1. None of the evaluated models organize their latent spaces around physical rules, despite containing structure organized around visual and task-driven features.
2. All three models exploit background shortcuts, but the pattern varies by architecture.
3. The failure mode is shaped by the training objective in predictable ways.

**Shortcut exploitation by model and camera type:**

| Model        | Overall | Fixed Camera | Moving Camera |
|--------------|---------|-------------|--------------|
| V-JEPA 2     | 21.3%   | 31.0%       | 14.0%        |
| DreamerV3    | 12.6%   | 13.0%       | 12.0%        |
| VideoMAE v2  | 8.1%    | 16.5%       | ~0%          |

**Latent structure metrics:**

| Model       | GT Sil. | KM Sil. | Centroid Gap | NN Gap | Invariance |
|-------------|---------|---------|--------------|--------|------------|
| V-JEPA 2    | -0.006  | 0.169   | +0.079       | -0.631 | 0.004      |
| VideoMAE v2 | +0.013  | 0.222   | +0.002       | -0.033 | 0.029      |
| DreamerV3   | -0.026  | 0.314   | -71.29       | +0.002 | -0.007     |

A preprint with full methodology and analysis is forthcoming.
