#! /bin/bash

ssh swarm-manager << EOF

cd prize-draw
git pull
docker stack deploy --compose-file docker-compose.yaml prize-draw

EOF
