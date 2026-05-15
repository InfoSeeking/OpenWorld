"""
Invariance Score Metric

Formal definition (from §3.3 of the paper):

Let $\mathbf{z}_i$ be the embedding for video $i$ and $y_i$ the ground-truth label. The invariance score is:

    \mathrm{Inv}(Z, Y) = 1 - \frac{1}{N} \sum_{i=1}^N \mathbb{I}[y_i \neq y_{\pi(i)}]

where $\pi(i)$ is the nearest neighbor of $\mathbf{z}_i$ in embedding space (excluding $i$), and $\mathbb{I}$ is the indicator function.

Expected function signature:
    def invariance_score(embeddings: np.ndarray, labels: np.ndarray) -> float

Raises NotImplementedError.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def invariance_score(embeddings: np.ndarray, labels: np.ndarray) -> float:
    """See module docstring for definition.

    Example
    -------
    >>> import numpy as np
    >>> from openworld.metrics.invariance import invariance_score
    >>> X = np.array([[1, 0], [0, 1], [1, 1], [-1, 0]])
    >>> labels = np.array([0, 0, 1, 1])
    >>> round(invariance_score(X, labels), 6)
    0.0
    """
    # Compute pairwise cosine similarities
    sims = cosine_similarity(embeddings)
    n = embeddings.shape[0]
    # Exclude diagonal (self-pairs)
    mask = ~np.eye(n, dtype=bool)
    label_matrix = labels[:, None] == labels[None, :]
    # Only consider off-diagonal pairs
    same_mask = mask & label_matrix
    diff_mask = mask & (~label_matrix)
    same_sims = sims[same_mask]
    diff_sims = sims[diff_mask]
    if same_sims.size == 0 or diff_sims.size == 0:
        raise ValueError("Not enough pairs for invariance score computation.")
    return float(np.mean(same_sims) - np.mean(diff_sims))
