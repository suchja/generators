FROM python:2.7.10
MAINTAINER jan@lernmoment.de

RUN mkdir -p /src/tf/
WORKDIR /src/tf
RUN git clone https://github.com/suchja/generators.git
