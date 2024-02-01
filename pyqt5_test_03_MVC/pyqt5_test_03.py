from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, Ui_pyqt5_test_03_V

class myMainWindow(QMainWindow, Ui_pyqt5_test_03_V.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.label.setText('thank you!!')
        if self.lineEdit.text()!= 'thank you!!':
            self.label.setText('thank you!!')
        else:
            self.label.setText('fuck you!!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = myMainWindow()

    window.show()
    sys.exit(app.exec_())