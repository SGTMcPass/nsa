### Launching > Automatically Opening Files > TV Files

imum`. Character pointers and arrays have a check box allowing them to be treated as strings. The position radio buttons specify where in the variable table the variables will be added, relative to the currently selected row.

#### Variable Table

The variable table lists all the added variables, displaying their names, values, units, and formats. Columns can be freely rearranged by clicking and dragging their headers. Rows can be sorted by clicking the column header corresponding to the property by which they should be sorted. Rows are sorted first by the most recently clicked column header, then by the header clicked before that, and so forth. Rows can be manually reordered by clicking and dragging them. Note that manual reordering will remove any currently applied sorting. Further display customization is available via the Column Control Menu, which is accessed by clicking the miniature table icon in the upper right-hand corner of the table. Pressing the **Delete** key while the variable table has focus is equivalent to clicking the delete variable button.

While you cannot actually change a variable's name, you can quickly add another variable of a similar name by double-clicking the name cell of a variable and modifying it. The original variable will remain unchanged, and a variable of the new name will be added.

Each variable's value is displayed according to its type and format. Booleans are represented by check boxes; enumerated types, by combo boxes; and all other types, by a string. Modifying a variable's value is achieved by clicking the check box, selecting a value from the combo box, or directly entering a new value. Inputs are validated against the variable's type before being submitted to the Variable Server. Note that the displayed value will not change until the Variable Server reflects the change.

Variable units are displayed via a combo box containing all of the supported units. To change a variable's units, click its units cell and select a new value. Note that the displayed units will not change until the Variable Server reflects the change.

Variable formats are displayed via a combo box containing all of the supported formats for the variable's type. To change a variable's format, click its format cell and select a new value. The displayed value will be updated immediately.

Multiple, non-contiguous selections are allowed and may be used to affect mass value, unit, and format changes. When performing a mass edit, the assigned/selected value will only be applied to variables that can accept it.

##### Invalid References

Variables that the Variable Server failed to resolve display values of **\<Invalid Reference\>** and are highlighted in red. Such a variable's value and units cannot be changed, but its name can still be modified for the purpose of adding new variables.

#### Manual Entry Field

The manual entry field provides the user a means by which to directly add a variable of any name. This is useful if a variable's information is not present in the S_sie.resource file or the file itself is not present, or if the variable is a pointer to the beginning
