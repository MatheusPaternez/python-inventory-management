# Python Inventory Management

Short description
-----------------

A small command-line inventory management tool for adding, viewing, editing and removing products.

How to run
----------

1. Open a terminal and change to the project folder:

```
cd python-inventory-management
```

2. Run the script with your Python 3 interpreter:

```bash
python inventoryManagement.py
```

Features implemented
--------------------

- Add Item: prompt for name, category, brand, quantity and price and save to inventory.
- View all: list current menu or inventory contents.
- Edit Item: update name, category, brand, quantity or price for an existing product.
- Remove Item: delete a product from inventory.

Limitations / Known issues
--------------------------

- Minimal validation: inputs are checked simply; invalid inputs may be rejected without helpful guidance.
- Category values are not strictly enforced beyond a basic check; casing is normalized to lowercase.
- The program is single-user and not concurrent — running multiple instances may overwrite data.