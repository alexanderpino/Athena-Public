# 🧬 libunwind Mastery Strategy

This strategy follows the **Deep Learning Lab (DLL)** methodology to transform you from a user of `libunwind` to an expert in stack unwinding internals.

---

## 🌑 Phase 0: Scoping & The "Big Picture"

### 1. Define the Goal
Expertise in `libunwind` means:
- **Level 1 (Core):** Successfully integrating `libunwind` for local backtracing in C/C++ applications.
- **Level 2 (Idiom):** Correct usage of `unw_getcontext`, `unw_init_local`, and `unw_step` with proper error handling and symbol demangling.
- **Level 3 (Depths):** Understanding DWARF/CFI (`.eh_frame`), Signal Safety, and implementing Remote Unwinding via `ptrace` or custom accessors.
- **Level 4 (Architect):** Implementing custom unwinding for JIT engines or optimized profilers with caching.

### 2. Canonical Home
- **Primary Implementation (nongnu):** [http://www.nongnu.org/libunwind/](http://www.nongnu.org/libunwind/) (CS: 1.0)
- **Secondary Implementation (LLVM):** [https://libunwind.llvm.org/](https://libunwind.llvm.org/) (CS: 1.0)
- **Repository:** [https://github.com/libunwind/libunwind](https://github.com/libunwind/libunwind)

### 3. The Syllabus
| Level | Focus Area | Key Concepts |
| :--- | :--- | :--- |
| **L1** | Local Backtrace | `unw_getcontext`, `unw_init_local`, `unw_step`, `unw_get_proc_name`. |
| **L2** | Performance & Symbols | Caching (`UNW_CACHE_ALL`), Demangling (`abi::__cxa_demangle`), Cursor management. |
| **L3** | Internals & Remote | DWARF CIE/FDE, `.eh_frame` parsing, `ptrace` integration, `unw_accessors_t`. |
| **L4** | Advanced Integration | Signal-safe unwinding, JIT frame registration, custom address spaces. |

---

## 🌱 Phase 1: Rapid Immersion

### 1. Setup
- Install `libunwind-dev` (Debian/Ubuntu) or `libunwind` (Arch).
- Verify build with: `g++ main.cpp -lunwind`.

### 2. The "15-Minute Win"
Create a `backtrace_logger.cpp` that:
- Captures the stack when a specific function is called.
- Iterates using `unw_step`.
- Prints function names and instruction pointers.

---

## 📚 Phase 2: Structured Reading

### 1. Core Texts
- **"DWARF Debugging Information Format" Standard:** Focus on the Call Frame Information (CFI) section. (CS: 1.0)
- **"System V Application Binary Interface":** Essential for understanding how registers are saved and restored during calls. (CS: 1.0)

### 2. Internal Research
- Study the `libunwind` source code, specifically `src/dwarf/Gparser.c` and `src/mi/Gstep.c`.

---

## 🔍 Phase 3: The Pattern Audit

| Pattern | Source | CS | Verdict |
| :--- | :--- | :--- | :--- |
| **Local-Only Optimization** | Docs | 1.0 | Use `#define UNW_LOCAL_ONLY` before `#include <libunwind.h>` for better performance in local-only apps. |
| **Signal Handler Unwinding** | Community | 0.4 | **Double Validate:** libunwind is signal-safe, but `malloc` (often used in `demangle`) is NOT. Use a pre-allocated buffer. |
| **Remote Unwinding** | libunwind-ptrace | 1.0 | Requires `_UPT_accessors` and `ptrace(PTRACE_ATTACH)`. |

---

## 🏛️ Phase 4: Mastery Project (The Synthesis)

### The Capstone: "GhostProfiler"
Build a standalone CLI tool that:
1.  **Attaches** to a running process via PID (`ptrace`).
2.  **Samples** the stack at regular intervals using `libunwind` remote API.
3.  **Aggregates** the traces into a Flame Graph compatible format.
4.  **Handles** stripped binaries by reporting raw offsets if symbols are missing.

---

## 🛠️ The "libunwind" Cheat Sheet

### Idioms vs. Anti-Patterns
- **✅ DO:** Use `unw_init_local` inside the function where you want the trace to start.
- **✅ DO:** Use `unw_get_proc_name` but remember it may fail for static functions or stripped binaries.
- **❌ DON'T:** Assume `backtrace()` from `libc` is as fast as `libunwind` with caching enabled.
- **❌ DON'T:** Call `abi::__cxa_demangle` inside a signal handler (it allocates memory).

---
*Created via Deep Learning Lab Skill*
