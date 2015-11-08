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

## Open Issues

-	Cloning all git repositories into a data-only-container takes a lot of time. The question is whether this is an issue and if it is, how to improve the performance of this.
-	Currently I don't understand the dependencies between all the tinkerforge components. In `build_environment_setup.sh` all repositories are cloned. Hoewever, at least for building a language binding (including documentation), there are probably several repositories which are not required. The problem with cloning all repositories is that it takes a lot of space. Currently the image with all repositories is *2.7GB*, while its base image is *0.675GB*. So we do have more than *2GB* of data cloned from GitHub. Besides the size this is also an issue of time, because it takes pretty long to download all repositories.
-	The `doc` repository seems to be the largest by far. It contains tons of images and other data.
 -	Although each language binding contains a python script to generate the language specific documentation, that documentation is not part of the language binding release. The release only contains the build binaries, examples and source code.
 -	It seems that `doc` can be used by developers if they require a language specific documentation. Additionally this documentation is provided on the [Tinkerforge homepage](http://www.tinkerforge.com/en/doc/Software/API_Bindings_CSharp.html#api-reference-and-examples).
 -	It is important to note that the language specific documentation will be generated into a `doc` subfolder of the language binding. -> When and from where is this executed?

## Next Steps

-	Build C# language binding from changed master branch with travis using my container
-	Test created binaries for C# as part of the travis build
-	Try using Makefile based approach from docker development for building / developing
-	Setup a completely containerized runtime environment for TF
