from kafka import KafkaConsumer
import msgpack


def consumer():
    _consumer = KafkaConsumer('my-topic',
                              group_id='my-group',
                              bootstrap_servers=[
                                  'kafka:9092'],
                              value_deserializer=msgpack.loads)
    return _consumer
