# DirectX 12 Mastery Syllabus & Learning Plan

**Goal:** Achieve expert-level understanding of DirectX 12 (D3D12), transitioning from conceptual understanding to practical, performant implementations.

**Canonical Homes:**
1. Microsoft Direct3D 12 Programming Guide (Tier 1 - CS 1.0)
2. Microsoft DirectX-Graphics-Samples GitHub Repository (Tier 1 - CS 1.0)
3. Frank Luna's "Introduction to 3D Game Programming with DirectX 12" (Tier 1/2 - CS 0.8/1.0)

---

## 🌑 Phase 0: Scoping & The "Big Picture"
*   Setup workspace, environment, and tools.
*   Outline syllabus and gain approval. (Current step)

## 🌱 Phase 1: Rapid Immersion (The "Hello World" Loop)
*   **Setup:** Ensure Windows SDK, Visual Studio, and D3D12 Agility SDK are configured.
*   **The 15-Minute Win:** Extract and compile the minimal DX12 "Hello Window" and "Hello Triangle" from `C:\repos\GitHub\DirectX-Graphics-Samples`.
*   **Discovery:** Map the core D3D12 interface initialization sequence (Device -> Command Queue -> Swap Chain -> Descriptor Heaps -> Render Target View).

## 📚 Phase 2: Structured Reading (The "Deep Book" Phase)
*   **Source:** "Introduction To 3D Game Programming with DirectX 12.pdf"
*   **Action:** Systematically extract text from key chapters using the `pdf` skill, summarizing them into `.context/data/deep-learning-lab/directx12/summary.md`.
*   **Topics to cover:**
    *   Math & Transformation Vectors (SIMD specifics).
    *   Direct3D Initialization pipeline.
    *   **The Full Graphics Pipeline:** Comprehensive study of all shader stages (Vertex, Hull, Domain, Geometry, Pixel).
    *   **Compute Shaders:** GPGPU and post-processing.
    *   **The Depth/Stencil Stage:** Understanding Depth testing and Stencil Buffer techniques (masking, mirroring, shadows).
    *   Lighting & Texturing.

## 🔍 Phase 3: The Pattern Audit (Truth vs. Practice)
*   **Core Concepts to Audit against Microsoft Samples:**
    *   **Level 1: The Core** (Command Lists, Queues, Allocators, Swap Chain, Root Signatures, Pipeline State Objects).
    *   **Level 2: The Idiom** (Explicit Resource Binding, Descriptors, Constant Buffers, Textures).
    *   **Level 2.5: The Pipeline depth:** Auditing implementations of Tesselation (HS/DS), Geometry Shaders, and Stencil-based effects.
    *   **Level 3: The Depths** (Manual Memory Residency, Descriptor Heaps, Resource Barriers, Fences & Synchronization, Multi-threading work submission).
    *   **Level 4: The Architect** (Raytracing/DXR, Mesh Shaders (Amplification/Mesh), Multi-adapter systems, Querying & Performance Profiling).
*   **Action:** Cross-reference book patterns with modern Microsoft sample idioms (Agility SDK era) to ensure we're learning the most current practices.

## 🛠️ Phase 3.5: The Battlefield (Pitfalls & Troubleshooting)
*   **The D3D12 Debug Layer:** Master its usage and interpreting its output.
*   **GPU Breadcrumbs:** Learn the `D3D12_DEVICE_REMOVED_EXTENDED_DATA` (DRED) for debugging TDR (Timeout Detection and Recovery) and device removal.
*   **Common Pitfalls:**
    *   **Resource State Mismatches:** Incorrect use of Resource Barriers and missing transitions.
    *   **Synchronization Hazards:** Race conditions between CPU/GPU or multiple GPU queues.
    *   **Memory Management:** Descriptor Heap overflows and sub-allocation strategy failures.
    *   **Root Signature Bloat:** Performance impact of large root signatures.
*   **Action:** Build a "Troubleshooting Guide" based on common issues found in forums (Tier 3) and official Microsoft "Known Issues" (Tier 1).

## 🏛️ Phase 4: Mastery Project (The Synthesis)
*   **Capstone:** Build a custom, minimal renderer exercising all layers: Initialization -> Shaders -> Texturing -> Multi-threaded command recording.
*   **Validation:** Review architecture for synchronization hazards and sub-optimal memory allocations.

---
*Generated via Deep Learning Lab (DLL) Protocol*