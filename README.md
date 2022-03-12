# devops-tasks

[![Docker Compose Actions Workflow](https://github.com/5pid3rm3n/devops-tasks/actions/workflows/test.yml/badge.svg)](https://github.com/5pid3rm3n/devops-tasks/actions/workflows/test.yml)

<br>
The stack is built out of 5 services: 
- Kafka, MonogoDB, MongoConnect, Internal api, Extertnal web-server

<br>

## Services


``` Web-Server ``` provids 2 GET routes: Buy & Get-all-user_buys
 - buy/ - purchase random item,
 - get-all-user_buys/ - query internal api route for all purchesed items 

``` Api-Server ``` provids 1 GET routes: get-buy-list
- get-buy-list/ - return all purchesed items 

``` MongoConnect ``` provids automatic events streaming from the kafka to mongodb collection 
- configuration located at api/shell/sink-connector.json


## Data flow

+  http://localhost/buy/ : route __produce__ message (item) to kafka topic
 *  MongoConnect : is subscribed to the kafka topic & __consume__ the event and then __insert__ it mongo-db
+  http://localhost/get-all-user_buys/ : sends a request to internal api on route get-buy-list/ and return answer to client
 *  Internal Api : reutrn the results mongo query

## Starting the stack

run ``` docker-compose up ``` to build the stack <br>

### Troubleshot
Kafka & MongoConnect can take up to 5 min to fully startup, depands on hardware <br>
run ``` docker logs connector-init | grep -i -o mongo-sink | awk '{print $1}' ``` - if the results dose not contains "mongo-sink" or exit code 0 <br>
startup is still in progress.

## SwaggerUI
For convenience of the demo, visit http://localhost/docs for easy interaction

## Smoke Tests
the repo contains small smoke tests that will perform somewhat e2e test for the stack - check airflow badge above
