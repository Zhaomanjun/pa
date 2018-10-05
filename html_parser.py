# coding:utf8
# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.fing_all('a', href=re.compile("^/index\.php\?s=/home/xwzx/detail/id/\d\d\d\.html"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url

        title_node = soup.find('div', class_="news_list").find("h3")
        res_data['title'] = title_node.get_text()

        time_node = soup.find('div', class_="news_list").find("span")
        res_data['time'] = time_node.get_text()
        summary_node = soup.find('div', class_="news_view")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, page_url, from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data