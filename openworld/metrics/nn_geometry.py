"""
Nearest Neighbor Geometry Score

Formal definition (from §3.3 of the paper):

Let $\mathbf{z}_i$ be the embedding for video $i$. The NN geometry score is:

    \mathrm{NNG}(Z) = \frac{1}{N} \sum_{i=1}^N \mathbb{I}[y_i = y_{\pi(i)}]

where $\pi(i)$ is the nearest neighbor of $\mathbf{z}_i$ in embedding space (excluding $i$), and $y_i$ is the ground-truth label.

Expected function signature:

    # --- New implementations below ---
    from sklearn.neighbors import NearestNeighbors

"""
        """
        For each embedding, find its nearest neighbor (excluding itself).
        Compute the mean distance to NN when the NN has a different label,
        minus the mean distance to NN when the NN has the same label.
        Returns a float.

        Example
        -------
        >>> import numpy as np
        >>> from openworld.metrics.nn_geometry import nn_gap
        >>> X = np.array([[1, 0], [0, 1], [1, 1], [-1, 0]])
        >>> labels = np.array([0, 0, 1, 1])
        >>> round(nn_gap(X, labels), 6)
        0.0
        """
        n = embeddings.shape[0]
        nn = NearestNeighbors(n_neighbors=2, metric=metric)
        nn.fit(embeddings)
        dists, idxs = nn.kneighbors(embeddings)
        # idxs[:, 0] is self, idxs[:, 1] is NN
        nn_labels = labels[idxs[:, 1]]
        same = nn_labels == labels
        diff = ~same
        same_dists = dists[:, 1][same]
        diff_dists = dists[:, 1][diff]
        if same_dists.size == 0 or diff_dists.size == 0:
            raise ValueError("Not enough same/different label pairs for nn_gap computation.")
        return float(np.mean(diff_dists) - np.mean(same_dists))

import numpy as np
        """
        5-NN majority-vote classification accuracy (excluding self).
        Returns accuracy as a float between 0 and 1.

        Example
        -------
        >>> import numpy as np
        >>> from openworld.metrics.nn_geometry import knn5_accuracy
        >>> X = np.array([[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1]])
        >>> labels = np.array([0, 0, 1, 1, 1])
        >>> round(knn5_accuracy(X, labels), 2)
        0.6
        """
        n = embeddings.shape[0]
        k = min(6, n)  # 5-NN + self
        nn = NearestNeighbors(n_neighbors=k, metric=metric)
        nn.fit(embeddings)
        _, idxs = nn.kneighbors(embeddings)
        # Exclude self (first neighbor)
        neighbor_labels = labels[idxs[:, 1:]]
        # Majority vote
        from scipy.stats import mode
        maj = mode(neighbor_labels, axis=1, keepdims=False).mode
        acc = np.mean(maj == labels)
        return float(acc)

def nn_geometry_score(embeddings: np.ndarray, labels: np.ndarray) -> float:
    """See module docstring for definition."""
    raise NotImplementedError("nn_geometry_score is not yet implemented.")
