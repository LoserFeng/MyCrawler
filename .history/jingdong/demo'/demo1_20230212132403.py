
import requests


url=f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={product_id}&score=0&sortType=5&page={cur_page}&pageSize=10&isShadowSku=0&fold=1'
        res=requests.get(url=url,headers=headers)