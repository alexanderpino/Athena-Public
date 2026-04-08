# Project State

> **Purpose**: Living snapshot of workspace status.  
> **Last Updated**: 2026-04-08

---

## System Status

- **Health**: Stable. Python scripts in `scripts/` have been fixed and missing dependencies (python-dotenv, supabase) were addressed to ensure core tooling runs smoothly.
- **Memory**: 
  - Added global directive to always investigate and fix broken python scripts in `Athena-Public\scripts`.
  - Added global directive for larger refactoring, changes, and tasks: Research -> Plan & Get Approval -> Execute with Checklist -> Summarize.
- **Protocol**: Session active.

## Recent Context & Discoveries

- **.NET Dependency Analysis**: 
  - Analyzed `<ProjectReference>` tags across `Libraries`, `Core`, and `services-*` repositories.
  - The `Libraries` folder acts as the decoupled foundational layer (`Common`, `Configuration`, `Logging`, `DataAccess`).
  - The `Core` repository contains the legacy monolithic and POC services, notably `BusinessLogicService` and `AutomaatService`.
  - **BusinessLogicService History**: Started as a POC with a static "god class" structure. Transitioned to .NET Core/DI incrementally, leading to heavy use of abstractions, interface splintering (NetFx, CoreWCF), and a large module explosion. This represents a successful but complex modernization effort.
  - The `services-*` repositories reflect the newer, modernized microservices approach following Clean Architecture / DDD principles, some utilizing .NET Aspire (e.g., `services-automaat`).

## Action Items

- Keep the migration history of `Core` in mind when making changes: prioritize safe, incremental improvements.

---

# project-state #context
