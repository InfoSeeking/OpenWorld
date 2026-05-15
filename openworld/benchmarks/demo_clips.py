"""
DemoClips benchmark loader for WorldModelDemo physical scene clips.

Loads a JSON file containing a list of clip records, each with model predictions and metadata.

Example usage:
    from openworld.benchmarks.demo_clips import DemoClips
    demo = DemoClips.load()
    print(demo.n_clips)
    print(demo.labels)
    filtered = demo.filter('physical')
    print(filtered.n_clips)
"""
from pathlib import Path
import json
import numpy as np
from typing import Any, Iterator, List, Dict, Optional, Type, TypeVar
from .base import BaseBenchmark

T = TypeVar('T', bound='DemoClips')

class DemoClips(BaseBenchmark):
    def __init__(self, clips: List[Dict[str, Any]]):
        self._clips = clips

    @classmethod
    def load(cls: Type[T], path: str | Path | None = None) -> T:
        """
        Load clips from a JSON file. If path is None, loads from data/results/clip_results.json relative to repo root.
        """
        if path is None:
            default_path = Path(__file__).parent.parent.parent / 'data' / 'results' / 'clip_results.json'
            path = default_path
        with open(path, 'r', encoding='utf-8') as f:
            clips = json.load(f)
        return cls(clips)

    @property
    def clips(self) -> List[Dict[str, Any]]:
        """List of all clip records."""
        return self._clips

    @property
    def labels(self) -> np.ndarray:
        """Array of scenario_type labels for each clip."""
        return np.array([clip.get('scenario_type', '') for clip in self._clips])

    @property
    def n_clips(self) -> int:
        """Number of clips in the benchmark."""
        return len(self._clips)

    def filter(self: T, scenario_type: str) -> T:
        """
        Return a new DemoClips containing only clips with the given scenario_type.
        """
        filtered = [clip for clip in self._clips if clip.get('scenario_type', '') == scenario_type]
        return self.__class__(filtered)
