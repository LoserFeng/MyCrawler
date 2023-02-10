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









学习视频：[05丨下载安装浏览器驱动：教你解决最麻烦的版本匹配问题_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1BS4y1g74o/?p=5&spm_id_from=333.880.my_history.page.click&vd_source=39de5ac609bd713fda33f767041c4d10)

借鉴文章：[正大食品官方旗舰店_淘宝搜索 (taobao.com)](https://s.taobao.com/search?ie=utf8stats_click%3Dsearch_radio_all%3A1&js=1&imgfile=&q=正大食品官方旗舰店&suggest=0_3&_input_charset=utf-8&wq=正大&suggest_query=正大&source=suggest&bcoffset=-8&ntoffset=-8&p4ppushleft=2%2C48&s=176)



