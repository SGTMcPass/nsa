### Integrator Control Inputs

>Nystrom_Lear_2</td>
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
  <td>2nd Order </td>
  <td>3</td>
  <td>Good accuracy with less derivative evaluations, be careful with high frequency statesr</td>
 </tr>
 <tr>
  <td>Runge_Kutta_4</td>
  <td>4th Order</td>
  <td>1st Order </td>
  <td>4</td>
  <td>Good general purpose integrator, although a little time consuming</td>
 </tr>
 <tr>
  <td>Runge_Kutta_Gill_4</td>
  <td>4th Order</td>
  <td>1st Order </td>
  <td>4</td>
  <td>Good general purpose integrator, although a little time consuming</td>
 </tr>
 <tr>
  <td>Runge_Kutta_Fehlberg_45</td>
  <td>5th Order</td>
  <td>1st Order </td>
  <td>6</td>
  <td>Designed for larger time steps and smooth states, orbital state propagator</td>
 </tr>
 <tr>
  <td>Runge_Kutta_Fehlberg_78</td>
  <td>8th Order</td>
  <td>1st Order </td>
  <td>12</td>
  <td>Designed for larger time steps and smooth states, orbital state propagator</td>
 </tr>
 <tr>
  <td>User_Defined</td>
  <td>N/A</td>
  <td>N/A</td>
  <td>N/A</td>
  <td>Used to bypass trick integration utilities</td>
 </tr>
</table>

The <b> Option </b> column are the integration algorithm options.
The <b> Accuracy </b> column gives the order of accuracy for the integrator.
The <b> DiffEQ </b> column gives the order of teh differential equation set the integrator formulation assumes.
For example, a 1st order DiffEQ integrator integrates accelerations to velocities independently of the velocity
to position integration.  However, a 2nd order DiffEQ integrator integrates the velocity to position states
dependent on the acceleration to velocity state integration.  The # <b> Deriv </b> column specifies the number
of derivative evaluations performed to integrate across a full time step (also known as the number of
integration passes).  The <b> Comments </b> column gives some special notes for the usage of each integrator.

[Continue to Frame Logging](Frame-Logging)
