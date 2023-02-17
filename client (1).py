import socket
from decryption import Decryption
from protocol import Protocol

class Client():

    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.PROTOCOL = Protocol() # TODO get the protocol file
        self.DECRYPTION = Decryption() # TODO get the protocol file
        
    def connect(self):
        tries = 0

        trying = True
        while trying:
            print("connecting..")

            if tries >= 5:
                print(f"Failed to connect to server, too many tries.")
                return False

            try:
                self.my_socket.connect((self.ip, self.port))
                
            except:
                tries += 1
                continue

            print(f"Connected in [{tries+1}] tries.")
            print(f"You're connected! {self.ip} on port {self.port}")
            return True

    def get_server_msg(self):
        getting = True
        while getting:
            try:
                server_msg = self.my_socket.recv(1024)
            except:
                continue
            cmd, params = self.PROTOCOL.parse_received_message(server_msg) # TODO name will be modified
            return cmd, params
    
    def send_ans(self, params):
        print(params)
        answer = input("Answer>")

        if answer[:len("!DECRYPT!CAESAR!")] == "!DECRYPT!CAESAR!":
            i = 1
            while i <= 127:
                decrypted = self.DECRYPTION.caesar_decryption(params, i)
                print(f"shift={i}\n{decrypted}")
                client_input = input("Continue (c) or Stop (s)>")
                if client_input.lower() == 'c':
                    i += 1
                    print(params)
                elif client_input.lower() == 's': i = 200
                else:
                    print(params)
            
        elif answer[:len("!DECRYPT!VARNAM!")] == "!DECRYPT!VARNAM!":
            key = answer[len("!DECRYPT!VARNAM!"):]
            decrypted = self.DECRYPTION.code_varnam_decryption(params, key)
            print(f"key={key}\n{decrypted}")

        while answer[:len("!DECRYPT!CAESAR!")] == "!DECRYPT!CAESAR!" or answer[:len("!DECRYPT!VARNAM!")] == "!DECRYPT!VARNAM!":
            print(params)
            answer = input("Answer>")

            if answer[:len("!DECRYPT!CAESAR!")] == "!DECRYPT!CAESAR!":
                i = 1
                while i <= 127:
                    decrypted = self.DECRYPTION.caesar_decryption(params, i)
                    print(f"shift={i}\n{decrypted}")
                    client_input = input("Continue (c) or Stop (s)>")
                    if client_input.lower() == 'c':
                        i += 1
                        print(params)
                    elif client_input.lower() == 's': i = 200
                    else:
                        print(params)
                
            elif answer[:len("!DECRYPT!VARNAM!")] == "!DECRYPT!VARNAM!":
                key = answer[len("!DECRYPT!VARNAM!"):]
                decrypted = self.DECRYPTION.code_varnam_decryption(params, key)
                print(f"key={key}\n{decrypted}")


        msg = self.PROTOCOL.create_message("Answer", answer) # TODO name will be modified
        self.my_socket.send(msg.encode())

    def run(self):
        running = True
        if not self.connect(): running = False

        if running:
            msg = self.PROTOCOL.create_message("Start", None) # TODO name will be modified
            print(1111111111111111111,msg)
            self.my_socket.send(msg.encode())

        while running:

            cmd, params = self.get_server_msg()
            print(cmd, params)
            if cmd == "TryAgain":
                print("You Failed, Try Again..")
                # print(params)
                self.send_ans(params)
                # pass # TODO complete later
                
            elif cmd == "NextTask":
                # print(params)
                self.send_ans(params)
                # pass # TODO complete later
                
            elif cmd == "YouDidIt":
                running = False
                # pass # TODO complete later

        self.my_socket.close()  


        



c = Client("127.0.0.1",8820)
c.run()