"""
BaseWorldModel abstract base class for OpenWorld model embeddings.

A BaseWorldModel defines the interface for extracting fixed-size vector embeddings
from a list of videos. Subclasses must implement the following methods:

- embed(self, videos: list) -> np.ndarray
    Given a list of videos (format defined by the subclass), returns a NumPy array
    of shape (N, D) where N is the number of videos and D is the embedding dimension.
- name(self) -> str
    Returns a unique string identifier for the model.
- embedding_dim(self) -> int
    Returns the dimensionality D of the embeddings produced by this model.

Example subclass:

    import numpy as np
    from openworld.models.base import BaseWorldModel

    class MyModel(BaseWorldModel):
        def embed(self, videos: list) -> np.ndarray:
            # Dummy implementation: random vectors
            return np.random.randn(len(videos), self.embedding_dim())
        def name(self) -> str:
            return "my_model"
        def embedding_dim(self) -> int:
            return 128

"""
import abc
from typing import List
import numpy as np

class BaseWorldModel(abc.ABC):
    """
    Abstract base class for world model embedding extractors.
    """
    @abc.abstractmethod
    def embed(self, videos: List) -> np.ndarray:
        """
        Compute per-video embeddings.

        Args:
            videos (List): List of videos (format defined by subclass).
        Returns:
            np.ndarray: Array of shape (N, D) with embeddings for N videos.
        """
        pass

    @abc.abstractmethod
    def name(self) -> str:
        """
        Returns a unique string identifier for this model.
        """
        pass

    @abc.abstractmethod
    def embedding_dim(self) -> int:
        """
        Returns the embedding dimensionality D.
        """
        pass
