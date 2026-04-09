---
name: deep-learning-lab
description: A structured workflow for learning a new technology from scratch to expertise. Make sure to use this skill whenever a user mentions mastering a language, framework, library, or codebase, or asks for a "learning plan," "syllabus," "roadmap," or "mastery strategy." It handles syllabus generation, resource curation (books/docs), and identifies idiomatic patterns using a Credibility Score matrix.
created: 2026-04-09
auto-invoke: true
---

# 🧬 Deep Learning Lab (DLL)

> **Philosophy**: Expertise is the result of structured immersion, not accidental reading. Official docs are the "Source of Truth"; community sites are "Field Reports" that require validation.

## 1. Intent & Triggers

Use this skill whenever:
- The user wants to learn a new language, framework, library, or architectural pattern.
- The user needs to "onboard" onto a complex existing codebase.
- The user asks for a learning roadmap, syllabus, or "mastery path."

## 2. Resource Scoring & Credibility Matrix

When gathering information, assign a **Credibility Score (CS)** to every source:

| Tier | Source Type | CS | Rule |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Official Docs, Core Repos, Standards (W3C, ISO), Authoritative Handbooks. | **1.0** | **Source of Truth.** If Tier 1 says X and Tier 3 says Y, X is the canonical fact. |
| **Tier 2** | Industry Leader Blogs (e.g., Martin Fowler, Kent Beck), MDN, Official Tutorials. | **0.8** | **High Fidelity.** Generally safe, but verify against Tier 1 for latest versions. |
| **Tier 3** | StackOverflow, Reddit, Medium, Personal Blogs, Community Forums. | **0.4** | **Field Report.** Useful for "how it's used in the wild," but requires **Double Validation** (confirmation from 2+ Tier 3 sources OR 1 Tier 1/2 source). |

## 3. The Five-Phase Mastery Workflow

### 🌑 Phase 0: Scoping & The "Big Picture"
1.  **Define the Goal:** What does "expertise" look like for this specific tech?
2.  **Locate the "Canonical Home":** Identify the official documentation URL and primary repo.
3.  **Construct the Syllabus:** Break down the tech into:
    *   **Level 1: The Core** (Syntax, Tooling, "Hello World").
    *   **Level 2: The Idiom** (The "Standard Way" to do things).
    *   **Level 3: The Depths** (Concurrency, Memory, Metaprogramming, Internals).
    *   **Level 4: The Architect** (Scaling, Testing, Integration, Anti-Patterns).

### 🌱 Phase 1: Rapid Immersion (The "Hello World" Loop)
1.  **Setup & Tooling:** Don't just read; install. Get a local environment running.
2.  **The "15-Minute Win":** Build a minimal functional prototype (API, CLI, UI).
3.  **Discovery:** Map the directory structure and core configuration files.

### 📚 Phase 2: Structured Reading (The "Deep Book" Phase)
1.  **Select a Core Text:** Find a highly-rated book (PDF).
2.  **PDF Ingestion:** 
    *   Use the `pdf` skill to split the book into manageable chunks (e.g., by chapter or 100-page increments).
    *   Read/Analyze chunks sequentially.
    *   Extract key concepts and save to `.context/data/deep-learning-lab/[tech-name]/summary.md`.

### 🔍 Phase 3: The Pattern Audit (Truth vs. Practice)
1.  **Search & Validate:** Search for specific implementation patterns on the web.
2.  **Apply Scoring:** Use the Credibility Matrix. 
    *   If a Tier 3 (SO) answer is found, **must** cross-reference with Tier 1 (Docs).
    *   Identify "Legacy Patterns" (outdated advice) vs. "Modern Idioms."

### 🏛️ Phase 4: Mastery Project (The Synthesis)
1.  **Define a Capstone:** A project that exercises ALL layers of the syllabus.
2.  **Build with TDD:** Use Test-Driven Development (Protocol 175) to ensure correctness.
3.  **Architecture Review:** Self-audit for anti-patterns and performance bottlenecks.

## 4. Output Standards

- **Roadmap:** Always provide a visual or list-based roadmap at the start.
- **Citations:** Every claim must be cited with its **Credibility Score**.
- **The "Cheat Sheet":** Maintain a living document of "Idioms vs. Anti-Patterns" for the technology.

## 5. Interaction with Other Skills

- **`pdf` skill:** Essential for Phase 2. Use it to `split` and `extract_text` from books.
- **`codebase_investigator`:** Use if learning an existing codebase.
- **`research` workflow:** Use for Phase 3 deep-dives.

---
#skill #learning #research #expertise #pedagogy
