#!/bin/bash
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
pip install --user ansible
ansible-playbook -i ./inventory ./playbook.yaml
