# 🍽️ TextaBite

**TextaBite** is a Python-based CLI tool that allows you to retrieve nutritional information from food names using text input. It searches a dataset of common food items and returns key details like calories, protein, fat, carbohydrates, and more.

---

## 🔍 Features

- 🔤 Search food items by name (case-insensitive, partial match)
- 🧠 Uses **fuzzy matching** to find the closest food name even if there are typos or partial inputs
- 🔁 **Continuous input loop**: Keep searching for different foods until you type `exit` to quit
- 📊 View essential nutrition info (calories, protein, fat, carbs, sugars, fiber)
- 🧹 Removes duplicate entries for clean results
- 🖥️ Simple and lightweight – works from the command line
- 🚀 Easily extendable with a web UI or advanced matching techniques

---

## 📊 Sample Output

```
Enter the food name (or type 'exit' to quit): chickn

✅ Closest match: 'Chicken' (Match Score: 91%)

Food_Item  Category  Calories (kcal)  Protein (g)  Carbohydrates (g)  Fat (g)  Fiber (g)  Sugars (g)
Chicken    Protein   239              27.3         0.0                13.6     0.0        0.0

Enter the food name (or type 'exit' to quit): exit
👋 Exiting the program. Stay healthy!
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

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python textabite.py
```

> 🔁 You can enter multiple food names in sequence; type `exit` to quit.

---

## 🔧 Optional Enhancements

Want to make it smarter? Consider adding:

- 🔤 **Improved fuzzy matching** or typo tolerance
- 🌐 **Web UI** using Streamlit or Flask
- 📦 **Packaging** with CLI flags using `argparse`
- 🧪 **Unit tests** for robustness and maintainability

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
