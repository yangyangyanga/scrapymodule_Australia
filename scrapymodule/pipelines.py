# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapymodule.insert_mysql import InsertMysql

class BristolMasterSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, degree_type, start_date, " \
              "overview, duration, modules, career, deadline, tuition_fee, location, Rntry_requirements, IELTS, " \
              "URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s) on duplicate key update university=VALUES(university), department=VALUES(department), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),start_date=VALUES(start_date), " \
              "overview=VALUES(overview),duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), " \
              "deadline=VALUES(deadline), tuition_fee=VALUES(tuition_fee), location=VALUES(location)," \
              "Rntry_requirements=VALUES(Rntry_requirements), IELTS=VALUES(IELTS), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['department'], item['programme'], item['degree_type'], item['start_date'],
                                      item['overview'], item['duration'], item['modules'], item['career'], item['deadline'],
                                      item['tuition_fee'], item['location'], item['Rntry_requirements'], item['IELTS'], item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class StrathMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, programme, degree_type, start_date, " \
              "overview, type,duration,  modules, teaching_assessment, career, deadline, tuition_fee, Rntry_requirements, IELTS, " \
              "other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s) on duplicate key update university=VALUES(university), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),start_date=VALUES(start_date), " \
              "overview=VALUES(overview),type=VALUES(type),duration=VALUES(duration), modules=VALUES(modules), teaching_assessment=VALUES(teaching_assessment),career=VALUES(career), " \
              "deadline=VALUES(deadline), tuition_fee=VALUES(tuition_fee), " \
              "Rntry_requirements=VALUES(Rntry_requirements), IELTS=VALUES(IELTS),other=VALUES(other), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['programme'], item['degree_type'], item['start_date'],
                                      item['overview'], item['type'], item['duration'], item['modules'], item['teaching_assessment'], item['career'], item['deadline'],
                                      item['tuition_fee'], item['Rntry_requirements'], item['IELTS'], item['other'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class ManchesterMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, programme, degree_type, " \
              "overview, type, duration, modules,  career, tuition_fee, IELTS,interview, how_to_apply," \
              "entry_requirements, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
              "%s, %s, %s, %s) on duplicate key update university=VALUES(university), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type), " \
              "overview=VALUES(overview),type=VALUES(type),duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), " \
              "tuition_fee=VALUES(tuition_fee), " \
              "IELTS=VALUES(IELTS),interview=VALUES(interview),how_to_apply=VALUES(how_to_apply),entry_requirements=VALUES(entry_requirements),other=VALUES(other), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['programme'], item['degree_type'],
                                      item['overview'],  item['type'],item['duration'], item['modules'], item['career'],
                                      item['tuition_fee'],item['IELTS'], item['interview'],item['how_to_apply'],item['entry_requirements'],item['other'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class KingsMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university,department, programme, degree_type, " \
              "overview, mode, duration, modules,  career, deadline, application_fee, tuition_fee," \
              "Rntry_requirements, average_score, IELTS, application_documents, " \
              "entry_requirements, URL) values( %s, %s, %s,  %s, %s, %s, %s, %s, %s,  %s, %s, %s," \
              "%s, %s, %s, %s,  %s, %s) on duplicate key update university=VALUES(university), department=VALUES(department), " \
              "programme=VALUES(programme), degree_type=VALUES(degree_type),overview=VALUES(overview)," \
              "mode=VALUES(mode), duration=VALUES(duration), modules=VALUES(modules), career=VALUES(career), deadline=VALUES(deadline)," \
              "application_fee=VALUES(application_fee),tuition_fee=VALUES(tuition_fee),Rntry_requirements=VALUES(Rntry_requirements), " \
              "average_score=VALUES(average_score)," \
              "IELTS=VALUES(IELTS),application_documents=VALUES(application_documents)," \
              "entry_requirements=VALUES(entry_requirements), URL=VALUES(URL)"
        try:
            self.cursor.execute(sql,(item['university'], item['department'], item['programme'], item['degree_type'],
                                      item['overview'],  item['mode'],item['duration'], item['modules'], item['career'],item['deadline'], item['application_fee'],
                                      item['tuition_fee'],item['Rntry_requirements'],item['average_score'],item['IELTS'],
                                     item['application_documents'],item['entry_requirements'],item['URL']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class ManchesterMastersResearchSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class StrathMastersResearchSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

class AstonMastersSchoolPipeline(InsertMysql):
    def process_item(self, item, spider):
        sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
              "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
              "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
              "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
              "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
              "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
              "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
              " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
              "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
              "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
              "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
              "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
              "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
              "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
              " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
              "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
              "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
        try:
            self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
                                      item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
                                      item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
                                      item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
                                      item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
                                      item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
                                      item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
                                      item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
                                      item["ACT"], item["ACT_code"], item["other"], item["URL"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as e:
            self.db.rollback()
            print("数据插入失败：%s" % (str(e)))
        # self.close()
        return item

# class AstonMastersSchoolPipeline(InsertMysql):
#     def process_item(self, item, spider):
#         sql = "insert into hooli(university, department, programme, ucas_code, degree_type, start_date, overview, mode, " \
#               "type, duration, modules, teaching_assessment, career, application_date, deadline, application_fee, " \
#               "tuition_fee, location, Rntry_requirements, GPA, average_score, accredited_university, Alevel, IB, IELTS, " \
#               "TOEFL, GRE, GMAT, working_experience, interview, portfolio, application_documents, how_to_apply, entry_requirements, " \
#               "school_test, description_degree, SATI, SATII, SAT_code, ACT, ACT_code, other, URL) values(%s, %s, %s, %s, %s, %s, %s, %s, " \
#               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
#               "%s, %s, %s, %s) on duplicate key update university =VALUES(university), department =VALUES(department), " \
#               "programme =VALUES(programme), ucas_code =VALUES(ucas_code), degree_type =VALUES(degree_type), " \
#               "start_date =VALUES(start_date), overview =VALUES(overview), mode =VALUES(mode), type =VALUES(type)," \
#               " duration =VALUES(duration), modules =VALUES(modules), teaching_assessment =VALUES(teaching_assessment), " \
#               "career =VALUES(career), application_date =VALUES(application_date), deadline =VALUES(deadline), " \
#               "application_fee =VALUES(application_fee), tuition_fee =VALUES(tuition_fee), location =VALUES(location), " \
#               "Rntry_requirements =VALUES(Rntry_requirements), GPA =VALUES(GPA), average_score =VALUES(average_score), " \
#               "accredited_university =VALUES(accredited_university), Alevel =VALUES(Alevel), IB =VALUES(IB), IELTS =VALUES(IELTS), " \
#               "TOEFL =VALUES(TOEFL), GRE =VALUES(GRE), GMAT =VALUES(GMAT), working_experience =VALUES(working_experience), " \
#               "interview =VALUES(interview), portfolio =VALUES(portfolio), application_documents =VALUES(application_documents)," \
#               " how_to_apply =VALUES(how_to_apply), entry_requirements =VALUES(entry_requirements), school_test =VALUES(school_test), " \
#               "description_degree =VALUES(description_degree), SATI =VALUES(SATI), SATII =VALUES(SATII), SAT_code =VALUES(SAT_code), " \
#               "ACT =VALUES(ACT), ACT_code =VALUES(ACT_code), other =VALUES(other), URL =VALUES(URL)"
#         try:
#             self.cursor.execute(sql, (item["university"], item["department"], item["programme"], item["ucas_code"], item["degree_type"],
#                                       item["start_date"], item["overview"], item["mode"], item["type"], item["duration"], item["modules"],
#                                       item["teaching_assessment"], item["career"], item["application_date"], item["deadline"],
#                                       item["application_fee"], item["tuition_fee"], item["location"], item["Rntry_requirements"],
#                                       item["GPA"], item["average_score"], item["accredited_university"], item["Alevel"], item["IB"],
#                                       item["IELTS"], item["TOEFL"], item["GRE"], item["GMAT"], item["working_experience"], item["interview"],
#                                       item["portfolio"], item["application_documents"], item["how_to_apply"], item["entry_requirements"],
#                                       item["school_test"], item["description_degree"], item["SATI"], item["SATII"], item["SAT_code"],
#                                       item["ACT"], item["ACT_code"], item["other"], item["URL"]))
#             self.db.commit()
#         except Exception as e:
#             self.db.rollback()
#             with open("./error/astonMastersSchoolMysqlerror.txt", 'a+', encoding="utf-8") as f:
#                 f.write(str(e) + "\n========================")
#             print("数据插入失败：%s" % (str(e)))
#         # self.close()
#         return item