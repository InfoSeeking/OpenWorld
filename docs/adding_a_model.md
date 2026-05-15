# Adding Your Own Model Adapter to OpenWorld

## 1. Why Custom Adapters Matter

OpenWorld is designed so that any developer with a domain-specific video model can evaluate, compare, and analyze their model using the same SDK as large foundation models—without modifying the SDK itself. By writing a thin adapter, you can plug in your own model and immediately access all benchmarks and metrics.

## 2. The BaseWorldModel Contract

Every model adapter must subclass `BaseWorldModel` (see `openworld/models/base.py`). You must implement these three methods:

```python
from typing import List
import numpy as np

class BaseWorldModel(abc.ABC):
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
```

- `embed(self, videos: List) -> np.ndarray`: Given a list of videos (format is up to you), return a NumPy array of shape (N, D) with one embedding per video.
- `name(self) -> str`: Return a unique string identifier for your model.
- `embedding_dim(self) -> int`: Return the dimensionality of the embeddings (D).

## 3. Complete Example: MyVideoModel Adapter

Suppose you have a model that takes a list of video file paths and outputs a 128-dimensional embedding for each video. Here is a minimal adapter:

```python
from openworld.models.base import BaseWorldModel
from typing import List
import numpy as np

class MyVideoModel(BaseWorldModel):
    """
    Adapter for a custom video model that returns 128-dim embeddings.
    """
    def __init__(self, weights_path: str = "my_model.pt"):
        # Load your model here (replace with your actual loading code)
        self.weights_path = weights_path
        # self.model = ...

    def embed(self, videos: List[str]) -> np.ndarray:
        """
        Compute embeddings for a list of video file paths.
        Args:
            videos (List[str]): List of video file paths.
        Returns:
            np.ndarray: Array of shape (N, 128) with embeddings.
        """
        N = len(videos)
        # Replace with your actual model inference code
        # Example: return self.model.encode(videos)
        return np.random.randn(N, 128)  # Placeholder

    def name(self) -> str:
        return "myvideomodel"

    def embedding_dim(self) -> int:
        return 128
```

## 4. Using Your Custom Model

You can now use your adapter with the SDK:

```python
from openworld.benchmarks import DemoClips
from openworld.metrics import ground_truth_silhouette

clips = DemoClips.load()
model = MyVideoModel()
embeddings = model.embed([clip["video_url"] for clip in clips.clips])
score = ground_truth_silhouette(embeddings, clips.labels)
print(f"Silhouette: {score:.3f}")
```

## 5. Testing Your Adapter

A simple pytest test to check your adapter returns the right shape:

```python
def test_myvideomodel_embed_shape():
    from your_module import MyVideoModel
    import numpy as np
    model = MyVideoModel()
    dummy_videos = ["a.mp4", "b.mp4", "c.mp4"]
    embeddings = model.embed(dummy_videos)
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (3, 128)
```

## 6. Common Pitfalls

- **Mismatched embedding shapes:** Always return shape (N, D), not (D,) or (N,).
- **Missing temporal pooling:** If your model outputs per-frame features, pool (e.g., mean) across time to get one vector per video.
- **Device placement:** If using PyTorch or TensorFlow, ensure outputs are moved to CPU and converted to NumPy arrays before returning.
- **Input format mismatch:** Make sure your embed() method accepts the format you expect (file paths, arrays, etc.).
- **Mixing PIL and tensor inputs:** Be consistent—convert all frames to the same format before passing to your model.

---

With this adapter, your model is fully compatible with all OpenWorld benchmarks and metrics. For more details, see [docs/methodology.md](methodology.md) and the SDK source code.
