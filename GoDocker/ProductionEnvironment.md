# Production Environment

Does it make sense to see the execution environment for brickv, brickd, ... as the production environment? What would it mean, if I do so?

Here we need to think about different layers. Let's use an easy to follow example. Assuming we like to create a Blog based on Wordpress and MySql. With regards to Docker I see the following Layers:

1.	Base-Technology: In this example that would be Wordpress and MySql. Both are Open Source projects and might even utilise Docker in their development, but that is irrelevant for this scenario. Both supply releases (binaries) on their respective web page.
2.	Base-Technology in Container: Wordpress and MySql are both containerised in an official repository on docker hub. So Docker / the community creates an image based on the releases (binaries) supplied by the base technology vendor.
3.	Application Containers: By utilising the containers with the base technology an application container or a set of application container is created which is used by Devs, QA and in production. At least this is the overall goal.

## Finding #1

It does make sense to create a complete Tinkerforge Application in containers and use it in a production environment. This probably includes that information about the hardware (e.g. IDs of Master Brick and Bricklets) is supplied via *environment variables* or needs to be taken care of by the application itself (e.g. autodetection of Bricks / Bricklets or connection to Bricks / Bricklets based on user input). For this to work, other tinkerforge components like brickd are also required in a container. The goal of doing this is to make it as easy as possible for the user to use just the application. For example a Tinkerforge C# application could now be run on any host environment without taking care of installing proper brickd, .NET or Mono execution environment.

Would this simplify the tinkerforge code base, because less environment dependencies would be required? I mean, it is said that TPL cannot be used for C#-binding, because many people using an older version of .NET. Once everything runs in a container there is no longer the need to support older .NET versions!?!

As with the next finding a containerized solution is probably only an addon. This is in accordance to many other projects (for example as shown in the provious section with Wordpress and MySql) using Docker. 

## Finding #2

Releasing tinkerforge components (like a language binding for C#) could mean a container is released (including the required examples, docs, execution environment, ...). However, this would mean that Docker becomes a requirement for using Tinkerforge which currently might not be a very good idea.

Instead it should be seen as an add-on. Thus it is either directly supplied by Tinkerforge or even by a third-party. That means out of development comes a release (in this case the language binding C#) and in addition it could also provide it as an image.

That means dockerizing the Tinkerforge language binding for C# means to add an additional deliverable, which is the image containing the language binding.

## Conclusion

It does make sense to supply Tinkerforge or a specific language stack of Tinkerforge as *Base-Technology in Container*. This would allow other users to easily create their *Application Container* with a specific application on a language stack of Tinkerforge.

It should always be seen as an add-on. Anybody willing to put in the effort could create first the *Base-Technology in Container* and then provide it to others for their specific Tinkerforge application.

It is crucial to separate this from any effort of using Docker in the development and / or build of any Tinkerforge components. Using Docker during development or build of any Tinkerforge component should always be supported and integrated by the Tinkerforge team.
