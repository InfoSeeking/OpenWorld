# OpenWorld v0.0.1 — Initial SDK skeleton.

This release provides the initial installable SDK skeleton (`pip install -e .`) and establishes the Phase 1 baseline.

Current status:
- Package skeleton is installable and structured as a Python package.
- One metric module is implemented: `ground_truth_silhouette` and `kmeans_silhouette`.
- Four metric modules are present as stubs with formal definitions in docstrings: invariance, NN geometry, centroid gap, and DCI.
- `DemoClips` benchmark loading is working.
- Model adapter stubs are included for V-JEPA 2, VideoMAE v2, and DreamerV3.
- Documentation includes quickstart, adding a model, methodology, and findings summary.

This is a foundation for Phase 1 work. See [ROADMAP.md](ROADMAP.md).
