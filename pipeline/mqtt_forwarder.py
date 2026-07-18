"""Stub: MQTT -> Kafka bridge. Subscribes to the sensor topic and republishes to Kafka."""
import paho.mqtt.subscribe as subscribe

import kafka_producer

MQTT_TOPIC = "sensor_data"
MQTT_HOST = "localhost"
MQTT_PORT = 1884


def run() -> None:
    while True:
        msg = subscribe.simple(MQTT_TOPIC, hostname=MQTT_HOST, port=MQTT_PORT)
        # TODO: validate/parse payload before forwarding
        kafka_producer.publish({"raw": msg.payload.decode("utf-8")})


if __name__ == "__main__":
    run()
