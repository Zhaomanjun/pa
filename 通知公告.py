#!/usr/bin/python
# -*- coding:utf-8 -*-
# 引入开发包
from urllib.request import urlopen
from urllib.request import Request
from urllib import request
from bs4 import BeautifulSoup
import re
import pymysql.cursors
resp = urlopen("http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg/p/1.html").read().decode("utf-8")

soup = BeautifulSoup(resp, "html.parser")

req = request.Request("http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg/p/1.html")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36")
resp = request.urlopen(req)
resp = request.urlopen(req)

TongZhi = soup.findAll("a", href=re.compile("^/index\.php\?s=/home/xwzx/detail/id/\d+\.html"))
f_结果 = open("_结果.txt", 'w')
for url in TongZhi:
  标题 = str(url.get_text())
  内容 = "http://cse.whu.edu.cn" + url["href"]
  时间 = str(soup("span"))
  结果 = 标题 + "<---->" + 时间 + "<---->" + 内容 + "\n"
  f_结果.writelines(结果)
  print(结果)
f_结果.close()


