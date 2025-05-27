### [Sim Control Panel](SimControlPanel) > Shared Options > Application Behavior

| [Home](/trick) → [Documentation Home](../../Documentation-Home) → [Running a Simulation](../Running-a-Simulation) → Runtime GUIs |
|------------------------------------------------------------------|

Trick provides the following graphical user interfaces:

## [Sim Control Panel](SimControlPanel)

Send control commands to and view the status of a simulation.

## [Trick View](TrickView)

Browse and modify a simulation's variables while it's running. Launch integrated strip charts.

## [Events/Malfunctions Trick View](MalfunctionsTrickView)

Manage the events and malfunctions of a simulation.

## [Monte Monitor](MonteMonitor)

Monitor the status of a Monte Carlo simulation; create, start, and stop slaves.

## Managing External Applications

External applications are managed by instantiating and invoking calls on instances of launcher classes, which provide interfaces for setting up external applications from the input file or user model code. For instance, to manipulate Trick View from the input file:
```
trickView = trick.TrickView()
```

You now have an instance of the Trick View launcher class on which you can invoke calls to modify the actual Trick View application's behavior at launch. For instance, you could set the host and port:
```
trickView.set_host("localhost")
trickView.set_port(7000)
```

And then add it for automatic launching:
```
trick.add_external_application(trickView)
```

Provided launcher classes are derived from and listed in Trick::ExternalApplication. Some functionality is shared among launcher classes, and each class provides its own specific additional options. Trick allows any number of instances of any subclass of ExternalApplication. This means you could automatically launch two different Trick Views with completely separate settings (if you find that sort of thing useful).

## Automatically Launching Applications

Applications can be set to automatically launch during the initialization job phase by adding them to the queue of external applications managed by Trick. To do this, instantiate an instance of the appropriate launcher class (see above) and call Trick::ExternalApplication::add_external_application.

## Manually Launching Applications

Trick automatically launches all applications that have been added to its queue during simulation initialization. However, applications may also be manually launched via Trick::ExternalApplication::launch.

## Launch Command

Default commands suitable to launch each application are provided by their individual constructors. However, they may be changed, if desired, via Trick::ExternalApplication::set_startup_command.

## Launching Custom Applications or Commands

Having Trick automatically launch a custom application, or execute any command at all really, is a simple matter of instantiating an instance of the base class ExternalApplication and then setting the desired command as described above.
```
customApplication = trick.ExternalApplication()
customApplication.set_startup_command("echo Hello World!")
customApplication.set_arguments("")
trick.add_external_application(customApplication)
```

Note that ExternalApplication automatically appends the host and port argument unless you set the
