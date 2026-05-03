# Benchmark Clip Schema

This schema defines a single record in the OpenWorld benchmark dataset. It is designed to be extended without breaking existing records: additional models slot in as new top-level string keys (following the `llm_output` / `vision_output` / `world_model_output` pattern) and as new entries under `models`. New scenario types are added to the `scenario_type` enumeration as the benchmark grows. Consumers should treat unrecognized keys as optional rather than raising errors.

---

## Field Reference

| Field | Type | Description |
|---|---|---|
| `clip_id` | string | Unique identifier for the clip. Recommended format: `<domain>-<sequence>`, e.g. `phys-0042`. |
| `scenario_type` | string (enum) | Category of reasoning required. Current values: `physical`, `causal`, `predictive`. |
| `video_url` | string | URL pointing to the clip file or stream. Should be a stable, versioned reference. |
| `pause_frame_seconds` | number | Timestamp (in seconds) at which the clip pauses and models are asked to predict what happens next. |
| `ground_truth` | string | Plain-language description of what actually occurs after the pause frame. This is the reference answer for scoring. |
| `llm_output` | string | The language model's prediction, recorded verbatim or summarized to a single sentence. |
| `vision_output` | string | The vision model's prediction in the same format. |
| `world_model_output` | string | The world model's prediction in the same format. |
| `analysis` | string | Qualitative summary of how the three outputs compare to each other and to ground truth. Written by a human annotator or a structured post-processing step. |
| `models` | object | Version metadata for the three models used. Each key (`llm`, `vision`, `world_model`) holds an object with `name` (string) and `version` (string). |

---

## Example Record

```json
{
  "clip_id": "phys-0042",
  "scenario_type": "physical",
  "video_url": "https://example.org/clips/phys-0042.mp4",
  "pause_frame_seconds": 4.1,
  "ground_truth": "The glass tips off the edge of the table and shatters on the floor.",
  "llm_output": "The glass will fall and break.",
  "vision_output": "The glass appears to be moving toward the edge; likely to fall.",
  "world_model_output": "Predicts the glass reaches the tipping point at ~4.3s and falls with high confidence.",
  "analysis": "All three models correctly anticipated the fall. The world model provided the most precise timing estimate. The LLM response was accurate but underspecified. The vision model hedged with 'likely', reflecting uncertainty about the exact trajectory.",
  "models": {
    "llm": {
      "name": "Claude Haiku",
      "version": "4.5"
    },
    "vision": {
      "name": "Amazon Nova Pro",
      "version": "1.0"
    },
    "world_model": {
      "name": "Meta V-JEPA",
      "version": "2.0"
    }
  }
}
```

---

## Extending the Schema

**Adding a model:** Add a new top-level key for the model's output (e.g., `"new_model_output": "..."`) and a corresponding entry under `models`. Existing records without the key are treated as having no output for that model.

**Adding a scenario type:** Append the new value to the `scenario_type` enumeration in this document and update the benchmark data generation pipeline accordingly. Current values: `physical`, `causal`, `predictive`.
