from PyQt5 import QtWidgets, QtGui, QtCore
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show(e):
    label.setText(e)

label = QtWidgets.QLabel(Form)
label.setText('A')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('A')
btn1.setGeometry(50,60,50,30)
btn1.clicked.connect(lambda:show('A'))  # 使用 lambda 函式

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('B')
btn2.setGeometry(110,60,50,30)
btn2.clicked.connect(lambda:show('B'))  # 使用 lambda 函式

Form.show()
sys.exit(app.exec_())