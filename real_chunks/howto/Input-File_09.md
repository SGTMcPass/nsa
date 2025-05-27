### Accessing Simulation Parameters > I Just Want to Know How Do I Set this Value...

 an event can be inserted before/after multiple target jobs,
# in which case it will be evaluated multiple times per frame
# The job name string is the "sim_object.job_name" from the S_define file.
# The job instance is used to specify which instance of the job to use if identically named jobs are
# multiply defined in a sim object.  If the argument is not specified, the first instance of the is the default.
trick.add_event_before(<event name>, "<job name string>" [, <job instance> = 1])
trick.add_event_after(<event name>, "<job name string>" [, <job instance> = 1])

# Remove an event from everywhere it's been added (you can then subsequently add the event again if you want)
trick.remove_event(<event_name>)

# Delete an event permanently from the sim so that you can no longer add it again
trick.delete_event(<event_name>)

# Use a model variable or job as a condition
# It is more optimal to use model code as a condition, because of the python parsing involved in a normal condition()
# Variable (the variable's value will be taken as the condition boolean) :
<event name>.condition_var(<index>, "<variable name>" [,"<optional comment displayed in mtv>"])
# Job (the job's return value will be taken as the condition boolean) :
<event name>.condition_job(<index>, "<job name>" [,"<optional comment displayed in mtv>"])
# Any combination of condition(), condition_var(), or condition_job() can be used for your malfunction condition(s).
# NOTE: If the job is something you created just for use in malfunctions (e.g. it is not a scheduled job),
        then it must be specified once and only once in the S_define file as a "malfunction" class job.

# Set an event condition's "hold" on so that when it fires, it stays in the fired state, causing actions to run every cycle
# (the default is hold off so fire only once)
<event name>.condtion_hold_on(<index>)    # the opposite would be <event name>.condition_hold_off(<index>)
# Note that you would still need "activate" in your action otherwise hold_on won't have any effect.

# Disable a condition from being evaluated (default is enabled)
<event name>.condition_disable(<index>)    # the opposite would be <event name>.condition_enable(<index>)

# Use a model job as an action
# It is more optimal to use model code as an action, because of the python parsing involved in a normal action()
<event name>.action_job(<index>, "<job name>" [,"<optional comment displayed in mtv>"])
# Turn a model job ON/OFF as an action
<event name>.action_job_on(<index>, "<job name>" [,"<optional
