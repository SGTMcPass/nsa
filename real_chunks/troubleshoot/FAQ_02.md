### Appendix > Is Trick gluten-free, grass-fed, organic, non-GMO, environmentally conservative, free-range, vegan, and dolphin safe?

 applications via the variable server; the variable server contains the values of a simulation which can then be sent over TCP/IP to a client application.

<a name="matlabsimulink"></a>

### MATLAB/Simulink
MathWorks developed a package to generate Trick friendly code from their models. An introduction video on Trick-MATLAB/Simulink interfacing can be found [here.](http://www.mathworks.com/videos/connecting-simulink-with-other-simulation-frameworks-86546.html)

<a name="coreflightsoftware"></a>

### Core Flight Software (CFS)

cFS support for Trick is provided by the following external projects:

* [TVS-IO](https://github.com/nasa/tvsio) is an open-source, Core Flight Software (cFS) application that provides for two-way communication between a **cFS** Software Bus Network (SBN) and a Trick simulation.

* Another soon to be released capability, presumably called TrickCFS should also be available soon as open-source software. Stay-tuned.

<a name="ifoundabugwithtrickhowdoitellsomeone"></a>

## I found a bug with Trick, how do I tell someone?
Create an issue on GitHub [here](https://github.com/nasa/trick/issues/new). The more descriptive you are, the faster we can solve the issue.

![SubmitAnIssue](images/SubmitAnIssue.jpg)


<a name="ihaveaquestionabouttrickwhereshouldiaskit"></a>

## I have a question about Trick, where should I ask it?
Create an issue on GitHub [here](https://github.com/nasa/trick/issues/new) with "QUESTION: " appended to the title.

![AskingAQuestion](images/AskingAQuestion.jpg)


<a name="whywontmytricksimulationcompile"></a>

## Why won't my Trick simulation compile?
There are many reasons why a simulation will fail to compile properly.

01. Trick can't find your header files or source code.
02. You haven't properly set your environmental variables.
03. You haven't properly installed all required dependencies.

<a name="whatunitscantrickuse"></a>

## What units can Trick use?
Trick is capable of utilizing the vast majority of imperial and metric units. Trick uses the UDUNITS C library/database in its unit calculations. For a list of the most common units, run
