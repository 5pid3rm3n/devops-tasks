FROM ubuntu:latest

RUN apt-get -y update

RUN apt-get install -y curl

WORKDIR /init-connector

COPY . .

RUN chmod +x initialize-container.sh

CMD ["/bin/bash", "initialize-container.sh"]