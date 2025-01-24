# Grocery Nutrition Tracker
Tracking grocery purchases and how much of that adds to nutrional intake.

**How to Use:**

1.  **Save:** Save the code as `grocery_nutrition_tracker.py`.
2.  **Run:** Execute it from your terminal: `python grocery_nutrition_tracker.py`
3.  **Data Entry**
    *   The first time you run it it will create a "nutrition\_data.json" file.
    *   You can add, modify or delete nutritional values from the JSON file. (Just be mindful of the JSON format).
    *   You must have your grocery bill in a plain text file (*.txt), each line with the format `item_name, quantity`
        *   For example:
            ```
            apple, 2
            banana, 1
            milk, 1
            bread, 2
            chicken breast, 1
            ```

**Explanation:**

1.  **`load_nutrition_data(filename)` and `create_nutrition_data_file()`:**
    *   Loads nutrition data from a JSON file, created when the script first starts. This file can be edited to include nutrition for a wider range of foods.
    *   The nutrition data is stored as a dictionary, where keys are the food item and the values are dictionaries with nutrients and their values per unit.
2.  **`process_bill_item(item, quantity, nutrition_data)`:**
    *   Takes a single item, its quantity, and the nutrition data.
    *   It looks up the item in the `nutrition_data`.
    *   Calculates the total nutrients for the specified quantity
    *   Returns a dictionary with nutrients and their totals for that item.
3.  **`process_bill(bill_text, nutrition_data)`:**
    *   Takes the text from the whole grocery bill, splits it into lines, each line is processed by the `process_bill_item`
    *   Aggregates nutrients over the whole bill, and returns a dictionary with the total of each nutrient
4.  **`get_bill_from_file()`:**
    *   Takes a file name, opens the file and returns all the text from it.
5.  **`generate_monthly_report(monthly_data)`:**
    *   Takes monthly data (a dictionary of date with a dictionary of nutrients) and prints a report of that data.
6.  **`main()`:**
    *   Contains the main loop of the application:
        *   Loads the nutrition data from the file.
        *   Presents options to process the bill, view monthly reports and exit the program.
        *   Takes user input for a text file, processes the data from the file, and prints a nutritional breakdown of the bill.
        *   Stores each bill processed during the month in the dictionary monthly\_data.

**Key Improvements and Challenges:**

1.  **Data Entry:**
    *   Currently relies on a very specific plain text format (`item, quantity`). Realistically, we would need a more flexible system for parsing bills, including different formats, like extracting data from a picture of the bill.
2.  **Nutrition Database:**
    *   The `nutrition_data.json` file is very limited and has to be built manually.
    *   **Solution:** Integrate with an external API (like the USDA FoodData Central API or similar) to access a large database. This would require handling API requests and managing API keys.
3.  **Natural Language Processing (NLP):**
    *   Currently, the script depends on exact item names.
    *   **Solution:** Use NLP to identify items, quantities, and units from a more flexible text input, allowing for variations in wording.
4.  **Data Storage:**
    *   The script stores everything in memory and `monthly_data`. If the program closes data is lost.
    *   **Solution:** Use a database (like SQLite or PostgreSQL) to store historical data for analysis and reporting.
5.  **Unit Handling:**
    *   The script assumes that quantities are all in one unit. We need to be able to handle different units (grams, liters, etc).
    *   **Solution:** Use a library or an algorithm for converting between different units, making sure that we are using the correct nutritional values.
6.  **Error Handling:**
    *   Currently does not handle errors from the json, files, API, or wrong input.
    *   **Solution:** Implement a robust error handling system, using `try-except` clauses or other approaches.

**Next Steps:**

1.  **API Integration:**  Start with a basic API call to the USDA database.
2.  **Simple GUI:** Explore GUI options with libraries like Tkinter or PyQt to make the app more user-friendly.
3.  **Database Implementation:** Use SQLite to store processed data.

Let me know if you'd like to delve into any of these improvements or any other aspect of this project!