# DirectX 12 Mastery - Summary of Key Concepts

## 🚀 State of DirectX 12 (April 2026 Update)

### Shader Model 6.9 (Agility SDK 1.619 Retail)
*   **Long Vectors**: Native HLSL support for vectors from **4 to 1024 elements**, enabling massive parallel processing without manual packing.
*   **Mandatory Feature Baseline**: Several previously optional features are now **required** for compliance:
    *   **Native 16-bit Float Ops** (`half` precision).
    *   **64-bit Integer Ops** (`int64`).
    *   **Wave Operations**: Full intrinsic suite.
*   **IsNormal()**: New HLSL intrinsic for checking normalized floating-point numbers.
*   **DXR 1.2 Standardization**:
    *   **Shader Execution Reordering (SER)**: Stable API for dynamic ray sorting, boosting path tracing performance by up to 90%.
    *   **Opacity Micromaps (OMM)**: Native support for alpha-tested geometry (foliage/fences) to skip "AnyHit" shaders.

### Work Graphs (Shader Model 6.8)
*   **GPU Autonomy**: Allows the GPU to manage its own execution flow. Shaders (Nodes) can spawn other nodes directly.
*   **Node Launch Modes**: `broadcasting` (standard compute style) and `thread` (one thread per input record).
*   **Eliminates CPU-GPU roundtrips**: Perfect for procedural generation, culling, and complex simulation.

### AI & Neural Rendering
*   **Cooperative Vectors**: Hardware-accelerated matrix-vector operations for Tensor Cores.
*   **DirectX Linear Algebra**: New 2026 API for higher-level NPU/GPU AI model execution.

### Tooling & GDK 2026
*   **DirectStorage + Zstandard**: Native hardware-accelerated decompression for faster asset streaming.
*   **Precompiled Shaders**: Storefront-level distribution to eliminate "shader compilation stutter."
*   **DirectX Dump Files (.dxdmp)**: Console-grade crash debugging with full hardware register state.

## Mathematical Foundations (DirectXMath)

### Vectors (XMVECTOR vs XMFLOAT*)
*   **XMVECTOR**: The core SIMD type. Maps to a 128-bit SIMD register (like `__m128` in SSE).
    *   Used for **all calculations**.
    *   Always 16-byte aligned.
*   **XMFLOAT2/3/4**: Storage types used for class members and data structures.
    *   Does NOT have SIMD alignment requirements (usually).
    *   Cannot be used directly for math; must be "Loaded" into an `XMVECTOR` first.
*   **Conversion Functions**:
    *   `XMLoadFloat3(&float3)` -> `XMVECTOR`
    *   `XMStoreFloat3(&float3, vector)` -> void

### Essential Operations
*   **Dot Product**: `XMVector3Dot(v1, v2)` -> Returns a vector where all components are the dot product result (to keep it in SIMD registers). Use `XMVectorGetX` to extract it.
*   **Cross Product**: `XMVector3Cross(v1, v2)`.
*   **Normalization**: `XMVector3Normalize(v)`.
*   **Length**: `XMVector3Length(v)`.

### Matrices (XMMATRIX vs XMFLOAT4X4)
*   **XMMATRIX**: 4x4 matrix using four `XMVECTOR` registers.
    *   Used for **all calculations**.
    *   Alignment: 16-byte aligned.
*   **XMFLOAT4X4**: Storage type for matrices in classes.
*   **Conversion Functions**:
    *   `XMLoadFloat4x4(&float4x4)` -> `XMMATRIX`
    *   `XMStoreFloat4x4(&float4x4, matrix)` -> void

### Identity and Transformations
*   **Identity**: `XMMatrixIdentity()`.
*   **Translation**: `XMMatrixTranslation(x, y, z)`.
*   **Scaling**: `XMMatrixScaling(x, y, z)`.
*   **Rotation**: `XMMatrixRotationX(angle)`, `XMMatrixRotationY(angle)`, `XMMatrixRotationZ(angle)`, `XMMatrixRotationRollPitchYaw(angles)`.
*   **Multiplication**: `XMMatrixMultiply(A, B)` or `operator*`.

## Direct3D 12 Initialization Sequence (from HelloTriangle)

1.  **Debug Layer**: Enable before device creation.
2.  **Factory (IDXGIFactory)**: Used to enumerate adapters and create the swap chain.
3.  **Device (ID3D12Device)**: The virtual adapter.
4.  **Command Queue (ID3D12CommandQueue)**: The "Inbox" for the GPU.
5.  **Swap Chain (IDXGISwapChain)**: Manages the back buffers.
6.  **Descriptor Heaps**: Memory for descriptors (pointers to resources).
    *   **RTV Heap**: Render Target Views.
    *   **DSV Heap**: Depth Stencil Views.
    *   **CBV/SRV/UAV Heap**: Constant Buffers, Shader Resource Views, Unordered Access Views.
7.  **Command Allocator**: Memory for recording commands.
8.  **Root Signature**: Defines what resources are bound to the pipeline (the "function signature" of the shaders).
9.  **Pipeline State Object (PSO)**: The massive state object containing shaders, blend state, rasterizer state, etc.
10. **Command List**: Used to record commands.
11. **Fences/Events**: For CPU-GPU synchronization.

## Resource Binding & Root Signatures

### Constant Buffers (CBV)
*   **Alignment**: MUST be **256-byte aligned**.
*   **Struct Padding**: Use padding in C++ structs to ensure size is a multiple of 256.
*   **Update Pattern**:
    *   Create resource in an `UPLOAD` heap.
    *   `Map` the resource once at startup to get a CPU pointer.
    *   Use `memcpy` to update data from CPU to GPU.
    *   `Unmap` is optional until the resource is destroyed.

### Root Signatures
*   **Definition**: The "Function Signature" of the pipeline. Defines what types of resources (CBV, SRV, UAV, Samplers) are bound to which registers (`b0`, `t0`, `u0`, `s0`).
*   **Components**:
    *   **Root Constants**: Small constants pushed directly in the command list (fastest, limited space).
    *   **Root Descriptors**: Direct pointers to resources (CBV/SRV/UAV) without a heap (fast, limited to CBV/SRV/UAV raw buffers).
    *   **Descriptor Tables**: Pointers to a range in a Descriptor Heap (most flexible, handles textures).
*   **Visibility**: Can be restricted to specific shader stages (e.g., `D3D12_SHADER_VISIBILITY_VERTEX`) for optimization.

### Descriptor Heaps
*   **Shader Visible**: Heaps containing CBV/SRV/UAV or Samplers must be marked `D3D12_DESCRIPTOR_HEAP_FLAG_SHADER_VISIBLE` to be used with `SetGraphicsRootDescriptorTable`.
*   **Binding**: Use `SetDescriptorHeaps` on the command list before binding tables.

## Advanced Shader Stages

### Compute Shader (CS)
*   **GPGPU**: General Purpose GPU programming. Used for non-graphical tasks or complex graphical effects (Blur, SSAO, Physics).
*   **Threading Model**:
    *   **Thread Groups**: Grids of threads executed on a multiprocessor.
    *   **Dispatch**: `Dispatch(x, y, z)` launches a 3D grid of thread groups.
    *   **numthreads**: `[numthreads(x, y, z)]` defines the size of each group.
*   **IDs**:
    *   `SV_GroupID`: ID of the group within the dispatch grid.
    *   `SV_GroupThreadID`: ID of the thread within its group.
    *   `SV_DispatchThreadID`: Global ID of the thread across the entire dispatch.
    *   `SV_GroupIndex`: Linearized version of `SV_GroupThreadID`.
*   **Shared Memory**: `groupshared` memory is local to a group, fast as cache (max 32KB). Use `GroupMemoryBarrierWithGroupSync()` for synchronization.
*   **Resources**:
    *   **Unordered Access Views (UAVs)**: Allows read/write access (`RWTexture2D`, `RWStructuredBuffer`).
    *   **Append/Consume Buffers**: For unordered data processing (e.g., particle systems).

### Tessellation Stages (HS, DS)
*   **Purpose**: Dynamically increase geometry detail on the GPU.
*   **Hull Shader (HS)**:
    *   **Constant Phase**: Computes tessellation factors (how much to subdivide).
    *   **Control Point Phase**: Processes input control points.
*   **Tessellator**: Fixed-function stage that subdivides the patch.
*   **Domain Shader (DS)**: Processes the subdivided vertices; evaluates the final position on the tessellated surface.

## Modern Graphics Pipeline (D3D12 Ultimate)

### Mesh Shaders & Amplification Shaders
*   **Replaces**: Input Assembler, Vertex, Hull, Domain, and Geometry shader stages.
*   **Meshlets**: Geometry is broken into small chunks (max 64 vertices, 126 triangles) for better cache locality and parallel processing.
*   **Amplification Shader (AS)**:
    *   Compute-style stage that runs before Mesh Shaders.
    *   Primary use: **Culling** (frustum/occlusion) and **LOD selection**.
    *   Launches Mesh Shader threadgroups using `DispatchMesh`.
*   **Mesh Shader (MS)**:
    *   Processes a meshlet and outputs vertices/primitives directly to the rasterizer.
    *   Uses `SetMeshOutputCounts` to define output size.
    *   Outputs via `vertices` and `indices` arrays.

### DirectX Raytracing (DXR)
*   **Acceleration Structures**:
    *   **Bottom-Level (BLAS)**: Stores actual geometry (triangles).
    *   **Top-Level (TLAS)**: Stores instances of BLAS with transformation matrices.
*   **Raytracing Pipeline State (RTPSO)**: Defines a set of shaders for ray generation, hits, and misses.
*   **Shader Binding Table (SBT)**: Bridges geometry instances to specific shaders and their resources (CBVs, SRVs).
*   **Shader Stages**:
    *   `RayGen`: Launches rays using `TraceRay`.
    *   `ClosestHit`: Executed at the nearest intersection; handles shading.
    *   `Miss`: Executed if no intersection is found (e.g., skybox).
    *   `AnyHit`: Executed for every intersection (useful for alpha-testing).
    *   `Intersection`: Custom logic for non-triangle geometry (spheres, etc.).
*   **Inline Raytracing (DXR 1.1)**: Allows using `RayQuery` in any shader stage (Compute, Pixel) without a full RTPSO.

## Expert-Level GPU Architecture

### GPU-Driven Rendering (ExecuteIndirect)
*   **Purpose**: Shift draw/dispatch decision logic from the CPU to the GPU.
*   **Mechanism**:
    *   **Command Signature**: Defines the layout of commands in memory (e.g., set root constants, then draw).
    *   **Argument Buffer**: A GPU buffer containing the command data (filled by a Compute Shader).
    *   **Count Buffer**: Optional buffer containing the number of commands to execute.
*   **Use Cases**: Frustum/Occlusion culling, LOD selection, and massive particle systems.
*   **Benefit**: Significant reduction in CPU overhead and API call counts.

### Residency Management
*   **The Challenge**: D3D12 requires manual management of VRAM (MakeResident/Evict).
*   **The Solution**: D3DX12 Residency Starter Library (ResidencyManager).
*   **Key Components**:
    *   **ManagedObject**: Wrapper for heaps/committed resources.
    *   **ResidencySet**: A list of resources required for a specific command list.
    *   **TrimResidency**: Periodically call to stay within the OS memory budget.
*   **Rule**: Never let the GPU touch evicted memory; always ensure the residency set is resident before execution.

## Key Pitfalls identified so far
*   **Wait for Previous Frame**: Luna notes that waiting for the frame to complete every time is NOT best practice (inefficient). Real apps should use triple buffering and fences to keep the GPU busy while the CPU prepares the next frame.
*   **Upload Heaps**: Used in samples for simplicity but not recommended for static geometry. Default Heaps are faster for GPU access.
