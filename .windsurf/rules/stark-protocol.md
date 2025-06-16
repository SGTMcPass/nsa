---
trigger: glob
globs: *.py, *.yaml, *.yml, *.json, *.sh, *.md, *.log 
---

## ⚙️ Stark Protocol

*A modular, resilient, and CLI-first engineering pattern for building fail-soft, traceable systems.*

Inspired by Tony Stark’s iterative and adaptive engineering style, the **Stark Protocol** defines a practical design pattern for building robust systems that don’t just work — they recover, adapt, and scale. It emphasizes operational clarity, clean automation, and resilience under fire.

### 📌 Core Principles

* **Modular by Default**
  Subsystems are isolated and self-contained, with minimal shared state. Each module should be independently buildable, testable, and replaceable.

* **Recoverable & Fail-Soft**
  Every subsystem is designed to degrade gracefully under partial failure. Timeouts, retries with backoff, and fallback paths are used to prevent cascading errors and maintain system continuity.

* **Explicit Logging**
  All critical actions and state transitions are logged with contextual metadata. No silent paths or ambiguous outputs.

* **Manifest Traceability**
  Every operation — from config to output — is versioned, logged, and traceable. This enables reproducible builds and full lineage inspection.

* **End-to-End Testability**
  The system must be verifiable both as a whole and in parts. CLI-level smoke tests, integration flows, and fault simulations are part of the design.

* **Scriptable Interfaces**
  Orchestration is CLI-driven. Every operation must be invocable via well-structured, automatable, and observable command-line workflows.

* **Explicit Interface Contracts**
  Subsystems define strict schemas and expectations (inputs, outputs, timeouts). Contract violations must fail loudly and predictably, not downstream.

* **Deliberate Abstraction & Composition**
  Reuse is encouraged, but must be driven by real duplication and clearly aligned behaviors. Prefer composition over inheritance unless subclassing provides a provable simplification. Avoid premature generalization — clarity and modularity are prioritized over cleverness.
