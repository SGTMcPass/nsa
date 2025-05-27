### 5 Verification

 value is calculated according to the following rules:
* For a distribution truncated at only one end, the truncation limit is used
* For a distribution truncated at both ends, the midpoint value between the two truncation limits is used.

`truncate( double limit, TruncationType)`

This method provides a symmetric truncation, with the numerical value provided by limit being interpreted as a number of standard-deviations either side of the mean, a relative numerical value from the mean, or an absolute value.

The value limit should be positive. If a negative value is provided, it will be negated to a positive value.

The use of TruncationType Absolute and this method requires a brief clarification because this may result in an asymmetric distribution. In this case, the distribution will be truncated to lie between (-limit, limit) which will be asymmteric for all cases in which the mean is non-zero.

`truncate( double min, double max, TruncationType)`

This method provides a more general truncation, with the numerical value provided by min and max being interpreted as a number of standard-deviations away from the mean, a relative numerical value from the mean, or an absolute value.

Unlike the previous method, the numerical arguments (min and max) may be positive or negative, and care must be taken especially when specifying min with TruncationType StandardDeviation or Relative. Realize that a positive value of min will result in a lower bound with value above that of the mean; min does not mean “distance to the left of the mean”, it means the smallest acceptable value relative to the mean.

`truncate_low( double limit, TruncationType)`

This method provides a one-sided trunc
