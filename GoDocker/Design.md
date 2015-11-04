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
