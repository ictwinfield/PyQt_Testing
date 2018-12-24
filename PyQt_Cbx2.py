import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QtWidgets.QLabel()
        self.cbx = QtWidgets.QCheckBox('Do you like dogs?')
        self.btn = QtWidgets.QPushButton('Push Me')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lbl)
        v_box.addWidget(self.cbx)
        v_box.addWidget(self.btn)

        self.setLayout(v_box)

        self.btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        if self.cbx.isChecked():
            self.lbl.setText('I guess you like dogs')
        else:
            self.lbl.setText('Dog hater then')

app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
