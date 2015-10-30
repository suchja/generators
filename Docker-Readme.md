# About

Describes how to build and run the tinkerforge language bindings in [Docker](https://www.docker.com) container.

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

# Design

Here some initial thought about how to design a solution for the use cases:

-	Seems like python is always required or I need to replace the existing `generate_..._zip.py`. So that would basically mean I need new Images for each langauge binding which consist of python and the biuld/execution environment for the langauge.
-	One idea for having a container, which can directly publish releases to github, is to bind-mount ssh-keys from either a host dir or from a dedicated data-container. **Attention:** It seems like the releases on github are only zipped source code files. The final binaries are only available from the Tinkerforge website. What's the intention of the zip files on GitHub?
-	It is probably a good idea to have a data-container, which initially receives the source code either from master or from development branch. All other development / build container will link this data-container and use the sources from there and also add their output (e.g. binaries) to that container. So it is something like a central data hub for all containers.
-	I guess the following Dockerfile / Images are required:
 -	Dockerfile cloning all repositories as basis for a data-only-container with the required source code. -> tf-root dir
 -	Dockerfile for building each of the language binding. -> in the language binding dir
 -	There is probably no need for a Dockerfile in the generators root dir.
 -	brickv as well as brickd will get their own Dockerfile for building and running.
 -	define how to handle firmware build and deploy process

# Current State & Next Steps

I'm working on this document as well as on the Dockerfiles and stuff around it. So this section basically shows me what I'm working on and what are the next steps.

## Activities I'm working on

-	Done: Build Dockerfile for compiling C# language binding
-	Understand how to get source code into containers [Discussion in Docker Forums](https://forums.docker.com/t/best-practices-for-getting-code-into-a-container-git-clone-vs-copy-vs-data-container/4077)
-	Try setting up a data container with the complete source code (including examples) and a volume for binaries
 -	Done: Ensure that `git clone` is always executed independently of the cache [compare this article](http://thenewstack.io/understanding-the-docker-cache-for-faster-builds/).
 -	Done: Avoid copying downloaded data when container is started from image [as outlined in this article](https://jpetazzo.github.io/2015/01/19/dockerfile-and-data-in-volumes/).
 -	Done: Do everything inside a container to be fully host independent.
 -	Step #1 - write Dockerfile based on the python image (already containing git) and cloning all required repositories [see build_environment_setup.sh](https://github.com/Tinkerforge/generators/blob/master/build_environment_setup.sh).
 -	Done: Step #2 - Create Makefile with target for building this container
 -	Done: Step #3 - Update to initially create the container as data-only-container an declare a volume for source and for release

## Next Steps

-	Build C# language binding from changed master branch with travis using my container
-	Test created binaries for C# as part of the travis build
-	Try using Makefile based approach from docker development for building / developing
-	Setup a completely containerized runtime environment for TF

# Other Ideas

## Production Environment

Does it make sense to see the execution environment for brickv, brickd, ... as the production environment? What would it mean, if I do so?

Here we need to think about different layers. Let's use an easy to follow example. Assuming we like to create a Blog based on Wordpress and MySql. With regards to Docker I see the following Layers:

1.	Base-Technology: In this example that would be Wordpress and MySql. Both are Open Source projects and might even utilise Docker in their development, but that is irrelevant for this scenario. Both supply releases (binaries) on their respective web page.
2.	Base-Technology in Container: Wordpress and MySql are both containerised in an official repository on docker hub. So Docker / the community creates an image based on the releases (binaries) supplied by the base technology vendor.
3.	Application Containers: By utilising the containers with the base technology an application container or a set of application container is created which is used by Devs, QA and in production. At least this is the overall goal.

### Finding #1

It does make sense to create a complete Tinkerforge Application in containers and use it in a production environment. This probably includes that information about the hardware (e.g. IDs of Master Brick and Bricklets) is supplied via *environment variables* or needs to be taken care of by the application itself (e.g. autodetection of Bricks / Bricklets or connection to Bricks / Bricklets based on user input). For this to work, other tinkerforge components like brickd are also required in a container. The goal of doing this is to make it as easy as possible for the user to use just the application. For example a Tinkerforge C# application could now be run on any host environment without taking care of installing proper brickd, .NET or Mono execution environment.

Would this simplify the tinkerforge code base, because less environment dependencies would be required? I mean, it is said that TPL cannot be used for C#-binding, because many people using an older version of .NET. Once everything runs in a container there is no longer the need to support older .NET versions!?!

### Finding #2

Releasing tinkerforge components (like a language binding for C#) could mean a container is released (including the required examples, docs, execution environment, ...). However, this would mean that Docker becomes a requirement for using Tinkerforge which currently might not be a very good idea.

Instead it should be seen as an add-on. Thus it is either directly supplied by Tinkerforge or even by a third-party. That means out of development comes a release (in this case the language binding C#) and in addition it could also provide it as an image.

That means dockerizing the Tinkerforge language binding for C# means to add an additional deliverable, which is the image containing the language binding.
