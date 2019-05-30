FROM ubuntu:18.04


RUN apt-get update
RUN apt-get install -y python2.7

WORKDIR /opt/

ADD . /opt/

EXPOSE 80

CMD python2.7 kobyDate.py

