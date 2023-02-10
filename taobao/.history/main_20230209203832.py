

import requests
import time
import json
import spider_utils
import random
import requests
import openpyxl
from openpyxl import Workbook





def main():
    wb=Workbook()
    ws=wb.active  #worksheet
    ws.append(['product_id', 'raw_title', 'view_price', 'view_sales', 'comment_count', 'area', 'userid',
     'name', 'detail_url', "categary"])
    driver=spider_utils.get_browser()







if __name__=='main':
    main()









