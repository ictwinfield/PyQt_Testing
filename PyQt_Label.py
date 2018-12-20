import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    lbl1 = QtWidgets.QLabel(w)
    lbl1.setText('Hello World!')
    w.setWindowTitle("PyQt Lesson 2")
    w.setGeometry(100, 100, 300, 200)
    lbl1.move(100, 20)
    w.show()
    sys.exit(app.exec_())

window()
