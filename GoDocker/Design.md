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

## Source-code in base image approach

An alternative to the data-container approach is to build a base image with all source code, python, git and maybe other utilities required for all language bindings. Based on that image a dedicated image for each language binding or other Tinkerforge components like `brickd` or `brickv` can be built.

I got this idea while looking into the [Dockerfile of atom editor](https://github.com/atom/atom/blob/master/build/debian/Dockerfile).

Now this means we probably have three images layered on top of each other:

1.	`python:2.7.10` - This image is the base image and can be used directly from Docker library. Besides `python` it contains `git` which is obviuously needed.
2.	*Tinkerforge source code* - This image simply clones all required Tinkerforge repositories for building all Tinkerforge components.
3.	*Tooling for language bindings* - Finally this image contains the required applications, libs and other dependencies to build and execute a dedicated language binding (e.g. mono for C#). 

### Usage / Update process

Basically the idea is to `git clone` a state of all Tinkerforge repositories into the base image. Now a specific language binding image could be build on top of this base image. The following aspects are part of the specific language binding image:

-	Install applications and other dependencies for the required language binding (e.g. mono for C#).
-	Update source code to the latest or required version with `git pull`.

Having a dedicated version of the source code in the base image would allow to easily switch to different versions in the language binding image via `git pull`. On the other hand the base image becomes more and more outdated with every `git commit` to the repositories. So at least for every major release of the Tinkerforge components the base image needs to be rebuild.

Which versions should go into the base image? The Tinkerforge components do not have a streamlined release. They can be released independently and do have very different versions. So it would either be possible to `git clone` each component's repository and `git pull` its latest version in one `RUN` in the base image or just `git clone` the current state of the repository and `git pull` the required version in the language binding image.

### Advantages of this approach

Although this approach layers several images, finally the developer only requires one image for a particular language binding or other Tinkerforge component. Each image contains the complete source code of all components, but is only responsible for one language binding. Thus it seems the *SRP - Single Responsibility Principle* is applied properly.

Via `automated build` on Docker hub it would be possible to constantly rebuild the *Tinkerforge source code* image when any of the Tinkerforge repositories are changed. *Is it possible to trigger an automated build from many different github repositories?*

Allows switching to different versions quite easily.

### Disadvantages of this approach

It seems strange to me that the *Tinkerforge source code* image, which probably changes frequently is a base image for the *Tooling for language bindings* image, which will not change frequently. *Is it better to have the image with the most frequent changes as top most image?*

From a performance point of view this might be problematic due to frequent copying of all the Tinkerforge source code repositories. According to Jerome in [this article](https://jpetazzo.github.io/2015/01/19/dockerfile-and-data-in-volumes/) it is better to have big data separated from the service container. He proposes to first build the service container and based on that image define a data-only-container with the data in it.

Avoiding this performance issue might be possible for this approach by simply not using a volume. As long as the directory containing the data is not defined as a volume, there should be no performance issue due to copying all data when starting a container from the image.

### Conclusion

Probably I need to try this approach. Somehow I'm not sure that it is easy to understand and maintain. I definitely like the adherence to *SRP* and the easy way to use local data instead of the data cloned / fetched from repositories.
