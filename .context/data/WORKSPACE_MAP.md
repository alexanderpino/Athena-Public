# Workspace Map: C:\repos

This map provides a recursive overview of the repositories and projects within the `C:\repos` directory.

## Core Projects

| Project | Path | Type | Description |
|---------|------|------|-------------|
| **Athena-Public** | `C:\repos\Athena-Public` | Python | Athena Sovereign Agent (This workspace) |
| **Nebula Engine** | `C:\repos\GitHub\NebulaEngine` | C++ / .NET | **AAA Game Engine**. DX12/Vulkan, Archetype ECS, DOD, Fiber Job System, Avalonia Editor. |
| **Core Infrastructure** | `C:\repos\core` | .NET (Legacy/Shared) | **Enterprise Core**. Includes Automaat, BusinessLogic, Notification, and Report services. |
| **Shared Libraries** | `C:\repos\libraries` | .NET (Shared) | **Data Access & Common Libs**. Uses LLBLGen for data access. |
| **Microservices** | `C:\repos\services-*` | .NET / WSO2 / Terraform | **Domain-Specific Services**. Employees, Schedule, Realization, etc. |

## Nebula Engine Deep Dive (`C:\repos\GitHub\NebulaEngine`)

The crown jewel of the workspace. A modern, cross-platform AAA engine.

- **Engine Core (`Engine/Source/NebulaEngine`)**:
  - **ECS**: Archetype-based, parallel execution.
  - **GAL**: Graphics Abstraction Layer (DX12 / Vulkan).
  - **Systems**: AI, Animation (Path/SM/Events), Physics (Jolt), Audio (OpenAL Soft), Scripting (Lua/C#).
  - **Rendering**: GPU-Driven, Bindless, Frame Graph, Post-Processing stack.
- **Editor (`Editor/`)**:
  - Built with .NET 10 and Avalonia 11.3.
  - Visual Node Graph, Scene Outliner, Property Inspector.
- **Build System**: CMake (Presets for Windows, Linux, Ninja, CI), `vcpkg` for dependencies.
- **Testing**: 1,600+ C++ tests (GoogleTest), 90+ C# tests (xUnit).

## Enterprise Infrastructure Deep Dive

### Core Services (`C:\repos\core`)
A monolithic or tightly coupled set of enterprise services.
- **AutomaatService**: Automated process handling.
- **BusinessLogicService**: Centralized business rules.
- **NotificationService**: System-wide messaging/alerts.
- **ReportService**: JasperReports integration.
- **MyCustomer / MyPlan**: Legacy client/customer management portals.
- **ServiceCommon**: Shared contracts and utilities for the core stack.

### Shared Libraries (`C:\repos\libraries`)
Foundation for data persistence across the .NET stack.
- **IPlan.DataAccess.LLBLGen**: ORM-based data access layer using LLBLGen Pro.
- **Directory.Packages.props**: Centralized NuGet package management.

### Microservices Portfolio (`C:\repos\services-*`)
Modern domain-driven services (mostly .NET 8/10).
- **Architecture**: Clean Architecture (src/test/terraform), OpenAPI/Swagger for contracts.
- **Deployment**: Terraform-based infra, WSO2 API gateway integration.
- **Portfolio**: Employees, Schedule, Preferences, Realization, Reports, Requests, Talent-Info, User-Info.

## Repository Index (Selection)

- `_nonpm/`: Non-NPM packages and zip archives.
- `.ai/`: AI configuration and experimental scripts.
- `.cmake/`: Global CMake binaries and templates.
- `apply-from-go-to-i-plan/`: Automation/migration scripts.
- `build-deploy/`: CI/CD and deployment scripts.
- `chapter/`: Educational or book-related code.
- `clockregistrations/`: Time tracking service.
- `clones/`: Forked or cloned external repositories.
- `content-editor/`: UI for content management.
- `database/`: SQL scripts and DB migrations.
- `datahub/`: Centralized data management.
- `Disco/`: UI/UX experiments or "Discovery" project.
- `git/`: Git-related utilities or local mirrors.
- `GitHub/`: GitHub Action templates and organization scripts.
- `py/`: Python scripts and scrapers.
- `rgn-frontend/`: Frontend application (likely React/Angular).
- `s3/`: AWS S3 integration and upload tools.
- `training/`: Machine learning or developer training materials.

## Search Protocol

To find a specific file or symbol across the entire workspace, use:
`grep_search --dir_path C:\repos --pattern "YOUR_PATTERN"`

---
#workspace-map #context #atlas #nebula-engine #microservices #core-infra
