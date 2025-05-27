### Format of Recording Groups > DRHDF5 Recording Format > Interaction with Checkpoints

 be added to the end of
the job class queue it is set.

```python
drg.set_job_class(<string class_name>)
```


## Changing the Max File Size of a Data Record Group (Ascii and Binary only)

The default size of a data record is 1 GiB. A new size can be set through the set_max_file_size method. For unlimited size, pass 0.

```python
drg.set_max_file_size(<uint64 file_size_in_bytes>)
```

## Example Data Recording Group

This is an example of a data recording group in the input file

```python
# Data recording HDF5 test
drg0 = trick.DRHDF5("Ball")
drg0.add_variable("ball.obj.state.output.position[0]")
drg0.add_variable("ball.obj.state.output.position[1]")
drg0.add_variable("ball.obj.state.output.velocity[0]")
drg0.add_variable("ball.obj.state.output.velocity[1]")
drg0.add_variable("ball.obj.state.output.acceleration[0]")
drg0.add_variable("ball.obj.state.output.acceleration[1]")
drg0.set_cycle(0.01)
drg0.freq = trick.DR_Always
trick.add_data_record_group(drg0, trick.DR_Buffer)

# This line is to tell python not to free this memory when drg0 goes out of scope
drg0.thisown = 0
```

## User accessible routines

Create a new data recording group:

```c++
Trick::DRAscii::DRAscii(string in_name);
Trick::DRBinary::DRBinary(string in_name);
Trick::DRHDF5::DRHDF5(string in_name);
```

This list of routines is for all recording formats:

```c++
int dr_disable_group( const char * in_name );
int dr_enable_group( const char * in_name );
int dr_record_now_group( const char * in_name );

int Trick::DataRecordGroup::add_variable
int Trick::DataRecordGroup::add_change_variable
int Trick::DataRecordGroup::disable
int Trick::DataRecordGroup::enable
int Trick::DataRecordGroup::set_cycle
int Trick::DataRecordGroup::set_freq
int Trick::DataRecordGroup::set_job_class
int Trick::DataRecordGroup::set_max_buffer_size

```
This list of routines provide file size configuration for Ascii and Binary:

```c++

int set_max_size_record_group (const char * in_name, uint64_t bytes ) ;
int dr_set_max_file_size ( uint64_t bytes ) ;

int Trick::DataRecordGroup::set_max_file_size

```

This list of routines provide some additional configuration for DR_Ascii format only:

```c++
int Trick::DRAscii::set_ascii_double_format
int Trick::DRAscii::set_ascii_float_format
int Trick::DRAscii::set_delimiter
int Trick::DataRecordGroup::set_single_prec_only
```

## DRAscii Recording Format

The DRAscii recording format is a comma separated value file named log_<group_name>.csv.  The contents
of this file type are readable by the Trick Data Products packages, ascii editors, and Microsoft Excel.
The format of the file follows.  Users are able to change the comma delimiter to another string.  Changing
the delimiter will change the file extension from ".csv" to ".txt".

```
name_1 {units_1},name_2 {units_2},etc...
value1,value2,etc...
value1,value2,etc...
value1,value2,etc...
value1,value2,etc...
```

## DRBinary Recording Format

The DRBinary recording format is a Trick simulation specific format.  Files written in this format are named
log_<group_name>.trk.  The contents of this file type are readable by the Trick Data Products packages from
Trick 07 to the current version.  The format of the file follows.

<a id=drbinary-file></a>
## DRBinary-File
|Value|Description|Type|#Bytes|
|---|---|---|---|
|Trick-\<vv>-\<e>| \<vv> is trick version (2 chars, "07" or "10"). \<e> is endianness (1 char) 'L' -> little endian, and 'B' -> big endian.|char|10|
|*numparms*|Number of recorded variables |char|4|
|| List of Variable Descriptors | [Variable-Descriptor-List](#variable-descriptor-list)||
|| List Data Records |[Data-Record-List](#data-record-list)||
|EOF| End of File |||


<a id=variable-descriptor-list></a>
### Variable-Descriptor-List
A Variable-
