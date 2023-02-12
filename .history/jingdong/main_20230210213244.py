


from bs4 import BeautifulSoup
import json
import re
import requests


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
    "cookie": "shshshfpa=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshfpb=yZaSjZXfeZ-R-j6eY1Nun6A; __jdu=16722123231461165655386; areaId=15; PCSYCityID=CN_330000_330100_0; shshshfp=b226777e555e74898a122690ffb3abc3; qrsc=3; jsavif=0; jsavif=0; __jdc=122270672; rkv=1.0; shshshfpx=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; ip_cityCode=1213; ipLoc-djd=15-1213-3038-59931; unpl=JF8EAKhnNSttCENVAxlRTEJDTAgEWwpYSh4HbGAEUg0IT1FXTFdLR0R7XlVdXxRKFB9vZhRXXFNIUg4fBisSEHtdVV9fCU0eAGhgNWRYW0xTBCsBGyIRe11TWF4LSxQBbGUFUVpYS1MBHAYfEBlMbVVuXQBMJwRuZw1dX1p7ZAQrAysTIB0zVF9cCUoeBG9hBRldX01XBhsBGRESS1hTXl0PTxAHa2UMU21Ze1c; __jdv=122270672|kong|t_1003078266_|jingfen|a9073bfab6da4fa0852607aa54cfdade|1676032075899; __jda=122270672.16722123231461165655386.1672212323.1676032076.1676034385.7; wlfstk_smdl=jdmfpxi6g5gqpvvenbkhansp7gwl63oq; pinId=F0lqqKsS7Ce1ffsfn98I-w; pin=LOSER%E4%B8%B0; unick=LOSER%E4%B8%B0; ceshi3.com=000; _tp=Iz8Q38tsk7Xe1Xc1Cy0l4Q%3D%3D; _pst=LOSER%E4%B8%B0; token=0f1f6835e11843597fb1c61484cd3969,3,931130; __tk=WZiMWUADWUVziZVziMnMWUGNixjKRxnLiZnFRZiJVMOxVMeKVcR0iG,3,931130; __jdb=122270672.15.16722123231461165655386|7.1676034385; shshshsID=d1e147c744fc5ed5c7d2163c74ae34e1_9_1676034919664; thor=B0FCAB6E82CA81C65C8CD0C89AFF0FD472C6D13CD66F3F5B02EAE879CA52154AF0AAB1699F3225FAF8704072D0555B4D7F9EEEE568406052B7128C62196DE64C544ABC431E6D3AC69570DA680FCD9BE692A8D668D0E094B61094AFCAF3D3930EC6A0C6FF4121AC759BFC09F8FDA144CE1A85AE2975B1DA8BEC42BA07B707FBD8; 3AB9D23F7A4B3C9B=C435LG3UEXGMHAEILE7G3HDVXAXNBB2CCFDLR6B4JYHHDL7YQD7DBXWW3GDPN6URM5RVNTAQMJK77BOJ7SZ6MWLZXY",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}

SEARCH_KEYWORD='正大食品（CP）京东自营旗舰店'






def main():

    search_url=''
    res=requests.get()
    soup = BeautifulSoup()




if __name__=='__main__':
    main()


