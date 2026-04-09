# DirectX 12 Troubleshooting & Pitfalls Guide

This guide compiles common errors, debugging techniques, and performance pitfalls identified during the mastery process.

## 🛠️ Debugging Tools

### 1. D3D12 Debug Layer
*   **Purpose**: Catch API misuse, parameter errors, and resource state mismatches on the CPU.
*   **How to enable**:
    ```cpp
    ComPtr<ID3D12Debug> debugController;
    if (SUCCEEDED(D3D12GetDebugInterface(IID_PPV_ARGS(&debugController)))) {
        debugController->EnableDebugLayer();
    }
    ```
*   **Critical Tip**: Always enable *before* creating the D3D12 device.

### 2. GPU Breadcrumbs (DRED)
*   **Purpose**: Debugging TDRs (Timeout Detection and Recovery) and Device Removal.
*   **Function**: `ID3D12DeviceRemovedExtendedDataSettings`.
*   **What it tells you**: Which command list was executing and which specific command caused the GPU to hang or crash.

### 3. PIX on Windows
*   **Purpose**: Frame capture, GPU timing, and state inspection.
*   **Key Feature**: "Debug Pixel" allows you to step through pixel shader execution.

---

## 🚧 Common Pitfalls

### 1. Resource State Mismatches (The #1 DX12 Error)
*   **Problem**: Accessing a resource in a state it's not currently in (e.g., writing to a buffer in `GENERIC_READ` state).
*   **Fix**: Use `ResourceBarrier` (Transition) correctly.
*   **Pitfall**: Implicit state transitions only work for certain resource types (mostly buffers) and only when using the `COMMON` state.

### 2. Synchronization Hazards (CPU-GPU & GPU-GPU)
*   **Problem**: CPU modifying a buffer (via Upload Heap) while the GPU is still reading it.
*   **Fix**: Use `ID3D12Fence` to wait for the GPU to finish before recycling command allocators or modifying shared resources.
*   **Optimization**: Use a "Frame Resource" pattern to keep N frames in flight without waiting for the GPU every frame.

### 3. Constant Buffer Alignment
*   **Problem**: `ID3D12Device::CreateConstantBufferView` fails or renders garbage.
*   **Fix**: Constant buffers MUST be multiples of **256 bytes**.
    ```cpp
    #define ALIGN_256(n) (((n) + 255) & ~255)
    ```

### 4. Descriptor Heap Overflows
*   **Problem**: Running out of space in a shader-visible descriptor heap.
*   **Strategy**: Use a large, static heap for static textures and a smaller, ring-buffer style heap for dynamic/per-frame descriptors.

### 5. Root Signature Bloat
*   **Problem**: Including too many Root Constants or Root Descriptors.
*   **Impact**: Hardware has a limited "Root Signature" budget (usually 64 DWORDs). Root constants cost 1 DWORD per 32-bit value. Descriptor tables cost 1 DWORD.
*   **Fix**: Prefer Descriptor Tables for large numbers of resources.

---

## 💥 Common Error Codes

*   **`DXGI_ERROR_DEVICE_REMOVED`**: The GPU has crashed or was physically disconnected. Check `GetDeviceRemovedReason()` and use DRED to find the cause.
*   **`E_INVALIDARG`**: Check the Debug Layer output; it's almost always a misaligned offset or an incompatible flag combination.
*   **`DXGI_ERROR_INVALID_CALL`**: Often caused by calling an API method that is invalid for the current resource state or hardware tier.

## 🏁 Performance Anti-Patterns
*   **Submitting too many small Command Lists**: Batch your work.
*   **Frequent `SetPipelineState` calls**: Sort your render items by PSO to minimize state changes.
*   **Not using Mipmaps**: Causes massive texture aliasing and memory bandwidth waste during minification.
*   **Excessive Resource Barriers**: Transitions are not free. Use "Resource Aliasing" and "Split Barriers" for advanced optimization.
