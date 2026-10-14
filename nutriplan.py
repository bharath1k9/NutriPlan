print("================================")
print("           NUTRIPLAN")
print(" Personal Calorie and Macro Planner")
print("================================")

while True:
    print("\nMAIN MENU")
    print("1. Set Personal Profile")
    print("2. View Food List")
    print("3. Add New Food")
    print("4. Log a Meal")
    print("5. View Daily Summary")
    print("6. View Weekly Summary")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Personal profile feature coming soon!")
    elif choice == "2":
        print("Food list feature coming soon!")
    elif choice == "3":
        print("Add new food feature coming soon!")
    elif choice == "4":
        print("Meal logging feature coming soon!")
    elif choice == "5":
        print("Daily summary feature coming soon!")
    elif choice == "6":
        print("Weekly summary feature coming soon!")
    elif choice == "7":
        print("Thank you for using NutriPlan!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")