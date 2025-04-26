# MSOSA Cryptography Examples
The Magic Model Analyst in MSOSA is a helpful tool for visualizing behavioral diagrams in CATIA Magic Systems of Systems Architect, used for Model-Based Systems Engineering (MBSE). The simulation tool is also flexible enough to enable modelers to call external programs and write custom code in different languages, one of which is Python. However, the Python deployment in MSOSA 2024 is version 2, which does not support the `bytes` and `bytearray` data types. This means libraries that depend on these data types are not available within MSOSA, such as the library documented at [https://cryptography.io](https://cryptography.io).

For this repository and its examples, the goal is to simulate some basic cryptographic recipes to demonstrate system design in simulated SysML activity diagrams. Since we want to use Python 3 for the examples, we must also craft external command-line scripts to call with opaque actions in the nested activity diagrams. This is a useful feature, so the package containing the `RunCommand` activity diagram is available in this repository at [CallingExternalFunctions](https://github.com/SystemsCyber/MBSE/tree/main/CallingExternalFunctions).

This directory should contain the following:
 * `.MDZIP` files, which are the native files for MSOSA.
 * `.py` files, which are the external helper functions.
 * Screenshots and diagram images to show the procedure.
 * `README.md` (this file), which contains examples from the files.

 ### System Context
 The examples and files in this directory have a system context modeled as a SysML block definition diagram (bdd) to show different concepts in cryptography. This hierarchy was inspired by Chapter 5 in Ross Anderson's *Security Engineering* text: [https://www.cl.cam.ac.uk/archive/rja14/book.html](https://www.cl.cam.ac.uk/archive/rja14/book.html). The bdd to show context is as follows:
 
 ![SystemsContext](Context.svg)