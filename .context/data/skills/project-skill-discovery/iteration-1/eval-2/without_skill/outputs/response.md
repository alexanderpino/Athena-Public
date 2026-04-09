# GPU Rendering Pipeline Optimization - Skill Discovery

I have analyzed the local skills available in `C:\repos\GitHub\NebulaEngine\.agents\skills` to identify those that can assist in optimizing the GPU rendering pipeline.

## Identified Relevant Skills

The following skills provide direct guidance and mandates for GPU performance and architectural integrity in the NebulaEngine project:

### 1. `gpu-rendering-pipeline`
- **Core Focus**: Render passes, shaders, Frame Graph bindings, and compute dispatches.
- **Optimization Value**:
    - Mandates **Next-Gen Rendering Architecture** (Meshlets via `DispatchMesh()`, Hardware Raytracing).
    - Enforces **GPU Indirect Drawing** to eliminate CPU-side draw call loops.
    - Provides a **Compute Dispatch Checklist** to ensure efficient and correct execution.
    - Specifies **GPU Struct Layout Rules** to prevent layout mismatches between C++ and HLSL, which can lead to performance-killing bugs.
    - Requires **Barrier Safety** documentation to prevent synchronization stalls or data corruption.

### 2. `hot-path-optimization`
- **Core Focus**: High-performance code, cache efficiency, and loop optimization.
- **Optimization Value**:
    - Includes a **Cardinal Rule**: "Never optimize without a profile."
    - Mandates that new GPU passes include **timestamp query pairs** for measurement.
    - Focuses on **Cache Efficiency** (Sequential access, SoA layouts) which is critical for the CPU-side of the rendering pipeline (feeding the GPU).
    - Provides guidance on **SIMD/Vectorization** and avoiding expensive operations in hot loops.

### 3. `profiling-and-instrumentation`
- **Core Focus**: Measurement, diagnostic HUDs, and external profiler integration.
- **Optimization Value**:
    - Detailed instructions for **GPU Timestamp Queries** via the GAL abstraction.
    - Explains how to use `NBL_PROFILE_SCOPE` for CPU-side rendering logic.
    - Covers **Memory Tracking** and VRAM budget monitoring.
    - Integration with **Tracy**, **PIX**, and **NSight** for deep GPU analysis.

### 4. `material-and-shader-authoring`
- **Core Focus**: HLSL authorship, MaterialGraph system, and shader permutations.
- **Optimization Value**:
    - Focuses on **Shader Variants / Permutations** to avoid expensive runtime branching in shaders.
    - Enforces strict **Register Binding Rules** and **GPU Struct Layout Rules**.
    - Mandates the use of **DXC** for high-quality SPIR-V and DXIL generation.

### 5. `memory-management`
- **Core Focus**: Allocation strategies and resource lifetime.
- **Optimization Value**:
    - Relevant for **VRAM aliasing** and efficient GPU resource allocation.
    - Emphasizes **zero heap allocations on hot paths**, which prevents driver-level stalls.

---

## File Interactions

To discover these skills, the following shell commands were executed:

1. **Listing available skills**:
   ```powershell
   ls -R C:\repos\GitHub\NebulaEngine\.agents\skills
   ```
2. **Reviewing `gpu-rendering-pipeline`**:
   ```powershell
   cat C:\repos\GitHub\NebulaEngine\.agents\skills\gpu-rendering-pipeline\SKILL.md
   ```
3. **Reviewing `hot-path-optimization`**:
   ```powershell
   cat C:\repos\GitHub\NebulaEngine\.agents\skills\hot-path-optimization\SKILL.md
   ```
4. **Reviewing `profiling-and-instrumentation`**:
   ```powershell
   cat C:\repos\GitHub\NebulaEngine\.agents\skills\profiling-and-instrumentation\SKILL.md
   ```
5. **Reviewing `material-and-shader-authoring`**:
   ```powershell
   cat C:\repos\GitHub\NebulaEngine\.agents\skills\material-and-shader-authoring\SKILL.md
   ```
