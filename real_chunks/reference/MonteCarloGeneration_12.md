### 5 Verification

-input to the simulation without requiring re-compilation; as such, it is typically handled in a Python input file. There are two sections for configuration:
* modifications to the regular input file, and
* new file-input or other external monte-carlo initiation mechanism

#### 4.2.2.1 Modifications to the regular input file

A regular input file sets up a particular scenario for a nominal run. To add monte-carlo capabilities to this input file, the
following code should be inserted somewhere in the file:

```python
if monte_carlo.master.active:
 # insert non-mc-variable MC configurations like logging
 if monte_carlo.master.generate_dispersions:
 exec(open(“Modified_data/monte_variables.py").read())
```

Let’s break this down, because it explains the reason for having 2 flags:

| `generate_dispersions` | `active` | Result |
| :--- |:---| :--- |
| false | false | Regular (non-monte-carlo) run |
| false | true | Run scenario with monte-carlo configuration and pre-generated dispersions |
| true | false | Regular (non-monte-carlo) runs |
| true | true | Generate dispersions for this scenario, but do not run the scenario |

 1. If the master is inactive, this content is passed over and the input file runs just as it would without this content
 2. Having the master `active` flag set to true instructs the simulation that the execution is intended to be part of a monte-carlo analysis. Now there are 2 types of executions that fit this intent:
    * The generation of the dispersion files
    * The
