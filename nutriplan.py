from datetime import date, datetime, timedelta

profile = {}

foods = [
    {"name": "Oats", "serving": "40 g", "calories": 152,
     "protein": 5.2, "carbs": 27, "fat": 2.8},
    {"name": "Banana", "serving": "1 medium", "calories": 105,
     "protein": 1.3, "carbs": 27, "fat": 0.4},
    {"name": "Boiled Egg", "serving": "1 egg", "calories": 78,
     "protein": 6.3, "carbs": 0.6, "fat": 5.3}
]

meal_log = []


def set_profile():
    global profile

    print("\n--- SET PERSONAL PROFILE ---")

    try:
        age = int(input("Enter age in years: "))
        height = float(input("Enter height in cm: "))
        weight = float(input("Enter weight in kg: "))

        if age <= 0 or height <= 0 or weight <= 0:
            print("Age, height and weight must be positive.")
            return

        print("\nSelect formula:")
        print("1. Male equation")
        print("2. Female equation")
        gender = input("Enter choice: ").strip()

        if gender not in ("1", "2"):
            print("Invalid formula choice.")
            return

        print("\nSelect activity level:")
        print("1. Sedentary")
        print("2. Lightly active")
        print("3. Moderately active")
        print("4. Very active")
        print("5. Extra active")

        activity = input("Enter choice: ").strip()

        factors = {
            "1": 1.2,
            "2": 1.375,
            "3": 1.55,
            "4": 1.725,
            "5": 1.9
        }

        if activity not in factors:
            print("Invalid activity choice.")
            return

        profile = {
            "age": age,
            "height": height,
            "weight": weight,
            "gender": gender,
            "activity": activity,
            "activity_factor": factors[activity]
        }

        print("Profile saved successfully!")

    except ValueError:
        print("Please enter valid numerical values.")


def calculate_daily_target():
    if not profile:
        return None

    age = profile["age"]
    height = profile["height"]
    weight = profile["weight"]

    if profile["gender"] == "1":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return bmr * profile["activity_factor"]


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
        calories = float(input("Calories per serving: "))
        protein = float(input("Protein in grams: "))
        carbs = float(input("Carbohydrates in grams: "))
        fat = float(input("Fat in grams: "))

        if min(calories, protein, carbs, fat) < 0:
            print("Nutrient values cannot be negative.")
            return

        foods.append({
            "name": name,
            "serving": serving,
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        })

        print(f"{name} added successfully!")

    except ValueError:
        print("Enter valid numerical nutrient values.")


def log_meal():
    if not foods:
        print("No foods available. Add a food first.")
        return

    print("\n--- LOG A MEAL ---")
    view_foods()

    try:
        food_number = int(input("\nEnter food number: "))

        if food_number < 1 or food_number > len(foods):
            print("Invalid food number.")
            return

        servings = float(input("Enter number of servings: "))

        if servings <= 0:
            print("Servings must be greater than zero.")
            return

        meal_date = input(
            "Enter date (YYYY-MM-DD), or press Enter for today: "
        ).strip()

        if meal_date == "":
            meal_date = date.today().isoformat()
        else:
            meal_date = datetime.strptime(
                meal_date, "%Y-%m-%d"
            ).date().isoformat()

        food = foods[food_number - 1]

        meal = {
            "date": meal_date,
            "name": food["name"],
            "servings": servings,
            "calories": food["calories"] * servings,
            "protein": food["protein"] * servings,
            "carbs": food["carbs"] * servings,
            "fat": food["fat"] * servings
        }

        meal_log.append(meal)

        print(f"{food['name']} logged successfully for {meal_date}!")

    except ValueError:
        print("Invalid input. Check the food number, servings or date.")


def daily_summary():
    selected_date = input(
        "Enter date (YYYY-MM-DD), or press Enter for today: "
    ).strip()

    try:
        if selected_date == "":
            selected_date = date.today().isoformat()
        else:
            selected_date = datetime.strptime(
                selected_date, "%Y-%m-%d"
            ).date().isoformat()
    except ValueError:
        print("Invalid date format.")
        return

    meals = [m for m in meal_log if m["date"] == selected_date]

    totals = {
        "calories": sum(m["calories"] for m in meals),
        "protein": sum(m["protein"] for m in meals),
        "carbs": sum(m["carbs"] for m in meals),
        "fat": sum(m["fat"] for m in meals)
    }

    print(f"\n--- DAILY SUMMARY: {selected_date} ---")

    for meal in meals:
        print(f"{meal['name']} - {meal['servings']} serving(s)")

    print(f"Calories: {totals['calories']:.1f} kcal")
    print(f"Protein: {totals['protein']:.1f} g")
    print(f"Carbohydrates: {totals['carbs']:.1f} g")
    print(f"Fat: {totals['fat']:.1f} g")

    target = calculate_daily_target()

    if target is None:
        print("Set your profile to calculate your calorie target.")
    else:
        difference = target - totals["calories"]
        print(f"Estimated daily calorie target: {target:.1f} kcal")

        if difference >= 0:
            print(f"Calories remaining to target: {difference:.1f} kcal")
        else:
            print(f"Target exceeded by: {-difference:.1f} kcal")


def weekly_summary():
    end_date = date.today()
    start_date = end_date - timedelta(days=6)

    daily_totals = {}

    for day_offset in range(7):
        current_date = start_date + timedelta(days=day_offset)
        daily_totals[current_date.isoformat()] = {
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0
        }

    for meal in meal_log:
        if meal["date"] in daily_totals:
            for nutrient in ("calories", "protein", "carbs", "fat"):
                daily_totals[meal["date"]][nutrient] += meal[nutrient]

    logged_days = sum(
        1 for day in daily_totals
        if any(m["date"] == day for m in meal_log)
    )

    print(f"\n--- WEEKLY SUMMARY ---")
    print(f"Period: {start_date} to {end_date}")
    print(f"Days with logged meals: {logged_days} of 7")

    if logged_days == 0:
        print("No meals logged during this period.")
        return

    for nutrient in ("calories", "protein", "carbs", "fat"):
        total = sum(day[nutrient] for day in daily_totals.values())
        average = total / logged_days
        unit = "kcal/day" if nutrient == "calories" else "g/day"
        print(f"Average {nutrient}: {average:.1f} {unit}")


def main():
    while True:
        print("\n================================")
        print("           NUTRIPLAN")
        print(" Personal Calorie and Macro Planner")
        print("================================")
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
            log_meal()
        elif choice == "5":
            daily_summary()
        elif choice == "6":
            weekly_summary()
        elif choice == "7":
            print("Thank you for using NutriPlan!")
            break
        else:
            print("Invalid choice! Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()