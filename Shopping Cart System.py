
shop_product = ["Pen", "Pencil", "Book"]
shop_price = [10, 21, 334]


cart_name = []
cart_price = []
cart_qty = []


def add():
    print("\nAvailable Items:")
    for i in range(len(shop_product)):
        print(f"{i+1}. {shop_product[i]} - ${shop_price[i]}")

    try:
        choice = int(input("Enter item number: "))
        qty = int(input("Enter quantity: "))

        if 1 <= choice <= len(shop_product):
            cart_name.append(shop_product[choice-1])
            cart_price.append(shop_price[choice-1])
            cart_qty.append(qty)
            print("Item added")
        else:
            print("Invalid choice")

    except:
        print("Invalid input ")



def remove():
    if not cart_name:
        print("Cart is empty")
        return

    print("\nCart Items:")
    for i in range(len(cart_name)):
        print(f"{i+1}. {cart_name[i]}")

    try:
        choice = int(input("Enter item number to remove: "))

        if 1 <= choice <= len(cart_name):
            cart_name.pop(choice-1)
            cart_price.pop(choice-1)
            cart_qty.pop(choice-1)
            print("Item removed ")
        else:
            print("Invalid choice ")

    except:
        print("Invalid input ")



def total_bill():
    total = 0
    for i in range(len(cart_name)):
        total += cart_price[i] * cart_qty[i]
    return total



def view():
    if len(cart_name) == 0:
        print("Cart is empty ")
        return

    print("\n------ YOUR CART ------")
    for i in range(len(cart_name)):
        item_total = cart_price[i] * cart_qty[i]
        print(f"{cart_name[i]} x {cart_qty[i]} = ${item_total}")

    print("Total Bill =", total_bill())



while True:
    print("\n===== SHOP MENU =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        remove()

    elif choice == "3":
        view()

    elif choice == "4":
        print("Thank you for shopping ")
        break

    else:
        print("Invalid input ")
