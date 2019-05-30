FROM ubuntu:18.04


RUN apt-get update
RUN apt-get install -y python2.7

# Add Version File:
ADD ./git_commit /mnt/git_commit


WORKDIR /opt/

ADD . /opt/

EXPOSE 80

CMD python2.7 kobyDate.py

