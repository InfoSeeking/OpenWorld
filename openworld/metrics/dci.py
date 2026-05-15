"""
DCI Disentanglement Metric

Formal definition (from §3.3 of the paper):

Let $Z$ be the embedding matrix and $Y$ the ground-truth factors. The DCI metric is computed as described in the referenced paper, quantifying Disentanglement, Completeness, and Informativeness.

Expected function signature:
    def dci_disentanglement(embeddings: np.ndarray, factors: np.ndarray) -> dict

Raises NotImplementedError.
"""
import numpy as np

def dci_disentanglement(embeddings: np.ndarray, factors: np.ndarray) -> dict:
    """See module docstring for definition."""
    raise NotImplementedError("dci_disentanglement is not yet implemented.")
