import pandas as pd
from fuzzywuzzy import process

# Load the dataset
df = pd.read_csv(r'C:\Users\sarve\Desktop\Codes\codes1\Projects_simple\calorei_detection\daily_food_nutrition_dataset.csv')

# Select only the necessary columns
columns_to_keep = ['Food_Item', 'Category', 'Calories (kcal)', 'Protein (g)', 
                   'Carbohydrates (g)', 'Fat (g)', 'Fiber (g)', 'Sugars (g)']
df = df[columns_to_keep]

# Remove duplicates and rows with missing Food_Item
df_reduced = df.drop_duplicates(subset='Food_Item', keep='first')
df_reduced = df_reduced[df_reduced['Food_Item'].notna()]

# Prepare choices for fuzzy matching
choices = df_reduced['Food_Item'].dropna().unique()

# Loop for continuous input
while True:
    food_input = input("\nEnter the food name (or type 'exit' to quit): ").strip().lower()

    if food_input == 'exit':
        print("👋 Exiting the program. Stay healthy!")
        break

    best_match = process.extractOne(food_input, choices)

    if best_match and best_match[1] >= 80:  # match score threshold
        matched_food = best_match[0]
        print(f"\n✅ Closest match: '{matched_food}' (Match Score: {best_match[1]}%)\n")
        result = df_reduced[df_reduced['Food_Item'] == matched_food]
        print(result.to_string(index=False))
    else:
        print("❌ Food not found in dataset.")
