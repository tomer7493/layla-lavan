import socket
import time
import random
import database as db

class Server:
    def __init__(self):
        self.server_socket=self.server_socket = socket.socket()
        self.server_socket.bind(("0.0.0.0", 8820))
        self.server_socket.listen()
        self.riddle_counter = 1
        self.group_id = 5 
        print("Server is up and running")
        (self.client_socket, self.client_address) = self.server_socket.accept()
        print("Client connected")
        self.db = db.riddle_db("try.db")
        self.db.add_riddle("who","yes")
        self.db.add_riddle("is","tru")
        self.db.add_riddle("broshi","ok")
        self.db.add_riddle("wtf","lol")
        self.handle_client()
    
    def handle_client(self):
        while(True):
            raw_data = self.client_socket.recv(1024).decode() 
            raw_data= raw_data.split("\r\n")   
            cmd = raw_data[0]
            data = raw_data[2]
            #
            if cmd == "Start":
                data = self.db.get_answer_by_number_id(self.riddle_counter)[2]
                
            elif cmd == "Answer":
                print("the data is: ", data)
                print("the db is: ",self.db.get_answer_by_number_id(self.riddle_counter)[1])
                if (self.db.get_answer_by_number_id(self.riddle_counter)[1] == data):
                    self.riddle_counter+=1
                    cmd = "NextTask"
                else:
                    cmd = "TryAgain"    
                data = self.db.get_answer_by_number_id(self.riddle_counter)[2]
                
            
            else:
                cmd = "wrong input"
            print("Client sent: " + cmd)
            self.send_msg(cmd, data)
    
    def send_msg(self,cmd:str,data:str):
        self.client_socket.send((cmd+"\r\n"+str(self.group_id)+"\r\n"+data).encode())
        pass
    
def main():
    Server()


if __name__ == "__main__":
    main() 