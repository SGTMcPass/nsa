### User accessible routines > Input File Setup > Dumping and Loading a Checkpoint

 own RUN_ directory).

The following are attributes for configuring the Master's checkpointing interface to each Slave:

```
Trick::SlaveInfo::chkpnt_dump_auto
Trick::SlaveInfo::chkpnt_load_auto
Trick::SlaveInfo::chkpnt_binary
Trick::SlaveInfo::reconnect_wait_limit
```

If you do not want the Slave to dump/load a checkpoint when the Master does, you can turn off either feature in the
Master input file like so:

```
new_slave.chkpnt_dump_auto = 0
new_slave.chkpnt_load_auto = 0
```

in which case your Slave would have to have its own model code to perform a checkpoint dump/load.

When chkpnt_load_auto=1, the Slave restarting and reconnecting should occur within a second or two. If chkpnt_load_auto=0, the user has
to restart the slave himself (and may even be typing in the checkpoint executable on the command line), so reconnect_wait_limit should be
set accordingly.

[Continue to Data Recording](Data-Record)
