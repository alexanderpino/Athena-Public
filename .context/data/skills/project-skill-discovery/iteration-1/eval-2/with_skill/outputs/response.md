# Project Skill Discovery: NebulaEngine GPU Rendering Optimization

I have successfully discovered and audited several project-specific skills in the `C:\repos\GitHub\NebulaEngine\.agents\skills` directory. These skills provide mandatory architectural constraints and optimization strategies tailored for the NebulaEngine's AAA rendering pipeline.

## 1. Discovered Relevant Skills

| Skill Name | Description | Key Optimization Insights |
|------------|-------------|---------------------------|
| `gpu-rendering-pipeline` | Mandatory rules for render passes, shaders, and Frame Graph bindings. | Virtualized Geometry (Meshlets), GPU Indirect Drawing, Bindless Resources, and strict Barrier Safety. |
| `hot-path-optimization` | Rules for performance-critical CPU/GPU code, cache efficiency, and profiling. | Data-oriented design (SoA), zero heap allocations in hot loops, branchless patterns, and SIMD vectorization. |
| `material-and-shader-authoring` | Guidelines for writing high-performance shaders and managing materials. | (Identified during discovery, highly relevant for GPU pipeline optimization). |
| `profiling-and-instrumentation` | Procedures for measuring and diagnosing performance bottlenecks. | Essential for the "Never optimize without a profile" cardinal rule. |

## 2. Key Procedural Guidance for GPU Optimization

### A. Frame Graph & Resource Management
- **GPU Indirect Drawing**: Per-object CPU draw-call loops are forbidden. All new scene-geometry draw calls must use GPU indirect drawing.
- **Virtualized Geometry**: Dense geometry must fall back to Mesh Shader pipelines (Meshlets) via `DispatchMesh()`.
- **Bindless Architecture**: All textures must be accessed via the `BindlessResourceManager`.
- **Barrier Safety**: UAV/storage barriers must be explicitly managed in both producer and consumer passes.

### B. Hot Path Efficiency (CPU & GPU)
- **Data Layout (SoA)**: Separate hot and cold data into Structure of Arrays (SoA) to maximize cache-line residency.
- **Zero Allocations**: Zero heap allocations are permitted on the hot path (steady-state gameplay).
- **SIMD/Vectorization**: Ensure no iteration dependencies or aliased pointers (`__restrict`) to allow auto-vectorization.

### C. Validation Mandates
- Every shader `register(t/u/b/s)` must have a matching CPU-side bind call.
- GPU-uploaded structs must have `static_assert` for both `sizeof` and `offsetof` to ensure HLSL alignment.
- All optimizations must be verified with `NBL_PROFILE_SCOPE` and GPU timestamp queries.

## 3. File Interactions Log

- **Discovery**: Listed `C:\repos\GitHub\NebulaEngine\.agents\skills` using `run_shell_command`.
- **Audit**: Read `gpu-rendering-pipeline/SKILL.md` to extract rendering-specific mandates.
- **Audit**: Read `hot-path-optimization/SKILL.md` to extract performance and cache efficiency rules.
- **Documentation**: Generated this `response.md` to summarize the localized expertise.

---
*I am now prepared to apply these project-specific mandates to any rendering optimization tasks within the NebulaEngine repository.*
