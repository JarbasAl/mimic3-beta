FROM debian:latest

RUN apt-get update && \
  apt-get install -y git python3 python3-dev python3-pip curl build-essential

COPY . /tmp/mimic3_src
RUN pip3 install /tmp/mimic3_src/opentts_abc
RUN pip3 install /tmp/mimic3_src/mimic3_tts
RUN pip3 install /tmp/mimic3_src/mimic3_http

ENTRYPOINT mimic3-server