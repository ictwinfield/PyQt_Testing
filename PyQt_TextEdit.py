import sys
import os
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class NotePad(QWidget):

    def __init__(self):
        super(NotePad, self).__init__()

        self.txt = QTextEdit(self)
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')
        self.clr_btn = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()

        h_box.addWidget(self.clr_btn)
        h_box.addWidget(self.sav_btn)
        h_box.addWidget(self.opn_btn)

        v_box.addWidget(self.txt)
        v_box.addLayout(h_box)

        self.clr_btn.clicked.connect(self.clear_txt)
        self.opn_btn.clicked.connect(self.open_txt)
        self.sav_btn.clicked.connect(self.save_txt)

        self.setLayout(v_box)
        self.setWindowTitle('Writer')

        self.show()

    def save_txt(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.txt.toPlainText()
            f.write(my_text)

    def open_txt(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_txt = f.read()
            self.txt.setText(file_txt)

    def clear_txt(self):
        self.txt.clear()


app = QApplication(sys.argv)
writer = NotePad()
sys.exit(app.exec_())
