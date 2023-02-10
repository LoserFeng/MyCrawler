

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



def main():
    wb=Workbook()
    ws=wb.active  #worksheet
    ws.append(['product_id', 'raw_title', 'view_price', 'view_sales', 'comment_count'
    , 'area', 'userid','name','detail_url', "categary"])
    
    driver=spider_utils.get_browser()
    driver.implicitly_wait(60)
    spider_utils.login(driver,login_id,login_password)







if __name__=='main':
    main()









