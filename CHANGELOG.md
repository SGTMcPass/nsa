# v1.1.0-lint-compliant — 2025-05-05

## ✨ Highlights

- ✅ Full `pre-commit` integration with custom `prompt-lint`, `yamllint`,
  `markdownlint`, `black`, etc.
- ✅ All prompt files brought into strict structural and stylistic compliance
- ✅ Added output formatting expectations to assistant profile
  (`*.md`, `*.yaml`)
- ✅ Updated all scripts for import-safe execution (`tools/*.py`)
- ✅ Tooling validated with `test_tools.sh` and CI-ready structure

## 🔧 Internal Improvements

- Added user-local Node.js config via `setup_node_env.sh`
- Created `scripts/bootstrap.sh` and `scripts/test_tools.sh` for automated
  setup + verification
- Markdown and YAML now fully pass all CI formatting gates
