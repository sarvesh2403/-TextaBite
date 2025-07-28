import pandas as pd

# Load the dataset
df = pd.read_csv('daily_food_nutrition_dataset.csv')

# Select only the columns you want to keep
columns_to_keep = ['Food_Item', 'Category', 'Calories (kcal)', 'Protein (g)', 
                   'Carbohydrates (g)', 'Fat (g)', 'Fiber (g)', 'Sugars (g)']
df = df[columns_to_keep]

# Drop duplicates by keeping the first entry per 'Food_Item'
df_reduced = df.drop_duplicates(subset=['Food_Item'], keep='first')

# Get food name input from user (case-insensitive search)
food_input = input("Enter the food name: ").lower()

# Search in the reduced dataframe for partial, case-insensitive matches
result = df_reduced[df_reduced['Food_Item'].str.lower().str.contains(food_input)]

if not result.empty:
    # print(f"Found {len(result)} entries for '{food_input}':\n")
    print(result.to_string(index=False))
else:
    print("Food not found in dataset.")
