import requests
from kafka import KafkaProducer
import time
import json



# Velib API endpoint URL
API_URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=500&sort=duedate&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&facet=duedate&refine.nom_arrondissement_communes=Paris&refine.is_installed=OUI&timezone=Europe%2FParis"


# Kafka topic to send data to
TOPIC_NAME = "test_topic"




# Spark master URL and port
SPARK_MASTER_URL = "spark://d8dabd93e04c:7077"

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Function to fetch Velib data from the API
def get_velib_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to send Velib data to Kafka
# def send_velib_data_to_kafka(velib_data):
#     producer.send(TOPIC_NAME, velib_data.encode('utf-8'))


def send_velib_data_to_kafka(velib_data):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.send(TOPIC_NAME, json.dumps(velib_data).encode('utf-8'))



# Loop to continuously fetch and send Velib data to Kafka
while True:
   velib_data = get_velib_data()
   if velib_data:
       send_velib_data_to_kafka(velib_data)
       time.sleep(2) # wait for 2 second before sending next message
       print(velib_data) 
  

        
    
