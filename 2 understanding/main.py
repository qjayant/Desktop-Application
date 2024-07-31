# Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#sys module is responsible for processing command line arguments
import sys

app=QApplication(sys.argv)

window= QWidget()
window.show()

#start the event loop
app.exec_() 
