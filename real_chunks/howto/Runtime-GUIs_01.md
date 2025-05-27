### [Sim Control Panel](SimControlPanel) > Shared Options > Application Behavior

 automatically launch a custom application, or execute any command at all really, is a simple matter of instantiating an instance of the base class ExternalApplication and then setting the desired command as described above.
```
customApplication = trick.ExternalApplication()
customApplication.set_startup_command("echo Hello World!")
customApplication.set_arguments("")
trick.add_external_application(customApplication)
```

Note that ExternalApplication automatically appends the host and port argument unless you set the arguments by calling Trick::ExternalApplication::set_arguments.

Why would anyone want to have Trick automatically run additional commands? Well, for one thing, it saves you from manually running them each time you run a sim or writing a script to do it. But more importantly, applications managed by Trick are included in binary checkpoints, which means they can be saved and restored with no work on your part!

## Shared Options

As each Trick GUI was written by a different developer and few standards were in place, most options vary according to each GUI. The following apply to at least Trick View and Monte Monitor. Application-specific options can be passed from the input file or user model code via Trick::ExternalApplication::set_arguments or Trick::ExternalApplication::add_arguments.

### Host

The host of the Variable Server to which the application will connect at launch can be specified via one of:

- From the command line, use the --host option.
- From the input file or user model code, use Trick::ExternalApplication::set_host

If no host is specified, it will automatically be set to that of the simulation which is launching this application.

### Port

The port of the Variable Server to which the application will connect at launch can be specified via one of:

- From the command line, use the --port option.
- From the input file or user model code, use Trick::ExternalApplication::set_port

If no port is specified, it will automatically be set to that of the simulation which is launching this application.

### Automatically Reconnect

The application can be configured to automatically reestablish lost connections via one of:

- From the command line, use the --autoReconnect option.
- From the input file or user model code, use Trick::ExternalApplication::set_auto_reconnect
- From the application, use the File->Settings menu.

The default value is false.

### Window Size and Placement

The window's coordinates and dimensions at launch can be set via one of:
- From the command line, use the --x, --y, --width, or --height options.
- From the input file or user model code, use Trick::ExternalApplication::set_x, Trick::ExternalApplication::set_y, Trick::ExternalApplication::set_width, or Trick::ExternalApplication::set_height.

### Cycle Period

The period (in seconds) at which the Variable Server sends information to the application can be specified via one of:

- From the command line, use the --cycle option.
- From the input file or
