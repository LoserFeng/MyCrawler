

import requests
import time
import json

t_param = time.time()
t_list = str(t_param).split('.')
_ksTS = t_list[0]+'_'+t_list[1][:3]
callback = str(int(t_list[1][:3])+ 1)

url='https://s.taobao.com/search?ie=utf8&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E6%AD%A3%E5%A4%A7%E9%A3%9F%E5%93%81%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&suggest=0_3&_input_charset=utf-8&wq=%E6%AD%A3%E5%A4%A7&suggest_query=%E6%AD%A3%E5%A4%A7&source=suggest&bcoffset=-8&ntoffset=-8&p4ppushleft=2%2C48&s=176'

pl_url='https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.0&appKey=12574478&t=1675859372806&sign=079713d7046e09c6e72a360b50d5acf7&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=10000&dataType=json&valueType=string&ttid=2022@taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=json&data={"itemId":"656156749560","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":1}'