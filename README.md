# Crontab for crawler(dir crawl)
![image](https://raw.githubusercontent.com/pu6372689/study/master/ReadmePic/p1.jpg)

A simple autocrawl;run in container

# Eviroment 
Linux

# Prerequisites
docker

# How to use
* cd /tmp/&& git clone https://github.com/pu6372689/study

* cd /tmp/study/crawl/dockerfile_crawl

* docker build -t test .

#test crawl

* cd ../&& ./start-crawl.sh

#use crontab

* crontab -e

#每天12點執行

* \* 12 * * * /tmp/study/crawl/start-crawl.sh



# Create jupyter&MySQL for test by docker-compose(dir dockercompose)
![image](https://raw.githubusercontent.com/pu6372689/study/master/ReadmePic/p2.jpg)



# Eviroment 
Linux

# Prerequisites
docker
docker-compose

# How to use
* cd /tmp/&& git clone https://github.com/pu6372689/study

* cd /tmp/study/dockercompose&& docker-compose up -d

#check both container

* docker-compose ps -a

#use browser to check jupyter

* ip:8888

#use workbench to check MySQL
![image](https://raw.githubusercontent.com/pu6372689/study/master/ReadmePic/p3.jpg)
