profile = {}

foods = [
    {
        "name": "Oats",
        "serving": "40 g",
        "calories": 152,
        "protein": 5.2,
        "carbs": 27,
        "fat": 2.8
    },
    {
        "name": "Banana",
        "serving": "1 medium",
        "calories": 105,
        "protein": 1.3,
        "carbs": 27,
        "fat": 0.4
    },
    {
        "name": "Boiled Egg",
        "serving": "1 egg",
        "calories": 78,
        "protein": 6.3,
        "carbs": 0.6,
        "fat": 5.3
    }
]


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

        print("Profile saved successfully!")

    except ValueError:
        print("Please enter valid numerical values.")


def view_foods():
    print("\n--- FOOD LIST ---")

    for index, food in enumerate(foods, start=1):
        print(f"\n{index}. {food['name']} ({food['serving']})")
        print(f"Calories: {food['calories']} kcal")
        print(f"Protein: {food['protein']} g")
        print(f"Carbohydrates: {food['carbs']} g")
        print(f"Fat: {food['fat']} g")


def add_food():
    print("\n--- ADD NEW FOOD ---")

    name = input("Enter food name: ").strip()
    serving = input("Enter serving size: ").strip()

    if not name or not serving:
        print("Food name and serving size cannot be empty.")
        return

    if any(food["name"].lower() == name.lower() for food in foods):
        print("This food already exists.")
        return

    try:
        calories = float(input("Enter calories per serving: "))
        protein = float(input("Enter protein in grams: "))
        carbs = float(input("Enter carbohydrates in grams: "))
        fat = float(input("Enter fat in grams: "))

        if calories < 0 or protein < 0 or carbs < 0 or fat < 0:
            print("Nutrient values cannot be negative.")
            return

        new_food = {
            "name": name,
            "serving": serving,
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        }

        foods.append(new_food)
        print(f"{name} added successfully!")

    except ValueError:
        print("Please enter valid numerical nutrient values.")


def main():
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

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            set_profile()
        elif choice == "2":
            view_foods()
        elif choice == "3":
            add_food()
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
            print("Invalid choice! Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()