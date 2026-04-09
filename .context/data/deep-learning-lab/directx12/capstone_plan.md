# DirectX 12 Mastery - Capstone Project: "Bionic Renderer"

## Objective
Build a minimal, expert-grade D3D12 renderer that demonstrates mastery of the core pipeline, modern resource binding, and compute-driven post-processing.

## Features to Implement
1.  **Robust Initialization**:
    *   Enable D3D12 Debug Layer.
    *   Explicit Adapter selection.
    *   Triple Buffering with Fences for CPU-GPU sync.
2.  **Advanced Resource Binding**:
    *   Root Signature with:
        *   1 Root Constant (for per-object color).
        *   1 Root Descriptor Table (for per-frame Constant Buffer).
    *   256-byte aligned Constant Buffers.
3.  **Shaders**:
    *   Vertex Shader (VS): Standard transform.
    *   Pixel Shader (PS): Simple shading.
    *   Compute Shader (CS): Post-process "Scanline" or "Grayscale" effect.
4.  **Stencil Buffer**:
    *   Implement a simple stencil mask to prevent rendering in a specific screen region (e.g., a "bionic eye" overlay).
5.  **Debugging**:
    *   Integration of DRED (Device Removed Extended Data) settings.

## Implementation Plan
1.  **Step 1**: Scaffold Win32 window and D3D12 Device/Queue/SwapChain.
2.  **Step 2**: Create Root Signature and PSO.
3.  **Step 3**: Implement Vertex/Index buffers for a simple cube/triangle.
4.  **Step 4**: Implement the Compute Shader post-process pass.
5.  **Step 5**: Add Stencil-based masking.
6.  **Step 6**: Final validation with PIX.
