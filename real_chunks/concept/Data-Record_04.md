### Format of Recording Groups > DRHDF5 Recording Format > Interaction with Checkpoints

|*sizeof( typeof( Variable#1))* = 8|
|...|...|...|...|
|*value*|Value of Variable #numparms |*typeof( Variable#numparms)*|*sizeof( type-of( Variable#numparms))* |

<a id=trick-07-data-types></a>
## Trick 7 Data Types
The following data-types were used in Trick-07 data recording files (that is for, *vv* = "07").

|Type value|Data Type|
|---|---|
|0|char|
|1|unsigned char|
|2|string (char\*)|
|3|short|
|4|unsigned short|
|5|int|
|6|unsigned int|
|7|long|
|8|unsigned long|
|9|float|
|10|double|
|11|Bit field|
|12|unsigned Bit field|
|13|long long|
|14|unsigned long long|
|17|Boolean (C++)|

<a id=trick-10-data-types></a>
## Trick 10 Data Types
The following data-types are used in Trick versions >= 10, that is for, *vv* = "10".

|Type value|Data Type|
|---|---|
|1 | char |
|2|unsigned char|
|4| short |
|5|unsigned short|
|6| int |
|7|unsigned int|
|8| long |
|9|unsigned long|
|10| float |
|11| double |
|12|Bit field|
|13|unsigned Bit field|
|14|long long|
|15|unsigned long long|
|17|Boolean (C++)``|
## DRHDF5 Recording Format

HDF5 recording format is an industry conforming HDF5 formatted file.  Files written in this format are named
log_<group_name>.h5.  The contents of this file type are readable by the Trick Data Products packages from
Trick 07 to the current version.  The contents of the file are binary and is not included here.  The HDF5 layout
of the file follows.

```
GROUP "/" {
    GROUP "header" {
        DATASET "file_names" {
            "param_1_file_name", "param_2_file_name", etc...
        }
        DATASET "param_names" {
            "param_1_name", "param_2_name", etc...
        }
        DATASET "param_types" {
            "param_1_type", "param_2_type", etc...
        }
        DATASET "param_units" {
            "param_1_units", "param_2_units", etc...
        }
    }
    DATASET "parameter #1" {
        value1 , value2 , value3 , etc...
    }
    DATASET "parameter #2" {
        value1 , value2 , value3 , etc...
    }
    .
    .
    .
    DATASET "parameter #n" {
        value1 , value2 , value3 , etc...
    }
}
```


### Interaction with Checkpoints

Data recording groups are able to be checkpointed, reloaded, and restarted without any interaction by the user. When a checkpoint is loaded that includes data recording,
the data recording groups will be initiated and begin recording at the time in the checkpoint. For example, if a checkpoint was dumped when t=5, when the checkpoint is
loaded into another run, it will data record starting at t=5, no matter what time in the run it was loaded or whether the run was already data recording. Loading a checkpoint
will overwrite any data recording files that were being recorded before the load.

Loading a checkpoint with different data recording groups than the current run will overwrite the current data recording groups.

Refer to test/SIM_checkpoint_data_recording to see expected behavior in action. Overall, the loading a checkpoint should completely overwrite any other data recording the sim is currently doing, and the new recording will start at the time in the checkpoint. If you come across different behavior, please open an issue.

[Continue to Checkpointing](Checkpoints)
