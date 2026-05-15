# OpenWorld Benchmarks

OpenWorld provides two evaluation tracks for world models:

## 1. Demo Benchmark
- **Purpose:** Small, public-facing, and visual. Ideal for quick demos, tutorials, and interactive exploration.
- **Data:** `clips.json` (included)
- **Usage:** Powers the interactive demo at [https://InfoSeeking.github.io/WorldModelDemo/](https://InfoSeeking.github.io/WorldModelDemo/)
- **Loader:** `openworld.benchmarks.DemoClips`

**Example:**
```python
from openworld.benchmarks import DemoClips
clips = DemoClips()
print(clips[0])  # Show first demo clip
```

**When to use:**
- For public demos, teaching, or rapid prototyping
- When you want a lightweight, visual dataset
- Not suitable for systematic or large-scale evaluation

---

## 2. Diagnostic Benchmark
- **Purpose:** Systematic, research-grade evaluation. Based on IntPhys2, designed for probing model latent spaces and causal reasoning.
- **Data:** IntPhys2-based (not included by default)
- **Usage:** Used in the team's recent diagnostic study
- **Loader:** `openworld.benchmarks.IntPhys2` *(coming in Phase 1)*

**Example:**
```python
from openworld.benchmarks import IntPhys2
benchmark = IntPhys2('/path/to/intphys2_data')
print(benchmark[0])  # Show first diagnostic sample
```

**When to use:**
- For systematic, quantitative, or causal evaluation
- When you need controlled, large-scale, or research-grade data
- Not intended for quick demos or visualizations

---

**Summary Table:**

| Benchmark         | Purpose         | Loader                        | Data File         |
|------------------|----------------|-------------------------------|------------------|
| Demo             | Visual, public | `DemoClips`                   | `clips.json`     |
| Diagnostic       | Research, eval | `IntPhys2` *(coming soon)*    | IntPhys2 dataset |

See the [schema.md](schema.md) for data format details.
