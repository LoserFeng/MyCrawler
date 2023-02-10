

import requests
import time
import json
import spider_utils
import random
import requests
import openpyxl
import logging
from openpyxl import Workbook
from selenium.webdriver.common.by import By
import threading



#基础数据

login_id='15157165006'
login_password='110900fyf'

KEY_WORD='正大食品旗舰店'


def main():
    spider_utils.init_log()
    wb=Workbook()
    ws=wb.active  #worksheet
    ws.append(['product_id', 'raw_title', 'view_price', 'view_sales', 'comment_count'
    , 'area', 'userid','name','detail_url', "categary"])
    
    driver=spider_utils.get_browser()
    driver.implicitly_wait(60)
    spider_utils.login(driver,login_id,login_password)
    time.sleep(random.randint(3, 5))

    t1 = threading.Thread(target=spider_utils.monitor, args=(driver,))
    t1.start()
    
    flag=spider_utils.verify(driver)
    if not flag:
        return -1
    #url = f'https://s.taobao.com/search?q={quote(KEYWORD)}'
    url = f'https://s.taobao.com/search?q={KEY_WORD}'
    driver.get(url)
    time.sleep(random.randint(3,5))

    # flag=spider_utils.verify(driver)
    # if not flag:
    #     return -1
    
    page_str = driver.find_element(By.CSS_SELECTOR, "div.total").text
    total_page=int(page_str.split(" ")[1])




    for page in range(0,total_page):
        print('page: ',page+1)
        #url = f'https://s.taobao.com/search?q={quote(KEYWORD)}&s={48 * page}'
        url = f'https://s.taobao.com/search?q={KEY_WORD}&s={48 * page}'
        time.sleep(random.randint(3, 5))
        driver.get(url)
        time.sleep(random.randint(2, 4))

        # flag=spider_utils.verify(driver)
        # if not flag:
        #     return -2
        while driver.title=='验证码拦截'
        









if __name__=='main':
    main()









