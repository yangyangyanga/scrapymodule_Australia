# -*- coding: utf-8 -*-
import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.getItem import get_item
from scrapymodule.getTuition_fee import getTuition_fee
from scrapymodule.items import SchoolItem

class MyspiderSpider(scrapy.Spider):
    name = "myspiderBen"
    start_urls = []
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(SchoolItem)
        item['university'] = "University"
        item['country'] = 'Australia'
        item['website'] = ''
        item['url'] = response.url
        print("===========================")
        print(response.url)
        try:

            yield item
        except Exception as e:
            with open("./error/"+item['university']+item['degree_level']+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

