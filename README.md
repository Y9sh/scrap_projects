# 🧪 scrap_projects

A collection of experimental AI/NLP modules and half-formed ideas — part playground, part prototype. These aren't polished projects (yet), but they’re real pieces of something I’m building.

## 📂 Project Structure

### 🧠 `emodetector/` *(WIP NLP Emotion Pipeline)*
A lightweight, modular text processor built to detect emotional tone in raw input. It’s stitched together from a bunch of preprocessing tools and custom logic.

#### Key Modules:
- `main.py` – Runs the full pipeline and returns labeled outputs like `[EMO_HAPPY]`, etc.
- `contraction.py` – Expands contractions like “don’t” → “do not”
- `negation.py` – Tracks negation patterns for sentiment shifts
- `slang.py` – Normalizes slang terms
- `emoji.py` – Detects and interprets emoji as emotional signals
- `entity_emphasis.py` – Boosts emotional weight on key named entities
- `pos_guesser.py` – Simple POS pattern matcher (used in logic tweaks)
- `tokenizer.py` – Basic token splitting and cleaning
- `mainPipeline.py` – Possibly the combined runner for all components

> It's messy, modular, and kinda fun to break.

---

### 🧬 `injection/`
A sketchpad for mood-driven prompt engineering. Currently contains:
- `mood_primers`: dictionary of moods with prompt examples
- `scenario` and prompt templates
- No direct integration with transformers yet — still conceptual

---

## ✅ Status
- Some parts like `emodetector/main.py` are working and return output.
- Others (like `injection/`) are just structure, not functional yet.

This repo is mostly a work-in-progress — feel free to poke around if you're curious.

---

## 🧑‍🔬 Why share scraps?
Because the path to polished ideas is full of weird, broken, exciting half-projects. This repo is a slice of that process.

---

> ⚠️ Not production ready. No unit tests. No regrets.
