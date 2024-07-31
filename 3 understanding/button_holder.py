from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Button holder ")
        button = QPushButton("Press me !!")

        #set up the button as our central widget 
        self.setCentralWidget(button)