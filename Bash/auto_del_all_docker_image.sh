#!/bin/bash
# TODO add if else
# need chmod +
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker  images -q);