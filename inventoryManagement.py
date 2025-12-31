mainMenu = ("1.Add Item","2.View all","3.Edit Item","4.Remove Item","5.Exit")
categories = ["eletronics","home","office","other"]
inventory = dict()
selectedOption = 0

def showAll(items):
    # check if it is dict
    if isinstance(items, dict):
        print("Inventory:")
        for key, val in items.items():
            print(f"- {val.get('name', key)}")
            print(f"  Category: {val.get('category')}, Brand: {val.get('brand')}, Quantity: {val.get('quantity')}, Price: {val.get('price')}")
    else:
        for i, it in enumerate(items, 1):
            print(f"{i}. {it}")


def ask_yes_no(prompt):
    resp = input(prompt).strip().lower()
    return resp in ("y", "yes")


def addItem():
    print(" Add item ".center(50,"%"))
    # Getting product name
    name = input("Enter product name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    keyName = name.lower()

    # Getting product category
    category = input("Enter category(Eletronics, Home, Office, Other): ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    if category.lower() not in categories:
        print("Category should be Eletronics, Home, Office or Other.")
        return
    keyCategory = category.lower()

    # Getting brand name
    brand = input("Enter brand name: ").strip()
    if not brand:
        print("Product should have a brand.")
        return
    keyBrand = brand.lower()

    # Getting the quantity
    quantity = input("Enter quantity: ").strip()
    if not quantity:
        print("Quantity cannot be empty.")
        return
    try:
        keyQuantity = int(quantity)
        if keyQuantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return

    price = input("Enter product price: ").strip()
    if not price:
        print("Price cannot be empty.")
        return
    try:
        keyPrice = round(float(price), 2)
        if keyPrice < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price. Please enter a number (e.g. 102.99)")
        return
    

    if keyName in inventory: # If the product already exists
        old = inventory[keyName]
        print("Product already exists.")
        print(f" - Current product details: Product name: {old['name']} | Category: {old['category']} | Brand: {old['brand']} | Quantity: {old['quantity']} | Price: {old['price']}")
        replace = ask_yes_no("Replace this product? (y/n): ")
        if not replace:
            create_new = ask_yes_no("Create a new product with name incrementation? (y/n): ")
            if not create_new:
                print("Operation Cancelled...")
                return
            base = name
            counter = 2
            new_name = f"{base} - ({counter})"
            while new_name.lower() in inventory:
                counter += 1
                new_name = f"{base} - ({counter})"
            print(f"Suggested name: {new_name}")
            use_suggested = ask_yes_no("Use the suggested name? (y/n): ")
            if use_suggested:
                name = new_name
                keyName = name.lower()
            else:
                name = input("Enter a new name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    return
                keyName = name.lower()
                if keyName in inventory:
                    print("Name already exists. Operation cancelled.")
                    return

    inventory[keyName] = {
        "name": name,
        "category": keyCategory,
        "brand": keyBrand,
        "quantity": keyQuantity,
        "price": keyPrice,
    }
    print(f"Product '{name}' saved.")


def editItem():
    print(" Edit item ".center(50, "%"))
    name = input("Enter product name to edit: ").strip().lower()
    if name not in inventory:
        print("Product not found.")
        return
    item = inventory[name]
    print(f"Current: Name: {item['name']} | Category: {item['category']} | Brand: {item['brand']} | Quantity: {item['quantity']} | Price: {item['price']}")
    field = input("Which field to edit? (name/category/brand/quantity/price): ").strip().lower()
    if field == "name":
        new = input("Enter new name: ").strip()
        if not new:
            print("Name cannot be empty.")
            return
        del inventory[name]
        # Create a new name with ** (copy)
        inventory[new.lower()] = {**item, "name": new}
        print("Name updated.")
    elif field == "category":
        new = input("Enter new category: ").strip().lower()
        inventory[name]['category'] = new
        print("Category updated.")
    elif field == "brand":
        new = input("Enter new brand: ").strip()
        inventory[name]['brand'] = new
        print("Brand updated.")
    elif field == "quantity":
        new = input("Enter new quantity: ").strip()
        try:
            inventory[name]['quantity'] = int(new)
            print("Quantity updated.")
        except:
            print("Invalid quantity.")
    elif field == "price":
        new = input("Enter new price: ").strip()
        try:
            inventory[name]['price'] = round(float(new), 2)
            print("Price updated.")
        except:
            print("Invalid price.")
    else:
        print("Unknown field.")


def removeItem():
    print("Remove item".center(50, "%"))
    name = input("Enter product name to remove: ").strip().lower()
    if not name:
        print("Name cannot be empty.")
        return
    if name in inventory:
        del inventory[name]
        print("Product removed.")
    else:
        print("Product not found.")

while selectedOption != 5:
    print("Welcome to the Inventory Management System!")
    print("===========================================")
    showAll(mainMenu)
    selectedOption = int(input("Enter option number (1-5): "))
    if(selectedOption not in range(1,6)): # 1 to 4
        print("Enter a number between 1 and 5 please.")
        continue
    if selectedOption == 1:
        addItem()
    elif selectedOption == 2:
        showAll(inventory)
    elif selectedOption == 3:
        editItem()
    elif selectedOption == 4:
        removeItem()
    elif selectedOption == 5:
        print("End of executing.")