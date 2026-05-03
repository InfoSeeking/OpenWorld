# Adapters

Implementations are not yet available. Development begins Summer 2026. See [ROADMAP.md](../ROADMAP.md) for milestones.

---

## What Is a World Adapter?

A world adapter is a modular connector between domain-specific input data and an existing open world model architecture. The adapter handles the translation work: converting raw domain data into the tensor format a given world model expects, and mapping the model's output back into a structured prediction record that the OpenWorld benchmark can score.

Adapters do not modify the underlying world model. They do not retrain it. They standardize the data pipeline so that a practitioner with domain-specific data can evaluate an existing model without writing custom preprocessing and output-parsing code from scratch.

---

## Planned Domains (Phase 2, Fall 2026–Spring 2027)

**Climate and environment** — satellite and remote sensing imagery, weather observation sequences, land use time series. Target tasks: environmental state change prediction, anomaly detection.

**Health** — procedural video from clinical or care settings, structured time series from monitoring devices. Target tasks: activity prediction, state progression estimation. Adapters in this domain will not process identifiable patient data; inputs are assumed to be de-identified before ingestion.

**Agriculture** — field imagery, crop sensor readings, growth-stage sequences. Target tasks: crop state estimation, yield trajectory prediction.

---

## Intended Interface

Each adapter exposes two functions:

- `preprocess(raw_input) → model_input` — converts domain data into the tensor or frame sequence format expected by the target world model architecture.
- `postprocess(model_output) → prediction_record` — converts raw model output into a benchmark-compatible record conforming to the schema defined in [benchmark/schema.md](../benchmark/schema.md).

Adapters are stateless. They carry no model weights and have no training loop.
