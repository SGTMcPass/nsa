### Integrator Control Inputs

 the S_define file;
each integration job should have an associated <i> IntegLoop </i> declaration.
The available inputs for state integration control are listed in Table 18.

Table 18 State Integration Control Inputs
<table>
 <tr>
  <th width=375>Name</th>
  <th>Default</th>
  <th>Description</th>
 </tr>
 <tr>
  <td>getIntegrator(Integrator_type, unsigned int, double)</td>
  <td>No default value</td>
  <td>Tell Trick the Integrator scheme and the number of state variables.
      A call to this function is required otherwise a runtime error is generated.</td>
 </tr>
 <tr>
  <td>set_first_step_deriv(bool)</td>
  <td>True</td>
  <td>True=perform derivative evaluation for the first pass of the integrator;
      False=use the derivative evaluation from the last pass of the previous integration cycle.</td>
 </tr>
 <tr>
  <td>set_last_step_deriv(bool)</td>
  <td>False</td>
  <td>True=perform derivative evaluation for the last pass of the integrator;
      False=do not perform derivative evaluation for the last pass of the integrator.</td>
 </tr>
</table>

- <b> getIntegrator(Alg, State_size, Dt) </b>:  The <b> Alg </b> parameter is an enumerated type which currently
   has nine possible values.  These values and information about the associated integrator is shown in Table 19.
   The <b> State_size </b> parameter is the number of states that are to be integrated. This includes position
   <i> and </i> velocity states; e.g. for a three axis translational simulation, there would be three position
   states and three velocity states, hence the second parameter would equal 6 states.
   The <b> Dt </b> parameter is the integration frequency; however, this parameter is ignored unless using the
   <i> Integration </i> class stand-alone.  The frequency is defined in the S_define when using integration within Trick.
- <b> set_first_step_deriv(first_step) </b>: The <b> first_step </b> parameter is a boolean.  If <b> True </b> then
   Trick will run the derivative jobs for the first integration step.  If <b> False </b> then Trick will run only
   the integration jobs for the first integration step.
- <b> set_last_step_deriv(last_step) </b>: The <b> last_step </b> parameter is a boolean.  If <b> True </b> then
   Trick will run the derivative jobs after the last integration step.  If <b> False </b> then Trick will not run
   the derivative jobs after the last integration step.

Table 19 State Integration Options
<table>
 <tr>
  <th>Option</th>
  <th>Accuracy</th>
  <th>DiffEQ</th>
  <th># Deriv</th>
  <th>Comments</th>
 </tr>
 <tr>
  <td>Euler</td>
  <td>1st Order</td>
  <td>1st Order</td>
  <td>1</td>
  <td>yn + 1 = yn + y'n*dt</td>
 </tr>
 <tr>
  <td>Euler_Cromer</td>
  <td>2nd Order</td>
  <td>2nd Order</td>
  <td>2</td>
  <td>yn + 1 = yn + y'n + 1*dt</td>
 </tr>
 <tr>
  <td>ABM_Method</td>
  <td></td>
  <td>  </td>
  <td>  </td>
  <td>Adams-Bashforth-Moulton Predictor Corrector</td>
 </tr>
 <tr>
  <td>Nystrom_Lear_2</td>
  <td>2nd Order</td>
  <td>2nd Order </td>
  <td>1</td>
  <td>4th order accuracy for orbital state propagation, circular motion</td>
 </tr>
 <tr>
  <td>Runge_Kutta_2</td>
  <td>2nd Order</td>
  <td>2nd Order </td>
  <td>2</td>
  <td>Good general purpose integrator</td>
 </tr>
 <tr>
  <td>Modified_Midpoint_4</td>
  <td>4th Order</td>
  <td>2nd
