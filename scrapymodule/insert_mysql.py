import pymysql

class InsertMysql():
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '123456', 'englandben', charset='utf8')
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()
