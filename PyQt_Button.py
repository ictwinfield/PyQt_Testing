import sys
from PyQt5 import QtWidgets

def window():
    # Create an QApplication so that we can set up an event loop
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    btn = QtWidgets.QPushButton(w)
    btn.setText('Push Me')
    w.setWindowTitle("PyQt Lesson 3")
    btn.move(100, 50)
    w.show()
    sys.exit(app.exec_())

window()
