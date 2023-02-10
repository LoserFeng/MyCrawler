

import requests
import time
import json
import spider_utils
import random
import requests
import openpyxl
from openpyxl import Workbook





#基础数据

login_id='15157165006'
login_password='110900fyf'

KEY_WORD='正大食品旗舰店'


def main():
    wb=Workbook()
    ws=wb.active  #worksheet
    ws.append(['product_id', 'raw_title', 'view_price', 'view_sales', 'comment_count'
    , 'area', 'userid','name','detail_url', "categary"])
    
    driver=spider_utils.get_browser()
    driver.implicitly_wait(60)
    spider_utils.login(driver,login_id,login_password)
    time.sleep(random.randint(3, 5))
    flag=spider_utils.verify(driver)
    if not flag:
        return -1
    
    
        









if __name__=='main':
    main()









