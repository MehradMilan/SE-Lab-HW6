import requests

BASE_URL = "http://localhost:8001/items"

def list_items():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        for item in response.json():
            print(f"ID: {item[0]}, Name: {item[1]}, Value: {item[2]}")
    else:
        print("Failed to fetch items.")

def add_item():
    name = input("Enter item name: ")
    value = float(input("Enter item value: "))
    response = requests.post(BASE_URL, json={"name": name, "value": value})
    if response.status_code == 201:
        print("Item added successfully!")
    else:
        print("Failed to add item.")

def delete_item():
    item_id = int(input("Enter item ID to delete: "))
    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("Item deleted successfully!")
    else:
        print("Failed to delete item.")

def main():
    while True:
        print("\nCLI Interface")
        print("1. List Items")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()