"""Stub: Spark Structured Streaming job — Kafka topic -> typed dataframe -> Cassandra."""
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StructField, StructType, TimestampType

KAFKA_BROKER = "localhost:9093"
TOPIC = "sensor_data"

SCHEMA = StructType(
    [
        StructField("pm1", IntegerType(), True),
        StructField("pm2_5", IntegerType(), True),
        StructField("pm10", IntegerType(), True),
        StructField("timestamp_last", TimestampType(), True),
    ]
)


def main() -> None:
    spark = (
        SparkSession.builder.appName("aq-ingest")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2,"
            "com.datastax.spark:spark-cassandra-connector_2.12:3.4.0",
        )
        .getOrCreate()
    )

    stream = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", TOPIC)
        .load()
    )

    # TODO: parse value against SCHEMA and writeStream to Cassandra (see schema.cql)
    raise NotImplementedError


if __name__ == "__main__":
    main()
