# OpenWorld Quickstart

This guide will walk you through installing OpenWorld, loading the demo benchmark, generating embeddings, running evaluation metrics, and interpreting the results. All code examples are ready to run with the current SDK.

## 1. Installation

Clone the repository and install in editable mode:

```sh
pip install -e .
```

This will install all required dependencies for the SDK. (A PyPI release is planned for v0.1.)

## 2. Loading the Demo Benchmark

The OpenWorld SDK includes a demo benchmark of physical scene clips with ground-truth labels and model predictions. Load it with:

```python
from openworld.benchmarks import DemoClips

demo = DemoClips.load()
print(f"Loaded {demo.n_clips} clips.")
```

## 3. Computing Embeddings

To evaluate a model, you need per-clip embeddings. For now, we'll use random vectors as a placeholder:

```python
import numpy as np

embeddings = np.random.randn(demo.n_clips, 768)  # Replace with real model embeddings
```

**Note:** Model adapters for V-JEPA 2, VideoMAEv2, and DreamerV3 are in development. You can add your own model adapter—see [docs/adding_a_model.md](adding_a_model.md).

## 4. Running the Silhouette Metric

The silhouette score measures how well the embeddings separate the ground-truth classes (here, all clips are 'physical', so try with synthetic labels for demonstration):

```python
from openworld.metrics import ground_truth_silhouette

labels = demo.labels  # For the demo set, this is usually all 'physical'
score = ground_truth_silhouette(embeddings, labels)
print(f"Silhouette: {score:.3f}")
```

A higher silhouette score (closer to 1) means better separation between classes. If all labels are the same, the score may not be meaningful—try with synthetic or more varied labels for testing.

## 5. Swapping in a Different Metric

### KMeans Silhouette

You can also cluster the embeddings and compute the silhouette score using KMeans assignments:

```python
from openworld.metrics import kmeans_silhouette

score = kmeans_silhouette(embeddings, k=4)
print(f"KMeans Silhouette: {score:.3f}")
```

This measures how well the embeddings form clusters, independent of ground-truth labels.

### Invariance Score

The invariance score quantifies how similar embeddings are for clips with the same label versus different labels:

```python
from openworld.metrics import invariance_score

score = invariance_score(embeddings, labels)
print(f"Invariance Score: {score:.3f}")
```

A higher invariance score means embeddings are more consistent within classes and more distinct across classes.

## 6. Interpreting the Results

- **Silhouette**: High values (close to 1) indicate well-separated clusters; low or negative values suggest overlap or poor separation.
- **KMeans Silhouette**: High values mean the embeddings naturally cluster well, even without ground-truth labels.
- **Invariance Score**: Higher is better; it reflects how invariant the embeddings are to within-class variation.

## What's Next?

- To add your own model, see [docs/adding_a_model.md](adding_a_model.md).
- For details on metrics and methodology, see [docs/methodology.md](methodology.md).
- Explore the rest of the SDK and contribute improvements—see [CONTRIBUTING.md](../CONTRIBUTING.md).
