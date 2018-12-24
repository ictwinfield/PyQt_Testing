import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow

class Boton(QWidget):
    def __init__(self, parent=None):
        super(Boton, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('First')
        btn2 = QPushButton('Second')
        lbl1 = QLabel('A label')

        h_box = QHBoxLayout()
        h_box.addWidget(btn1)
        h_box.addWidget(btn2)


        v_box = QVBoxLayout()
        v_box.setContentsMargins(0, 0, 0, 0)
        v_box.addWidget(lbl1)
        v_box.addLayout(h_box)

        self.setLayout(v_box)


class Etiqueta(QWidget):
    def __init__(self, parent=None):
        super(Etiqueta, self).__init__(parent)

        self.init_ui()

    def init_ui(self):
        lbl = QLabel('This is a label')

        v_box = QVBoxLayout()
        v_box.setContentsMargins(0, 0, 0, 0)
        v_box.addWidget(lbl)

        self.setLayout(v_box)


class MyStack(QMainWindow):
    def __init__(self, parent=None):
        super(MyStack, self).__init__(parent)

        self.setWindowTitle('A staked Widget')
        self.setFixedSize(400, 400)

        self.init_ui()

    def init_ui(self):
        self.cbx = QComboBox(self)
        self.cbx.addItems(['Boton', 'Etiqueta'])
        self.cbx.setGeometry(20, 20, 360, 24)

        self.boton = Boton(self)
        self.et = Etiqueta(self)

        self.MyStack = QStackedWidget(self)
        self.MyStack.addWidget(self.boton)
        self.MyStack.addWidget(self.et)

        self.MyStack.setGeometry(20, 84, 360, 250)

        self.cbx.activated.connect(self.do_something)

    def do_something(self):
        widget = self.cbx.currentIndex()
        self.MyStack.setCurrentIndex(widget)



app = QApplication(sys.argv)
stack = MyStack()
stack.show()
sys.exit(app.exec_())
