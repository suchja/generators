# Analysis of dependency between Tinkerforge (sub)components

Tinkerforge consists of many different software components. Those have dependencies on each other. As these dependencies are only documented in source code, this documents tries to outline the most important dependencies. The knowledge about the dependencies is required to fully understand the workflow of developing and building the different components.

## CSharp - language binding

Building this language binding requires the following tools:

-	python:2.7.10-wheezy
-	mono-devel
-	nuget

The following scripts can be run with solely the `generators` repository:

-	`generate_csharp_bindings.py`
-	`generate_csharp_nuget_package.py`
-	`generate_csharp_zip.py`

For the `test_csharp_bindings.py` script additionally the repositories `wheather-station` and `hardware-hacking` are required.

Finally there is the language specific generation of documentation in the script `generate_csharp_doc.py`. This requires all bricks and bricklets repositories.
