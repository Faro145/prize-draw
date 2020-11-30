#! /bin/bash

sudo docker tag application rfarq75/service_1
sudo docker tag entry_code rfarq75/service_2
sudo docker tag letters rfarq75/service_3 
sudo docker tag numbers rfarq75/service_4

sudo docker push rfarq75/service_1
sudo docker push rfarq75/service_2
sudo docker push rfarq75/service_3
sudo docker push rfarq75/service_4