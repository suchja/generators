FROM python:2.7.10-wheezy
MAINTAINER jan@lernmoment.de

ENV GIT_USER tinkerforge
ENV TF_HOME /src/tf

RUN mkdir -p /scripts
COPY clone_all_gits.sh /scripts/
RUN chmod +x /scripts/clone_all_gits.sh

# It's important that this is done via RUN and not CMD, because we like
# to have it executed during build phase and not run phase!
RUN /scripts/clone_all_gits.sh
