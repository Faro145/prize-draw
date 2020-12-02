#! /bin/bash

sudo docker tag service_1 rfarq75/service_1
sudo docker tag service_2 rfarq75/service_2
sudo docker tag service_3 rfarq75/service_3 
sudo docker tag service_4 rfarq75/service_4

sudo docker push rfarq75/service_1
sudo docker push rfarq75/service_2
sudo docker push rfarq75/service_3
sudo docker push rfarq75/service_4