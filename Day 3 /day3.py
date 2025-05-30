# Create an inventory system tracking items and quantities with a dictionary
"""Consider a person running a shop i created inventory system 
   for adding Fruits, Removing Fruits and View Inventory"""

# Simple Fruit Inventory System

inventory = {}  # Empty dictionary to store fruits and their quantities

print("Welcome to the Fruit Inventory System:")

while True:
    print("1. Add Fruit")
    print("2. Remove Fruit")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        fruit = input("Enter fruit name to add: ")
        quantity = int(input("Enter number of fruits: "))
        if fruit in inventory:
            inventory[fruit] += quantity
        else:
            inventory[fruit] = quantity
        print(f"{fruit}:{quantity} Quantity added.")

    elif choice == '2':
        fruit = input("Enter fruit name to remove: ")
        if fruit in inventory:
            quantity = int(input("Enter number of fruits to remove:"))
            if quantity >= inventory[fruit]:
                print("Entered quantity is greater than or equal to the available quantity.")
                inventory.pop(fruit)
                print(f"All {fruit} removed.")
            else:
                inventory[fruit] -= quantity
                print(f"{fruit}:{quantity} removed.")
        else:
            print(f"{fruit} is not in the inventory.")

    elif choice == '3':
        print("Current Inventory:")
        for fruit, qty in inventory.items():
            print(f"{fruit}: {qty}")
        if not inventory:
            print("Inventory is empty.")

    elif choice == '4':
        print("Please visit again! Thank you for using the Fruit Inventory System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

