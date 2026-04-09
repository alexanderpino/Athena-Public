# Zig Research Plan: Phase 0

This plan outlines the steps for setting up your environment and mastering the foundational philosophy of Zig.

## Goal: Master the "Zen of Zig" and the Command Line Toolchain.

### Step 1: Environment Setup
- [ ] **Install Zig:** Download the latest master build from [ziglang.org/download](https://ziglang.org/download/).
- [ ] **Verify Installation:** Run `zig version` and ensure it reflects the expected version.
- [ ] **IDE Setup:** Install the Zig extension for your preferred editor (VS Code, Vim, Emacs, etc.).

### Step 2: The Zen of Zig
- [ ] **Read the Zen:** Visit the [Zen section](https://ziglang.org/documentation/master/#Zen) in the Language Reference.
- [ ] **Analysis:** Write a brief (1-sentence) explanation of what "No hidden control flow" and "No hidden memory allocations" means in practice.
- [ ] **Cross-Reference:** Read the "Introduction" in the Zig Guide and note how it describes these same concepts.

### Step 3: Hello World (The Toolchain)
- [ ] **Write it:** Create a file named `hello.zig` with a basic print statement.
- [ ] **Run it:** Execute `zig run hello.zig`.
- [ ] **Build it:** Execute `zig build-exe hello.zig` and examine the resulting binary size.
- [ ] **Test it:** Create a simple test block in `hello.zig` and run `zig test hello.zig`.

### Step 4: Language Reference Exploration
- [ ] **Map the Reference:** Open the [Language Reference](https://ziglang.org/documentation/master/) and find the sections for:
  - `const` vs `var`
  - Comments
  - Integers
- [ ] **Compare:** Look for these same topics in the [Zig Guide](https://zig.guide/language-basics/variables/).

### Step 5: Start Ziglings
- [ ] **Clone the Repo:** `git clone https://github.com/ratfactor/ziglings`
- [ ] **Begin Exercises:** Complete exercises `001_hello.zig` and `002_comments.zig`.
