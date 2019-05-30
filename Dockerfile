FROM python

# Add Version File:
ADD ./git_commit /mnt/git_commit


WORKDIR /opt/

ADD . /opt/

EXPOSE 80

CMD python kobyDate.py

