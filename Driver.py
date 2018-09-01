from Product import Product


glazed = Product("Glazed", 1.00)

twist = Product("twists and bars", 1.10)

print(glazed.name, glazed.price)

#A list of Products
cart = []


#add a product to cart
def add(productA):
    cart.append(productA)


def getTotal():
    totalPrice = 0

    if not cart:
        print("cart is empty")

    else:
        for item in cart:
            totalPrice = totalPrice + item.price

    return totalPrice

cart.append(glazed)
cart.append(glazed)
cart.append(glazed)
cart.append(twist)
cart.append(twist)


print("the total is ", '${:,.2f}'.format(getTotal()))