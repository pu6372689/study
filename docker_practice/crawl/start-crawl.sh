d=$(date '+%Y%m')

mkdir -p $d

docker run -v /tmp/study/crawl/crawl.py:/tmp/crawl/crawl.py \
-v /tmp/study/crawl/$d:/tmp/crawl/$d \
--rm test python /tmp/crawl/crawl.py

