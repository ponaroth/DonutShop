import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


def app():
    myApp = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("DonutMenu")

    glaze_btn = QtWidgets.QPushButton(window)
    glaze_btn.setText('Glaze')
    glaze_btn.setGeometry(10,10, 100, 100)

    glaze2_btn = QtWidgets.QPushButton(window)
    glaze2_btn.setText('Twist')
    glaze2_btn.setGeometry(110, 10, 100, 100)

    cart_lb = QtWidgets.QLabel(window)
    cart_lb.setText('Cart total: ')
    cart_lb.move(10, 400)

    window.setGeometry(100, 100, 500, 500)





    window.show()
    sys.exit(myApp.exec_())

app()