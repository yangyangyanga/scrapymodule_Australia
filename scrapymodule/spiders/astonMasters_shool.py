import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import SchoolItem1
from scrapymodule.getItem import get_item1

class AstonMastersSchoolSpider(scrapy.Spider):
    name = "astonMasters"
    start_urls = ["http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-accounting-finance/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/biomedical-sciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/abs/msc-business-analytics/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-business-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/abs/msc-business-economics-and-finance/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/life-health-sciences/mscneurophysiology",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/life-health-sciences/mscneurophysiology/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/life-health-sciences/msc-clinical-science-neurosensory-sciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/cognitive-neurosciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/cognitive-neurosciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/eas/msc-computer-science/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/life-health-sciences/doctor-of-hearing-therapy/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/pharmaceutical-sciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/eas/-msc-electrical-power-engineering/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/languages-social-sciences/emerging-global-europe/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-engineering-leadership-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-engineering-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-entrepreneurship-and-international-business/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/europe/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/eu-internationalrelations/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/eu-internationalrelations/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-finance-investments/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/forensic-linguistics-ma/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/forensic-linguistics-ma/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/double-masters-in-governance-and-international-politics-ma/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/health-psychology/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/msc-health-psychology/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-human-resource-management-business/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/isba/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/abs/msc-international-accounting-finance/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-international-business/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/abs/abs/pre-masters/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/international-relations-global-gov/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/international-relations-global-gov/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-investment-analysis/",
"http://www.aston.ac.uk/aston-business-school/programmes/aston-mba/full-time-mba/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/eas/msc-mechanical-engineering/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/eas/msc-product-design/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/multilevel-governance-and-international-relations/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-organisational-behaviour/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/pharmaceutical-sciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/postgraduate-certificate-in-pharmacist-independent-prescribing/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/life-health-sciences/pharmaceutical-sciences/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/policy-and-social-research/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/policy-and-social-research/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/overseas-pharmacists/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-professional-engineering/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/msc-psychiatric-pharmacy-practice/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/certificate-psychiatric-therapeutics/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/abs/abs/msc-services-innovation/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/sociology-and-social-research/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/sociology-and-social-research/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-software-engineering/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/eas/msc-software-project-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/life-health-sciences/msc-stem-cells-and-regenerative-medicine/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-strategic-marketing-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-strategy-international-business/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-supply-chain-management/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-telecommunications-systems/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/ma-tesol-translation/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/ma-tesol-translation/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/languages-social-sciences/ma-tesol/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/translation-european/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/translation-european/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/translation-studies/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/languages-social-sciences/translation-studies/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/eas/msc-in-wireless-communications-and-networking/",
"http://www.aston.ac.uk/study/postgraduate/taught-programmes/school/abs/msc-work-psychology-business/",]

    def parse(self, response):
        item = get_item1(SchoolItem1)
        item['country'] = "England"
        item["website"] = "https://www.aston.ac.uk/"
        item['degree_level'] = '1'
        print("======================================")
        item['university'] = "Aston University"
        try:
            programmeDegreetype = response.xpath("//h1[@id='skiplinks']//text()").extract()
            programmeDegreetypeStr = ''.join(programmeDegreetype)
            # print(programmeDegreetypeStr)
            degree_type = re.findall(r"^\w+\s", programmeDegreetypeStr)
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)
            programme = programmeDegreetypeStr.split(''.join(degree_type))
            item['programme'] = ''.join(programme)
            # print(item['programme'])

            # 全部内容
            allcontent = response.xpath("//div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-rho']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-delta']//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-sigma'][2]//text() | //div[@class='tabbed-zone-outer oAccordionPanels tabbed-zone-upsilon']//text()").extract()
            clear_space(allcontent)
            # print(allcontent)

            # 专业描述、课程设置、就业方向、评估方向
            if "Course Outline" in allcontent:
                overviewIndex = allcontent.index("Course Outline")
            elif "Course Outline & Modules" in allcontent:
                overviewIndex = allcontent.index("Course Outline & Modules")
            elif "Course outline" in allcontent:
                overviewIndex = allcontent.index("Course outline")
            elif "Programme outline and modules" in allcontent:
                overviewIndex = allcontent.index("Programme outline and modules")
            else:
                overviewIndex = -1

            if "Subject guide and modules" in allcontent:
                modulesIndex = allcontent.index("Subject guide and modules")
            elif "Modules" in allcontent:
                modulesIndex = allcontent.index("Modules")
            elif "What you will study" in allcontent:
                modulesIndex = allcontent.index("What you will study")
            elif "Modules with Post A-Level French/German/Spanish" in allcontent:
                modulesIndex = allcontent.index("Modules with Post A-Level French/German/Spanish")
            elif "Subject Guide & Modules" in allcontent:
                modulesIndex = allcontent.index("Subject Guide & Modules")
            elif "What you will learn" in allcontent:
                modulesIndex = allcontent.index("What you will learn")
            elif "Subject guide & modules" in allcontent:
                modulesIndex = allcontent.index("Subject guide & modules")
            else:
                modulesIndex = -1

            item['overview'] = ''.join(allcontent[overviewIndex:modulesIndex-1])

            if "Professional development programme" in allcontent:
                overviewIndex1 = allcontent.index("Professional development programme")
                if "Career opportunities" in allcontent:
                    overviewIndexEnd = allcontent.index("Career opportunities")
                    item['overview'] = item['overview'] + ''.join(allcontent[overviewIndex1:overviewIndexEnd])
                else:
                    item['overview'] = item['overview'] + ''.join(allcontent[overviewIndex1:])

            if "Learning, teaching & assessment" in allcontent:
                assessmentIndex = allcontent.index("Learning, teaching & assessment")
            elif "Learning, Teaching & Assessment" in allcontent:
                assessmentIndex = allcontent.index("Learning, Teaching & Assessment")
            elif "Learning, Teaching and Assessment" in allcontent:
                assessmentIndex = allcontent.index("Learning, Teaching and Assessment")
            elif "Learning, teaching and assessment" in allcontent:
                assessmentIndex = allcontent.index("Learning, teaching and assessment")
            elif "Learning, teaching and assessments" in allcontent:
                assessmentIndex = allcontent.index("Learning, teaching and assessments")
            else:
                assessmentIndex = -1
            item['modules'] = ''.join(allcontent[modulesIndex:assessmentIndex-1])

            if "Professional development programme" in allcontent:
                assessmentIndexEnd = allcontent.index("Professional development programme")
            elif "Career Prospects" in allcontent:
                assessmentIndexEnd = allcontent.index("Career Prospects")
            elif "Professional Development Programme" in allcontent:
                assessmentIndexEnd = allcontent.index("Professional Development Programme")
            elif "Career Opportunities" in allcontent:
                assessmentIndexEnd = allcontent.index("Career Opportunities")
            elif "Career prospects" in allcontent:
                assessmentIndexEnd = allcontent.index("Career prospects")
            elif "Facilities" in allcontent:
                assessmentIndexEnd = allcontent.index("Facilities")
            elif "Your future career prospects" in allcontent:
                assessmentIndexEnd = allcontent.index("Your future career prospects")
            else:
                assessmentIndexEnd = -1
            item['teaching'] = ''.join(allcontent[assessmentIndex:assessmentIndexEnd])

            if "Career Opportunities" in allcontent:
                careerIndex = allcontent.index("Career Opportunities")
            elif "Career Prospects" in allcontent:
                careerIndex = allcontent.index("Career Prospects")
            elif "Your future" in allcontent:
                careerIndex = allcontent.index("Your future")
            elif "Career prospects" in allcontent:
                careerIndex = allcontent.index("Career prospects")
            elif "Your future career prospects" in allcontent:
                careerIndex = allcontent.index("Your future career prospects")
            elif "Careers " in allcontent:
                careerIndex = allcontent.index("Careers ")
            else:
                careerIndex = -1

            if "Fees and scholarships" in allcontent:
                careerIndexEnd = allcontent.index("Fees and scholarships")
            else:
                careerIndexEnd = -1
            item['career'] = ''.join(allcontent[careerIndex:careerIndexEnd])

            if "Entry requirements & fees" in allcontent:
                entryRequirementsIndex = allcontent.index("Entry requirements & fees")
            elif "Entry Requirements & Fees" in allcontent:
                entryRequirementsIndex = allcontent.index("Entry Requirements & Fees")
            elif "Key information for applicants & entry requirements" in allcontent:
                entryRequirementsIndex = allcontent.index("Key information for applicants & entry requirements")
            elif "Entry requirements" in allcontent:
                entryRequirementsIndex = allcontent.index("Entry requirements")
            elif "Entry Requirements" in allcontent:
                entryRequirementsIndex = allcontent.index("Entry Requirements")
            else:
                entryRequirementsIndex = -1

            if "Course outline" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Course outline")
            elif "Fees" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Fees")
            elif "Fees and Scholarships" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Fees and Scholarships")
            elif "Course Outline" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Course Outline")
            elif "Course outline" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Course outline")
            elif "Programme outline and modules" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Programme outline and modules")
            elif "Subject Guide & Modules" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Subject Guide & Modules")
            elif "Course Outline & Modules" in allcontent:
                entryRequirementsIndexEnd = allcontent.index("Course Outline & Modules")
            else:
                entryRequirementsIndexEnd = -1
            item['entry_requirements'] = ''.join(allcontent[entryRequirementsIndex:entryRequirementsIndexEnd])


            if "Duration of course:" in allcontent:
                durationIndex = allcontent.index("Duration of course:")
            elif "Duration: " in allcontent:
                durationIndex = allcontent.index("Duration: ")
            elif "Duration of programme:" in allcontent:
                durationIndex = allcontent.index("Duration of programme:")
            elif " Duration of course" in allcontent:
                durationIndex = allcontent.index(" Duration of course")
            elif " Duration of course" in allcontent:
                durationIndex = allcontent.index(" Duration of course")
            else:
                durationIndex = -1
            item['duration'] = ''.join(allcontent[durationIndex+1:durationIndex+3])

            if "Start date:" in allcontent:
                startdateIndex = allcontent.index("Start date:")
            elif "Start Date:" in allcontent:
                startdateIndex = allcontent.index("Start Date:")
            elif "Start date(s):" in allcontent:
                startdateIndex = allcontent.index("Start date(s):")
            elif "Start date: " in allcontent:
                startdateIndex = allcontent.index("Start date: ")
            else:
                startdateIndex = -1
            item['start_date'] = ''.join(allcontent[startdateIndex+1:startdateIndex+2])
            # print(item['start_date'])

            allcontentStr = ''.join(allcontent)
            feeList = re.findall(r'\d+,\d+', allcontentStr)
            for index in range(len(feeList)):
                feeList[index] = ''.join(feeList[index].split(","))
                # print(feeList[index])
            maxfee = 0
            # print(feeList)
            for fee in feeList:
                if int(fee) > maxfee:
                    maxfee = int(fee)
            item['tuition_fee'] = str(maxfee)
            # print(item['tuition_fee'])
            # print(item['start_date'])
            # print(item['overview'])
            # print(item['modules'])
            # print(item['teaching_assessment'])
            print(response.url)
            # print(item)
            # item['type'] = "Taught"
            item['url'] = response.url
            yield item
        except Exception as e:
            with open("./error/astonMastersSchoolerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
