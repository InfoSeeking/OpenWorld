# Contributing to OpenWorld

Thanks for your interest. This is an early-stage research project, so contributions are welcome but the codebase and data formats are still stabilizing. When in doubt, open an issue before writing code.

---

## Adding Benchmark Clips

New clips must conform to the schema defined in [benchmark/schema.md](benchmark/schema.md). Before submitting:

1. Confirm the clip has a stable, publicly accessible `video_url`. Do not commit video files to the repository.
2. Fill all required fields. The `scenario_type` must be one of the enumerated values in the schema; if your clip requires a new type, propose it first (see below).
3. Verify that `ground_truth` is written from direct observation of the clip, not inferred from model outputs.
4. Add your record(s) to `benchmark/results/clip_results.json` and open a pull request with a brief description of what the clips test and where they came from.

Clips that cannot be independently verified against a ground truth will not be merged.

---

## Proposing a New Adapter Domain

Open a GitHub issue using the **Adapter Proposal** label and include:

- The target domain and what real-world task it addresses.
- The data format (modality, typical input shape, publicly available example datasets).
- Which world model architecture you plan to connect to.
- Any known access or licensing constraints on the data.

Proposals without example data sources are unlikely to be prioritized. If you have an existing implementation, link to it.

---

## Code Style

This is a research toolkit, not a production system. The bar is: readable, documented at the function level, and not broken. Specifically:

- Python: follow PEP 8, use type hints on public function signatures, keep functions short.
- No external dependencies without justification. If you need a library, add it to `requirements.txt` and explain why in your PR.
- Tests are appreciated but not required for data contributions. They are expected for adapter code.

---

## Reaching the Team

Open a GitHub issue for bugs, questions, or proposals. For anything that should not be public, email the UW InfoSeeking Lab at the address listed on the [lab website](https://infoseeking.org).

Response times will vary. This project is run by a small academic team alongside other research commitments.
