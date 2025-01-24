
import datetime
import json

def load_nutrition_data(filename="nutrition_data.json"):
    """Loads nutrition data from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it first.")
        return {}  # Returns an empty dictionary if not found

def create_nutrition_data_file(filename = "nutrition_data.json"):
    """Creates a json file for the nutrition information of foods"""
    with open(filename, 'w') as f:
        json.dump({
            "apple": {"calories": 95, "protein": 0.3, "carbs": 25, "fat": 0.3, "fiber": 4.4, "sugar": 19},
            "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4, "fiber": 3.1, "sugar": 14},
            "milk": {"calories": 120, "protein": 8, "carbs": 12, "fat": 5, "calcium": 300}, #Example with a nutrient that is not fiber, sugar, carbs, protein or fat
            "eggs": {"calories": 70, "protein": 6, "carbs": 0.5, "fat": 5, "cholesterol": 215}, #Example with a nutrient that is not fiber, sugar, carbs, protein or fat
            "bread": {"calories": 75, "protein": 3, "carbs": 15, "fat": 1}, #Example with a nutrient that is not fiber, sugar, carbs, protein or fat
            "chicken breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6, "sodium": 65},  # Example with sodium
            "rice": {"calories": 200, "protein": 4, "carbs": 45, "fat": 0.4} # Example without sodium

        }, f, indent=4)
        print("Nutriton data file created")

def process_bill_item(item, quantity, nutrition_data):
    """Processes a single bill item and calculates its nutritional value."""
    item = item.lower()  # Normalize the item name to lowercase
    if item in nutrition_data:
        nutrition = nutrition_data[item]
        nutrient_values = {}
        for nutrient, value in nutrition.items():
            nutrient_values[nutrient] = value * quantity
        return nutrient_values
    else:
        print(f"Warning: Nutrition data not found for '{item}'.")
        return {}

def process_bill(bill_text, nutrition_data):
    """Processes the entire grocery bill to get nutritional information."""
    total_nutrition = {}
    lines = bill_text.strip().split("\n")
    for line in lines:
        try:
            parts = line.split(",")
            if len(parts) == 2:
                item_name, quantity_str = parts
                quantity = float(quantity_str.strip())
                item_name = item_name.strip()
                item_nutrition = process_bill_item(item_name, quantity, nutrition_data)
                for nutrient, value in item_nutrition.items():
                    total_nutrition[nutrient] = total_nutrition.get(nutrient, 0) + value

            else:
                print(f"Skipping line: '{line}'. Format should be 'Item, quantity'")

        except Exception as e:
            print(f"Error processing line '{line}': {e}")

    return total_nutrition

def get_bill_from_file(filename):
    """Gets a bill from a text file"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        return ""

def generate_monthly_report(monthly_data):
    """Generates a report for the end of month """
    print("\n----- Monthly Nutritional Report -----\n")
    for date, nutrition in monthly_data.items():
        print(f"Date: {date}")
        for nutrient, value in nutrition.items():
            print(f"  {nutrient}: {value:.2f}")
        print("-----\n")

def main():
    nutrition_data_file = "nutrition_data.json"
    create_nutrition_data_file(nutrition_data_file)
    nutrition_data = load_nutrition_data(nutrition_data_file)
    monthly_data = {}
    while True:
        choice = input("Select an option:\n1. Process Bill\n2. View Monthly Report\n3. Exit\n")

        if choice == "1":
            bill_file = input("Enter the file name for your grocery bill:\n")
            bill_text = get_bill_from_file(bill_file)

            if bill_text:
                today = datetime.date.today().strftime("%Y-%m-%d")
                bill_nutrition = process_bill(bill_text, nutrition_data)
                monthly_data.setdefault(today, {}).update(bill_nutrition)  # Update nutrition for today

                print(f"Nutritional breakdown for {today}:")
                for nutrient, value in bill_nutrition.items():
                    print(f"  {nutrient}: {value:.2f}")
                print("\n Bill processed Successfully")
        elif choice == "2":
            if monthly_data:
                generate_monthly_report(monthly_data)
            else:
                print("No data available to view report")

        elif choice == "3":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()