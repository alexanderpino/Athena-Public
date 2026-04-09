# Adding a New Entity to NebulaEngine's ECS

Based on the `ecs-architecture` skill and the `ArchetypeECS` implementation in the NebulaEngine codebase, here is how to add a new entity.

## 1. Define Your Components
Components must be **Plain Old Data (POD)**. They cannot contain logic, virtual functions, smart pointers, or containers (like `TArray`). Hot-path components should be 64-byte aligned.

```cpp
struct Position {
    float x, y, z;
};

struct Velocity {
    float dx, dy, dz;
};
```

## 2. Basic Entity Creation
Use the `CreateEntity<T...>()` method on an `ArchetypeECS` instance. This creates the entity and allocates space for the specified components in the appropriate archetype chunk.

```cpp
nbl::core::ArchetypeECS ecs;

// Create an entity with Position and Velocity
nbl::core::Entity myEntity = ecs.CreateEntity<Position, Velocity>();

// Set initial values
ecs.Set<Position>(myEntity, {0.0f, 0.0f, 0.0f});
ecs.Set<Velocity>(myEntity, {1.0f, 0.0f, 0.0f});
```

## 3. Deferred Creation/Mutation (Parallel Contexts)
If you are inside a parallel loop (e.g., `ParallelForEach`), you **must not** modify the ECS structure directly (no `CreateEntity`, `DestroyEntity`, or `AddComponent`). Instead, use an `EntityCommandBuffer` (ECB).

Note: While the ECB supports `RecordAddComponent`, `RecordRemoveComponent`, and `RecordDestroyEntity`, it does not explicitly have a `RecordCreateEntity` method in the current implementation. You should create entities on the main thread before or after parallel phases, or use a pattern where you recycle existing "inactive" entities.

```cpp
nbl::core::EntityCommandBuffer ecb;

ecs.ParallelForEach<Position>([&](nbl::core::Entity e, Position& pos) {
    if (pos.x > 1000.0f) {
        // Schedule component addition or destruction
        ecb.RecordAddComponent<Velocity>(e, {0.0f, 0.0f, 0.0f});
    }
});

// Apply changes after the parallel loop
ecb.Playback(ecs);
```

## 4. Architectural Constraints (AAA Standards)
*   **Archetype-Based**: Entities are grouped by their component signature into "Archetypes" and stored in 16KB "Chunks".
*   **SIMD Friendly**: Data is stored in SoA (Structure of Arrays) layout for cache efficiency and SIMD vectorization.
*   **No Structural Changes During Iteration**: Direct calls to `DestroyEntity` or `AddComponent` during a `ForEach` loop will trigger an assertion. Always use `EntityCommandBuffer` for deferred mutations.
*   **Component Traits**: Ensure your components are registered with reflection metadata if necessary (check `nebula/core/component_traits.h`).

## Discovery Log
The following project-specific skills were identified in `C:\repos\GitHub\NebulaEngine\.agents\skills`:
- `ecs-architecture`: Core guidance on ECS design, component rules, and parallel safety.
- `cpp-engine-implementation`: General C++ standards for the engine.
- `hot-path-optimization`: Advice on cache efficiency and SoA layouts.
- `memory-management`: Details on the allocator tiers used by the ECS.
