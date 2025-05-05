# Trick Model Scaffolding Prompt

**Purpose:** Generate reusable C++ simulation modules compatible with NASA Trick
based on structured YAML or JSON input.
**ID:** trick_model_scaffold
**Tag:** toolbuild, trick, codegen
**Domain:** simulation, GNC
**Version:** 0.1
**Status:** draft

---

## 🧠 Prompt Specification

You are an AI tool that converts a system definition (in YAML) into:

- C++ class header/source files with Trick macros
- CMakeLists.txt for build integration
- Initialization logic based on the system parameters

Ensure all code is modular and complies with Trick conventions.

---

## 📥 Example Input

```yaml
name: ThrusterModule
mass: 85.5
components:
  - name: Thruster1
    location: [0.0, 0.0, 1.0]
    force: 150.0
```

---

## 📤 Output Expectation

```plaintext
- ThrusterModule.hh
- ThrusterModule.cpp
- CMakeLists.txt
```

---

## 📝 Notes

- Extend with controller and sensor templates in future versions
- Ensure compatibility with GitLab CI by including basic unit test stubs
- Consider supporting YAML → TrickDataRecord auto-mapping later
