### 5 Verification

 `active` flag set to true instructs the simulation that the execution is intended to be part of a monte-carlo analysis. Now there are 2 types of executions that fit this intent:
    * The generation of the dispersion files
    * The execution of this run with the application of previously-generated dispersions

Any code to be executed for case (a) must go inside the `generate_dispersions` gate. Any code to be executed for
case (b) goes inside the `active` gate, but outside the `generate_dispersions` gate.

You may wonder why this distinction is made. In many cases, it is desirable to make the execution for monte-carlo
analysis subtly different to that for regular analysis. One commonly used distinction is logging of data; the logging
requirement may differ between a regular run and one as part of a monte-carlo analysis (typically, monte-carlo runs
execute with reduced logging). By providing a configuration area for a monte-carlo run, we can support these
distinctions.
Note – any code to be executed for only non-monte-carlo runs can be put in an else: block. For example, this code
will set up one set of logging for a monte-carlo run, and another for a non-monte-carlo run of the same scenario:
```python
if monte_carlo.master.active:
 exec(open(“Log_data/log_for_monte_carlo.py”).read())
 if monte_carlo.master.generate_dispersions:
 exec(open(“Modified_data/monte_variables.py").read())
else:
 exec(open(“Log_data/log_for_regular.py”).read())
```
 3. If
