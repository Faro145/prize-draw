#! /bin/bash
sudo apt install python3 python3-pip python3-venv python3-flask -y

python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt

pytest --cov ./service_1/application --cov-report term-missing
pytest --cov ./service_2/application --cov-report term-missing
pytest --cov ./service_3/application --cov-report term-missing
pytest --cov ./service_4/application --cov-report term-missing

deactivate
rm -rf venv
