FROM pu6372689/python38

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk add -U tzdata && ls /usr/share/zoneinfo&& \
cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime

#change date to taipei in alpine
