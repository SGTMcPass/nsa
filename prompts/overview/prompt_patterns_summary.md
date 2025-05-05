# Prompt Design Patterns for Simulation Engineers

**Purpose:** Provide a conceptual summary of reusable prompt engineering patterns
applicable to simulation, GNC, and tool generation workflows.
**ID:** prompt_patterns_summary
**Tag:** overview, promptengineering, designpatterns
**Domain:** simulation, prompting
**Version:** 0.1
**Status:** draft

---

## 🧠 Prompt Specification

Summarize prompt types and techniques commonly used in simulation workflows:

1. Describe → Generate → Validate
2. Self-refining prompt loops
3. Modular code generation scaffolds
4. Prompt chains for multi-step simulation building
5. Structured data → structured code (YAML → C++/Trick)

Each pattern should include:

- Description
- Example use case (preferably GNC or Trick)
- Input/output format expectations
- Benefits and limitations

---

## 📥 Example Input

```yaml
context: simulation engineering
goal: discover reusable prompt patterns
focus: trick / codegen / registry-based workflows
```

---

## 📤 Output Expectation

```plaintext
- Markdown summary
- Sectioned by pattern type
- With inline examples and benefits/limitations
```

---

## 📝 Notes

- This summary will feed into internal documentation for reusable prompt strategies
- Future candidates for templated codegen or registry-aware automation
