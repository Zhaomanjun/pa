# coding:utf8
# -*- coding:utf-8 -*-

from 网页版爬取通知 import url_manager, html_downloader, html_parser, html_outputer
import urllib.request

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
