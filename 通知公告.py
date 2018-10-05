#!/usr/bin/python
# -*- coding:utf-8 -*-
# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen("http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg/p/1.html").read().decode("utf-8")

soup = BeautifulSoup(resp, "html.parser")

TongZhi = soup.findAll("a", href=re.compile("^/index\.php\?s=/home/xwzx/detail/id/\d+\.html"))


for url in TongZhi:
  标题 = url.get_text()
  时间 = soup("span")
  内容 = "http://cse.whu.edu.cn" + url["href"]
  print (标题, "<---->", 时间, "<---->", 内容)
