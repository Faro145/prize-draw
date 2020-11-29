#! /bin/bash

ssh rjfar@[ip_address] << EOF

cd prize-draw
git pull
docker stack deploy --compose-file docker-compose.yaml prize-draw

EOF