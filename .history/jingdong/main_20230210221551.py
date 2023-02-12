


from bs4 import BeautifulSoup
import json
import re
import requests
from urllib.parse import quote


headers={


    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Microsoft Edge\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"
}

SEARCH_KEYWORD='正大食品（CP）京东自营旗舰店'

TOTAL_PAGE=3  #这里懒得自动了，直接手动算了
PAGE_SIZE=3




def get_search_page(cur_page,idx):
    search_url=f'https://search.jd.com/Search?keyword={quote(SEARCH_KEYWORD)}&page={cur_page}&s={idx}&click=1'
    res=requests.get(url=search_url,headers=headers)
    html = BeautifulSoup(res.text, 'lxml')
    return res.text


def main():
    
    #search_url=f'https://search.jd.com/Search?keyword={quote(SEARCH_KEYWORD)}&enc=utf-8'

    
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup)



if __name__=='__main__':
    main()


