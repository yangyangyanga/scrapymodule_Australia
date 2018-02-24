import scrapy
import re
from scrapymodule.clearSpace import clear_space, clear_space_str
# from scrapymodule.getItem import get_item
from scrapymodule.items import SchoolItem1
from scrapymodule.getItem import get_item1

class ManchesterMastersResearchSchoolSpider(scrapy.Spider):
    name = "manchesterResearchMasters"
    url_start = "http://www.manchester.ac.uk/study/masters/courses/list/"
    url_end = ["11038/phd-astar/",
"01696/mphil-accounting-and-finance/",
"02880/phd-accounting-and-finance/",
"07004/msc-by-research-advanced-aerospace-materials-engineering/",
"08136/phd-advanced-metallic-systems-cdt/",
"06887/mphil-aerospace-engineering/",
"06437/phd-aerospace-engineering/",
"11053/mphil-animal-biology-mphil/",
"11063/phd-animal-biology-phd/",
"08459/phd-anthropology-media-and-performance/",
"05305/phd-applied-mathematics/",
"09980/phd-applied-social-research/",
"08249/phd-applied-theatre/",
"07039/phd-arab-world-studies/",
"02893/phd-archaeology/",
"05236/phd-architecture/",
"02898/phd-art-history-and-visual-studies/",
"09085/phd-arts-and-cultural-management/",
"08435/phd-arts-management-and-cultural-policy/",
"02353/msc-by-research-astronomy-and-astrophysics/",
"05482/phd-astronomy-and-astrophysics/",
"05670/mphil-atmospheric-sciences/",
"06633/msc-by-research-atmospheric-sciences/",
"05667/phd-atmospheric-sciences/",
"11032/phd-audiology/",
"11229/phd-basic-dental-sciences/",
"05685/mphil-basin-studies-and-petroleum-geoscience/",
"06637/msc-by-research-basin-studies-and-petroleum-geoscience/",
"05678/phd-basin-studies-and-petroleum-geoscience/",
"11040/phd-bbsrc-doctoral-training-partnership/",
"11043/phd-bhf-phd-programme/",
"11692/phd-bioarchaelogy-phd/",
"11054/mphil-bioarchaeology-mphil/",
"06896/mphil-biocatalysis/",
"06894/phd-biocatalysis/",
"10914/phd-mphil-biochemistry/",
"06250/phd-bioethics-and-medical-jurisprudence/",
"10916/phd-mphil-bioinformatics/",
"06767/mphil-biological-chemistry/",
"06765/phd-biological-chemistry/",
"05486/phd-biological-physics/",
"11235/phd-biomaterials-science-and-dental-technology/",
"10917/phd-mphil-biomedical-imaging-sciences/",
"06719/mphil-biomedical-materials/",
"06649/msc-by-research-biomedical-materials/",
"06717/phd-biomedical-materials/",
"11696/phd-biomolecular-science-mphil/",
"11064/phd-biomolecular-science-phd/",
"10920/phd-mphil-biostatistics/",
"10918/phd-mphil-biotechnology/",
"11118/mphil-biotechnology-mphil/",
"11065/phd-biotechnology-phd/",
"08082/mphil-business-and-management/",
"08080/phd-business-and-management/",
"10919/phd-mphil-cancer-sciences/",
"11226/phd-mphil-cardiovascular-sciences/",
"11041/cdt-regenerative-medicine/",
"10921/phd-mphil-cell-biology/",
"10940/phd-mphil-cell-matrix/",
"06723/mphil-ceramics-and-glasses/",
"06651/msc-by-research-ceramics-and-glasses/",
"06721/phd-ceramics-and-glasses/",
"03987/mphil-chemical-engineering/",
"04554/phd-chemical-engineering/",
"03991/mphil-chemical-engineering-and-analytical-science/",
"09643/msc-by-research-chemical-engineering-and-analytical-science/",
"04559/phd-chemical-engineering-and-analytical-science/",
"05962/phd-chemical-engineering-and-analytical-science-integrated/",
"07134/entd-chemistry/",
"06806/ment-chemistry/",
"01745/mphil-chemistry/",
"05903/msc-by-research-chemistry/",
"02934/phd-chemistry/",
"06089/mphil-chinese-studies/",
"06087/phd-chinese-studies/",
"01751/mphil-civil-engineering/",
"02942/phd-civil-engineering/",
"02945/phd-classics-and-ancient-history/",
"11228/phd-clinical-dentistry/",
"11031/phd-clinical-psychology/",
"10925/phd-mphil-cognitive-neuroscience/",
"06900/mphil-colloids-crystals-interfaces-and-materials/",
"06898/phd-colloids-crystals-interfaces-and-materials/",
"11033/phd-communication-disorders/",
"06653/msc-by-research-composite-materials/",
"06725/phd-composite-materials/",
"01761/mphil-computer-science/",
"02954/phd-computer-science/",
"08855/phd-computer-science-cdt/",
"11759/engd-computer-systems-engineering/",
"05490/phd-condensed-matter-physics/",
"06655/msc-by-research-corrosion-and-protection/",
"04011/mphil-corrosion-and-protection/",
"04604/phd-corrosion-and-protection/",
"08588/pd-counselling-psychology/",
"02957/phd-creative-writing/",
"08067/mphil-criminology/",
"08065/phd-criminology/",
"11761/engd-data-engineering/",
"09620/dba/",
"11230/phd-mphil-dental-health-sciences/",
"10922/phd-mphil-dermatological-sciences/",
"10923/phd-mphil-developmental-biology/",
"05228/phd-development-policy-and-management/",
"10173/clinpsyd-doctorate-in-clinical-psychology/",
"02970/phd-drama/",
"10942/phd-mphil-drug-design-development-and-delivery/",
"05693/mphil-earth-atmospheric-and-environmental-sciences/",
"05905/msc-earth-atmospheric-and-environmental-sciences/",
"05689/phd-earth-atmospheric-and-environmental-sciences/",
"08030/mphil-east-asian-studies/",
"08014/phd-east-asian-studies/",
"02976/phd-mres-economics/",
"00852/edd-education/",
"02980/phd-education/",
"06781/dedchpsy-educational-and-child-psychology/",
"04019/mphil-electrical-and-electronic-engineering/",
"04620/phd-electrical-and-electronic-engineering/",
"10924/phd-mphil-endocrinology-and-diabetes/",
"11232/phd-mphil-endodontics/",
"02988/phd-english-and-american-studies/",
"02986/phd-english-language/",
"10926/phd-mphil-environmental-biology/",
"11055/mphil-environmental-biology-mphil/",
"07932/mphil-environmental-engineering/",
"07930/phd-environmental-engineering/",
"05722/mphil-environmental-geochemistry-and-geomicrobiology/",
"06639/msc-by-research-environmental-geochemistry-and-geomicrobiology/",
"05720/phd-environmental-geochemistry-and-geomicrobiology/",
"04133/mphil-environment-and-sustainable-technology/",
"04843/phd-environment-and-sustainable-technology/",
"10927/phd-mphil-epidemiology/",
"11227/phd-mphil-evolutionary-biology/",
"11128/mphil-evolutionary-biology-mphil/",
"11090/phd-evolutionary-biology-phd/",
"11989/phd-mphil-experimental-psychology/",
"08148/phd-financial-mathematics/",
"01801/mphil-french-studies/",
"02998/phd-french-studies/",
"10398/phd-fusion-energy-cdt-mace/",
"10399/phd-fusion-energy-cdt-materials/",
"11332/phd-mphil-gastroenterology/",
"10928/phd-mphil-genetics/",
"11698/mphil-genetics-mphil/",
"11691/phd-genetics-phd/",
"10929/phd-genomics/",
"01816/mphil-german-studies/",
"03014/phd-german-studies/",
"10931/phd-mphil-health-economics/",
"10932/phd-mphil-health-informatics/",
"10933/phd-mphil-health-psychology/",
"10934/phd-mphil-health-services-and-primary-care/",
"01828/mphil-history/",
"03030/phd-history/",
"11376/phd-mphil-history-of-science-technology-and-medicine/",
"05220/phd-human-geography/",
"08245/phd-humanitarianism-and-conflict-response/",
"10935/phd-mphil-immunology/",
"10930/phd-mphil-infectious-diseases/",
"10937/phd-mphil-inflammation-sciences/",
"06771/mphil-inorganic-chemistry/",
"06769/phd-inorganic-chemistry/",
"06904/mphil-instrumentation/",
"06902/phd-instrumentation/",
"08497/phd-interpreting-studies/",
"06923/mphil-isotope-geochemistry-and-cosmochemistry/",
"06641/msc-by-research-isotope-geochemistry-and-cosmochemistry/",
"06921/phd-isotope-geochemistry-and-cosmochemistry/",
"01838/mphil-italian-studies/",
"03042/phd-italian-studies/",
"06908/mphil-japanese-studies/",
"06905/phd-japanese-studies/",
"05843/mphil-latin-american-cultural-studies/",
"05844/phd-latin-american-cultural-studies/",
"01846/mphil-law/",
"03050/phd-law/",
"03052/phd-linguistics/",
"05940/mphil-management-of-projects/",
"05939/phd-management-of-projects/",
"08235/ment-master-of-enterprise-business-and-entrepreneurship/",
"06714/mphil-materials/",
"06712/phd-materials/",
"06775/mphil-materials-chemistry/",
"06773/phd-materials-chemistry/",
"10041/phd-materials-for-demanding-environments-cdt/",
"05318/phd-mathematical-logic/",
"01852/mphil-mathematical-sciences/",
"08402/phd-mathematics-in-actuarial-science/",
"01856/mphil-mechanical-engineering/",
"03061/phd-mechanical-engineering/",
"10938/phd-mphil-medical-genetics/",
"10939/phd-mphil-medical-microbiology/",
"11027/phd-mphil-medical-mycology/",
"10946/phd-mphil-medical-virology/",
"11045/md-medicine/",
"11044/phd-mphil-medicine/",
"10943/phd-mphil-mental-health/",
"06739/mphil-metallic-materials/",
"06660/msc-by-research-metallic-materials/",
"06737/phd-metallic-materials/",
"10944/phd-mphil-microbiology/",
"11131/mphil-microbiology-mphil/",
"11095/phd-microbiology-phd/",
"01883/mphil-middle-eastern-studies/",
"03089/phd-middle-eastern-studies/",
"11048/phd-mphil-midwifery/",
"11658/phd-midwifery-4-years/",
"10945/phd-mphil-molecular-biology/",
"11702/mphil-molecular-biology-mphil/",
"11098/phd-molecular-biology-phd/",
"11039/phd-mrc-dtp-phd-programme/",
"06914/mphil-multi-scale-modelling/",
"06912/phd-multi-scale-modelling/",
"11028/phd-mphil-musculoskeletal/",
"03097/phd-museology/",
"08325/phd-museum-practice/",
"07169/phd-music-composition/",
"07170/phd-music-electroacoustic-composition/",
"07171/phd-music-musicology/",
"06743/mphil-nanostructured-materials/",
"06665/msc-by-research-nanostructured-materials/",
"06741/phd-nanostructured-materials/",
"10947/phd-mphil-neuroscience/",
"09697/msc-by-research-nonlinear-physics/",
"05496/phd-nonlinear-physics/",
"01902/mphil-nuclear-engineering/",
"03112/phd-nuclear-engineering/",
"06699/msc-by-research-nuclear-physics/",
"05505/phd-nuclear-physics/",
"05311/phd-numerical-analysis/",
"11046/phd-mphil-nursing/",
"11656/phd-nursing-4-years/",
"11034/phd-mphil-nutrition/",
"10948/phd-mphil-occupational-and-environmental-health/",
"10949/phd-mphil-ophthalmology/",
"10950/phd-mphil-optometry/",
"11236/phd-mphil-oral-and-maxillo-facial-surgery/",
"06779/mphil-organic-chemistry/",
"06777/phd-organic-chemistry/",
"11231/phd-mphil-orthodontics/",
"10951/phd-mphil-paediatric-sciences/",
"05747/mphil-palaeontology/",
"06642/msc-by-research-palaeontology/",
"05741/phd-palaeontology/",
"04098/mphil-paper-science/",
"04780/phd-paper-science/",
"06702/msc-by-research-particle-physics/",
"05510/phd-particle-physics/",
"10953/phd-mphil-pharmacology/",
"11049/phd-mphil-pharmacy-and-pharmaceutical-sciences/",
"10954/phd-mphil-pharmacy-practice/",
"03159/phd-philosophy/",
"05518/phd-photon-physics/",
"06784/mphil-physical-chemistry/",
"06782/phd-physical-chemistry/",
"05222/phd-physical-geography/",
"03161/phd-physics/",
"05758/mphil-physics-and-chemistry-of-minerals-and-fluids/",
"06646/msc-by-research-physics-and-chemistry-of-minerals-and-fluids/",
"05753/phd-physics-and-chemistry-of-minerals-and-fluids/",
"10955/phd-mphil-physiology/",
"09449/phd-planning-and-environmental-management/",
"10956/phd-mphil-plant-science/",
"11134/mphil-plant-sciences-mphil/",
"11113/phd-plant-sciences-phd/",
"06093/mphil-polish-studies/",
"06091/phd-polish-studies/",
"03016/phd-politics/",
"06755/mphil-polymer-science-and-engineering/",
"06671/msc-by-research-polymer-science-and-engineering/",
"06753/phd-polymer-science-and-engineering/",
"01958/mphil-portuguese-studies/",
"03178/phd-portuguese-studies/",
"10042/phd-power-networks-cdt/",
"08191/phd-probability/",
"04109/mphil-process-integration/",
"04801/phd-process-integration/",
"10382/dprof-project-management/",
"11233/phd-mphil-prosthodontics/",
"10958/phd-mphil-psychiatry/",
"11030/phd-mphil-psychology/",
"10959/phd-mphil-public-health/",
"05325/phd-pure-mathematics/",
"10383/dprof-reliability-engineering-and-asset-management/",
"01974/mphil-religions-and-theology/",
"03195/phd-religions-and-theology/",
"10960/phd-mphil-reproductive-sciences/",
"01978/mphil-russian-studies/",
"03201/phd-russian-studies/",
"10323/phd-science-technology-and-innovation-policy/",
"03205/phd-social-anthropology/",
"07284/phd-social-anthropology-with-visual-media/",
"02932/phd-social-statistics/",
"11047/phd-mphil-social-work/",
"11657/phd-social-work-4-years/",
"03210/phd-sociology/",
"06697/msc-by-research-soft-matter-and-liquid-crystals/",
"09722/phd-soft-matter-and-liquid-crystals-physics/",
"11760/engd-software-systems-engineering/",
"01990/mphil-spanish-studies/",
"03212/phd-spanish-studies/",
"08195/phd-statistics/",
"10961/phd-mphil-stem-cell-research/",
"05772/mphil-structural-and-petrological-geoscience/",
"05765/phd-structural-and-petrological-geoscience/",
"10962/phd-mphil-structural-biology/",
"06919/mphil-systems-biology/",
"06916/phd-systems-biology/",
"07000/msc-by-research-technical-textiles/",
"06759/mphil-textile-design-fashion-and-management/",
"06675/msc-by-research-textile-design-fashion-and-management/",
"06757/phd-textile-design-fashion-and-management/",
"07057/ment-textiles-and-fashion/",
"06763/mphil-textile-science-and-technology/",
"06677/msc-by-research-textile-science-and-technology/",
"06761/phd-textile-science-and-technology/",
"06788/mphil-theoretical-chemistry/",
"06786/phd-theoretical-chemistry/",
"06706/msc-by-research-theoretical-physics/",
"05527/phd-theoretical-physics/",
"02002/mphil-translation-and-intercultural-studies/",
"03222/phd-translation-and-intercultural-studies/",
"11138/phd-wellcome-trust-molecular-and-cell-biology/",
"11139/phd-wellcome-trust-quantitative-and-biophysical-biology/",]
    start_urls = []
    for u in url_end:
        url = url_start + u + "all-content/"
        start_urls.append(url)
    # print(len(start_urls))
    # print(start_urls)
    def parse(self, response):
        item = get_item1(SchoolItem1)
        item['country'] = "England"
        item["website"] = "https://www.manchester.ac.uk/"
        item['degree_level'] = '1'
        item['university'] = "University of Manchester"
        print("===========================")
        try:
            # 专业、学位类型
            programmeDegree = response.xpath("//div[@id='course-profile']/div[@class='heading']/h1//text()").extract()
            clear_space(programmeDegree)
            programmeDegreeStr = ''.join(programmeDegree)
            print(programmeDegreeStr)
            degree_type = list(re.findall(r"^(\w{0,6})|(\w{0,6}/\w{0,6})\s", programmeDegreeStr)[0])
            while '' in degree_type:
                degree_type.remove('')
            # print("degree_type = ", degree_type)
            item['degree_type'] = ''.join(degree_type)
            programme = programmeDegreeStr.split(''.join(degree_type))
            # print(programme[-1])
            item['programme'] = programme[-1]

            duration = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[2]//text()").extract()
            item['duration'] = ''.join(duration)

            other = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/div[@class='fact-file']/dl/dd[@class='how-to-apply']//text()").extract()
            item['other'] = ''.join(other)

            # //div[@id='course-profile']/div[@class='course-profile-content full-page']
            # 专业描述，雅思托福，就业方向, 学术要求，How To Apply
            allcontent = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']//text()").extract()
            clear_space(allcontent)
            print(allcontent)
            if "Programme overview" in allcontent:
                overviewIndex = allcontent.index("Programme overview")
                if "Open days" in allcontent:
                    overviewIndexEnd = allcontent.index("Open days")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd-1])
                elif "Fees" in allcontent:
                    overviewIndexEnd = allcontent.index("Fees")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd - 1])

            elif "Programme description" in allcontent:
                overviewIndex = allcontent.index("Programme description")
                if "Open days" in allcontent:
                    overviewIndexEnd = allcontent.index("Open days")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd-1])
                elif "Fees" in allcontent:
                    overviewIndexEnd = allcontent.index("Fees")
                    item['overview'] = ''.join(allcontent[overviewIndex:overviewIndexEnd - 1])
            # print(item['overview'])

            # //div[@id='contact-details-container']/dl/dd[@class='department']/a
            department = response.xpath("//div[@id='contact-details-container']/dl/dd[@class='department']/a//text()").extract()
            item['department'] = ''.join(department)

            # Entry requirements
            howtoapplyIndex = -1
            if "Application and selection" in allcontent:
                howtoapplyIndex = allcontent.index("Application and selection")
            if "Entry requirements" in allcontent:
                entryrequirementsIndex = allcontent.index("Entry requirements")
                item['entry_requirements'] = ''.join(allcontent[entryrequirementsIndex:howtoapplyIndex-1])
            modulesIndex = -1
            if "Programme details" in allcontent:
                modulesIndex = allcontent.index("Programme details")
            item['how_to_apply'] = ''.join(allcontent[howtoapplyIndex:modulesIndex-1])

            if "Careers" in allcontent:
                careerIndex = allcontent.index("Careers")
                item['career'] = ''.join(allcontent[careerIndex:])
                item['modules'] = ''.join(allcontent[modulesIndex:careerIndex-1])
            else:
                item['modules'] = ''.join(allcontent[modulesIndex:])

            if "English language" in allcontent:
                ieltsIndex = allcontent.index("English language")
                if "English language test validity" in allcontent:
                    ieltsIndexEnd = allcontent.index("English language test validity")
                    item['IELTS'] = ''.join(allcontent[ieltsIndex:ieltsIndexEnd])
                else:
                    item['IELTS'] = ''.join(allcontent[ieltsIndex:howtoapplyIndex])

            if "Interview requirements" in allcontent:
                interviewIndex = allcontent.index("Interview requirements")
                if "Re-applications" in allcontent:
                    interviewIndexEnd = allcontent.index("Re-applications")
                    item['interview'] = ''.join(allcontent[interviewIndex:interviewIndexEnd])
                else:
                    item['interview'] = ''.join(allcontent[interviewIndex:modulesIndex])
            print(item['interview'])
            # item['type'] = "Research"
            fee1 = response.xpath("//div[@id='course-profile']/div[@class='course-profile-content full-page']/ul[1]/li[1]//text()").extract()
            fee1 = ''.join(fee1)
            fee = clear_space_str(fee1)
            item['tuition_fee'] = ''.join(fee)

            item['url'] = response.url
            print(response.url)
            # print(item)
            yield item
        except Exception as e:
            with open("./error/manchesterMastersResearchSchoolerror.txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)
