### Trick DP - Data Products Application > Viewing Data > Using External Program

b>
![trick_qp_vars_area](images/trick_qp_vars_area.jpg)

#### Vars Popup Menus

Right clicking on a variable from the Vars as shown above causes a corresponding popup menu displayed. This menu is actually the same as Vars menu.

#### Vars Popup Menus

![trick_vars_popup1](images/trick_qp_vars_popup1.jpg)
- <b>Add Var</b>
    - Adds the Vars highlighted variables to DP Content on the right.
        - If nothing is highlighted or if "Plots" is highlighted:
            - One plot per page for each selected variable will be created.
        - If "Tables" is highlighted:
            - One table with each variable representing one column will be created.
        - If "Programs" is highlighted :
            - Nothing will happen.
        - If any sub node of "Plots", "Tables", or "Programs" is highlighted:
            - Variables will be added to the corresponding node if possible.
- <b>Expand Var</b>
    - Expands the Vars highlighted variables.
- <b>Contract Var</b>
    - Collaps the Vars highlighted variables.
- <b>Change Units...</b>
    - Prompts for changing highlighted variables (first one if multiple variables selected) units.

##### DP Content

DP Content area presents the content of a DP file graphically.

<b>Trick QP - DP Content</b>

![trick_qp_dpcontent_area](images/trick_qp_dpcontent_area.jpg)

##### DP Content Popup Menus

Right clicking on a tree node at any level from the DP Content as shown above causes a corresponding popup menu displayed.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup1](images/trick_qp_dpcontent_popup1.jpg)

- <b>New Page</b>
    - Creates a new page node.
- <b>Remove All Pages</b>
    - Removes all pages.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup2](images/trick_qp_dpcontent_popup2.jpg)

- <b>New Plot</b>
    - Creates a new plot node for the page.
- <b>Remove</b>
    - Removes this page.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup3](images/trick_qp_dpcontent_popup3.jpg)

- <b>New Curve</b>
    - Creates a new curve node for the plot.
- <b>Remove</b>
    - Removes this plot.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup4](images/trick_qp_dpcontent_popup4.jpg)

- <b>Add Var</b>
    - Adds the highlighted variable from Vars to this curve.
        - If more than one variables are highlighted, error window will be shown.
        - Only one variable can be added to a curve and by default, the X variable is sys.exec.out.time.
        - A variable from Vars can be dragged over sys.exec.out.time to replace it.
        - Also, a variable from Vars can be added to a curve by dragging it over the curve node.
- <b>Remove</b>
    - Removes this curve.
- <b>New Varcase</b>
    - Adds a new varcase node.
        - If there are already variables added for this curve, new varcase node can not be added.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup5](images/trick_qp_dpcontent_popup5.jpg)

- <b>Remove</b>
    - Removes this variable.
        - X variable can not be removed.
        - X variable can be replaced.
        - Y variable can be removed.
        - Y variable can not be replaced. You need to simply remove the Y variable, and then add a new variable.

##### DP Content Popup Menus

![trick_qp_dpcontent_popup6](images/trick_qp_dpcontent_popup6.jpg)

- <b>Add Var</b>
    - Adds the highlighted variable from Vars to the varcase.
        - If more than one variables are highlighted, error window will be shown.
        - Only one variable can be added to a varcase and by default, the X variable is sys.exec.out.time.
        - A variable from Vars can be dragged over sys.exec.out.time to replace it.
        - Also, a variable from Vars can be added to a varcase by dragging it over the varcase node.
- <b>Remove</b>
    - Removes this variable.
        - X variable can not be removed.
        - X variable can be replaced.
        - Y variable can be removed.
        - Y variable can not be replaced. You need to simply remove the Y variable, and then add a new variable.

##### DP Content Popup Menus

![trick_qp
