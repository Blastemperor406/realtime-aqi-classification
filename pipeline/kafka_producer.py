import json

from kafka import KafkaProducer

TOPIC = "sensor_data"

producer = KafkaProducer(bootstrap_servers="localhost:9093", security_protocol="PLAINTEXT")


def publish(reading: dict) -> None:
    producer.send(TOPIC, json.dumps(reading).encode("utf-8"))
