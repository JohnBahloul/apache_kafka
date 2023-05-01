from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import time

# Define the Kafka configuration properties
kafka_config = {
    "bootstrap_servers": "localhost:9092",
    "group_id": "my-group",
    "auto_offset_reset": "latest"
}

# Define the Kafka topics
input_topic = "input-topic"
output_topic = "output-topic"

# Define the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_config["bootstrap_servers"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Define the Kafka consumer
consumer = KafkaConsumer(
    input_topic,
    bootstrap_servers=kafka_config["bootstrap_servers"],
    group_id=kafka_config["group_id"],
    auto_offset_reset=kafka_config["auto_offset_reset"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

# Process the incoming messages
for message in consumer:
    input_data = message.value
    # Perform real-time processing on the input data
    output_data = {"processed_data": input_data, "timestamp": time.time()}
    # Send the processed data to the output topic
    producer.send(output_topic, value=output_data)
