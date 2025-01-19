# Calling External Functions
CATAI Magic Systems of Systems Architect (MSOSA) has a great feature to call external programs for analysis. These are called using Opaque Actions. This example demonstrates how to call Python 3 functions from MSOSA Activity Diagrams.

This directory should contain the following
 * .MDZIP files, which are the native file for MSOSA.
 * .py files, which are the external helper functions.
 * Screenshots and diagram images to show the procedure.
 * README.md (this file) that has code snippets for the opaque actions.
 
## Setting up the Model
For this minimal example, setup a Systems Context and establish Use Cases. From the Use Case, we'll call an activity diagram. There will be a couple helper actions that we can use to glue the inputs and outputs.

The external functions should be commandline interfaces and use the argument parser to process inputs from the a command line interface (CLI). In this case, input arguments must not contain new line or carriage return characters and be input as ASCII. If more complex inputs are needed, then file saving and reading can be used. 

If binary (i.e. non-ASCII) data is needed, we'll encode the data using base64. 

### Example: Asymmetric Keys
THis example is to generate a public-private key pair using Ellipic Curve Cryptograpy. This is useful to ensure the system modeler is able to generate and demonstrate an instance that is mathematically correct. A private key is used to derive a public key. Therefore, the private key must be generated first. If a systems modeler were to reverse these oprations in a bahavior model, there are no built-in checks to catch this. Without calling external functions, MSOSA and the model analyst would simply pass an execution token from one action to another without regards to the mathematical artifacts generated with those actions. In this example, however, we'll show the artifact generation and the process will fail if not done in the correct order. This helps with model checking.

### System Context


### Use Cases

### Activity Diagram

### Helper Functions

## Results
