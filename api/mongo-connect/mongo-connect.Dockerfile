FROM confluentinc/cp-kafka-connect:latest

# Install MongoDB Kafka Connector
RUN confluent-hub install --no-prompt mongodb/kafka-connect-mongodb:1.7.0

# Set plugin path environment variable
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"