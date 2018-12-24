import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create actions for Menus
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+s')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+n')

        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)

        # Add actions to Menus
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)


        # Events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("My Menu Example")
        self.resize(600, 400)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
