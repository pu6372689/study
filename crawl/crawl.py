import feedparser
import requests
import time
from datetime import date
import os
from bs4 import BeautifulSoup

rss_url = "https://feeds.feedburner.com/ettoday/lifestyle"

newsFeed = feedparser.parse(rss_url)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
my_headers = {
    'User-Agent': user_agent,
}

text = []
for e in newsFeed['entries']:

    href = e['feedburner_origlink']
    r = requests.get(href,headers=my_headers)
    html = r.text
    soup = BeautifulSoup(html,'html.parser')

    first = soup.select('div[class="story"]')[0].text.split('【你可能也想看】')[0].split('[廣告]請繼續往下閱讀...')[0].strip('\n')
    second = soup.select('div[class="story"]')[0].text.split('【你可能也想看】')[0].split('[廣告]請繼續往下閱讀...')[1].strip('\n')
    text.append(first+second)

now = date.today()
getdir = now.strftime('%Y%m')
getfile = now.strftime('%m%d')

with open('/tmp/crawl/%s/%s.txt'%(getdir, getfile), 'w+', encoding='utf-8') as f:
    for i in text:
        f.writelines(i)
