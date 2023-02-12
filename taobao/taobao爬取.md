# 爬取淘宝评论



目标：爬取正大食品的评论，小白入门从头开始



## 寻找评论所对应的URL

![image-20230208204744916](C:\Users\feng_\Desktop\市场调研\Crawler\taobao\assets\image-20230208204744916.png)



~~~html
https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.0&appKey=12574478&t=1675859372806&sign=079713d7046e09c6e72a360b50d5acf7&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=10000&dataType=json&valueType=string&ttid=2022@taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=json&data={"itemId":"656156749560","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":1}
~~~





url构成



jsv=2.7.0

appKey=12574478

t=1675859372806

sign=079713d7046e09c6e72a360b50d5acf7

api=mtop.alibaba.review.list.for.new.pc.detail

v=1.0

isSec=0

ecode=0

timeout=10000

dataType=json

valueType=string

ttid=2022@taobao_litepc_9.17.0

AntiFlood=true&AntiCreep=true&preventFallback=true&type=json

data={"itemId":"656156749560","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":1}



## selenium





1. 下载 selenium

~~~
conda install selenium
~~~

2. 下载浏览器驱动

[ChromeDriver - WebDriver for Chrome - Downloads (chromium.org)](https://chromedriver.chromium.org/downloads)



然后给这个添加一下环境变量











## selenium的使用

[(14条消息) selenium模块中的find_element_by_id方法无法使用,改用driver.find_element(by=By.ID, value=None)_vchayi的博客-CSDN博客](https://blog.csdn.net/weixin_51637785/article/details/125509483)





通过文字确定元素

[(14条消息) selenium 通过文字定位元素_selenium 文字定位_lonet的博客-CSDN博客](https://blog.csdn.net/lonet/article/details/124636246)

我们要确定评论的位置，所以先尝试用XPath，但是XPath并不准确，所以我还是用文字来确定好了。。。

![image-20230210160230876](C:\Users\feng_\Desktop\市场调研\Crawler\taobao\assets\image-20230210160230876.png)







爬取失败，原因，必须手机查看所有评论(寄)



学习视频：[05丨下载安装浏览器驱动：教你解决最麻烦的版本匹配问题_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1BS4y1g74o/?p=5&spm_id_from=333.880.my_history.page.click&vd_source=39de5ac609bd713fda33f767041c4d10)

借鉴文章：[正大食品官方旗舰店_淘宝搜索 (taobao.com)](https://s.taobao.com/search?ie=utf8stats_click%3Dsearch_radio_all%3A1&js=1&imgfile=&q=正大食品官方旗舰店&suggest=0_3&_input_charset=utf-8&wq=正大&suggest_query=正大&source=suggest&bcoffset=-8&ntoffset=-8&p4ppushleft=2%2C48&s=176)















# 爬取京东评论



shshshfpa=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshfpb=yZaSjZXfeZ-R-j6eY1Nun6A; __jdu=16722123231461165655386; o2State={"webp":true,"avif":false}; areaId=15; PCSYCityID=CN_330000_330100_0; ipLoc-djd=15-1213-3038-59931; unpl=JF8EAKhnNSttCENVAxlRTEJDTAgEWwpYSh4HbGAEUg0IT1FXTFdLR0R7XlVdXxRKFB9vZhRXXFNIUg4fBisSEHtdVV9fCU0eAGhgNWRYW0xTBCsBGyIRe11TWF4LSxQBbGUFUVpYS1MBHAYfEBlMbVVuXQBMJwRuZw1dX1p7ZAQrAysTIB0zVF9cCUoeBG9hBRldX01XBhsBGRESS1hTXl0PTxAHa2UMU21Ze1c; __jdv=122270672|kong|t_1003078266_|jingfen|a9073bfab6da4fa0852607aa54cfdade|1676032075899; pinId=F0lqqKsS7Ce1ffsfn98I-w; pin=LOSER丰; unick=LOSER丰; ceshi3.com=000; _tp=Iz8Q38tsk7Xe1Xc1Cy0l4Q==; _pst=LOSER丰; TrackID=1mSHuzyhNlfuEWBCxKgW-N6lHF_V2KtXt-KI7TyejUN3h6wmgV6D2nwdGeOTYNBvd7ItugyTd7HBeMwB5jm3bcYX7Fhcj4wx_FhKBst8nScPDr4eEMEDIOFvpdE3jmWQV; thor=B0FCAB6E82CA81C65C8CD0C89AFF0FD4B4F8009CD8011E1A50F11C8381552072F143D30D85E88FE7ABC5A2A75CEE4BAB7EE9DAB97F661FF873675CF2D35188371321AB88E380B2917D47D8D7C1499234E5D6B0B2329AF772697CDECCD7B72CC00366E537C5CB9CBF60FF4719A51EC64D3B5425C85B8F6AACF9FEE42DD01D5317; __jda=76161171.16722123231461165655386.1672212323.1676032076.1676034385.7; __jdb=76161171.25.16722123231461165655386|7.1676034385; __jdc=76161171; shshshfp=4acae8cebf7bd7f65f70313dbcf72b00; shshshfpx=a59ef60d-c8a6-92ba-2baf-a646895cc98d-1672212324; shshshsID=d1e147c744fc5ed5c7d2163c74ae34e1_17_1676036669040; 3AB9D23F7A4B3C9B=FTSDKAYZNZKCZEI2SHBQY2UVW7R5ZBD7C4KZOV6I52DX4YPOAOJ2OLORCGQB5P35WXNCTLBOXG6CZWIZCSDSGUAJ5U





## beautifulsoup4 学习

首先是headers

[(15条消息) 爬虫中遇到登陆问题的解决方法_阿怪呢的博客-CSDN博客_爬虫遇到登录](https://blog.csdn.net/weixin_41998772/article/details/106476166)











## 学习一下re

[(15条消息) python re库_彼岸花灬Sakura的博客-CSDN博客_python re库](https://blog.csdn.net/ShorttubeLy/article/details/128014227)

