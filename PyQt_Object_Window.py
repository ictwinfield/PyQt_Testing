import sys
from PyQt5 import QtWidgets, QtCore

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setWindowTitle('My Object Window')
        lbl = QtWidgets.QLabel('This is a Labal')

        lbl.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(lbl)

app = QtWidgets.QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()
