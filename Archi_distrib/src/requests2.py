import requests
from kafka import KafkaProducer
import time
import json




API_URL = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm&q=&sort=date&facet=date&facet=nom&facet=temps_present&facet=libgeo&facet=nom_epci&facet=nom_dept&facet=nom_reg&refine.date=2023"



TOPIC_NAME = "test_topic"





SPARK_MASTER_URL = "spark://d8dabd93e04c:7077"


producer = KafkaProducer(bootstrap_servers='localhost:9092')


def get_temps():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None




def send_temps_kafka(temps_data):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.send(TOPIC_NAME, json.dumps(temps_data).encode('utf-8'))




while True:
   temps_data = get_temps()
   if temps_data:
       send_temps_kafka(temps_data)
       time.sleep(2) 
       print(temps_data) 
