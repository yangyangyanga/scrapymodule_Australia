import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import SchoolItem1
from scrapymodule.getItem import get_item1

class StrathMastersSchoolSpider(scrapy.Spider):
    name = "strathMasters"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?attendance=full-time&level_ug=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        # print(response.text)
        contentText = response.text
        # with open("strathhtml.txt", "a+", encoding='utf-8') as f:
        #     f.write(contentText)

        taughtUrl = re.findall(r"/courses/postgraduatetaught/.*/", contentText)
        # print(len(taughtUrl))
        print(taughtUrl)
        for link in taughtUrl:
            url = "https://www.strath.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, errback=self.error_back)
    def error_back(self, response):
        with open("err.txt", "a+") as f:
            f.write(response.url+"\n==============")
    def parse_data(self, response):
        item = get_item1(SchoolItem1)
        item['country'] = "England"
        item["website"] = "https://www.strath.ac.uk/"
        item['degree_level'] = '1'
        item["university"] = "University of Strathclyde"
        print("==========================")
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)

            # 专业名
            programme = response.xpath(
                "//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/text()").extract()
            # print("programme = ", programme)
            item['programme'] = ''.join(programme)

            # 课程长度、开学时间、截止日期
            durationStartdateDeadline = response.xpath("//section[@class='related-link-group']//text()").extract()
            clear_space(durationStartdateDeadline)
            # print(durationStartdateDeadline)
            item['start_date'] = ""
            item['duration'] = ""
            if "Study mode and duration" in durationStartdateDeadline:
                durationIndex = durationStartdateDeadline.index("Study mode and duration")
                if "Start date" in durationStartdateDeadline:
                    startDateIndex = durationStartdateDeadline.index('Start date')
                    duration = durationStartdateDeadline[durationIndex+2:startDateIndex-1]
                    # print(duration)
                    item['duration'] = ''.join(duration)
                    start_date = durationStartdateDeadline[startDateIndex+1]
                    item['start_date'] = ''.join(start_date).strip(":")

            # 截止日期
            if "Application deadline" in durationStartdateDeadline:
                deadlineIndex = durationStartdateDeadline.index("Application deadline")
                item['deadline'] = durationStartdateDeadline[deadlineIndex+1].strip(":")
            else:
                item['deadline'] = ""

            # 专业描述
            overview1 = response.xpath("//article[@id='why-this-course']//text()").extract()
            overview = ''.join(overview1)
            overview = clear_space_str(overview)
            item['overview'] = overview

            # 课程设置、评估方式
            modulesAssessment = response.xpath("//article[@id='course-content']//text()").extract()
            clear_space(modulesAssessment)
            # print(modulesAssessment)
            if "Learning & teaching" in modulesAssessment:
                assessmentIndex = modulesAssessment.index("Learning & teaching")
                item['modules'] = ''.join(modulesAssessment[:assessmentIndex-1])
                item["teaching"] = ''.join(modulesAssessment[assessmentIndex:])
            else:
                item['modules'] = ''.join(modulesAssessment)
                item["teaching"] = ''

            # 学术要求、英语要求
            entryRequirement = response.xpath("//article[@id='entry-requirements']//text()").extract()
            clear_space(entryRequirement)
            # print(entryRequirement)
            item['other'] = ''.join(entryRequirement)
            templist = ["English language requirements for international students", "English Language Requirements for International Students",
                        "English language requirements"]
            entryIndex = 0
            for temp in templist:
                if temp in entryRequirement:
                    entryIndex = entryRequirement.index(temp)
            if "Pre-Masters preparation course" in entryRequirement:
                entryIndexEnd = entryRequirement.index("Pre-Masters preparation course")
            else:
                entryIndexEnd = -1
            ielts = entryRequirement[entryIndex:entryIndexEnd]
            item["IELTS"] = ''.join(ielts)

            if entryIndex == 0:
                if "Pre-Masters preparation course" in entryRequirement:
                    entryIndex = entryRequirement.index("Pre-Masters preparation course")
                else:
                    entryIndex = -1
            Rntry_requirements = entryRequirement[:entryIndex]
            item['entry_requirements'] = ''.join(Rntry_requirements)

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("/article[@id='fees-and-funding']/ul[3]/li//text()").extract()
            tuition_fee = ''.join(tuition_fee)
            item['tuition_fee'] = tuition_fee

            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='careers']//text()").extract()
            career = ''.join(career)
            item['career'] = career
            item['url'] = response.url
            # item['type'] = "Taught"
            yield item
        except Exception as e:
            with open("./error/" + item['university'] + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)



