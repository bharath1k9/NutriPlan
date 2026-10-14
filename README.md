# NutriPlan — Personal Calorie and Macro Planner

NutriPlan is a Python-based console application that helps users track their daily food intake, estimate calorie requirements, and monitor macronutrients.

## Features

- **Personal Profile:** Stores age, height, weight, formula selection, and activity level.
- **Calorie Target:** Estimates daily energy requirements using the Mifflin–St Jeor equation and an activity multiplier.
- **Food Management:** Displays predefined foods and allows users to add custom foods.
- **Meal Tracking:** Records food, serving quantities, and dates.
- **Daily Summary:** Calculates calories, protein, carbohydrates, and fat consumed.
- **Weekly Summary:** Displays daily calorie totals and average nutrient intake over the past seven days.
- **Meal Management:** Views, edits, and deletes logged meals.
- **CSV Persistence:** Saves profile, food, and meal data locally between program runs.
- **Input Validation:** Handles invalid menu selections, quantities, and dates.

## Technologies Used

- Python 3
- CSV module
- Datetime module
- OS module
- Visual Studio Code

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal in the project folder.
5. Run:

   `python nutriplan.py`

6. Follow the menu displayed in the terminal.

## Data Storage

NutriPlan stores information in local CSV files:

- `profile.csv` — personal profile and activity information
- `foods.csv` — food items and their nutrient values
- `meals.csv` — logged meals and nutrient totals

These files are created or updated as the application saves data.

## Testing

The application has been manually tested for:

- Invalid menu choices
- Invalid profile inputs
- Duplicate food entries
- Invalid serving quantities
- Invalid dates
- Persistence after restarting the application
- Viewing, editing, and deleting meal entries
- Weekly summary calculations

## Limitations

- Nutritional values depend on the values entered for each food.
- Calorie targets are estimates and are not medical advice.
- Data is stored locally rather than in an online database.
- The application currently uses a text-based console interface.

## Future Enhancements

- Food search and deletion
- Improved data recovery and error handling
- Nutrient goals and progress reports
- Graphical user interface
- Automated unit testing

## Author

Developed as a Python foundation-level capstone project.
