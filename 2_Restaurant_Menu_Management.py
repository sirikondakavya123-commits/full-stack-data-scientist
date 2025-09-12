'''2. Restaurant Menu Management
Scenario:
You are managing a restaurant's menu. Write a program to update the menu by adding 
or removing items and allow users to check if a particular item is available.
Requirements:
- Use functions for adding, removing, and checking menu items.
- Handle cases where the item to be removed does not exist.
Input Example:
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
Expected Output:
Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]
Availability: "Pizza is available"'''
def add_menu_item(menu, item):
    menu.append(item)
    print(f"{item} added to the menu.")

def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
        print(f"{item} removed from the menu.")
    else:
        print(f"{item} is not in the menu!")

def check_menu_item(menu, item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")
menu = []
n = int(input("Enter number of initial menu items: "))
for i in range(n):
    item = input(f"Enter item {i+1}: ")
    menu.append(item)
print("\nInitial Menu:", menu)
add_item = input("\nEnter an item to add: ")
add_menu_item(menu, add_item)
remove_item = input("Enter an item to remove: ")
remove_menu_item(menu, remove_item)
check_item = input("Enter an item to check availability: ")
check_menu_item(menu, check_item)
print("\nUpdated Menu:", menu)
