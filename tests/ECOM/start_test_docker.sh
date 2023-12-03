#!/bin/bash
# TODO add if only container name
# need chmod +
sudo docker compose up;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^fastapi_stud-back_fastapi" | cut -d' ' -f2);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^fastapi_stud-mongo_upload" | cut -d' ' -f2);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^fastapi_stud-testing_back" | cut -d' ' -f2);