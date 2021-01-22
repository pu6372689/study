import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
     'Referer':'https://www.104.com.tw/'
}
Search = input('請輸入需求職缺:')
searchJS_url = 'https://www.104.com.tw/jobs/search/list?ro=0&keyword={}'.format(Search)
#使用開發人員工具查詢Network的XHR(XMLHttpRequest)內取得網址
searchJS_res = requests.get(searchJS_url,headers=headers)
search_Json = json.loads(searchJS_res.text)['data']

print("職缺共{}件".format(search_Json['count'][0]))

selectPage = int(input('請問想要爬取幾頁的資料(共{}頁):'.format(search_Json['totalPage'])))

if selectPage <= search_Json['totalPage']:
    pass
else:
    selectPage = int(search_Json['totalPage'])
#輸入超過總頁面時做修正    

def function(Tools):     #判斷是否需要該工具
    if Tools in [i['description'] for i in offer_json['condition']['specialty']]:
        return 1
    else:
        return 0

Page = 1
df_All = []

while Page <= selectPage:

    url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword={}&page={}'.format(Search,Page)
    res = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    offer = soup.select('div[class="b-block__left"]')

    for offername in offer:
        if len(offername.select('a')) == 0:
            pass
            #查詢時略過空資料
        else:
            get_url = offername.select('a')[0]['href']
            offer_url = 'https:' + get_url[:21] + 'ajax/content/' + get_url[21:]      
            #使用開發人員工具查詢Network的XHR(XMLHttpRequest)內取得網址
            offer_res = requests.get(offer_url, headers=headers)
            offer_json = json.loads(offer_res.text)['data']

            df = pd.DataFrame([{
                                'Offer_Company':offer_json['header']['custName'], # 公司名稱
                                'Offer_Name':offer_json['header']['jobName'], # 職缺名稱
                                'Offer_Content':offername.select('p')[0].text, # 工作內容
                                'AcceptRole':[i['description'] for i in offer_json["condition"]["acceptRole"]["role"]],
                                                                                                         # 接受身份
                                'Offer_Welfare':offer_json['welfare']['welfare'], # 福利
                                'Offer_Contact':offer_json['contact']['hrName'], # 聯絡人
                                'Offer_Url':'https:' + get_url, # 公司網址
                                'AppearDate': offer_json['header']['appearDate'], # 刊登日期
                                'Salary': offer_json['jobDetail']['salary'], #薪水
                                                             
                                'Python':function('Python'),
                                'Java':function('Java'),
                                'JavaScript':function('JavaScript'),
                                'R language':function('R'),
                                'MySQL':function('MySQL'),
                                'AWS':function('AWS'),
                                'Oracle':function('Oracle'),
                                'Systems Analysis':function('Systems Analysis'),
                                'Git':function('Git'),
                                'Linux':function('Linux')             #所需工具                   
                }])
            df_All.append(df)
    print("目前第{}頁/共{}頁".format(Page,selectPage))
    Page += 1
    time.sleep( 5 )  #休息五秒
df_All=pd.concat(df_All,axis=0,  ignore_index=True) #合併資料
df_All.to_csv('搜尋職缺{}{}.csv'.format(Search,time.strftime("%Y-%m-%d_%H%M", time.localtime())), index=0, encoding='utf_8_sig')
