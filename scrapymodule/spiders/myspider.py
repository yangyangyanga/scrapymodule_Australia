# -*- coding: utf-8 -*-
import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.getItem import get_item1
from scrapymodule.getTuition_fee import getTuition_fee
from scrapymodule.items import BathspaBenSchoolItem

class MyspiderSpider(scrapy.Spider):
    name = "myspiderBen"
    start_urls = []

    def parse(self, response):
        item = get_item1(BathspaBenSchoolItem)
        item['university'] = "University"
        item['url'] = response.url
        # print("===========================")
        # print(response.url)
        try:

            yield item
        except Exception as e:
            with open("./error/bathspaBenSchoolerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)

