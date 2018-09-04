import sys

from PyQt5.QtCore import pyqtSlot

from ProductList import productList
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget



# cart
cart = []



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

    buttonList = []
    i = 0
    for product in productList:
        print(product.name, "/n", product.price )
        name = product.name + "\n" + str(product.price)
        btn = QtWidgets.QPushButton(window)
        btn.setText(name)
        btn.clicked.connect(lambda: addToCart(product))
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

    # add a product to cart
    @pyqtSlot()
    def addToCart(product):
        cart.append(product)

        cart_lb.setText("Cart total: " + str(getTotal()))
        cart_lb.adjustSize()


    def getTotal():
        totalPrice = 0
        print(type(totalPrice))

        for item in cart:
            print(type(item.price))
            totalPrice = totalPrice + item.price
            print("2 total " + totalPrice)

        print(totalPrice)
        return totalPrice

    window.show()
    sys.exit(myApp.exec_())

app()



