# World Models: A Primer

## What Is a World Model?

In 1943, the British psychologist Kenneth Craik proposed in [*The Nature of Explanation*](https://archive.org/details/natureofexplanat0000crai) that the mind works by constructing small-scale models of reality — internal representations that can be manipulated to anticipate events before they happen. Rather than reacting to the world as it presents itself, an intelligent agent carries a compact simulation: run the model forward, observe the predicted outcome, adjust behavior accordingly.

This idea predates modern AI by decades, but it describes what the field now calls a *world model*: a learned representation of an environment that supports prediction. Given a current state — a physical scene, a robot's sensor readings, a game board — a world model estimates what will happen next.

---

## How World Models Differ from Large Language Models

Large language models (LLMs) such as GPT-4 or Claude are trained to predict the next token in a sequence of text. They are extraordinarily capable at tasks that can be framed as text in, text out: summarization, question answering, code generation, translation. Their internal representations encode statistical relationships across language, including a great deal of implicit knowledge about the physical world absorbed from written descriptions of it.

But token prediction is not the same as physical state prediction. When an LLM is asked what happens when a glass is pushed to the edge of a table, it generates a plausible continuation of the sentence — it does not simulate the trajectory of the glass. Its answer may be correct, but it is correct in the way a well-read person who has never dropped anything might be correct: by pattern-matching to descriptions rather than by modeling the underlying dynamics.

World models are trained differently. They learn from multimodal inputs — video, sensor streams, simulated physics — and their objective is predictive accuracy over physical states, not linguistic plausibility. This distinction matters for robustness: LLMs can be confidently wrong about physical outcomes in ways that reveal the limits of text-only training. World models fail too, but they fail differently and often more diagnostically.

---

## Key Frameworks and Recent Systems

The modern research program on learned world models was consolidated by [Ha and Schmidhuber in a 2018 paper](https://arxiv.org/abs/1803.10122) that trained an agent to play video games using a compressed internal model of the environment. The agent could dream — plan and train within its own internal simulation rather than in the actual environment.

Yann LeCun has proposed a more ambitious architecture called the [Joint Embedding Predictive Architecture (JEPA)](https://openreview.net/forum?id=BZ5a1r-kVsf). Rather than predicting raw pixels or tokens, JEPA learns to predict abstract representations — the essential structure of what will happen, without committing to irrelevant perceptual detail. [Meta's V-JEPA 2](https://arxiv.org/abs/2506.09985) (2025) applies this approach to video understanding and physical scene prediction. Other recent systems include Google DeepMind's [Genie 3](https://deepmind.google/research/publications/genie-3/), which generates interactive environments from a single image, and [NVIDIA Cosmos](https://arxiv.org/abs/2501.03575), a family of world foundation models designed for robotics, trained on large-scale video of physical environments.

---

## Why the Field Is Underdeveloped

Despite this momentum, the infrastructure gap between world models and LLMs is large. LLMs benefit from accumulated tooling: standardized benchmarks ([MMLU](https://arxiv.org/abs/2009.03300), [BIG-Bench](https://arxiv.org/abs/2206.04615), [HELM](https://arxiv.org/abs/2211.09110)), evaluation harnesses, model APIs, and a shared vocabulary for comparing systems. A researcher who wants to evaluate a new LLM can do so in an afternoon using existing infrastructure.

No equivalent exists for world models. There is no agreed-upon benchmark format, no shared schema for physical scene data, and evaluation methods are fragmented across research groups. The compute required to train competitive world models is concentrated in a small number of industrial labs — the same labs best positioned to set de facto standards, with limited incentive to share them.

The result is that a research group at a university, or a practitioner at a resource-constrained institution, has no straightforward path to building on or evaluating world model systems.

---

## What OpenWorld Is Doing About It

OpenWorld is a research toolkit developed at the University of Washington aimed at lowering that barrier. Rather than training new world models from scratch, it provides the infrastructure needed to use existing ones: a benchmark dataset of physical scene clips with ground-truth annotations, a schema for recording and comparing model predictions, and adapter modules that connect models to the evaluation pipeline without requiring large-scale compute.

The initial benchmark places three model classes — an LLM, a vision model, and a world model — on the same physical prediction tasks, making their differences concrete and measurable. The longer-term goal is shared evaluation infrastructure that any research group can use and extend, independent of institutional affiliation or hardware budget.

The tooling gap is not a fundamental problem. It is an organizational and resource problem that open infrastructure can address.
