from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget, QLineEdit
from PyQt5 import uic, QtGui, QtWidgets
import sys
import sqlite3


conn = sqlite3.connect('bandy.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists account (
    title TEXT NOT NULL UNIQUE,
	org TEXT NOT NULL,
	bsb TEXT NOT NULL UNIQUE,
	acctnum TEXT NOT NULL UNIQUE,
	obal REAL,
	odate TEXT
)""")

conn.commit()

c.execute("""CREATE TABLE if not exists category (
        cat	TEXT NOT NULL UNIQUE,
	    type TEXT NOT NULL,
	    parent TEXT
)""")
conn.commit()

c.execute("""CREATE TABLE if not exists tran (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	cct TEXT NOT NULL DEFAULT 'Savings' UNIQUE,
	payee TEXT NOT NULL,
	date REAL NOT NULL,
	amt INTEGER NOT NULL,
	dr TEXT,
	cr TEXT,
	cat TEXT NOT NULL DEFAULT 'Miscellaneous',
	descr INTEGER
)""")

conn.commit()
conn.close()



newAcct = ""
newInst = ""
newBsb = ""
newNum = ""
newBal = 0
newDate = ""


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
        
        # define the widgets
        
            
        self.newAcct = self.findChild(QLineEdit, "acct_name_lineEdit.text")
        self.newInst = self.findChild( QLineEdit, "institution_name_lineEdit.text")
        self.newBsb = self.findChild( QLineEdit, "acct_bsb_lineEdit.text")
        self.newNum = self.findChild( QLineEdit, "acct_number_lineEdit.text")
        self.newBal = self.findChild( QLineEdit, "opening_bal_lineEdit.text")
        self.newDate = self.findChild( QLineEdit, "balance_date_lineEdit.text")
        
        print("Good so far") 
        
        def new_account(self):
            try:
                conn = sqlite3.connect('bandy.db')
                c = conn.cursor()
                
                # insert_sql = "INSERT INTO account VALUES ('Savings', 'NAB','196446', '224343545875', 995348.47, '29-06-22')" 
                # insert_sql = "INSERT INTO category VALUES ('Pension', 'Income','Income')"
                c.execute(insert_sql)
                
                print("No issues yet !!!")
                conn.commit()
                conn.close()

            except:
                sqlquery = "SELECT * FROM account"
                for row in c.execute(sqlquery):
                    print(row)
                
                print("Problem creating or populating tables")
            
        self.exitButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(new_account)
        
        

            
                      
# initialise the app            
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
