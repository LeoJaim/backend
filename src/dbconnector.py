import sqlite3
import json

class DBConnector:

    def __init__(self):
        self.conn = None

    def __del__(self):
        self.close()
    
    def connect(self, dbname):
        self.conn = sqlite3.connect(dbname)
        return self.conn
    
    def close(self):
        self.conn.close()

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def storeJSONdata(self, jsonData):
        convertedData = json.loads(jsonData)