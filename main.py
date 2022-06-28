from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget
from PyQt5 import uic, QtGui
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

        def show_add_acct(self):
            self.open_new_acct = QDialog.add_acct()
            self.open_new_acct.show()
                
        # self.actionopen_add_acct.triggered.connect(self.show_add_acct)
        
        self.show()
       
   
              
    class add_acct(QDialog):
        def __init__(self):
            super(add_acct, self).__init__()
            uic.loadUi("add_new_acct.ui", self)  
            self.show()
            
            self.exitButton.clicked.connect(self.close_window)
            
        def close_window(self):
            self.close()            
       
       
    class add_new_acct(QDialog):
        def __init__(self):
           super(add_new_acct, self).__init__()
           uic.loadUi("add_new_acct.ui", self)  
           self.show()
        
        def close():
           self.hide()
            
        

class FooTable(QTableWidget):
    def __init__(self):
        super().__init__()

        
    def addPressed(self):
        print("New page was pressed")
        
                
    
    
    
   
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
              
# initialise the app            
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
