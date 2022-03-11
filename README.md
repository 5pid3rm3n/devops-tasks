# devops-tasks

The stack is built out of 5 services: 
- Kafka, monogoDB, MongoConnect, api & web-server

Web folder contains the web server & small kafka producer client

Api folder contains the internal web server & small mongo client 


``` docker-compose up ``` will make everything run, but the sink (for some reason) won't write to mongo
