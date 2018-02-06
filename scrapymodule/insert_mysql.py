import pymysql

class InsertMysql():
    def __init__(self):
        # self.db = pymysql.connect('localhost', 'root', '123456', 'englandben', charset='utf8')
        self.db = pymysql.connect('192.168.3.195', 'root', '521797', 'pythonnb', charset='utf8')
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()
