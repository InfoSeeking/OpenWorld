r"""
Centroid Gap Metric

Formal definition (from §3.3 of the paper):

Let $C_k$ be the set of embeddings for class $k$, and $\mu_k$ their centroid. The centroid gap is:

    \mathrm{CentroidGap}(Z, Y) = \frac{1}{K} \sum_{k=1}^K \|\mu_k - \mu\|^2

where $\mu$ is the global mean embedding, $K$ is the number of classes, and $\|\cdot\|$ is the Euclidean norm.

Expected function signature:
    def centroid_gap(embeddings: np.ndarray, labels: np.ndarray) -> float

Raises NotImplementedError.
"""
import numpy as np

def centroid_gap(embeddings: np.ndarray, labels: np.ndarray) -> float:
    """See module docstring for definition."""
    raise NotImplementedError("centroid_gap is not yet implemented.")
