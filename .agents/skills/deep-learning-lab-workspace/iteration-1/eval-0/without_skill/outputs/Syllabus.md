# Zig Learning Syllabus: The Master Path

This syllabus is designed to help you master Zig by cross-referencing the **Zig Language Reference (Technical Spec)** with the **Zig Guide (Tutorial)** and **Ziglings (Hands-on Practice)**.

## Phase 0: Orientation & Environment
*Focus: Setup, Philosophy, and Toolchain.*

| Topic | Zig Language Reference | Zig Guide | Ziglings |
| :--- | :--- | :--- | :--- |
| **Zen of Zig** | [Zen](https://ziglang.org/documentation/master/#Zen) | [Intro](https://zig.guide/introduction/) | N/A |
| **Installation** | [Getting Started](https://ziglang.org/learn/getting-started/) | [Getting Started](https://zig.guide/introduction/getting-started/) | N/A |
| **Hello World** | [Hello World](https://ziglang.org/documentation/master/#Hello-World) | [Basics](https://zig.guide/language-basics/hello-world/) | `001_hello.zig` |
| **Comments** | [Comments](https://ziglang.org/documentation/master/#Comments) | [Comments](https://zig.guide/language-basics/comments/) | `002_comments.zig` |
| **Build System** | [Zig Build System](https://ziglang.org/learn/build-system/) | [Build System](https://zig.guide/build-system/) | N/A |

---

## Phase 1: Core Syntax & Primitive Types
*Focus: The building blocks of the language.*

- **Variables & Assignment:** `const` vs `var`, type inference, `undefined`.
- **Primitive Types:** Integers, Floats, `bool`, `void`, `noreturn`.
- **Control Flow:** `if` expressions, `switch`, `while`, `for`.
- **Operators:** Arithmetic, Logical, and Bitwise.

---

## Phase 2: Data Structures & Memory Layout
*Focus: How Zig organizes data in memory.*

- **Arrays & Vectors:** Fixed-size collections and SIMD.
- **Slices:** The power of `[]T`.
- **Structs:** `extern`, `packed`, and default values.
- **Enums & Unions:** Tagged unions and non-exhaustive enums.
- **Pointers:** Alignment, `volatile`, and sentinel termination.

---

## Phase 3: Error Handling & Optionals
*Focus: Safety without exceptions.*

- **Error Sets:** Defining and returning errors.
- **Error Unions:** The `!T` type.
- **Optionals:** The `?T` type and `null`.
- **Payload Capturing:** Using `if (x) |val|` and `while (y) |val|`.
- **Control Flow:** `try`, `catch`, `errdefer`.

---

## Phase 4: Metaprogramming (Comptime)
*Focus: Zig's most powerful feature.*

- **Comptime Variables:** Values known at compile-time.
- **Generic Types:** Functions that take `type`.
- **Reflection:** `@typeInfo`, `@field`, and `@hasDecl`.
- **Inline Loops:** `inline while` and `inline for`.

---

## Phase 5: Standard Library & C Interoperability
*Focus: Building real-world systems.*

- **Allocators:** `GPA`, `Arena`, `FixedBufferAllocator`.
- **C Integration:** `@importC`, calling C functions, translating C code.
- **Standard Library:** `std.fs`, `std.net`, `std.json`, `std.mem`.
- **Testing:** Unit tests directly in source files.
