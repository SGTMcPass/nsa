# Assistant Extension Layer: Domain Behaviors & Formats

---

## 1. Trick Simulation Environment
**Relevant Modes:** `/docgen`, `/review`, `/derive`

**Default Environment:** Trick  
**Key File Types:**
- `S_define`: Object and variable declarations (C++-like)
- `*.sm`: Simulation manager scripts
- `input.py`: Python config with SWIG bridge

**Standard Practices:**
- Use `trick.var_server` for all runtime variable access
- Use `trick.add_read()` in Python inputs
- All new physical variables must use **SI units**
- Use `_si` suffix for ambiguous names (e.g., `force_si`, `temp_si`)

---

## 2. Testing Coverage Protocol
**Relevant Modes:** `/testgen`, `/docgen`

**Python**: Use `unittest` with support for:
- Parametrized tests
- Mocking with `unittest.mock`

**C++**: Use `GTEST` with fixture-based testing preferred

**Template Example:**

```python
import unittest
from unittest.mock import patch

class TestMotor(unittest.TestCase):

    def test_speed_conversion(self):
        self.assertEqual(convert_speed_kph_to_mps(36), 10)

    @patch('motor.read_sensor')
    def test_sensor_mock(self, mock_sensor):
        mock_sensor.return_value = 42
        self.assertEqual(read_sensor_value(), 42)
```

---

## 3. Documentation Standards
**Relevant Modes:** `/docgen`

- Use **Markdown** for internal docs, wikis, and developer references
- Use **LaTeX** only for formal derivations or publishable materials
- Docstring formats: default to **Google-style**

---

## 4. Sprint Planning & Tracking
**Relevant Modes:** `/plan`

**Sprint Trigger:**
- Manually via `/plan`
- Inferred if:
  - 3+ steps issued
  - A "step" = any bullet line beginning with “Task:” or use of `/plan`

**Filename Convention:**
- `sprint_<short>_<YYYYMMDD>_<N>.md`

**Sprint Fields:**
- Tasks, blockers, reviewed items, uncovered tests, notes

---

## 5. Glossary & Code Conventions

Refer to the centralized glossary in `simulation_assistant.md`.

Only non-duplicate, domain-specific extensions should be listed here.

**Code Conventions:**
- `snake_case` for variables
- `CamelCase` for classes
- `UPPER_CASE` for constants
- Use SI units for all physical quantities

