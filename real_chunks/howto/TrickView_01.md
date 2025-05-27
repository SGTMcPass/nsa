### Launching > Automatically Opening Files > TV Files

 the directory from which TV launches.

- From the input file or user model code, use `Trick::TrickView::set_auto_set_file`.
  File paths are relative to the directory containing the S_main executable.

### Strip-Chart-Only Mode

Once a collection of strip charts is established and saved to a TV file, you may wish to prevent future launches from displaying the main GUI window to allow users to view the strip charts without providing them (potentially dangerous) access to the simulation's internal variables. You can cause Trick View to launch in strip-chart-only mode via one of:

- From the command line, use the `--stripChartsOnly` option.

- From the input file or user model code, use `Trick::TrickView::set_strip_charts_only`.

Note that you must provide a TV file to be automatically opened as described above when launching in strip-chart-only mode.

### The Trick View GUI

The GUI pictured below may have a different look and feel based on the architecture of the machine on which it is running, but the functionality will remain the same.

![TrickView](images/TrickView.jpg)

#### File Buttons

The file buttons provide persistent storage of variable lists. From left to right, they are:

- **New**
  Clears the variable table.

- **Open**
  Opens a dialog allowing the user to select a TV file. The variable table will be cleared and replaced by the variables from the file. The saved cycle period and any strip charts will be restored.

- **Open And Set**
  Opens a dialog allowing the user to select a TV file. The variable table will be cleared and replaced by the variables from the file. Additionally, the variables will be set to their corresponding values in the file. The saved cycle period and any strip charts will be restored.

- **Set**
  Opens a dialog allowing the user to select a TV file. The variables listed in the file will be set to their corresponding values in the file. The variable table, cycle period, and any strip charts will be unaffected.

- **Save**
  Opens a dialog allowing the user to specify a file name. The variables in the variable table and their associated information, the cycle period, and any strip charts will be written to the file.

#### Monitor Button

The monitor button displays the current state of the monitor and allows the user to toggle receiving updates on the variables in the variable table. A blue screen indicates that updates are being received. A black screen indicates they are not.

#### Variable Buttons

The variable buttons affect variables in the variable table. From left to right, they are:

- **Strip Chart**
  Launches a strip chart that will plot all selected variables on the same graph while the simulation is running.

- **Delete**
  Removes the selected variables from the variable table and all strip charts.

#### Variable Hierarchy Tree

This panel displays all of the simulation
