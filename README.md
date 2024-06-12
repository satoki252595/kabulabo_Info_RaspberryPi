# kabulabo_Info_RaspberryPi

docker build -t kabu .
docker run -it -v ./:/src -d --name kabu kabu
docker exec -it kabu /bin/bash

# crontab -e

00 05 \* _ 0 docker exec -i kabu /bin/bash -c "cd /src && python3 main.py"
00 05 _ \* 0 sudo docker exec -i kabu /bin/bash -c "cd /src && python3 main.py" > /root/error.log 2>&1
