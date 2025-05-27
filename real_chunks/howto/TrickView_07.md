### Launching > Automatically Opening Files > TV Files

 series properties is not currently supported.

### TV Files

TV files allow the user to store the states of the variable table and any existing strip charts to persistent memory. This saves configuration time for commonly used variable lists and strip chart selections.

TV files are stored as XML, the schema for which can be found [here](https://github.com/nasa/trick/blob/master/trick_source/java/src/trick/tv/resources/trickView.xsd). Trick 15 TV files are not backwards compatible with any previous version of Trick. However, a script exists to convert Trick 13 TV files. See ${TRICK_HOME}/bin/convert_tv_file.

While it is possible to manually modify TV files, users do so at their own risk. TV only checks that a file is well-formed. No further validation is performed.

Forward compatibility of TV files with future releases is not guaranteed.
