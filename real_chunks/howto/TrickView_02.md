### Launching > Automatically Opening Files > TV Files

 A black screen indicates they are not.

#### Variable Buttons

The variable buttons affect variables in the variable table. From left to right, they are:

- **Strip Chart**
  Launches a strip chart that will plot all selected variables on the same graph while the simulation is running.

- **Delete**
  Removes the selected variables from the variable table and all strip charts.

#### Variable Hierarchy Tree

This panel displays all of the simulation's Trick-managed variables in a hierarchical format. Initially, only the top-level simulation objects are displayed. A variable representing a structure or class containing variables can be expanded or collapsed by double-clicking its name or by single-clicking the expand/collapse node to the left of its name. Double-clicking a variable that does not represent a structure or class will add it to the variable table. Multiple variables can be simultaneously selected via the shift and control (command on Mac) keys. Variables can also be added by selecting them, right-clicking anywhere in the variable hierarchy tree, and selecting **Add Selection** from the pop-up menu. Adding a variable that represents a structure or class will add all of its contained variables (at all lower levels). The top layer of the variable hierarchy tree will be populated when TV has finished parsing the information from the simulation, which takes place in the background. Lower levels are loaded on-demand as the tree is expanded. Although unlikely to occur in practice, it is possible that expanding every node in a large simulation will consume all of the application's available memory, in which case it will become unresponsive.

#### Search Panel

The search panel allows the user to search the variable hierarchy tree by partial name or regular expression, with an option for case sensitivity. Resulting listed variables can be added to the variable table in manners similar to those of the variable hierarchy tree. The search panel becomes available for use at the same time as the variable hierarchy tree. Search progress is indicated by a progress bar below the results list. During the initial search, only an indication of activity is given while the application counts the total number of variables. In subsequent searches, a quantitative value of progress is displayed.

#### Index Specification Window

When adding variables to the variable table, if any variables are pointers or arrays, the index specification window will be displayed, allowing the user to specify the ranges to add.

![Specify Indices](images/SpecifyIndices.jpg)

Each array displays a combo box over its allowable range. Each pointer has a single text box that accepts values in the form `minimum-maximum`. Character pointers and arrays have a check box allowing them to be treated as strings. The position radio buttons specify where in the variable table the variables will be added, relative to the currently selected row.

#### Variable Table

The variable table lists all the added variables, displaying their names, values, units, and formats. Columns can be freely rearranged by clicking and dragging their headers. Rows can be sorted by clicking the column header corresponding to the
