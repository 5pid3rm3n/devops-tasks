#!/bin/sh

# get status code to check connector api is up
STATUS_CODE=$(curl -I http://connect:8083/connectors 2>/dev/null | grep 200 | awk '{print $2}')

if [[ $STATUS_CODE -eq 200 ]]; then
  # add sink data to connector
  curl -X POST -H "Content-Type: application/json" --data @sink-connector.json http://connect:8083/connectors -w "\n"
else
  # exit if the connector API is not up
  exit 1
fi