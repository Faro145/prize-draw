sudo docker build -f testing/Dockerfile -t prizedraw-testing-image .
sudo docker run -it -d --name testing-container prizedraw-testing-image

sudo docker exec testing-container pytest ./application --cov ./application
sudo docker exec testing-container pytest ./entry_code --cov ./entry_code
sudo docker exec testing-container pytest ./letters --cov ./letters
sudo docker exec testing-container pytest ./numbers --cov ./numbers

docker stop testing-container
docker rm testing-container