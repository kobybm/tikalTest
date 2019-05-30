FROM python:2

# Add Version File:
ADD ./git_commit /mnt/git_commit


WORKDIR /opt/

ADD . /opt/

RUN pip install BaseHTTPServer
EXPOSE 80

CMD python kobyDate.py

