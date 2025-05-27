### Product.dtd > A general DP Product XML File Example

                --
------------------------------------------------------------------------
     -6.859943e-01     -4.115966e-01     -6.859943e+00     -4.115966e+00
     -6.853979e-01     -4.125891e-01     -6.853979e+00     -4.125891e+00
     -6.848069e-01     -4.135693e-01     -6.848069e+00     -4.135693e+00
     -6.842212e-01     -4.145375e-01     -6.842212e+00     -4.145375e+00
     -6.836408e-01     -4.154939e-01     -6.836408e+00     -4.154939e+00
     -6.830657e-01     -4.164388e-01     -6.830657e+00     -4.164388e+00
     -6.824956e-01     -4.173724e-01     -6.824956e+00     -4.173724e+00
     -6.819306e-01     -4.182949e-01     -6.819306e+00     -4.182949e+00
     -6.813706e-01     -4.192065e-01     -6.813706e+00     -4.192065e+00
     -6.808155e-01     -4.201075e-01     -6.808155e+00     -4.201075e+00
     -6.802652e-01     -4.209980e-01     -6.802652e+00     -4.209980e+00
     -6.797196e-01     -4.218782e-01     -6.797196e+00     -4.218782e+00
     -6.791788e-01     -4.227484e-01     -6.791788e+00     -4.227484e+00
     -6.786426e-01     -4.236086e-01     -6.786426e+00     -4.236086e+00
     -6.781109e-01     -4.244592e-01     -6.781109e+00     -4.244592e+00
     -6.775837e-01     -4.253003e-01     -6.775837e+00     -4.253003e+00
     -6.770610e-01     -4.261320e-01     -6.770610e+00     -4.261320e+00
     -6.765426e-01     -4.269545e-01     -6.765426e+00     -4.269545e+00
     -6.760285e-01     -4.277680e-01     -6.760285e+00     -4.277680e+00
     -6.755186e-01     -4.285727e-01     -6.755186e+00     -4.285727e+00
     -6.750130e-01     -4.293687e-01     -6.750130e+00     -4.293687e+00
     -6.745114e-01     -4.301562e-01     -6.745114e+00     -4.301562e+00
     -6.740139e-01     -4.309353e-01     -6.740139e+00     -4.309353e+00
```

## DP External Programs

The <b>extfn</b> element provides a means for transforming data. Users build a program that is dynamically linked into
Trick data products for manipulating data specified in the DP Product XML file and its document type definition file
is stated as @ref product_dtd "Product.dtd".

### Element extfn Specifications
The <b>extfn</b> needs to have 3 element specifications associated with it. These elements are <b>fname</b>, <b>inputs</b>, and <b>outputs</b>.
The <b>fname</b> is a full path to a program which accepts the inputs and generates the outputs. This
program
