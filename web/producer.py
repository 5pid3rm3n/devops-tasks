from kafka import KafkaProducer
# import msgpack
import json


def producer():

    return KafkaProducer(security_protocol="PLAINTEXT",value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=['kafka:9092'])

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an errback', exc_info=excp)
    # handle exception