# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import time
import re
import json
import requests
import openpyxl
from openpyxl import Workbook


# 创建表格
wb = Workbook()
ws = wb.active
# 写入一行的数据, 从第一列的空白单元格开始
ws.append(
    ['product_id', 'raw_title', 'view_price', 'view_sales', 'comment_count', 'area', 'userid',
     'name', 'detail_url'])
for page in range(0, 99):
    print(page)

    member_url = f'https://s.taobao.com/search?q=%E6%B4%97%E5%8F%91%E6%B0%B4&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20220729&ie=utf8&s={44 * page}'


    headers = {
        'cookie': '_samesite_flag_=true; cookie2=12916e432d94f31d38c1ebafc11332c0; t=4fb6ba1d4ca9d995510a8473056095bd; thw=cn; enc=A68nCl1pLRLjnr2uYDVkSpXhZPZuOEgYyFOvOaeDv7sIXLlhZDx1Stx9PRO0dkfsonq1JoRiJiY03fXAZ0y0xA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; xlly_s=1; _tb_token_=f64568ee7ea76; _m_h5_tk=5205a52a52333440076e8ea0b04b2029_1659369500923; _m_h5_tk_enc=15b0ae9a41779fb4a2f2b7861c1eb9dc; x5sec=7b227365617263686170703b32223a223130363739643264396537663164343037383331353832366464353730353861434a62426e356347454c69566a35483036706d6d62426f4e4d6a49344d7a6b314f444d354d6a73304e6a436e68594b652f502f2f2f2f384251414d3d227d; mt=ci=0_0; cna=saJbGzL7RRQCARsucmvHYiBG; sgcookie=E100zz4P2dWQ6sqOfiJ6MqSsZaRQrrPSL%2FziSOaYl9onnf%2Ba8aegcm87A7%2FWCBy%2FgSeL%2FP%2BJ3B4QwGgz9f9f9d2Bz5gYL3KlQQ183XbWrs%2B8QRg%3D; unb=2283958392; uc1=cookie21=VFC%2FuZ9aiKCbhSSUah6i&existShop=false&cookie14=UoexOz%2FdNaYVNw%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&pas=0&cookie15=URm48syIIVrSKA%3D%3D; uc3=nk2=G5Vc0zQ%3D&vt3=F8dCv4JseHfPcIGbDIg%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&id2=UUppqxjlViDBnQ%3D%3D; csg=0ea2fb89; lgc=xugne; cancelledSubSites=empty; cookie17=UUppqxjlViDBnQ%3D%3D; dnk=xugne; skt=a4b7b55974b58882; existShop=MTY1OTM2MzY2NQ%3D%3D; uc4=id4=0%40U2gjFQB3i0JP2MsIR0KeMVY4LZvF&nk4=0%40GSa4r%2BoYQfjIgjepW7a%2BFg%3D%3D; tracknick=xugne; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=e2f; _nk_=xugne; cookie1=BxeMIUlEMkB2pK49M6R1rLTsKawKuryePS6wiEUDlWI%3D; JSESSIONID=2EF592D1B28B36D8D3A182E06D8C10B4; tfstk=ccoVBu0e_nK2q7gEzuZwCtnKXCEAZvzg8gyToBNNTnqOZ8zci2CTEBR_UJBPsrf..; l=eBNKB2ynL8X3jC5tBOfZourza77OQIRvmuPzaNbMiOCP_4fp5TYRW6xoaLY9CnGVh6jeR3Wrj_IwBeYBqIv4n5U62j-laOHmn; isg=BKWlkQOTK0PyHE8ethoFFUeatGHf4ll0SCtOQaeKQVzrvsUwbzBrRAhcTCLIinEs',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    time.sleep(random.randint(2, 4))
    response = requests.get(member_url, headers=headers)
    html = response.content
    # print(html)
    with open('05-cookie.html', 'wb') as f:
        f.write(html)

    html_text = response.text
    try:
        json_str = re.findall(r'g_page_config = (.*?) g_srp_loadCss', html_text, re.S)[0].strip()[:-1]
    except:
        print("NG", member_url)

        continue
    # 格式化
    json_dict = json.loads(json_str)

    # 获取信息列表
    auctions = json_dict['mods']['itemlist']['data']['auctions']
    DATA = []
    # 提取数据 注意是否有通过异步进行加载的数据，需要在进行请求
    for auction in auctions:
        temp = {
            'product_id': auction['nid'],
            'raw_title': auction['raw_title'],
            'view_price': auction['view_price'],
            'view_sales': auction['view_sales'],
            'comment_count': auction['comment_count'],
            'view_fee': '否' if float(auction['view_fee']) else '是',
            'isTmall': '是' if auction['shopcard']['isTmall'] else '否',
            'area': auction['item_loc'],
            'userid': auction['user_id'],
            'name': auction['nick'],
            'detail_url': auction['detail_url'],
        }
        DATA.append(temp)
        ws.append([auction['nid'], auction['raw_title'], auction['view_price'], auction['view_sales'],
                   auction['comment_count'],
                   auction['item_loc'], auction['user_id'], auction['nick'], auction['detail_url']])
    # 覆盖方式保存表格
    wb.save(os.getcwd() + '/test.xlsx')
    wb = openpyxl.load_workbook(os.getcwd() + '/test.xlsx')
    # 对xlsx文件操作之前,要 active.
    ws = wb.active

wb.save(os.getcwd() + '/test.xlsx')
