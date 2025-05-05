# Prompt Engineering Research Report

**Purpose:** Generate a deep technical report summarizing foundational and recent
prompt engineering research (2020–2025) with applications to aerospace simulation
workflows.
**ID:** prompt_engineering_report
**Tag:** deepdive, promptengineering, simulation
**Domain:** AI tools, GNC, Trick
**Version:** 0.1
**Status:** draft

---

## 🧠 Prompt Specification

You are an AI research assistant trained in advanced prompt engineering. Your task
is to create a full Markdown report that includes:

1. Foundational methods (few-shot, CoT, RAG, agents)
2. Recent publications (2023–2025) with summaries and citations
3. Aerospace-specific applications (Trick, GNC, YAML configs, CI/CD integration)
4. Modular prompting patterns useful for simulation engineering

Use chain-of-thought reasoning. Prioritize accuracy and traceability over speed.
Output must be well-structured for reuse and export.

---

## 📥 Example Input

```yaml
focus: recent techniques
depth: deep
aerospace_context: true
```

---

## 📤 Output Expectation

```plaintext
- Full Markdown report with research summaries
- Sectioned by theme: foundations, applications, techniques
- References included (APA or IEEE format)
```

---

## 📝 Notes

- This prompt supports assistant-driven literature synthesis
- Useful for onboarding simulation teams into LLM tooling best practices
- Potential to auto-link to `prompt_patterns_summary`
