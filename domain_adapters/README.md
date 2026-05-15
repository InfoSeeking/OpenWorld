
# Domain Adapters (Phase 2)

**This directory (`domain_adapters/`) is reserved for DOMAIN adapters, not model adapters.**

## What are Domain Adapters?
Domain adapters are connectors for domain-specific data sources. They transform raw data from specialized fields into a standardized format that OpenWorld benchmarks can consume.

**Examples:**
- Satellite imagery for climate science
- Electronic health records for healthcare
- Sensor data for agriculture

Domain adapters are essential for applying world model evaluation to real-world, cross-domain problems. They handle the unique preprocessing, normalization, and structuring required for each domain.

---

## How are Domain Adapters Different from Model Adapters?
- **Domain adapters** (this directory):
	- Convert raw domain data (e.g., images, records, sensor streams) into benchmark-ready datasets.
	- Example: A climate adapter that loads and preprocesses satellite data for evaluation.
- **Model adapters** (`openworld/models/`):
	- Wrap AI models (e.g., V-JEPA 2, DreamerV3) to conform to the `BaseWorldModel` interface.
	- Convert model outputs into a format that OpenWorld metrics can consume.

**Do not confuse these!**
- Domain adapters = data connectors
- Model adapters = model wrappers

---

## Status
Domain adapters are coming in **Phase 2**. See [ROADMAP.md](../ROADMAP.md) for details and planned domains.

For now, see `openworld/models/` for model adapters and `data/` for evaluation datasets.
