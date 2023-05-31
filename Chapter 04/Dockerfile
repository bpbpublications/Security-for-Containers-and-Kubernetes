# syntax=docker/dockerfile:1
FROM jenkins/jenkins:lts AS base
USER root
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
RUN jenkins-plugin-cli --plugins docker-plugin:1.3.0
USER jenkins

# Use the base Jenkins image to build the matrix plugin
FROM base AS development
USER root
RUN jenkins-plugin-cli --plugins configuration-as-code:latest
USER jenkins

# Use the development image to build the production image
FROM development AS production
USER root
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
RUN jenkins-plugin-cli  --plugins job-dsl:latest
COPY casc.yaml /var/jenkins_home/casc.yaml
USER jenkins