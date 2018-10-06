#!/usr/bin/python
# -*- coding:utf-8 -*-
# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors
resp = urlopen("http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg/p/1.html").read().decode("utf-8")

soup = BeautifulSoup(resp, "html.parser")

TongZhi = soup.findAll("a", href=re.compile("^/index\.php\?s=/home/xwzx/detail/id/\d+\.html"))
ShiJian = soup.findAll("span")

for url in TongZhi:
 for uurl in ShiJian:
  标题 = url.get_text()
  内容 = "http://cse.whu.edu.cn" + url["href"]
  时间 = uurl.get_text()
  print (标题, "<---->", 时间, "<---->", 内容)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='wikiurl',
                             charse='utf8mb4')

try:
      with connection.cursor() as cursor:
          sql = "insert into `urls`(`urlname`,`urlhref`)values(%s, %s)"
          cursor.execute(sql,(url.get_text(),"http://cse.whu.edu.cn" + url["href"]))
          connection.commit()
finally:
      connection.close()
