import socket

class Protocol:
    """
    < cmd >\r\n
    Id = < group
    id >\r\n
    < parameters >\r\n
    \r\n
    """
    @staticmethod
    def check_message_paramz(command: str, param: str):
        """ a method to check if the data the client sent is valid
            Start - 0 params, Answer - 1 param (everything is valid) """

        if command == "Start" and param != "":
            return False
        return True

    @staticmethod
    # assuming client ran check message and everything was ok. You have to run check message before calling create message...
    def create_message(command: str, param: str):
        """ a method that creates a message based on the slides of the presentation."""
        # if(command == "Start"):
        return f"{command}\r\nId=5\r\n{param}\r\n\r\n"
        # else:
        #     return f"{command}\r\n{param}\r\n\r\n"

    @staticmethod
    def parse_received_message(received_message):
        """this method returns the command and paramaters of an encoded message we received from the server, in a decoded manner"""
        received_message = received_message.decode()
        split_message = received_message.split("\r\n")
        print(22222222222222222222,split_message,"\n",received_message)
        return split_message[0], split_message[2] # are the params in place one because there is no id sent from the server






