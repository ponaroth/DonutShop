import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


def app():
    myApp = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("DonutMenu")
    window.show()
    sys.exit(myApp.exec_())

app()