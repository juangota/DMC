FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    wget \
    xvfb \
    xserver-xephyr

# install geckodriver and firefox

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz && \
    tar -zxf geckodriver-v0.24.0-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

RUN apt-get update && apt-get install -y firefox


RUN pip3 install selenium
RUN pip3 install pyvirtualdisplay

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY . $APP_HOME/

# CMD tail -f /dev/null
CMD python3.5 script.py
