### 5 Verification

 are:
1. variable name
2. seed for random generator, defaults to 0
3. mean of distribution, defaults to 0
4. standard-deviation of distribution, defaults to 1.

The normal distribution may be truncated, and there are several configuration settings associated with truncation. Note that for all of these truncation options, if the lower truncation bound is set to be larger than the upper truncation bound, the generation of the dispersed value will fail and the simulation will terminate without generation of files. If the upper andlower bound are set to be equal, the result will be a forced assignment to that value.

`TruncationType`

This is an enumerated type, supporting the specification of the truncation limits in one of three ways:
* `StandardDeviation`: The distribution will be truncated at the specified number(s) of standard deviations away from the mean.
* `Relative`: The distribution will be truncated at the specified value(s) relative to the mean value.
* `Absolute`: The distribution will be truncated at the specified value(s).

`max_num_tries`

The truncation is performed by repeatedly generating a number from the unbounded distribution until one is found that lies within the truncation limits. This max_num_tries value determines how many attempts may be made before the algorithm concedes. It defaults to 10,000. If a value has not been found within the specified number of tries, an error message is sent and the value is calculated according to the following rules:
* For a distribution truncated at only one end, the truncation limit is used
* For a distribution truncated at both ends, the midpoint value between the two truncation limits is used.

`truncate( double limit
