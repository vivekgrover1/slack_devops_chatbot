# Set the base image to vivek77/errbot
FROM vivek77/errbot

# File Author / Maintainer
MAINTAINER Vivek

# Update the repository sources list
RUN yum -y update && yum clean all

WORKDIR /root/errbot/plugins

RUN git clone https://github.com/vivekgrover1/err-command-plugin.git && \
git clone https://github.com/vivekgrover1/err-aws-plugin.git

WORKDIR /root/errbot/

COPY config.py errbot_start.sh /root/errbot/

RUN chmod u+x errbot_start.sh

ENV ANSIBLE_HOST_KEY_CHECKING=False

ENTRYPOINT ["/root/errbot/errbot_start.sh"]
