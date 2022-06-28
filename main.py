from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget
from PyQt5 import uic, QtGui, QtWidgets
import sys
import sqlite3


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)
          
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,250)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,200)
        
        self.actionopen_add_acct.triggered.connect(self.show_add_acct)
        
        self.show() 
        
        
    def printit(self):
        print("It works OK") 
        
    def show_add_acct(self):
        self.open_new_acct = add_new_acct()
        
       
class add_new_acct(QDialog):
    def __init__(self):
        super(add_new_acct, self).__init__()
        uic.loadUi("add_new_acct.ui", self)  
        self.show()
        
        self.exitButton.clicked.connect(self.close)
        
              
# initialise the app            
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
