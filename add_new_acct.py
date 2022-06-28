from os import close
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QDialog
from PyQt5 import uic
import sys


class add_new_acct(QDialog):
    def __init__(self):
        super(add_new_acct, self).__init__()

        # load the ui file
        uic.loadUi("add_new_acct.ui", self)  
        
        # show the app
        self.show()
    
    def close():
        self.hide()
    
         
                   
              
# initialise the app            
app = QApplication(sys.argv)
UIWindow = add_new_acct()
app.exec_()
