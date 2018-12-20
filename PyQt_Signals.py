import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn = QtWidgets.QPushButton("Push Me")
        self.lbl = QtWidgets.QLabel("I have not been clicked yet")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.lbl)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.btn)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Signals')

        self.btn.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.lbl.setText("I have been clicked")

app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
