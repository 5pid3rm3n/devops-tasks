# devops-tasks

[![Docker Compose Actions Workflow](https://github.com/5pid3rm3n/devops-tasks/actions/workflows/test.yml/badge.svg)](https://github.com/5pid3rm3n/devops-tasks/actions/workflows/test.yml)

The stack is built out of 5 services: 
- Kafka, monogoDB, MongoConnect, api & web-server

Web folder contains the web server & small kafka producer client

Api folder contains the internal web server & small mongo client 


``` docker-compose up ``` will make everything run, but the sink (for some reason) won't write to mongo
