FROM ubuntu:20.04
#FROM debian:buster-slim
#FROM python:3

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential git


# set a directory for the app
RUN groupadd app && useradd -g app app

# copy all the files to the container
RUN git clone https://dev.ilab.cl/public/pythonweb.git /srv


# install dependencies
WORKDIR /srv/web-interface
RUN pip3 install setuptools gunicorn
RUN pip3 install --no-cache-dir -r requirements.txt

# define the port number the container should expose
RUN chown -R app:app /srv
USER app
EXPOSE 8000

# run the command
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8000", "wsgi:app"]