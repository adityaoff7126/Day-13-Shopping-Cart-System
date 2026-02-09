Shopping Cart System - README

Project Overview
----------------
This is a simple console-based Shopping Cart System written in Python.  
The program allows users to add items to a cart, remove items, view cart contents, and calculate the total bill.

Features
--------
1. Display available shop items with prices.
2. Add items to the cart with quantity.
3. Remove items from the cart.
4. View cart items with total price calculation.
5. Input validation using try-except.
6. Continuous menu-driven interface.

Project Structure
-----------------
shop_product : List storing product names available in the shop.
shop_price   : List storing product prices.

cart_name    : List storing selected product names.
cart_price   : List storing selected product prices.
cart_qty     : List storing selected product quantities.

Functions
---------
add()
Displays shop items and allows user to add selected items to the cart.

remove()
Displays cart items and allows user to remove selected items.

view()
Displays all items in the cart along with quantity and item total.

total_bill()
Calculates and returns the final bill amount.

How To Run
----------
1. Install Python (version 3 or above).
2. Copy the program into a Python file (example: shopping_cart.py).
3. Run the file using:
   python shopping_cart.py
4. Follow the menu instructions displayed in the console.

Example Workflow
----------------
1. User selects Add Item.
2. User enters item number and quantity.
3. Item is stored in cart lists.
4. User can view cart or remove items.
5. Total bill is calculated automatically.

Concepts Used
-------------
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Menu Driven Programming

Limitations
-----------
- Uses parallel lists instead of advanced data structures.
- Data is not stored permanently.
- No graphical user interface.

Future Improvements
-------------------
- Use dictionaries or classes for better data handling.
- Add file or database storage.
- Add update quantity feature.
- Create graphical interface using Tkinter or web framework.
- Add discount and tax calculation.

Author
------
Aditya

