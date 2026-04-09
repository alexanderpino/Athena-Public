# 🧬 Zig Mastery Syllabus (v0.14.0/Master)

This syllabus follows the **Deep Learning Lab (DLL)** methodology, structuring learning into four progressive levels of expertise. It serves as the roadmap for mastering the Zig programming language.

## 🏛️ Phase 0: The Big Picture
- **Primary Goal:** Achieve full mastery of Zig for high-performance, memory-safe (spatial safety), and reliable software engineering.
- **Canonical Home:** [ziglang.org](https://ziglang.org) (Tier 1)
- **Primary Repo:** [github.com/ziglang/zig](https://github.com/ziglang/zig) (Tier 1)
- **Status:** Phase 0 Initiated.

---

## 🏗️ Level 1: The Core (Syntax & Basic Tooling)
**Objective:** Learn how to write basic Zig, use the compiler, and understand the fundamental type system.
- [ ] **Introduction & Philosophy:** Why Zig? (No hidden control flow, no hidden allocations, no preprocessor).
- [ ] **Setup:** Installing Zig, `zig build-exe`, `zig run`, `zig test`.
- [ ] **Basic Syntax:** Constants (`const`), Variables (`var`), Semicolons, Comments (`///`).
- [ ] **Primitive Types:** Integers (`u8`-`u128`, `isize`, `usize`), Floats, Booleans, `void`, `noreturn`.
- [ ] **Control Flow:** `if`, `while`, `for`, `switch`, `blocks`.
- [ ] **Functions:** Parameters, return types, `inline` functions.
- [ ] **Testing:** The `test` block, `std.testing` namespace.

## 🧱 Level 2: The Idiom (The "Standard Way")
**Objective:** Write Zig that looks like Zig. Understand patterns for safety and clarity.
- [ ] **Error Handling:** Error sets, error unions (`!T`), `try`, `catch`, `errdefer`.
- [ ] **Optionals:** `?T`, `orelse`, `if` with optionals.
- [ ] **Structures:** `struct`, `packed struct`, `extern struct`, field defaults.
- [ ] **Enums & Unions:** Tagged unions, exhaustive switching.
- [ ] **Pointers & Slices:** Single-item vs. Many-item, `*T` vs `[]T`, sentinel-terminated (`[*:0]T`).
- [ ] **Defer:** Resource management pattern (`defer`, `errdefer`).
- [ ] **The Standard Library:** Navigating `std`, core modules (`std.mem`, `std.fs`, `std.io`).

## 🌪️ Level 3: The Depths (Advanced Concepts & Internals)
**Objective:** Leverage Zig's most powerful features: metaprogramming and precise memory control.
- [ ] **Comptime:** The "Killer Feature." Compile-time variables, types as values, generic types.
- [ ] **Memory Management:** Allocators (`std.mem.Allocator`), Stack vs. Heap, FixedBufferAllocator, GPA.
- [ ] **Reflection:** `@typeInfo`, `@typeName`, `@field`, generic function generation.
- [ ] **Vectors & SIMD:** `@Vector`, manual SIMD optimizations.
- [ ] **Advanced Pointers:** Alignment, `volatile`, pointer casting, `allowzero`.
- [ ] **Build System:** `build.zig`, adding dependencies, custom build steps.

## 🏛️ Level 4: The Architect (Systems & Integration)
**Objective:** Build production-grade, interoperable, and highly optimized systems.
- [ ] **C Interop:** `@cImport`, linking C libraries, Zig as a C compiler (`zig cc`).
- [ ] **Cross-Compilation:** Targeting different OS/Architectures with one flag.
- [ ] **Concurrency:** (Tracking) The current state of `async`/`await` and threading models.
- [ ] **Optimality:** Build modes (`ReleaseFast`, `ReleaseSafe`, `ReleaseSmall`), inline assembly.
- [ ] **The Toolchain:** `zig fetch`, package manager, building libraries vs. executables.
- [ ] **Capstone:** Build a high-performance system (e.g., a custom memory allocator or a simple web server from scratch).

---

## 📜 Resource Matrix

| Tier | Source | Credibility Score (CS) |
| :--- | :--- | :--- |
| **Tier 1** | [Official Language Reference](https://ziglang.org/documentation/master/) | **1.0** |
| **Tier 1** | [Zig Std Library Docs](https://ziglang.org/documentation/master/std/) | **1.0** |
| **Tier 2** | [Zig by Example](https://zig-by-example.com/) | **0.8** |
| **Tier 2** | [Zig News](https://zig.news/) | **0.8** |
| **Tier 3** | [Zig Community Wiki](https://github.com/ziglang/zig/wiki) | **0.4** |
| **Tier 3** | [Reddit (r/Zig)](https://reddit.com/r/Zig) | **0.4** |

---
*Created via Deep Learning Lab (DLL) - Phase 0 Complete.*
