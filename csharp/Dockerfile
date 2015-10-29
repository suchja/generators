FROM python:2.7.10-wheezy
MAINTAINER jan@lernmoment.de

#based on Dockerfile for official mono image

RUN apt-get update \
	&& apt-get install -y curl zip \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

# TODO: Install with no-install-recommends ?

RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.10.0 main" > /etc/apt/sources.list.d/mono-xamarin.list \
        && echo "deb http://download.mono-project.com/repo/debian 310-security main" >> /etc/apt/sources.list.d/mono-xamarin.list \
	&& apt-get update \
	&& apt-get install -y mono-devel nuget \
	&& rm -rf /var/lib/apt/lists/*

RUN mozroots --machine --import --sync --quiet
