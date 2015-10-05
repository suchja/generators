# About

This repository contains a fork of [Tinkerforge/generators](https://github.com/Tinkerforge/generators). The source code for the C# binding could be improved in several ways. Especially `IPConnection.cs` is a very large file and the classes in there seem not to follow all best practices about clean and object oriented code.

So it is basically a project for myself trying to improve my coding and refactoring skills on a daily basis. You can watch the progress, if you like and start commenting on the progress via Issues, if you see it is going into a wrong direction.

# Goals & Restrictions

Here I'll document goals for the improvement, once I'm clear on what exactly I see as the problem.

## Goals

1.	One obvious issue is the size of the file `IPConnection.cs`. It currently contains 1990 lines of code and comments. This is difficult to handle.

## Restrictions

1.	Currently the binding is developed against .NET 2.0. The reason is to be backward compatible with older embedded Windows Versions (see this [Issue on Github](https://github.com/Tinkerforge/generators/issues/42) for details). So it is not possible to introduce newer language features or libraries.

# ToDos

-	Check these principles and apply them to `IPConnection`.
-	Check whether there will be problems with the build, if `IPConnection.cs` is split up into several files.
-	Install Screenflow and capture all refactoring sessions in order to further analyse and document them afterwards.
-	Document key responsibilities of `IPConnection` class and the related methods.
-	Check how it is possible to unit test `IPConnection` without anything else.
 -	`IPConnection` uses `BrickDaemon`. So I could try to mock it.
 -	How about using interfaces and dependency injection?
-	Check whether it is possible to have integration tests without hardware.
-	Setup containers for brickd & brickv to run examples / integration tests
-	Setup integration tests with my hardware (temperature bricklet, display, ...).

# Open Issues

# Ideas

-	Define why exactly the large size of the file is an issue.
 -	Maybe it is not the size. See this [answer](http://programmers.stackexchange.com/a/177102). Probably I should ask wehther everything in that file does really belong to the `IPConnectoin` class.
 -	Does `IPConnection` violate the Interface Segregation Principle? If yes it might be an indicator, that it is not good. See this [analysis](http://fagblogg.mesan.no/how-bad-is-smelly-code/).
 -	Another principle to consider is Single Responsibility Principle (SRP). Does `IPConnection` have only a single responsibility? See [here](http://blog.millermedeiros.com/keep-your-modules-and-functions-small/) for details.

