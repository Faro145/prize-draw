#! /bin/bash
ssh swarm-manager << EOF
git clone https://github.com/Faro145/prize-draw.git
cd prize-draw
docker pull rfarq75/service_1:latest
docker pull rfarq75/service_2:latest
docker pull rfarq75/service_3:latest
docker pull rfarq75/service_4:latest
docker pull nginx:alpine
docker stack deploy --compose-file docker-compose.yaml prize-draw
EOF
