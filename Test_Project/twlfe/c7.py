# import requests
# from bs4 import BeautifulSoup
# res=requests.get('http://news.sina.com.cn/china/')
# res.encoding='utf-8'
# soup=BeautifulSoup(res.text,'html.parser')
# alink=soup.select('.news-item')
# for i in alink:
#     if len(i.select('h2'))>0:
#         Time=i.select('.time')[0].text
#         Title=i.select('a')[0].text
#         Href=i.select('a')[0]['href']
#         print(Time,Title,Href)
# import json
# a='{"one":1,"two":2,"three":3}'
# print(json.loads(a))
# a={'1':1,'2':2,'3':3}
# print(a['2'])

step1: 买家登录
step2: 买家选择商家B商品c6型号1的物品1件并立即购买
step3: 商家B登录，获取期望金额并与订单结算结果进行校验
step4: 买家提交订单
step5: 买家通过钱包付款, 并调用钱包支付回调接口
step6: 商家B发货
step7: 买家确认收货, 并评价
step8: 更新订单时间为交易完成的7天后
step9: 平台登录
step10: 平台出账
step11: 商家登录
step12: 商家确认
step13: 平台登录
step14: 平台打款，打款成功
step15: 平台再次打款，打款失败

import requests
import abc
requests.p
