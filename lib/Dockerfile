FROM ubuntu:focal
RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pip
ADD lib/ /app/lib
RUN pip install /app/lib
