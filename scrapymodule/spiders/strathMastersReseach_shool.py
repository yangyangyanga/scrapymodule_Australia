import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import StrathMastersResearchSchoolItem
from scrapymodule.getItem import get_item

class StrathMastersSchoolSpider(scrapy.Spider):
    name = "strathResearchMasters"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?attendance=full-time&level_ug=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        # print(response.text)
        contentText = response.text
        # with open("strathhtml.txt", "a+", encoding='utf-8') as f:
        #     f.write(contentText)

        reseachUrl = re.findall(r"/courses/research/.*/", contentText)
        # print(len(reseachUrl))
        # print(reseachUrl)
        for link in reseachUrl:
            url = "https://www.strath.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, errback=self.error_back)

    def error_back(self, response):
        with open("./error/strathResearchMasterserr.txt", "a+") as f:
            f.write(response.url+"\n==============")

    def parse_data(self, response):
        item = get_item(StrathMastersResearchSchoolItem)
        item["university"] = "University of Strathclyde"
        print("==========================")
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)

            # 专业名
            programme = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/text()").extract()
            # print("programme = ", programme)
            item['programme'] = ''.join(programme)

            # department
            department = response.xpath("//section[@id='key-aside']//text()").extract()
            clear_space(department)
            while '' in department:
                department.remove('')
            # print(department)
            if "Our department" in department:
                departmentIndex = department.index("Our department")
                department1 = department[departmentIndex+2].split("Find out more about ")
                item['department'] = ''.join(department1)
            print(item['department'])
            # 专业描述
            overview = response.xpath("//article[@id='research-opportunities']//text()").extract()
            clear_space(overview)
            # print(overview)
            if "Our current opportunities" in overview:
                overviewIndexEnd = overview.index("Our current opportunities")
                item['overview'] = ''.join(overview[:overviewIndexEnd-1])
            else:
                item['overview'] = ''.join(overview)

            # 学术要求、英语要求
            item["IELTS"] = "Our IELTS requirement is 6.5, however some courses may look for more."
            item['Rntry_requirements'] = "Students are required to have a GPA of approximately 80 in academic subjects from a four-year Bachelors degree.Students interested in PhD must usually have a Masters and must include a proposal in their application.For further information on entry requirements, you can contact our representative Colin Rogers"

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("//article[@id='fees-and-funding']//text()").extract()
            clear_space(tuition_fee)
            while '' in tuition_fee:
                tuition_fee.remove('')
            # print(tuition_fee)
            if "International students" in tuition_fee:
                feeIndex = tuition_fee.index("International students")
                item['tuition_fee'] = tuition_fee[feeIndex+1]
            # print(item['tuition_fee'])

            # 申请材料//article[@id='how-can-i-apply']
            applicationDoc = response.xpath("//article[@id='how-can-i-apply']//text()").extract()
            clear_space(applicationDoc)
            if "The application" in applicationDoc:
                applicationDocIndex = applicationDoc.index("The application")
                if "Supervisors" in applicationDoc:
                    applicationDocIndexEnd = applicationDoc.index("Supervisors")
                    item["application_documents"] = ''.join(applicationDoc[applicationDocIndex:applicationDocIndexEnd])
                else:
                    item["application_documents"] = ''.join(applicationDoc[applicationDocIndex:])

            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='support-and-development']//text()").extract()
            clear_space(career)
            career = ''.join(career)
            item['career'] = career
            item['URL'] = response.url
            item['type'] = "Research"
            # print(item)
            yield item
        except Exception as e:
            with open("./error/strathResearchMasterserror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)



