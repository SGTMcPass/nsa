### Format of Recording Groups > DRHDF5 Recording Format > Interaction with Checkpoints

|---|---|---|---|
|Trick-\<vv>-\<e>| \<vv> is trick version (2 chars, "07" or "10"). \<e> is endianness (1 char) 'L' -> little endian, and 'B' -> big endian.|char|10|
|*numparms*|Number of recorded variables |char|4|
|| List of Variable Descriptors | [Variable-Descriptor-List](#variable-descriptor-list)||
|| List Data Records |[Data-Record-List](#data-record-list)||
|EOF| End of File |||


<a id=variable-descriptor-list></a>
### Variable-Descriptor-List
A Variable-Descriptor-List is a sequence of [Variable-Descriptors](#variable-descriptor).
The number of descriptors in the list is specified by *numparms*. The list describes each of the recorded variables, starting with the simulation time variable.

|Value|Description|Type|#Bytes|
|---|---|---|---|
|[*Time-Variable-Descriptor*](#time-variable-descriptor)| Descriptor for Variable # 1. This first descriptor always represents the simulation time variable.| [Variable-Descriptor](#variable-descriptor) |34|
|...|...|...|...|
|| Descriptor for Variable # *numparms* |[Variable-Descriptor](#variable-descriptor)|variable|

<a id=variable-descriptor></a>
### Variable-Descriptor
A Variable-Descriptor describes a recorded variable.

|Value|Description|Type|Bytes|
|---|---|---|---|
| *namelen*| Length of Variable Name |int|4|
| *name*   | Variable Name ||*namelen*|
| *unitlen*| Length of Variable Units |int|4|
| *unit*   | Variable Units ||*unitlen*|
| *type*   | Variable Type (see Notes 2. & 3.)|int|4|
| *sizeof(type)*   | Variable Type Size |int|4|

**Notes:**

1. the size of a Variable-Descriptor in bytes = *namelen* + *unitlen* + 16.
2. If *vv* = "07", use [Trick 07 Data Types](#trick-07-data-types).
3. If *vv* = "10", use [Trick 10 Data Types](#trick-10-data-types).

<a id=time-variable-descriptor></a>
### *Time-Variable-Descriptor*
|Value|Description|Type|Bytes|
|---|---|---|---|
|17| Length of Variable Name |int|4|
|```sys.exec.out.time```| Variable Name |char|17|
|1| Length of Variable Units |int|4|
|```s```| Variable Units (see Note 1.) |char|1|
|11| Variable Type |int|4|
|8| Variable Type Size |int|4|

**Notes:**

1. Here, we are assuming "vv" = "10", and so, referring to [Trick 10 Data Types](#trick-10-data-types), Variable Type = 11, which corresponds to **double**.

<a id=data-record-list></a>
### Data-Record-List
A Data-Record-List contains a collection of [Data-Records](#data-record), at regular times.

|Value|Description|Type|Bytes|
|---|---|---|---|
||Data-Record #1|[Data-Record](#data-record)||
|...|...|...|...|
||Data-Record #Last|[Data-Record](#data-record)||

<a id=data-record></a>
### Data-Record
A Data-Record contains a collection of values for each of the variables we are recording, at a specific time.

|Value|Description|Type|Bytes|
|---|---|---|---|
|*time*|Value of Variable #1 (time) |*typeof( Variable#1 )*|*sizeof( typeof( Variable#1))* = 8|
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
|
