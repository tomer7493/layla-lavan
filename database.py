from datetime import datetime
import sqlite3


class riddle_db:
    def __init__(self, path="\\", tablename="riddle_db", answer_col="answer",riddle_col="riddle"):
        self.path = path
        self.tablename = tablename
        self.answer_col = answer_col
        self.riddle_col =riddle_col
        conn = sqlite3.connect(self.path)
        conn.execute(
            f'CREATE TABLE IF NOT EXISTS {self.tablename} (id INTEGER PRIMARY KEY, {self.answer_col} STRING,{self.riddle_col} STRING)')
        conn.commit()
        conn.close()

    def add_riddle(self, riddle,answer:str):
        conn = sqlite3.connect(self.path)
        str_insert = f"INSERT INTO {self.tablename} ({self.riddle_col},{self.answer_col}) VALUES ('{riddle}','{answer}')"
        try:
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    
    def get_answer_by_riddle(self,riddle:str):
        conn = sqlite3.connect(self.path)
        cursor = conn.execute(
            f"SELECT * FROM {self.tablename} WHERE {self.riddle_col} = '{riddle}'")
        data = cursor.fetchall()
        conn.close()
        print("db sent: ",data[0])
        return data[0]
    
    def get_answer_by_number_id(self,riddle_id:int):
        conn = sqlite3.connect(self.path)
        cursor = conn.execute(
            f"SELECT * FROM {self.tablename} WHERE id = '{riddle_id}'")
        data = cursor.fetchall()
        conn.close()
        print("db sent: ",data[0])
        return data[0]
