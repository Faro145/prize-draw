#! /bin/bash

ssh rjfar@[ip_address] << EOF

cd prize-draw
git pull

export DB_URI: ${DB_URI}
export KEY: ${KEY}

docker stack deploy --compose-file docker-compose.yaml prize-draw

EOF