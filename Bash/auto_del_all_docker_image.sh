#!/bin/bash
# TODO add if only container name
# need chmod +
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker  images -q);