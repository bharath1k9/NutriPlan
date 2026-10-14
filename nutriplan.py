profile = {}

def set_profile():
    global profile

    print("\n--- SET PERSONAL PROFILE ---")

    try:
        age = int(input("Enter your age in years: "))
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))

        if age <= 0 or height <= 0 or weight <= 0:
            print("Age, height and weight must be positive.")
            return

        print("\nSelect formula:")
        print("1. Male equation")
        print("2. Female equation")
        gender = input("Enter your choice: ")

        if gender not in ("1", "2"):
            print("Invalid formula choice.")
            return

        print("\nSelect activity level:")
        print("1. Sedentary")
        print("2. Lightly active")
        print("3. Moderately active")
        print("4. Very active")
        print("5. Extra active")

        activity = input("Enter your choice: ")

        activity_factors = {
            "1": 1.2,
            "2": 1.375,
            "3": 1.55,
            "4": 1.725,
            "5": 1.9
        }

        if activity not in activity_factors:
            print("Invalid activity choice.")
            return

        profile = {
            "age": age,
            "height": height,
            "weight": weight,
            "gender": gender,
            "activity": activity,
            "activity_factor": activity_factors[activity]
        }

        print("\nProfile saved successfully!")

    except ValueError:
        print("Please enter valid numerical values.")


while True:
    print("\n================================")
    print("           NUTRIPLAN")
    print(" Personal Calorie and Macro Planner")
    print("================================")

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
        set_profile()
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