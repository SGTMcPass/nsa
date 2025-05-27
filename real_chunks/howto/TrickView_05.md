### Launching > Automatically Opening Files > TV Files

  Variables are sorted alphabetically A to Z.

- **Descending Alphabetical**
  Variables are sorted alphabetically Z to A.

##### Variable Addition

The placement of newly added variables within the variable table is specified via the Position combo box. The available options are **Top**, **Before**, **After**, and **Bottom**. The **Before** and **After** options are relative to the currently selected row.

Character pointers and arrays can be treated as strings by default by checking the **char[] as string** check box. When added as such, arrays will be collapsed into single string entries. Otherwise, they will be displayed element by element.

##### Font Size

This setting affects the variable hierarchy tree, search panel, and variable table text size.

##### Default Units

Default units for each unit type can be specified via its corresponding combo box, which lists all of its available units. Selecting **xx** results in units as specified in the model code. The **Default All** check box, when selected, is equivalent to selecting **xx** for all unit types.

##### Default Formats

Default formats for each variable type can be specified via its corresponding combo box.

### The Strip Chart GUI

Strip charts allow users to plot variables in the variable table in real-time. The GUI pictured below may have a different look and feel based on the architecture of the machine on which it is running, but the functionality will remain the same.

![stripchart](images/Stripchart.jpg)

#### Domain Axis Panel

The domain axis panel allows the user to affect the range of the domain axis.

- **All**
  The domain axis will continuously adjust to contain the entirety of all plotted variables' domain values.

- **Strip**
  The domain axis will continuously scroll such that the latest sub-set (as set by the adjacent text box) of domain values is contained.

- **Fixed**
  The domain axis will not automatically change.

#### Display Panel

The display panel allows the user to specify whether or not the chart should display certain features.

- **Lines**
  When enabled, lines will be drawn between the data points.

- **Points**
  When enabled, the data points themselves will be drawn.

- **Legend**
  When enabled, the chart's legend will be shown.

#### Variables Panel

The variables panel allows the user to add and remove dependent variables, and to change the independent variable. To add a dependent variable, select it from the adjacent combo box and click the **Add** button. To remove a dependent variable, select it from the adjacent combo box and click the **Remove** button. To change the independent variable, select it from the adjacent combo box.

#### Right-Click Menu

Right-clicking the plot area will display a context menu with the following options:

- **Properties**
  Opens a dialog allowing the user to customize the plot as described below.

- **Copy**
  Copies the plot to the clipboard,
