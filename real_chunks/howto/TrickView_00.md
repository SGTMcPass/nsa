### Launching > Automatically Opening Files > TV Files

| [Home](/trick) → [Documentation Home](../../Documentation-Home) → [Running a Simulation](../Running-a-Simulation) → [Runtime GUIs](Runtime-GUIs) → Trick View |
|------------------------------------------------------------------|

Trick View (hereafter referred to as TV) is a graphical user interface that allows users to view and modify Trick-managed variables in a simulation while it is running. It also provides for the launching of integrated strip charts and can save and restore lists of variables and their associated strip charts.

### Launching
TV can be launched via one of:

- From the Simulation Control Panel, under the **Actions** menu.

![Launching Trick View from the Simulation Control Panel](images/Launch.jpg)

 - From the command line:
   `trick-tv [options]`
   The TV launch script is located in `$TRICK_HOME/bin`. Pass `--help` for a description of available options.

For additional launching options, see [Automatically Launching Applications](Runtime-GUIs#automatically-launching-applications).

### Automatically Opening Files

Files that are to be automatically opened when TV launches can be specified via one of:

- From the command line, use the `--open` option.
  File paths are relative to the directory from which TV launches.

- From the input file or user model code, use `Trick::TrickView::set_auto_open_file`.
  File paths are relative to the directory containing the S_main executable.

Opening a TV file will overwrite the current cycle period or any argument to `--cycle` with the value from the file, subject to the minimum cycle period.

### Automatically Opening and Setting Files

Files that are to be automatically opened and set when TV launches can be specified via one of:

- From the command line, use the `--openSet` option.
  File paths are relative to the directory from which TV launches.

- From the input file or user model code, use `Trick::TrickView::set_auto_open_and_set_file`.
  File paths are relative to the directory containing the S_main executable.

Opening a TV file will overwrite the current cycle period or any argument to `--cycle` with the value from the file, subject to the minimum cycle period.

### Automatically Setting Files

Files that are to be automatically set when TV launches can be specified via one of:

- From the command line, use the `--set` option.
  File paths are relative to the directory from which TV launches.

- From the input file or user model code, use `Trick::TrickView::set_auto_set_file`.
  File paths are relative to the directory containing the S_main executable.

### Strip-Chart-Only Mode

Once a collection of strip charts is established and saved to a TV file, you may wish to prevent future launches from displaying the main GUI window to allow users to view the strip charts
