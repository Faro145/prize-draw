#!/bin/bash

sudo docker build -t service_1 ./service_1 
sudo docker build -t service_2 ./service_2
sudo docker build -t service_3 ./service_3
sudo docker build -t service_4 ./service_4

sudo docker network create my-network
sudo docker network connect my-network service_1
sudo docker network connect my-network service_2
sudo docker network connect my-network service_3
sudo docker network connect my-network service_4

sudo docker run -d -p 5000:5000 --name service_1 --network my-network service_1
sudo docker run -d -p 5000:5000 --name service_2 --network my-network service_2
sudo docker run -d -p 5000:5000 --name service_3 --network my-network service_3
sudo docker run -d -p 5000:5000 --name service_4 --network my-network service_4