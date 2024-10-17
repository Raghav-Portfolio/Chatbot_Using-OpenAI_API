from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import sys
from backend import ChatBot
import threading

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatBot()
        
        self.setMinimumSize(700,400)
        
        #Add the chat area widget
        self.chat_area = QTextEdit(self) #relate to the main window using self
        self.chat_area.setGeometry(10, 10, 480, 320) # expects two coordinates and two dimensions
        self.chat_area.setReadOnly(True)
        
        #Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message) # enabling the 'send' function on pressing 'Enter'
        
        #Add the button
        self.button = QPushButton('Send', self)
        self.button.setGeometry(500, 340, 90, 40)
        self.button.clicked.connect(self.send_message)
        
        self.show()  # need to use this when not using set.centralWidget
    
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()
        
        thread = threading.Thread(target=self.get_bot_response, args =(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")
        

app = QApplication(sys.argv)
main_obj = ChatBotWindow()
sys.exit(app.exec())