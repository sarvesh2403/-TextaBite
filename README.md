# 🍽️ TextaBite

**TextaBite** is a Python-based CLI tool that allows you to retrieve nutritional information from food names using text input. It searches a dataset of common food items and returns key details like calories, protein, fat, carbohydrates, and more.

---

## 🔍 Features

- Search food items by name (case-insensitive, partial match)
- View essential nutrition info (calories, protein, fat, carbs, sugars, fiber)
- Removes duplicate entries for clean results
- Simple and lightweight – works from the command line
- Easily extendable with fuzzy matching or UI

---

## 📊 Sample Output

```
Enter the food name: apple

Food_Item   Category  Calories (kcal)  Protein (g)  Carbohydrates (g)  Fat (g)  Fiber (g)  Sugars (g)
Apple       Fruit     52               0.3          14.0               0.2      2.4        10.0
```

---

## 📁 Dataset

This project uses a CSV file (`daily_food_nutrition_dataset.csv`) containing nutritional data for a variety of common foods. You can expand or modify this file as needed.

### Columns used:
- `Food_Item`
- `Category`
- `Calories (kcal)`
- `Protein (g)`
- `Carbohydrates (g)`
- `Fat (g)`
- `Fiber (g)`
- `Sugars (g)`

---

## 🛠️ How to Use

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/TextaBite.git
cd TextaBite
```

### 2. Install dependencies (if any)
Currently, no external dependencies are required for basic use.

### 3. Run the script
```bash
python textabite.py
```

> 🔁 It will prompt you to enter a food name, and return the matching nutritional info.

---

## 🔧 Optional Enhancements

Want to make it smarter? Add:
- 🔤 **Fuzzy Matching** (for typo-tolerance)
- 🌐 **Web UI** using Streamlit or Flask
- 📦 **Package it** with argparse for CLI flags

---

## 📃 License

MIT License – feel free to use, share, and improve!

---

## 🙌 Contributions

Pull requests and ideas are welcome!  
If you find a bug or have a feature request, feel free to open an issue.

---

## 🧠 Author

Made with care by **Sarvesh R Hampali**  
📧 Contact: [sarveshhampali@gmail.com](mailto:sarveshhampali@gmail.com)
