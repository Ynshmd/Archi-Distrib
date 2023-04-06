# Archi-Distrib

Ce Github est un Projet d'architecture distribué. Dans ce projet nous allons travailler avec la location de velib en temps réel en coorélation avec la météo.

Nous avons utilisé le site de gouv data Paris pour récolter les donnée des velib en temps réel et Opendatasoft pour la météo. Pour pouvoir récolter ces donnée nous avons utilié les API .

Ce Read me a été réalisé sous windows 10 mais est identique pour Windows 11 , Linux et Mac.


### Pour lancer docker 

```
docker compose-up 
```

### KAFKA

```
docker exec -it archi_distrib-kafka-1 bash
```


Une fois entrer dans la VM Kafka il faut se rendre dans ce dossier

````
/opt/bitnami/kafka/bin
````


Puis nous allons créer un topic , qui va être notre Producer

````
kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test_topic
````

Ensuite nous allons lancer le topic qui a été créer avec cette commande 

````
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test_topic --property "parse.key=true" --property "key.separator=:"
````

### SPARK-MASTER

````
docker exec -it archi_distrib-spark-1
````

Une fois entrer dans la VM Spark Master nous allons nous rendre dans le dossier suivant 

````
/opt/bitnami/spark/bin
````

Copier le submit dans ce dossier 

````
docker cp submit.py d8dabd93e04c:/opt/bitnami/spark/bin
````





