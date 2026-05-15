"""
transform.py

Reshapes WorldModelDemo clips.json into the OpenWorld benchmark schema.

Usage:
    python benchmark/transform.py \
        --input  <path-or-url to clips.json> \
        --output benchmark/results/clip_results.json

If --input is omitted, the script fetches the canonical demo file from GitHub.
"""

import argparse
import json
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SOURCE_URL = (
    "https://raw.githubusercontent.com/InfoSeeking/WorldModelDemo/main/data/clips.json"
)

VIDEO_BASE_URL = "https://InfoSeeking.github.io/WorldModelDemo/"

# Model name  (canonical_name, version)
# The source embeds model names as free-text strings; this mapping normalises them.
MODEL_METADATA: dict[str, dict[str, str]] = {
    "Claude 4.5 Haiku": {"name": "Claude 4.5 Haiku", "version": "4.5"},
    "Amazon Nova Pro":  {"name": "Amazon Nova Pro",  "version": "1.0"},
    "Meta VJEPA-2":     {"name": "Meta V-JEPA",      "version": "2.0"},
}

# Per-clip scenario_type overrides.
# The source does not carry a scenario_type field; all clips are physical by
# default. Add entries here as the benchmark expands to causal / predictive clips.
SCENARIO_OVERRIDES: dict[str, str] = {}


# ---------------------------------------------------------------------------
# Transform logic
# ---------------------------------------------------------------------------

def resolve_model(raw_name: str) -> dict[str, str]:
    """Return a {name, version} dict for a raw model string from the source."""
    if raw_name in MODEL_METADATA:
        return MODEL_METADATA[raw_name]
    # Fallback: keep the string as-is, mark version unknown.
    return {"name": raw_name, "version": "unknown"}


def transform_clip(clip: dict) -> dict:
    """Convert one source clip record to the OpenWorld benchmark schema."""
    clip_id: str = clip["id"]
    outputs: dict = clip.get("outputs", {})

    llm = outputs.get("llm", {})
    vision = outputs.get("vision", {})
    world_model = outputs.get("world_model", {})

    video_path: str = clip.get("video", "")
    if video_path.startswith(("http://", "https://")):
        video_url = video_path
    else:
        video_url = VIDEO_BASE_URL + video_path

    return {
        "clip_id":            clip_id,
        "scenario_type":      SCENARIO_OVERRIDES.get(clip_id, "physical"),
        "video_url":          video_url,
        "pause_frame_seconds": clip.get("pause_at"),
        "ground_truth":       clip.get("ground_truth", ""),
        "llm_output":         llm.get("prediction", ""),
        "vision_output":      vision.get("prediction", ""),
        "world_model_output": world_model.get("prediction", ""),
        "analysis":           clip.get("analysis", ""),
        "models": {
            "llm":         resolve_model(llm.get("model", "")),
            "vision":      resolve_model(vision.get("model", "")),
            "world_model": resolve_model(world_model.get("model", "")),
        },
    }


def load_source(path_or_url: str) -> list[dict]:
    if path_or_url.startswith(("http://", "https://")):
        with urllib.request.urlopen(path_or_url) as response:  # noqa: S310
            return json.loads(response.read().decode())
    with open(path_or_url, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Transform WorldModelDemo clips to OpenWorld schema.")
    parser.add_argument("--input",  default=SOURCE_URL, help="Path or URL to source clips.json")
    parser.add_argument("--output", default="benchmark/results/clip_results.json",
                        help="Output path for transformed records")
    args = parser.parse_args()

    print(f"Loading source from: {args.input}")
    source_clips = load_source(args.input)
    print(f"  {len(source_clips)} clip(s) found")

    transformed = [transform_clip(c) for c in source_clips]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(transformed, fh, indent=2, ensure_ascii=False)

    print(f"Wrote {len(transformed)} record(s) to {output_path}")

if __name__ == "__main__":
    main()
