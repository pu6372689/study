# Crontab for crawler(dir crawl)
![image](https://raw.githubusercontent.com/pu6372689/study/master/ReadmePic/p1.jpg)

A simple autocrawl in container

# Eviroment 
Linux

# Prerequisites
docker

# How to use
cd /tmp/&& git clone https://github.com/pu6372689/study

cd dockerfile_crawl

docker build -t test .

#test crawl
cd ../&& ./start-crawl.sh

#use crontab
crontab -e

#每天12點執行
/* 12 * * * /tmp/study/crawl/start-crawl.sh
