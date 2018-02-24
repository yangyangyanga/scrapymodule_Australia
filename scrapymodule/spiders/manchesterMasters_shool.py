import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
from scrapymodule.items import SchoolItem1
from scrapymodule.getItem import get_item1

class ManchesterMastersSchoolSpider(scrapy.Spider):
    name = "manchesterMasters"
    url_start = "http://www.manchester.ac.uk/study/masters/courses/list/"
    url_end = ["10867/msc-accounting/",
"02061/msc-accounting-and-finance/",
"08339/msc-acs-advanced-web-technologies/",
"08342/msc-acs-artificial-intelligence/",
"08343/msc-acs-computer-security/",
"08344/msc-acs-computer-systems-engineering/",
"08345/msc-acs-data-and-knowledge-management/",
"08346/msc-acs-digital-biology/",
"08351/msc-acs-multi-core-computing/",
"08353/msc-acs-semantic-technologies/",
"08354/msc-acs-software-engineering/",
"09304/msc-acswitm-information-management/",
"08603/msc-actuarial-science/",
"08540/msc-pgdip-advanced-audiology-studies/",
"07354/msc-advanced-chemical-engineering/",
"11815/msc-advanced-clinical-practice-paediatric-anaesthesia/",
"10227/pg-credit-advanced-clinical-skills-short-course/",
"02069/msc-advanced-computer-science/",
"02066/msc-advanced-computer-science-and-it-management/",
"09203/mres-advanced-computer-science-mres/",
"04166/msc-advanced-control-and-systems-engineering/",
"09718/msc-advanced-electrical-power-systems-engineering/",
"04169/msc-advanced-engineering-materials/",
"11763/msc-advanced-general-dental-practice/",
"04172/msc-advanced-manufacturing-technology-and-systems-management/",
"10084/msc-advanced-midwifery-practice-and-leadership/",
"10083/msc-advanced-nursing-practice-and-leadership/",
"09760/msc-advanced-process-integration-and-design/",
"10082/msc-advanced-professional-practice-and-leadership/",
"10085/msc-advanced-social-work-practice-and-leadership/",
"10202/pgcert-advanced-specialist-training-in-emergency-medicine/",
"08025/msc-aerospace-engineering/",
"01086/ma-anthropological-research/",
"06051/msc-apimh-psychosocial-interventions-for-psychosis-cope/",
"09128/msc-applied-mathematics/",
"09342/march-architecture/",
"07785/ma-architecture-and-urbanism/",
"01100/ma-art-gallery-and-museum-studies/",
"08035/ma-arts-management-policy-and-practice/",
"02087/msc-audiology/",
"08171/msc-biochemistry/",
"08854/msc-bioinformatics-and-systems-biology/",
"02036/mres-biological-sciences/",
"08839/msc-biomaterials/",
"07778/msc-biotechnology-and-enterprise/",
"01039/mba-business-administration/",
"09839/msc-business-analysis-and-strategic-management/",
"09454/msc-business-analytics-operational-research-and-risk-analysis/",
"09994/msc-business-psychology/",
"11833/msc-pgdip-pgcert-cancer-biology-and-radiotherapy-physics/",
"08861/msc-cancer-research-and-molecular-biomedicine/",
"08934/mres-cardiovascular-health-and-disease/",
"08168/msc-cell-biology/",
"11707/msc-chemical-food-safety-and-integrity/",
"08492/msc-chemistry/",
"07915/ma-classics-and-ancient-history/",
"08070/msc-clinical-and-health-psychology/",
"02113/msc-clinical-biochemistry/",
"11762/msc-clinical-dentistry-paediatric-dentistry/",
"09859/msc-clinical-immunology/",
"09892/msc-clinical-pharmacy/",
"11951/clinical-pharmacy-cpd/",
"08175/mclin-res-clinical-research/",
"02120/msc-clinical-rheumatology-and-musculoskeletal-medicine/",
"04201/msc-commercial-project-management/",
"12034/msc-communications-and-signal-processing/",
"10164/musm-composition-electroacoustic-music-and-interactive-media/",
"10163/musm-composition-instrumental-and-vocal-music/",
"08505/ma-pgdip-conference-interpreting/",
"04218/msc-construction-project-management/",
"05861/llm-corporate-governance/",
"04229/msc-corrosion-control-engineering/",
"01125/ma-creative-writing/",
"09778/ma-criminology/",
"09782/mres-criminology/",
"09780/pgdip-criminology/",
"10377/mres-criminology-social-statistics/",
"11424/msc-data-science/",
"08632/msc-pgdip-deaf-education/",
"06052/msc-dementia-care-apimh/",
"05989/msc-pgdip-pgcert-dental-implantology-dental-specialties/",
"08238/mres-dental-public-health/",
"08237/msc-dental-public-health-mdph/",
"08166/msc-developmental-biology/",
"06012/msc-development-economics-and-policy/",
"06537/msc-development-finance/",
"06954/ma-digital-technologies-communication-and-education/",
"08084/ma-economics/",
"01380/msc-economics/",
"08293/ma-education-international/",
"08289/ma-educational-leadership/",
"09719/ma-educational-leadership-part-time/",
"07875/msc-electrical-power-systems-engineering/",
"10408/msc-electrical-power-systems-engineering-distance-learning/",
"07772/msc-clin-endodontics/",
"02147/msc-endodontics-dental-specialties/",
"04259/msc-engineering-project-management/",
"11541/ma-english-literature-and-american-studies/",
"06967/msc-environmental-governance/",
"09424/msc-environmental-impact-assessment-and-management/",
"02180/msc-environmental-monitoring-modelling-and-reconstruction/",
"02618/pgdip-ethics/",
"10368/msc-evidence-based-health-care/",
"11664/evidence-based-healthcare-cpd/",
"10146/mres-experimental-cancer-medicine/",
"10153/ma-film-studies/",
"01383/msc-finance/",
"07946/msc-financial-economics/",
"07770/msc-clin-fixed-and-removable-prosthodontics/",
"02149/msc-fixed-and-removable-prosthodontics-dental-specialties/",
"09847/msc-forensic-psychology-and-mental-health/",
"01167/ma-gender-sexuality-and-culture/",
"10140/msc-genomic-medicine/",
"07053/msc-geographical-information-science/",
"09105/pgcert-global-health/",
"08212/msc-global-urban-development-and-planning/",
"08181/mres-pgdip-pgcert-health-and-social-care/",
"02618/pgdip-healthcare/",
"09218/pgcert-healthcare-ethics-distance-learning/",
"09213/llm-healthcare-ethics-and-law/",
"01180/ma-healthcare-ethics-and-law/",
"09215/llm-healthcare-ethics-and-law-distance-learning/",
"01203/ma-healthcare-ethics-and-law-distance-learning/",
"02498/pgdip-healthcare-ethics-and-law-distance-learning/",
"07880/msc-healthcare-ethics-and-law-intercalated/",
"02618/pgdip-healthcare-ethics-and-law-postgraduate-diploma/",
"09216/pgcert-healthcare-ethics-postgraduate-certificate/",
"09221/pgcert-healthcare-law-distance-learning/",
"09219/pgcert-healthcare-law-postgraduate-certificate/",
"10076/msc-health-data-science/",
"10060/msc-health-psychology/",
"12035/ma-heritage-studies/",
"01197/ma-history/",
"05966/msc-history-of-science-technology-and-medicine-including-medical-humanities-award-route/",
"08264/ma-humanitarianism-and-conflict-response/",
"07862/msc-human-resource-development-international-development/",
"07866/msc-human-resource-management-international-development/",
"06727/msc-human-resource-management-and-development-international-development-by-distance-learning/",
"02222/msc-human-resource-management-and-industrial-relations/",
"06158/ma-human-rights-law-political-science-pathway-research-route/",
"06160/ma-human-rights-law-political-science-pathway-standard-route/",
"06159/ma-human-rights-political-science-research-route/",
"01362/ma-human-rights-political-science-standard-route/",
"06237/msc-icts-for-development/",
"09815/independent-prescribing-short-course/",
"09170/informatics-for-healthcare-systems-improving-skills-for-patient-driven-healthcare/",
"08199/msc-innovation-management-and-entrepreneurship/",
"01061/llm-intellectual-property-law/",
"08815/ma-intercultural-communication/",
"07991/llm-international-business-and-commercial-law/",
"10364/msc-international-business-and-management-management/",
"09891/msc-international-development/",
"09887/msc-international-development-development-management/",
"09890/msc-international-development-environment-climate-change-and-development/",
"09885/msc-international-development-globalisation-trade-and-industry/",
"09886/msc-international-development-politics-governance-and-development-policy/",
"09888/msc-international-development-poverty-inequality-and-development/",
"09889/msc-international-development-poverty-conflict-and-reconstruction/",
"01211/msc-international-development-public-policy-and-management/",
"09910/msc-international-disaster-management/",
"09907/msc-international-fashion-marketing/",
"04317/msc-international-fashion-retailing/",
"07689/msc-international-fashion-retailing-business-process-improvement/",
"09053/msc-international-fashion-retailing-multichannel-marketing/",
"01060/llm-international-financial-law/",
"07065/msc-international-human-resource-management-and-comparative-industrial-relations/",
"10877/ma-international-political-economy-research/",
"10876/ma-international-political-economy-standard/",
"10873/ma-international-relations-research/",
"10872/ma-international-relations-standard/",
"07796/llm-international-trade-transactions/",
"08335/msc-investigative-ophthalmology-and-vision-science/",
"08446/llm-law/",
"02618/pgdip-law/",
"01233/ma-linguistics/",
"02059/mres-management/",
"08633/msc-management/",
"02242/msc-management-and-implementation-of-development-projects/",
"01388/msc-management-and-information-systems-change-and-development/",
"08003/msc-management-and-information-systems-change-and-development-distance-learning/",
"04332/msc-management-of-projects/",
"08504/-manchester-global-mba/",
"08502/-manchester-global-mba-finance-accelerated/",
"02247/msc-marketing/",
"02250/msc-mathematical-finance/",
"04342/msc-mechanical-engineering-design/",
"09164/msc-medical-education/",
"10263/msc-pgdip-medical-imaging-science/",
"08939/msc-medical-microbiology/",
"02052/mres-medical-sciences/",
"08965/msc-medical-virology/",
"10132/ma-medieval-and-early-modern-studies/",
"08749/msc-model-based-drug-development/",
"11543/ma-modern-and-contemporary-literature/",
"11966/ma-modern-languages-and-cultures/",
"10418/msc-molecular-pathology/",
"10159/musm-music-ethnomusicology/",
"10158/musm-music-musicology/",
"11998/msc-nanomaterials/",
"09754/msc-neuroimaging-for-clinical-and-cognitive-neuroscience/",
"08173/msc-neuroscience/",
"02275/msc-nuclear-science-and-technology/",
"07884/msc-occupational-hygiene/",
"07886/msc-occupational-medicine/",
"08422/mres-oncology/",
"07783/msc-operations-project-and-supply-chain-management/",
"07776/msc-clin-oral-and-maxillofacial-surgery/",
"02152/msc-pgdip-oral-and-maxillofacial-surgery-dental-specialties/",
"02303/msc-organisational-change-and-development/",
"02302/msc-organisational-psychology/",
"07773/msc-clin-orthodontics/",
"09784/ma-peace-and-conflict-studies/",
"08444/msc-clin-periodontology/",
"02873/msc-petroleum-exploration-geoscience/",
"08708/msc-petroleum-geoscience-for-reservoir-development-and-production/",
"02846/pgce-primary/",
"09289/pgce-primary-school-direct-5-11/",
"11649/pgce-secondary-geography/",
"11650/pgce-secondary-history/",
"02860/pgce-secondary-business-education/",
"02849/pgce-secondary-chemistry/",
"10367/pgce-secondary-economics-and-business-education/",
"02853/pgce-secondary-english/",
"02854/pgce-secondary-french/",
"02855/pgce-secondary-german/",
"02857/pgce-secondary-mathematics/",
"02858/pgce-secondary-physics/",
"09171/pgce-secondary-physics-with-maths/",
"09324/pgce-secondary-school-direct-english/",
"09325/pgce-secondary-school-direct-mathematics/",
"09322/pgce-secondary-school-direct-business-education-14-19/",
"09319/pgce-secondary-school-direct-science-biology-11-16-or-11-18/",
"09320/pgce-secondary-school-direct-science-chemistry-11-16-or-11-18/",
"09321/pgce-secondary-school-direct-science-physics-11-16-or-11-18/",
"02848/pgce-secondary-science-biology/",
"02859/pgce-secondary-spanish/",
"09123/msc-pharmaceutical-industrial-advanced-training-piat/",
"09912/msc-pharmaceutical-technology-and-quality-assurance/",
"10048/ma-philosophy/",
"10279/pgdip-physician-associate-studies/",
"09421/msc-planning/",
"07048/ma-political-economy-research-route/",
"06969/ma-political-economy-standard-route/",
"07237/ma-political-science-democracy-and-elections-research-route/",
"07236/ma-political-science-democracy-and-elections-standard-route/",
"06166/ma-political-science-european-politics-and-policy-pathway--research-route/",
"06169/ma-political-science-european-politics-and-policy-pathway-standard-route/",
"06167/ma-political-science-governance-and-public-policy-pathway-research-route/",
"06171/ma-political-science-governance-and-public-policy-pathway-standard-route/",
"10231/ma-political-science-philosophy-and-political-theory/",
"06168/ma-political-science-political-theory-pathway-research-route/",
"06172/ma-political-science-political-theory-pathway-standard-route/",
"01177/ma-politics/",
"02325/msc-pollution-and-environmental-control/",
"04380/msc-polymer-materials-science-and-engineering/",
"09978/pgcert-postgraduate-certificate-approved-mental-health-professional-practice/",
"09326/postgraduate-certificate-in-education-secondary-school-direct-french/",
"09803/postgraduate-certificate-in-education-secondary-school-direct-geography/",
"09327/postgraduate-certificate-in-education-secondary-school-direct-german/",
"09799/postgraduate-certificate-in-education-secondary-school-direct-history/",
"09318/postgraduate-certificate-in-education-secondary-school-direct-physics-with-maths/",
"09328/postgraduate-certificate-in-education-secondary-school-direct-spanish/",
"05994/mres-primary-care-web-based-learning/",
"06050/msc-pgdip-primary-mental-health-care-pathway-apimh/",
"04392/msc-project-management/",
"11182/msc-pgdip-pgcert-project-management/",
"02055/mres-psychology/",
"01527/med-psychology-of-education/",
"06002/mph-public-health-web-based-learning/",
"05995/mres-public-health-web-based-learning/",
"09644/llm-public-international-law/",
"09110/msc-pure-mathematics-and-mathematical-logic/",
"10251/msc-quantitative-finance/",
"09634/msc-real-estate-asset-management/",
"09632/msc-real-estate-development/",
"10005/msc-real-estate-distance-learning/",
"09822/msc-reliability-engineering-and-asset-management/",
"11899/msc-reliability-engineering-and-asset-management-dubai/",
"01297/ma-religions-and-theology/",
"09009/msc-renewable-energy-and-clean-technology/",
"10058/mres-reproduction-and-pregnancy/",
"11841/msc-research-methods-with-education/",
"11843/msc-research-methods-with-human-geography/",
"11845/msc-research-methods-with-international-development/",
"11847/msc-research-methods-with-planning-and-environmental-management/",
"08327/pgdip-restorative-and-aesthetic-dentistry/",
"10022/msc-science-communication/",
"09832/ma-screenwriting/",
"09658/llm-security-and-international-law/",
"09660/ma-security-and-international-law/",
"09805/msc-skin-ageing-and-aesthetic-medicine/",
"01311/ma-social-anthropology/",
"08515/ma-social-anthropology-culture-ethnography-and-development-pathway/",
"08518/ma-social-anthropology-visual-and-sensory-media-pathway/",
"06097/msc-social-research-methods-and-statistics/",
"01315/ma-social-work/",
"02356/msc-sociological-research/",
"01317/ma-sociology/",
"10985/msc-specialist-practice-cancer/",
"02362/msc-statistics/",
"04410/msc-structural-engineering/",
"11610/pgcert-teaching-and-learning-in-biology-medicine-and-health-sciences/",
"01367/ma-tesol/",
"08611/msc-textile-technology-technical-textiles/",
"11136/mba-the-kelley-manchester-global-mba/",
"04435/msc-thermal-power-and-fluid-engineering/",
"06439/mres-tissue-engineering-for-regenerative-medicine/",
"07290/mres-translational-medicine-interdisciplinary-molecular-medicine/",
"07006/ma-translation-and-interpreting-studies/",
"09646/llm-transnational-dispute-resolution/",
"09915/msc-urban-design-and-international-planning/",
"09505/msc-urban-regeneration-and-development/",
"10029/ma-visual-anthropology/",]
    start_urls = []
    for u in url_end:
        url = url_start + u + "all-content/"
        start_urls.append(url)
    # print(len(start_urls))
    def parse(self, response):
        item = get_item1(SchoolItem1)
        item['country'] = "England"
        item["website"] = "https://www.manchester.ac.uk/"
        item['degree_level'] = '1'
        item['university'] = "University of Manchester"
        # print("===========================")
        try:
            # print(response.url)
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='course-profile']/div[@class='heading']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            # print(programmeDegreeStr)
            degree_type = list(re.findall(r"^(\w{0,6})|(\w{0,6}/\w{0,6})\s", programmeDegreeStr)[0])
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)
            programme = programmeDegreeStr.split(''.join(degree_type))
            item['programme'] = programme[-1]

            duration = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[2]//text()").extract()
            item['duration'] = ''.join(duration)

            other = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[@class='how-to-apply']//text()").extract()
            item['other'] = ''.join(other)

            # //div[@id='course-profile']/div[@class='course-profile-content full-page']
            # 专业描述，雅思托福，就业方向, 学术要求，How To Apply
            item['overview'] = ''
            item['IELTS'] = ''
            item['career'] = ''
            allcontent = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']//text()").extract()
            clear_space(allcontent)
            # print(allcontent)
            if "Course overview" in allcontent:
                overviewIndex = allcontent.index("Course overview")
                if "Open days" in allcontent:
                    overviewIndexEnd = allcontent.index("Open days")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd-1])
            elif "Course description" in allcontent:
                overviewIndex = allcontent.index("Course description")
                if "Fees" in allcontent:
                    overviewIndexEnd = allcontent.index("Fees")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd-1])

            item['entry_requirements'] = ''
            item['how_to_apply'] = ''
            item['modules'] = ''
            item['career'] = ''
            item['IELTS'] = ''
            # Entry requirements
            howtoapplyIndex = -1
            if "Application and selection" in allcontent:
                howtoapplyIndex = allcontent.index("Application and selection")
            if "Entry requirements" in allcontent:
                entryrequirementsIndex = allcontent.index("Entry requirements")
            item['entry_requirements'] = ''.join(allcontent[entryrequirementsIndex:howtoapplyIndex-1])
            modulesIndex = -1
            if "Course details" in allcontent:
                modulesIndex = allcontent.index("Course details")
            item['how_to_apply'] = ''.join(allcontent[howtoapplyIndex:modulesIndex-1])

            careerIndex = -1
            if "Careers" in allcontent:
                careerIndex = allcontent.index("Careers")
            item['modules'] = ''.join(allcontent[modulesIndex:careerIndex-1])
            item['career'] = ''.join(allcontent[careerIndex:])

            if "English language" in allcontent:
                ieltsIndex = allcontent.index("English language")
                if "English language test validity" in allcontent:
                    ieltsIndexEnd = allcontent.index("English language test validity")
                    item['IELTS'] = ''.join(allcontent[ieltsIndex:ieltsIndexEnd])

            item['interview'] = ''
            if "Interview requirements" in allcontent:
                interviewIndex = allcontent.index("Interview requirements")
                if "Fitness to practise / health requirements" in allcontent:
                    interviewIndexEnd = allcontent.index("Fitness to practise / health requirements")
                    item['interview'] = ''.join(allcontent[interviewIndex:interviewIndexEnd])
                else:
                    item['interview'] = ''.join(allcontent[interviewIndex:modulesIndex])
            # item['type'] = "Taught"
            fee1 = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/ul[1]/li[1]//text()").extract()
            fee1 = ''.join(fee1)
            fee = clear_space_str(fee1)
            item['tuition_fee'] = ''.join(fee)

            item['url'] = response.url
            # print(response.url)
            yield item
        except Exception as e:
            with open("manchesterMastersSchoolerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
