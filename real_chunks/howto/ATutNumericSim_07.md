### State Propagation with Numerical Integration > Numeric Versus Analytical

" simulation with latest version using
Trick integration.

1. Start the trick data products: `% trick-dp &`.
There should be the two SIMs in the "Sims/Runs" pane of trick-dp:

    1. `SIM_cannon_analytic`, and
    2. `SIM_cannon_numeric`.

2. Double click `SIM_cannon_analytic->RUN_test`
This will move `SIM_cannon_analytic/RUN_test` to the selection box.

3. Double click `SIM_cannon_numeric->RUN_test`
Now the two RUNs we wish to compare will be present in the selection box.

4. Double click `SIM_cannon_analytic/DP_cannon_xy`
DP_cannon_xy will be moved into the selection box.

5. Click the Co-Plot button (collated white sheets icon) located on the
menu bar.  Voila!  The curves appear the same, but there is a slight difference.
Living with less than a billionth of a meter difference will not cause us to
lose sleep.  However, we still dont like it!  It is no fun being a sloppy
perfectionist!

Congratulations, you are now running a simulation with numerical integration.

[Next Page](ATutDynamicEvents)
