from kafka import KafkaProducer
import msgpack


def producer():

    return KafkaProducer(security_protocol="PLAINTEXT",value_serializer=msgpack.dumps, bootstrap_servers=['kafka:9092'])

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an errback', exc_info=excp)
    # handle exception