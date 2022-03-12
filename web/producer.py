from kafka import KafkaProducer
import json


def producer():

    return KafkaProducer(security_protocol="PLAINTEXT", value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=['kafka:9092'])
