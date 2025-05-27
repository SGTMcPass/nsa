### [Sim Control Panel](SimControlPanel) > Shared Options > Application Behavior

.
- From the input file or user model code, use Trick::ExternalApplication::set_x, Trick::ExternalApplication::set_y, Trick::ExternalApplication::set_width, or Trick::ExternalApplication::set_height.

### Cycle Period

The period (in seconds) at which the Variable Server sends information to the application can be specified via one of:

- From the command line, use the --cycle option.
- From the input file or user model code, use Trick::ExternalApplication::set_cycle_period.
- From the application, use the File->Settings menu.

The cycle period must be a non-negative number. Specify 0 to recieve updates at the maximum rate. Values below the minimum cycle period will be set to the minimum cycle period.

### Minimum Cycle Period

The minimum period (in seconds) at which the Variable Server can be requested to send information to the application can be specified via one of:

- From the command line, use the --minCycle option.
- From the input file or user model code, use Trick::ExternalApplication::set_minimum_cycle_period.

The minimum cycle period must be a non-negative number. The recommended and default value is 0.1. Values below this may cause instability in Trick GUIs.

### Application Behavior

The application can take one of several actions when it loses the connection with the simulation:

- Close
    Terminate and close.

- Notify
    Present a notification dialog describing the failure.

- Nothing
    Do nothing.

This behavior can be specified via one of:

- From the command line, use the --disconnectBehavior option.
- From the input file or user model code, use Trick::ExternalApplication::set_disconnect_behavior.
- From the application, use the File->Settings menu.

[Continue to Runtime Output](../Runtime-Output)
