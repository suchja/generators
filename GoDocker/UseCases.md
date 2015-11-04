# General Introduction to Docker container for the TF language bindings

Why is it a good idea to use docker for the tinkerforge language bindings? I see the following use cases:

1.	Have an easy to use development environment which can be quickly setup on any machine running Docker.
2.	Have an build environment which can be used with (m)any continuous integration and deployment plattform.
3.	Have an deployment environment, which lets you use and test any version and variant of the language binding.

## Development environment (Use Case #1)

The generators are completely developed in Python. That means developing a language binding requires a development environment for Python. This is well documented in the [generator's Readme](https://github.com/Tinkerforge/generators). Looking further into the first use case it appears, that not only Python is required, but also the technology required for each of the language bindings. Otherwise it is possible to change the generator's code, but it is not possible to test those changes.

So we can say it is required to have a development environment for Python to change and recompile any/all of the available generators. Basically this environment is required to ensure that the changes are compile-clean, but nothing more.

### Input for this environment

Either the master branch of the generators repository or a specific development branch is the key input for this environment.

### Output of this environment

The final output of this environment is a commit to the generators repository (either master or development branch). Inbetween the generators binaries are created to ensure that changes are compile clean. These binaries are an intermediate output, because they should be tested as well. However, that will not happen in this development environment, because for testing a language binding the matching technology, tests and additional infrastructure is required.

### Required functionality in this environment

For changing any of the generators the following functionality is required:

-	Git including access rights / ssh keys to commit changes and pull requests
-	Python to generate a new version of the language binding containing the changes
-	Editor to change python code of the generators, bricks and bricklets.
-	Editor to change the language specific parts of the language binding
-	Execution / build environment according to the language binding (e.g. mono, ruby, ...)
-	Environment containing brickv, brickd and the hardware for testing an example attached to it. A better alternative would be to have unit and integration tests, which do not require the hardware. What would be a good way to simulate the hardware? Could we use something like a Mock brickd for examples? Brickd is written in pure C.

## Build environment (Use Case #2)

Building a releasable version of each of the language bindings is basically the same as building a development version. The key difference is that the 

### Input for this environment

The master branch of the generators repository.

### Output of this environment

A zip-file for each language binding containing the binaries. The zip-file is created by the python script `generate_..._zip.py`.

### Required functionality in this environment

-	Git including access rights / ssh keys to commit changes and pull requests
-	Python to generate a new version of the language binding containing the changes
-	Execution / build environment according to the language binding (e.g. mono, ruby, ...)
-	Environment containing brickv, brickd and the hardware for testing an example attached to it. A better alternative would be to have unit and integration tests, which do not require the hardware. What would be a good way to simulate the hardware? Could we use something like a Mock brickd for examples? Brickd is written in pure C.
-	Are there any additional requirements for continuous integration environments?
