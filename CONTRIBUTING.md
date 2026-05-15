
# Contributing to OpenWorld

Thank you for your interest in contributing! OpenWorld is an evolving research SDK. We welcome contributions of models, metrics, data, and documentation. If in doubt, open an issue before starting work.

---

## Setup

1. Clone the repository:
	```sh
	git clone https://github.com/InfoSeeking/OpenWorld.git
	cd OpenWorld
	```
2. Create a virtual environment (recommended):
	```sh
	python -m venv .venv
	source .venv/bin/activate
	```
3. Install dependencies (including dev tools):
	```sh
	pip install -e .[dev]
	```

---

## Contributing a New Model Adapter

Model adapters wrap AI models (e.g., V-JEPA 2, DreamerV3) to conform to the `BaseWorldModel` interface. See [docs/adding_a_model.md](docs/adding_a_model.md) for a step-by-step guide.

---

## Contributing a New Metric

Add new metrics as a single function in `openworld/metrics/`.

- Use type hints on all arguments and return values.
- Include a docstring with the formal definition. If the docstring contains LaTeX, use a raw string (prefix with `r"""`).
- One function per metric; keep it focused.

Example skeleton:
```python
def my_metric(embeddings: np.ndarray, labels: np.ndarray) -> float:
	 r"""
	 Computes the MyMetric score.
	 Formal definition: ...
	 """
	 # implementation
```

---

## Contributing Benchmark Data

Benchmark data must follow the schema described in [benchmark/README.md](benchmark/README.md) (see also [benchmark/schema.md](benchmark/schema.md)).

- Do not commit video files; use stable, public URLs.
- Fill all required fields and provide verifiable ground truth.
- Add new records to the appropriate results file (e.g., `benchmark/results/clip_results.json`).

---

## Code Style

- Use [ruff](https://docs.astral.sh/ruff/) for linting and formatting.
- Type hints are required on all public functions.
- Every module (file) should start with a short docstring.
- Keep code readable and well-documented, but don't over-engineer.

---

## Running Tests

Run all tests with:
```sh
pytest
```

---

## Reaching the Team

Open a GitHub issue for bugs, questions, or proposals. For private matters, email the UW InfoSeeking Lab (see [lab website](https://infoseeking.org)).

Response times may vary; this project is run by a small academic team.
