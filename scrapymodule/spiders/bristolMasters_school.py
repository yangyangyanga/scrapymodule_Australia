# -*- coding: utf-8 -*-
import scrapy
import re
from scrapymodule.items import SchoolItem1
from scrapymodule.getItem import get_item1

class BristolMasterShoolSpider(scrapy.Spider):
    name = "bristolMasters"
    # allowed_domains = ['baidu.com']
    start_urls = ['https://www.bristol.ac.uk/study/postgraduate/search/']

    def parse(self, response):
        links = response.xpath("//body[@id='bristol-ac-uk']/div[@class='wrapper']/main[@class='content']/div[@class='prog-az-listings full-width']/ul[@class='list-no-style list-half-spacing prog-results-list']/li/a/@href").extract()
        print(len(links))
        for link in links:
            # print(link)
            yield scrapy.Request("https://www.bristol.ac.uk"+link, callback=self.parse_data)

    # def clear_data(self, str):
    #     str = str.replace("\n", " ").replace("\r", " ").strip()

    def clear_space(self, templist):
        for i in range(len(templist)):
            templist[i] = templist[i].replace('\n', " ")
            templist[i] = templist[i].strip(" ")
            templist[i] = templist[i].replace('\r', " ")

    def parse_data(self, response):
        items = get_item1(SchoolItem1)
        print("=================================")
        items['country'] = "England"
        items["website"] = "https://www.bristol.ac.uk/"
        items['degree_level'] = '1'
        items['university'] = "University of Bristol"

        try:
            # 专业
            course = response.xpath("//h1[@id='pagetitle']/span//text()").extract()
            # print("course = ", course)
            items['programme'] = ''.join(course).replace("\n", " ").replace("\r", " ").strip()

            # degreeaward
            degreeaward = response.xpath("//table[@class='table-basic table-solid']/tbody/tr[1]/td//text()").extract()
            # print("degreeaward = ", degreeaward)
            items['degree_type'] = ''.join(degreeaward).replace("\n", " ").replace("\r", " ").strip()

            # duration
            duration = response.xpath("//table[@class='table-basic table-solid']/tbody/tr[2]/td//text()").extract()
            # print("duration = ", duration)
            items['duration'] = ''.join(duration).replace("\n", " ").replace("\r", " ").strip()

            # location
            location = response.xpath("//table[@class='table-basic table-solid']/tbody/tr[3]/td//text()").extract()
            # print("location = ", location)
            items['location'] = ''.join(location).replace("\n", " ").replace("\r", " ").strip()

            # startdate
            startdate = response.xpath("//table[@class='table-basic table-solid']/tbody/tr[5]/td//text()").extract()
            # print("startdate = ", startdate)
            items['start_date'] = ''.join(startdate).replace("\n", " ").replace("\r", " ").strip()

            # deadline
            deadline = response.xpath("//div[@id='apply']/div[@class='apply-deadline']/p//text()").extract()
            # print("deadline = ", deadline)
            items['deadline'] = ''.join(deadline).replace("\n", " ").replace("\r", " ").strip()

            # department
            department = response.xpath("//div[@id='contact']/p[@class='pg-contact-address']/text()").extract()
            # print("department = ", department)
            items['department'] = ''.join(department).replace("\n", " ").replace("\r", " ").strip()

            # overview  //div[@id='programme-overview']//text()
            overview = response.xpath("//div[@id='programme-overview']//text() | //div[@id='pgr-overview']//text()").extract()
            items['overview'] = ''.join(overview).replace("\n", " ").replace("\r", " ").strip()

            # tuitionFee   //div[@id='fees']
            tuitionFee = response.xpath("//div[@id='fees']//text()").extract()
            self.clear_space(tuitionFee)
            # print("tuitionFee = ", tuitionFee)
            if "Overseas: full-time" in tuitionFee:
                feeIndex = tuitionFee.index("Overseas: full-time")
                fees = tuitionFee[feeIndex+1]
            else:
                fees = ""
            items['tuition_fee'] = fees

            # modules   //div[@id='programme-structure']
            modules = response.xpath("//div[@id='programme-structure']//text()").extract()
            items['modules'] = ''.join(modules).replace("\n", " ").replace("\r", " ").strip()

            # 学术要求本科特殊专业要求、IELTS
            entryRequirements = response.xpath("//div[@id='entry-requirements']//text()").extract()
            self.clear_space(entryRequirements)
            print("entryRequirements = ", entryRequirements)
            entryRequirementsIndex = entryRequirements.index("Entry requirements")
            entryRequirementsIndexEnd = entryRequirements.index("English language requirements")
            entryRequirementsResult = entryRequirements[entryRequirementsIndex+1:entryRequirementsIndexEnd-1]
            items['entry_requirements'] = ''.join(entryRequirementsResult)

            ieltsIndexEnd = entryRequirements.index("Admissions statement")
            ielts = entryRequirements[entryRequirementsIndexEnd+1:ieltsIndexEnd-1]
            items['IELTS'] = ''.join(ielts)

            # 就业    //div[@id='careers']
            career = response.xpath("//div[@id='careers']//text()").extract()
            # print("department = ", department)
            items['career'] = ''.join(career).replace("\n", " ").replace("\r", " ").strip()

            items['url'] = response.url
            # print(items)
            yield items
        except Exception as e:
            print("异常：", str(e))
            print(response.url)
            print("====----====")
            with open("./error/"+items['university']+".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")







