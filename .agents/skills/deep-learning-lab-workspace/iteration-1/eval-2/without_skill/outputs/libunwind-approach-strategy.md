# Mastering libunwind: A Structured Approach Strategy

`libunwind` is a powerful, low-level library designed to determine the call chain (stack backtrace) of a program. It is essential for building debuggers, profilers, and sophisticated exception-handling mechanisms.

## Prerequisites
Before diving into `libunwind`, ensure you have a solid foundation in the following:
- **C/C++ Programming:** Intermediate to advanced knowledge.
- **Computer Architecture:** Understanding of CPU registers (IP/PC, SP, BP/FP) and calling conventions (e.g., x86-64 System V ABI).
- **Executable Formats:** Familiarity with ELF, symbol tables, and how programs are laid out in memory.
- **Operating System Internals:** Knowledge of process memory maps (`/proc/self/maps`) and signal handling.

---

## 🗺️ Learning Roadmap

### Phase 1: Local Introspection (The Basics)
*Goal: Programmatically capture and print the call stack of the current process.*

1.  **Understand the Core API:**
    - `unw_getcontext(3)`: Capturing the current machine state.
    - `unw_init_local(3)`: Initializing a cursor for the current stack.
    - `unw_step(3)`: Moving the cursor up the stack.
    - `unw_get_proc_name(3)`: Resolving instruction pointers to function names.
2.  **Exercise:** Write a "Hello Backtrace" program that prints the function names and instruction pointers of all frames in the current call stack.
3.  **Intermediate Exercise:** Use `unw_get_reg` to inspect specific register values (like `RSP` or `RAX`) at different points in the stack.

### Phase 2: Remote Unwinding (The Debugger Path)
*Goal: Unwind the stack of a different process (useful for building debuggers).*

1.  **Learn about Address Spaces:**
    - Understand `unw_create_addr_space`.
    - Explore "Accessors": Callbacks `libunwind` uses to read memory from a target process.
2.  **Ptrace Integration:**
    - Use `ptrace(PTRACE_ATTACH, ...)` to pause a child process.
    - Use `unw_init_remote` to initialize unwinding for that process.
3.  **Exercise:** Create a minimal CLI tool that takes a PID as input and prints its current backtrace.

### Phase 3: Signal Safety & Performance (The Profiler Path)
*Goal: Use libunwind safely in high-frequency, performance-critical environments.*

1.  **Signal Safety:**
    - Identify which `libunwind` functions are **Async-Signal-Safe**.
    - Learn why `unw_get_proc_name` is generally *not* safe inside a signal handler (due to `malloc` or `dladdr`).
2.  **Caching and Performance:**
    - Research `unw_set_caching_policy`.
    - Experiment with `UNW_LOCAL_ONLY` for performance gains when remote unwinding is not needed.
3.  **Exercise:** Implement a basic sampling profiler that triggers on `SIGPROF` and records backtraces into a buffer.

### Phase 4: Under the Hood (Expert Level)
*Goal: Understand the "magic" of how unwinding works without frame pointers.*

1.  **DWARF & CFI:**
    - Study **DWARF CFI (Call Frame Information)**.
    - Use `readelf -w` to inspect `.eh_frame` and `.debug_frame` sections.
2.  **Dynamic Code (JIT):**
    - Learn how to register dynamically generated code with `libunwind` using `_U_dyn_register`.
3.  **Advanced Exercise:** Manually parse a simple DWARF CFI entry to understand how `libunwind` calculates the return address of a frame.

---

## 📚 Key Resources

### Official Documentation
- [HP/Savannah libunwind (The Original)](https://www.nongnu.org/libunwind/)
- [LLVM libunwind](https://libunwind.llvm.org/)

### Essential Reading
- **Eli Bendersky:** ["Obtaining the backtrace with libunwind"](https://eli.thegreenplace.net/2015/programmatic-access-to-the-call-stack-in-c/) (Best starting point).
- **Josh Haberman:** ["Deep Wizardry: Stack Unwinding"](https://blog.reverberate.org/2013/05/deep-wizardry-stack-unwinding.html) (Deep dive into DWARF).
- **Manual Pages:** Run `man libunwind` on your Linux terminal.

## ✅ Mastery Checklist
- [ ] Implement a local backtrace printer.
- [ ] Read and understand the difference between Savannah and LLVM implementations.
- [ ] Successfully unwind a remote process via `ptrace`.
- [ ] Write a signal-safe backtrace recorder for a profiler.
- [ ] Inspect `.eh_frame` sections of a binary using `readelf`.
