import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    btn = QtWidgets.QPushButton("Push Me")
    lbl = QtWidgets.QLabel('Look at me')

    h_box =QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(lbl)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(btn)
    v_box.addLayout(h_box)

    w.setLayout(v_box)

    w.setWindowTitle("A Layout")
    w.show()

    sys.exit(app.exec_())

window()
