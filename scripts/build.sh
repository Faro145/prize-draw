sudo docker build -t application ./application 
sudo docker build -t entry_code ./entry_code
sudo docker build -t letters ./letters
sudo docker build -t numbers ./numbers

sudo docker network create my-network
sudo docker network connect my-network application
sudo docker network connect my-network entry_code
sudo docker network connect my-network letters
sudo docker network connect my-network numbers

sudo docker run -d -p 5000:5000 --name application --network my-network application
sudo docker run -d -p 5000:5000 --name entry_code --network my-network entry_code
sudo docker run -d -p 5000:5000 --name letters --network my-network letters
sudo docker run -d -p 5000:5000 --name numbers --network my-network numbers