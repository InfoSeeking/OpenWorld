"""
BaseBenchmark abstract base class for OpenWorld benchmarks.

Defines the common interface for benchmark loaders:
- load(): class method to load the benchmark
- labels: property returning labels for each example
- n_clips: property returning the number of examples
"""
from abc import ABC, abstractmethod
from typing import Any
import numpy as np

class BaseBenchmark(ABC):
    @classmethod
    @abstractmethod
    def load(cls, path: str | None = None) -> 'BaseBenchmark':
        """Load the benchmark from a file or default location."""
        pass

    @property
    @abstractmethod
    def labels(self) -> np.ndarray:
        """Return an array of labels for each example."""
        pass

    @property
    @abstractmethod
    def n_clips(self) -> int:
        """Return the number of examples in the benchmark."""
        pass
