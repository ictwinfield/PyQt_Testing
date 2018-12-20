import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn1 = QtWidgets.QPushButton("Clear")
        self.btn2 = QtWidgets.QPushButton("Print")
        self.lEd = QtWidgets.QLineEdit()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lEd)
        v_box.addWidget(self.btn1)
        v_box.addWidget(self.btn2)

        self.setLayout(v_box)
        self.setWindowTitle('LineEdit')

        self.btn1.clicked.connect(self.btn_click)
        self.btn2.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == "Print":
            print(self.lEd.text())
        else:
            self.lEd.clear()

app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
