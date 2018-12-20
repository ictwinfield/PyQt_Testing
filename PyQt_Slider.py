import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.btn1 = QtWidgets.QPushButton("Clear")
        self.btn2 = QtWidgets.QPushButton("Print")
        self.lEd = QtWidgets.QLineEdit()
        self.sdr = QtWidgets.QSlider(Qt.Horizontal)
        self.sdr.setMinimum(1)
        self.sdr.setMaximum(99)
        self.sdr.setValue(25)
        self.sdr.setTickInterval(10)
        self.sdr.setTickPosition(QtWidgets.QSlider.TicksBelow)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lEd)
        v_box.addWidget(self.btn1)
        v_box.addWidget(self.btn2)
        v_box.addWidget(self.sdr)

        self.setLayout(v_box)
        self.setWindowTitle('LineEdit')

        self.btn1.clicked.connect(lambda: self.btn_click(self.btn1, 'Hello from Clear'))
        self.btn2.clicked.connect(lambda: self.btn_click(self.btn2, 'Hello from Print'))
        self.sdr.valueChanged.connect(self.v_change)

        self.show()

    def btn_click(self, b, string):
        if b.text() == 'Print':
            print(self.lEd.text())
        else:
            self.lEd.clear()
        print(string)

    def v_change(self):
        my_value = str(self.sdr.value())
        self.lEd.setText(my_value)

app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
