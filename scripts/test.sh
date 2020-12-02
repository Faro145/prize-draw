#! /bin/bash
export DB_URI: ${DB_URI}
export KEY: ${KEY}

sudo docker build -f testing/Dockerfile -t prizedraw-testing-image .
sudo docker run -it -d --name testing-container prizedraw-testing-image

sudo docker exec testing-container pytest ./service_1 --cov ./service_1
sudo docker exec testing-container pytest ./service_2 --cov ./service_2
sudo docker exec testing-container pytest ./service_3 --cov ./service_3
sudo docker exec testing-container pytest ./service_4 --cov ./service_4

docker stop testing-container
docker rm testing-container