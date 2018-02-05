# -*- coding: utf-8 -*-
import scrapy


class SwanseaShoolSpider(scrapy.Spider):
    name = "swanseaben"
    # allowed_domains = ['baidu.com']
    start_urls = ['http://www.swansea.ac.uk/undergraduate/courses/']

    def parse(self, response):
        # print(response.text)
        # response = response.text
        div1 = response.xpath("//div[@class='widget--course--a-to-z']")
        links = response.xpath('//div[@class="widget--course--a-to-z"]//ul[@class="course--a-to-z--section-courses"]/li/a/@href')
        print(links)
