r"""
Nearest Neighbor Geometry Score

Formal definition (from §3.3 of the paper):

Let $\mathbf{z}_i$ be the embedding for video $i$. The NN geometry score is:

    \mathrm{NNG}(Z) = \frac{1}{N} \sum_{i=1}^N \mathbb{I}[y_i = y_{\pi(i)}]

where $\pi(i)$ is the nearest neighbor of $\mathbf{z}_i$ in embedding space (excluding $i$), and $y_i$ is the ground-truth label.

This function computes the mean cosine distance to the nearest neighbor with a different label
minus the mean cosine distance to the nearest neighbor with the same label.

References:
- OpenWorld paper, §3.3
"""

import numpy as np
from sklearn.neighbors import NearestNeighbors

def nn_geometry_score(
    embeddings: np.ndarray,
    labels: np.ndarray
) -> float:
    r"""
    Compute the NN geometry score as described in the OpenWorld paper.

    For each embedding, find its nearest neighbor (excluding itself) using cosine distance.
    Compute the mean distance to NN when the NN has a different label,
    minus the mean distance to NN when the NN has the same label.

    Args:
        embeddings (np.ndarray): Array of shape (N, D) with embedding vectors.
        labels (np.ndarray): Array of shape (N,) with integer or string labels.

    Returns:
        float: Mean NN distance (different label) minus mean NN distance (same label).

    Example
    -------
    >>> import numpy as np
    >>> X = np.array([[1, 0], [0, 1], [1, 1], [-1, 0]])
    >>> labels = np.array([0, 0, 1, 1])
    >>> round(nn_geometry_score(X, labels), 6)
    0.0
    """
    n = embeddings.shape[0]
    nn = NearestNeighbors(n_neighbors=2, metric='cosine')
    nn.fit(embeddings)
    dists, idxs = nn.kneighbors(embeddings)
    # idxs[:, 0] is self, idxs[:, 1] is NN
    nn_labels = labels[idxs[:, 1]]
    same = nn_labels == labels
    diff = ~same
    same_dists = dists[:, 1][same]
    diff_dists = dists[:, 1][diff]
    if same_dists.size == 0 or diff_dists.size == 0:
        raise ValueError("Not enough same/different label pairs for nn_geometry_score computation.")
    return float(np.mean(diff_dists) - np.mean(same_dists))