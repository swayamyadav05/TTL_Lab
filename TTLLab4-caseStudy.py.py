#!/usr/bin/env python
# coding: utf-8

# In[ ]:


product = {
    1: {"name": "Dress", "price": 1200, "quantity": 50},
    2: {"name": "shoes", "price": 2200, "quantity": 150},
    3: {"name": "watch", "price": 2700, "quantity": 100},
    4: {"name": "Necklace", "price": 3000, "quantity": 30},
}

user_cart = [] 

product_discounts = {
    1: 0.2,  # 20% discount on Product1
    3: 0.1,  # 10% discount on Product3
}

def add_to_cart(product_id, quantity):
    if product_id in product and product[product_id]["quantity"] >= quantity:
        user_cart.append((product_id, quantity))
        product[product_id]["quantity"] -= quantity
        print(f"Product added to the cart")
    else:
        print(f"Product not available or quantity exceeds the available quantity")
        
def remove_from_cart(product_id):
    for item in user_cart:
        if item[0] == product_id:
            user_cart.remove(item)
            product[product_id]["quantity"] += item[1]
            print("Product removed from the cart")
            break

def view_cart_contents():
    for item in user_cart:
        print(f"Product ID: {item[0]}, Quantity: {item[1]}")
        
def total_cost():
    total_cost = 0
    for item in user_cart:
        product_id, quantity = item
        cost = product[product_id]["price"]
        if product_id in product_discounts:
            cost -= cost * product_discounts[product_id]
        total_cost += cost * quantity
    print (total_cost)

def optionss():
    while True:
        action = input("Do you want to add, remove or buy items from the cart? (add/remove/checkout/exit): ")
        if action.lower() == "add":
            product_id = int(input("Enter the product ID: "))
            quantity = int(input("Enter the quantity: "))
            add_to_cart(product_id, quantity)
        elif action.lower() == "remove":
            product_id = int(input("Enter the product ID: "))
            remove_from_cart(product_id)
        elif action.lower() == "checkout":
            print("cart details: \n")
            view_cart_contents()
            print("Total amount to be paid:")
            total_cost()
        elif action.lower() == "exit":
            break
        else:
            print("Invalid action. Please enter add, remove, or exit.")

optionss()


# In[ ]:




