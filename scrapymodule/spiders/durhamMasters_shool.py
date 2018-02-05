import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import ManchesterMastersSchoolItem

class DurhamMastersSchoolSpider(scrapy.Spider):
    name = "durhamMasters"
    # url_start = "http://www.manchester.ac.uk/study/masters/courses/list/"
    start_urls = ["https://www.dur.ac.uk/courses/all/"]

    def parse(self, response):
        # with open("durham.html", 'w+', encoding='utf-8') as f:
        #     f.write(response.text)
        pat = re.findall(r'\w+\s(PostgraduateTaught\s2018)\s\w+', response.text)
        print(pat)
        pat = ''.join(pat)
        url_end = response.xpath("//div[@id='content']/div/table[@class='courses']/tbody/tr[@class='"+str(pat)+"']/td/a/@href").extract()
        print(url_end)
        print(len(url_end))