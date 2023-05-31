# syntax=docker/dockerfile:1
FROM jenkins/jenkins:lts
# Elevate permissions to install additional plugins
USER root
# Disable interactive installation wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
# set the CasC file var
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
# Install additional plugins
RUN jenkins-plugin-cli --plugins docker-plugin:1.3.0 configuration-as-code:latest job-dsl:latest
# Copy the casc.yaml file
COPY casc.yaml /var/jenkins_home/casc.yaml
# Drop back permissions to the regular jenkins user
USER jenkins