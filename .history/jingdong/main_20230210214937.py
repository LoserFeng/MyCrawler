


from bs4 import BeautifulSoup
import json
import re
import requests


headers={

    "cookie": 'shshshfpa=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshfpb=yZaSjZXfeZ-R-j6eY1Nun6A; __jdu=16722123231461165655386; o2State={"webp":true,"avif":false}; areaId=15; PCSYCityID=CN_330000_330100_0; ipLoc-djd=15-1213-3038-59931; unpl=JF8EAKhnNSttCENVAxlRTEJDTAgEWwpYSh4HbGAEUg0IT1FXTFdLR0R7XlVdXxRKFB9vZhRXXFNIUg4fBisSEHtdVV9fCU0eAGhgNWRYW0xTBCsBGyIRe11TWF4LSxQBbGUFUVpYS1MBHAYfEBlMbVVuXQBMJwRuZw1dX1p7ZAQrAysTIB0zVF9cCUoeBG9hBRldX01XBhsBGRESS1hTXl0PTxAHa2UMU21Ze1c; __jdv=122270672|kong|t_1003078266_|jingfen|a9073bfab6da4fa0852607aa54cfdade|1676032075899; pinId=F0lqqKsS7Ce1ffsfn98I-w; pin=LOSER丰; unick=LOSER丰; ceshi3.com=000; _tp=Iz8Q38tsk7Xe1Xc1Cy0l4Q==; _pst=LOSER丰; TrackID=1mSHuzyhNlfuEWBCxKgW-N6lHF_V2KtXt-KI7TyejUN3h6wmgV6D2nwdGeOTYNBvd7ItugyTd7HBeMwB5jm3bcYX7Fhcj4wx_FhKBst8nScPDr4eEMEDIOFvpdE3jmWQV; thor=B0FCAB6E82CA81C65C8CD0C89AFF0FD4B4F8009CD8011E1A50F11C8381552072F143D30D85E88FE7ABC5A2A75CEE4BAB7EE9DAB97F661FF873675CF2D35188371321AB88E380B2917D47D8D7C1499234E5D6B0B2329AF772697CDECCD7B72CC00366E537C5CB9CBF60FF4719A51EC64D3B5425C85B8F6AACF9FEE42DD01D5317; __jda=76161171.16722123231461165655386.1672212323.1676032076.1676034385.7; __jdb=76161171.25.16722123231461165655386|7.1676034385; __jdc=76161171; shshshfp=4acae8cebf7bd7f65f70313dbcf72b00; shshshfpx=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshsID=d1e147c744fc5ed5c7d2163c74ae34e1_17_1676036669040; 3AB9D23F7A4B3C9B=FTSDKAYZNZKCZEI2SHBQY2UVW7R5ZBD7C4KZOV6I52DX4YPOAOJ2OLORCGQB5P35WXNCTLBOXG6CZWIZCSDSGUAJ5U',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}

SEARCH_KEYWORD='正大食品（CP）京东自营旗舰店'






def main():

    search_url=f'https://search.jd.com/Search?keyword={SEARCH_KEYWORD}&enc=utf-8'

    res=requests.get(search_url,headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup)



if __name__=='__main__':
    main()


