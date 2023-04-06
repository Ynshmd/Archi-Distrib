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
![image](https://user-images.githubusercontent.com/118398845/230250807-2e1401a5-1837-4a8f-a85d-c591173babb8.png)


#### Producer Velib

![image](https://user-images.githubusercontent.com/118398845/230250350-cf4f870c-9393-445a-804f-b956169d2678.png)

#### Producer Météo
![image](https://user-images.githubusercontent.com/118398845/230251231-0b47fd66-98b0-4567-a889-694d716c6357.png)



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

Lancer le Consumer

````
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /src/consumer.py
````
###  DATAVIZ

Pour la data Viz une fois le consumer effectuer , il faut exporter les données sur la base Mongo puis les exploité. Ensuite on peux les analysé grâce a un script. 

Voici ce qui a été réaliser.


![image](https://user-images.githubusercontent.com/118398845/230433909-4aef944f-3f00-4097-ae1e-e627bed2d321.png)

![image](https://user-images.githubusercontent.com/118398845/230434124-c5ccb812-3b4f-4818-8758-f461e8519761.png)


![image](https://user-images.githubusercontent.com/118398845/230434253-fd2ccb8d-ffd8-41cf-98c1-a0b67c1540e3.png)

![image](https://user-images.githubusercontent.com/118398845/230434376-f7ba1fe1-7ce1-4e54-8eb4-48bc0dc074d9.png)





