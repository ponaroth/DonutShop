import sys

from PyQt5.QtCore import pyqtSlot

from ProductList import productList
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget



cart = []
# cart

# menu GUI
def app():
    myApp = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("DonutMenu")

    cart_lb = QtWidgets.QLabel(window)
    cart_lb.setText("Cart total: ")
    cart_lb.move(10, 400)


    # geometry of the buttons
    geo = [10, 10, 100, 100]

    numOfItemInRow = 0
    column = 0

    for product in productList:
        print(product.name, "/n", product.price )
        name = product.name + "\n" + product.price
        btn = QtWidgets.QPushButton(window)
        btn.setText(name)
        btn.clicked.connect(lambda: on_click(cart_lb))
        btn.setGeometry(geo[0], geo[1], geo[2], geo[3])

        if numOfItemInRow < 4:
            geo[0] = geo[0] + 100
            numOfItemInRow = numOfItemInRow + 1
        else:
            geo[1] = geo[1] + 100
            geo[0] = 10
            numOfItemInRow = 0
            column = column + 1


    window.setGeometry(400, 100, 600, 600)

    @pyqtSlot()
    def on_click(cart_lb):
        cart_lb.setText("Cart total: " + product.price)
        cart_lb.adjustSize()

    # add a product to cart
    def add(product):
        cart.append(product)
        print(product.price)

        cart_lb.setText("Cart total: " + product.price)
        print(getTotal())


    def getTotal():
        totalPrice = 0

        if not cart:
            print("cart is empty")

        else:
            for item in cart:
                totalPrice = totalPrice + item.price

        return totalPrice

    window.show()
    sys.exit(myApp.exec_())

app()



