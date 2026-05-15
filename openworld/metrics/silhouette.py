"""
Silhouette score metrics for world model embeddings.

Implements the formal definition from §3.3 (Clustering) of the referenced paper:

    s(i) = (b(i) - a(i)) / max{a(i), b(i)}
where a(i) is the mean intra-cluster distance for sample i, and b(i) is the mean nearest-cluster distance.

- ground_truth_silhouette: Computes the silhouette score using ground-truth labels.
- kmeans_silhouette: Computes the silhouette score using KMeans cluster assignments.

All scores use cosine distance as in the paper.

Example usage:
    import numpy as np
    from openworld.metrics.silhouette import ground_truth_silhouette, kmeans_silhouette
    X = np.random.randn(100, 32)
    labels = np.random.randint(0, 4, size=100)
    print(ground_truth_silhouette(X, labels))
    print(kmeans_silhouette(X, k=4))
"""
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

def ground_truth_silhouette(embeddings: np.ndarray, labels: np.ndarray) -> float:
    """
    Computes the silhouette score using ground-truth labels.
    Follows the formal definition from §3.3 (Clustering) of the paper, using cosine distance.
    Args:
        embeddings (np.ndarray): Array of shape (N, D) with embedding vectors.
        labels (np.ndarray): Array of shape (N,) with integer cluster labels.
    Returns:
        float: Mean silhouette score over all samples.
    """
    return float(silhouette_score(embeddings, labels, metric="cosine"))

def kmeans_silhouette(embeddings: np.ndarray, k: int = 4) -> float:
    """
    Computes the silhouette score using KMeans cluster assignments.
    Follows the formal definition from §3.3 (Clustering) of the paper, using cosine distance.
    Args:
        embeddings (np.ndarray): Array of shape (N, D) with embedding vectors.
        k (int): Number of clusters for KMeans (default: 4).
    Returns:
        float: Mean silhouette score over all samples.
    """
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
    cluster_labels = kmeans.fit_predict(embeddings)
    return float(silhouette_score(embeddings, cluster_labels, metric="cosine"))
