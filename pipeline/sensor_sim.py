"""Stub: simulated sensor node. Replace with real node firmware output."""
import random
import time
from datetime import datetime, timezone


def read_sensor() -> dict:
    return {
        "pm1": random.randint(5, 60),
        "pm2_5": random.randint(10, 250),
        "pm10": random.randint(20, 400),
        "timestamp_last": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    while True:
        print(read_sensor())
        time.sleep(2)
