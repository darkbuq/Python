# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:46:08 2024

@author: yr.chen
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import socket

import ui_02


#%%
class myMainWindow(QMainWindow, ui_02.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.btn_conn.clicked.connect(self.buttonClicked)
        self.btn_read.clicked.connect(self.buttonRead)
        
    def buttonClicked(self):
        self.txt_result.setText(conn())
        # self.txt_result.setText(query("*IDN?"))
        
    def buttonRead(self):
        self.txt_result.setText(query("read?"))


#%%

def query(cmd):
    s.send(bytes(cmd+"\r\n",'ansi'))
    return s.recv(BUFFER_SIZE).decode('utf8')

#%%

TCP_IP      = '169.254.4.61'  # or whatever address you'll find on the E4980A screen
TCP_PORT    = 5025
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0)

def conn():
    # s.connect((TCP_IP, TCP_PORT))
    try:
        s.connect((TCP_IP, TCP_PORT))
        return 'connect success'
    except Exception as e:
        # self.txt_result.setText(str(e))
        return str(e)



#%%


### end of script

#%%
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myMainWindow()

    window.show()
    sys.exit(app.exec_())