# Adding a New Entity to the NebulaEngine ECS System

This guide explains how to add a new entity to the NebulaEngine's Archetype-based ECS system, based on the codebase's standards and repository-specific skills found in C:\repos\GitHub\NebulaEngine\.agents\skills.

## 1. Overview
NebulaEngine uses an **Archetype-based ECS** (
bl::core::ArchetypeECS) that prioritizes Data-Oriented Design (DOD) and cache efficiency. Entities are handles, and components are stored contiguously in memory chunks grouped by their \"archetype\" (the unique set of components they possess).

## 2. Defining Components
Components must be **Plain Old Data (POD)**. Logic, virtual functions, smart pointers, and containers (like std::vector or 
bl::TArray) are strictly forbidden inside components.

`cpp
namespace nbl {
    struct Position {
        float x, y, z;
    };

    struct Velocity {
        float dx, dy, dz;
    };
}
`

**Rules:**
- Use 
bl:: aliases for containers if absolutely necessary in other parts of the engine, but keep components as simple structs.
- Components should be 64-byte aligned for optimal SIMD/cache performance in hot paths.

## 3. Creating an Entity
You create entities through the ArchetypeECS instance, which is typically owned by the SceneManager.

### Basic Creation
`cpp
nbl::core::Entity entity = ecs.CreateEntity();
`

### Creation with Components (Template)
You can create an entity with a predefined set of components in a single call, which is more efficient as it avoids multiple structural changes.
`cpp
auto entity = ecs.CreateEntity<Position, Velocity, NameComponent>();
`

## 4. Adding Components
If an entity already exists, you can add components dynamically. Note that this causes a **structural change** (moving the entity to a new archetype chunk).

`cpp
// Method 1: Template with initial data
ecs.AddComponent<Position>(entity, Position{ 0.0f, 1.0f, 0.0f });

// Method 2: Passing an instance
Velocity vel = { 1.0f, 0.0f, 0.0f };
ecs.AddComponent(entity, vel);
`

## 5. Deferred Operations (EntityCommandBuffer)
**CRITICAL:** You must NEVER perform structural changes (like CreateEntity, DestroyEntity, or AddComponent) while iterating over entities in a system (e.g., inside ParallelForEachChunkAware). Use an EntityCommandBuffer (ECB) to defer these changes.

`cpp
nbl::core::EntityCommandBuffer ecb;

ecs.ParallelForEachChunkAware<Position, Health>([&](auto chunk) {
    for (auto& entity : chunk) {
        if (entity.Get<Health>().current <= 0) {
            ecb.DestroyEntity(entity.entity); // Defer destruction
        }
    }
});

ecb.Flush(ecs); // Apply changes safely after iteration
`

## 6. Repository-Specific Skills Discovered
The following skills in C:\repos\GitHub\NebulaEngine\.agents\skills provide additional context:
- **ecs-architecture**: Details the ArchetypeECS API, DOD principles, and safety rules for parallel iteration.
- **cpp-engine-implementation**: Defines naming conventions (PascalCase for functions), mandatory 
bl:: container aliases, and the \"Nuclear Rule\" (full implementation required).
- **scene-and-world-management**: Explains how SceneManager coordinates ECS with spatial indexing (BVH) and world streaming.
- **game-development**: Provides the high-level GameApplication lifecycle (OnGameFixedUpdate vs OnGameUpdate).

## 7. Validation Checklist
- [ ] Components are POD (no logic/virtuals/containers).
- [ ] Functions use PascalCase.
- [ ] Structural changes are deferred via EntityCommandBuffer if inside a system loop.
- [ ] Components are registered via ComponentTraits for reflection (if needed for serialization).
- [ ] Entity handles are used (not raw pointers) across frame boundaries.
