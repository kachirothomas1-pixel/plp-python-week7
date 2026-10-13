# Shopping List Manager
shopping_list = []

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Enter item: ").strip()
        if item:
            shopping_list.append(item)
        else:
            print("Item cannot be empty.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")
