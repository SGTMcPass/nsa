### Launching > Automatically Opening Files > TV Files

 To remove a dependent variable, select it from the adjacent combo box and click the **Remove** button. To change the independent variable, select it from the adjacent combo box.

#### Right-Click Menu

Right-clicking the plot area will display a context menu with the following options:

- **Properties**
  Opens a dialog allowing the user to customize the plot as described below.

- **Copy**
  Copies the plot to the clipboard, allowing the user to paste the content into other applications.

- **Save As...**
  Opens a dialog allowing the user to save the plot as a PNG file.

- **Print...**
  Opens a dialog allowing the user to print the plot.

- **Zoom In**
  Zooms in either or both axes. This can also be achieved by left-click-dragging a box from its top-left to bottom-right
  corner.

- **Zoom Out**
  Zooms out either or both axes. This can also be achieved by left-click-dragging any other way than described above.

- **Auto Range**
  Automatically adjusts one or both axes.

#### Chart Properties Dialog
The Chart Properties dialog can be opened by selecting **Properties** from the plot's right-click menu. It allows the user to customize the appearance of the chart. These settings are part of the properties that are saved in TV files.

![ChartPropertiesTitleTab](images/ChartPropertiesTitleTab.jpg)

The **Title** tab allows the user to toggle visibility of the title and to set the title's text, font, size, and color.

![ChartPropertiesPlotTab](images/ChartPropertiesPlotTab.jpg)

The **Plot** tab allows the user to set the label text, font, size, and color for the domain and range axes. It also provides for toggling the visibility of each axis' tick labels and marks, for setting each axis' label font and size, and for adjusting the range of each axis.

![ChartPropertiesAppearanceTab](images/ChartPropertiesAppearanceTab.jpg)

The **Appearance** tab within the **Plot** tab allows the user to set the plot's border's width and color and the plot's background color. It also provides for inverting the axes.

![ChartPropertiesOtherTab](images/ChartPropertiesOtherTab.jpg)

The **Other** tab allows the user to set the background color of the area surrounding the plot (outside of the plot's borders) and also provides for toggling of the anti-aliasing feature. Modifying series properties is not currently supported.

### TV Files

TV files allow the user to store the states of the variable table and any existing strip charts to persistent memory. This saves configuration time for commonly used variable lists and strip chart selections.

TV files are stored as XML, the schema for which can be found [here](https://github.com/nasa/trick/blob/master/trick_source/java/src/trick/tv/resources/trickView.xsd).
