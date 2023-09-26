from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys



def add_label():
    print("clicked")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Messenger")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QPlainTextEdit(window)
    main_text.setPlainText("test test")
    main_text.move(100, 100)

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("test")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)


    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()