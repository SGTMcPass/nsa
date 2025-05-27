### Monte Carlo > Optimization > Modifications to S_Define

cannon ) ;
            ("shutdown") cannon_shutdown( &cannon ) ;
        }
} ;

CannonSimObject dyn ;
IntegLoop dyn_integloop (0.01) dyn ;
void create_connections() {
    dyn_integloop.getIntegrator(Runge_Kutta_4, 4);
}
```

Run the script and plot the curves.

```
% trick-CP
...
% ./S_main*.exe RUN_test/input.py
```

Once the simulation is complete, the x-y position plot should look like this:

<p align="center">
	<img src="images/MONTE_calculated_plot.png" alt="Trick-QP-Calculated"/>
</p>
