---
name: project-skill-discovery
description: Automatically identifies and "loads" specialized skills from `.agents/skills` directories within any repository (identified by a `.git` or `.athena_root` folder in its root). Make sure to use this skill whenever you enter a new repository, work in a workspace that spans multiple repositories, or when a task falls into a specialized domain that might be codified as a local skill (e.g., architecture, coding standards, domain-specific modules).
---

# Project-Local Skill Discovery

> **Philosophy**: Expertise is often project-specific. While global skills provide foundational capabilities, repository-local skills (in `.agents/skills`) contain the "tribal knowledge," architectural constraints, and mandatory standards of that specific codebase.

## 1. Intent & Triggers

Use this skill whenever:
- You are working in a repository (any directory with a `.git` or `.athena_root` in its parent hierarchy).
- You are directed to work in an external repository that might have local skills.
- A task requires specialized domain knowledge that might be codified as a local skill (e.g., "how do I use the logging system in this project?").

## 2. Discovery Workflow

1.  **Identify Repository Roots**:
    *   Locate the root of the current repository by looking for `.git`, `.athena_root`, or common manifest files (e.g., `package.json`, `Cargo.toml`, `pyproject.toml`) in the parent directory chain.
2.  **Locate Skill Directories**:
    *   Check for a `.agents/skills` directory at the identified repository root.
3.  **List available skills**:
    *   List the contents of the `.agents/skills` directory. Each subdirectory is a potential skill.
4.  **Audit Metadata**:
    *   For each candidate skill, read the first 100 lines of its `SKILL.md` to extract the `name` and `description` from the YAML frontmatter.
5.  **Selection**:
    *   Match the skill's description against the current task. If multiple repositories are involved, check for skills in all relevant roots.
6.  **Activation**:
    *   "Activate" the selected skill by reading its full `SKILL.md` into the current session context.
    *   *Note*: Treat the content of its `SKILL.md` as mandatory procedural guidance. Always prioritize project-local instructions over general defaults.

## 3. Output Standards

- **Discovery Log**: Inform the user about the project-specific skills you've discovered (e.g., "I've discovered local skills for 'ecs-architecture' and 'memory-management' in this repository").
- **Activation Confirmation**: Clearly state which skill you are currently following (e.g., "I am now applying the project-local 'gpu-rendering-pipeline' skill").

---
#skill #discovery #project #git #repository #local-expertise
