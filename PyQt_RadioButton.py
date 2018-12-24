import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QtWidgets.QLabel('Which do you like best?')
        self.dog = QtWidgets.QRadioButton('Dogs')
        self.cat = QtWidgets.QRadioButton('Cats')
        self.btn = QtWidgets.QPushButton('Select')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lbl)
        v_box.addWidget(self.dog)
        v_box.addWidget(self.cat)
        v_box.addWidget(self.btn)

        self.setLayout(v_box)
        self.setWindowTitle('Radio Button')

        self.btn.clicked.connect(lambda: self.btn_click(self.dog.isChecked(), self.lbl))

        self.show()

    def btn_click(self, chk, lbl):
        if chk:
            lbl.setText('You like dogs')
        else:
            lbl.setText('You like cats')




app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
