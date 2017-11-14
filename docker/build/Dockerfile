FROM frolvlad/alpine-python3

USER root

RUN apk update && apk add gcc linux-headers musl-dev python3-dev && \
    pip install flask pymongo requests uwsgi && \
    adduser -s /bin/sh -G daemon -D demo

ADD ./src /opt/demo/src

USER demo
