# Personal Expense Analyzer 💰

A Python-based command-line application to track, manage, and analyze personal expenses. The application supports expense management, spending calculations, filtering, and persistent data storage using JSON.

## 🚀 Features

- **Add Expenses:** Record expense name, amount, and category.
- **View Expenses:** Display all recorded expenses in an organized format.
- **Calculate Total Spending:** Calculate the total amount spent.
- **Find Highest Expense:** Identify the most expensive transaction.
- **Filter Expenses:** Display expenses above a user-defined amount.
- **Input Validation:** Handle invalid inputs and prevent empty entries or non-positive expense amounts.
- **JSON Persistence:** Automatically save expenses and load them when the application restarts.

## 🛠️ Technologies Used

- Python 3
- JSON
- OS Module
- Git & GitHub

## 📂 Project Structure

```text
personal-expense-analyzer/
│
├── main.py
├── .gitignore
├── expenses.json       # Generated locally
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/personal-expense-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd personal-expense-analyzer
```

### 3. Run the application

```bash
python main.py
```

## 📌 Application Menu

```text
------------------------------
Personal Expense Tracker
------------------------------
1. Add Expense
2. View Expenses
3. Calculate Total Spending
4. Find Highest Expense
5. Exit
6. Filter Expenses
```

## 💾 Data Storage

The application uses JSON for local data persistence.

- Expenses are stored in `expenses.json`.
- Existing expenses are loaded when the application starts.
- New expenses are saved automatically after being added.
- The JSON file is excluded from Git tracking to protect personal expense records.

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Python variables and data types
- Lists and dictionaries
- Conditional statements and loops
- Functions and modular programming
- Exception handling
- File handling
- JSON serialization and deserialization
- Data filtering and iteration
- Basic Git and GitHub version control

## 🔮 Future Improvements

- Expense category-wise analysis
- Monthly spending reports
- Expense visualization using charts
- Edit and delete expense functionality
- Export reports to CSV
- GUI-based interface

## 👨‍💻 Author

**Siddhesh Gire**

B.Tech Artificial Intelligence and Machine Learning Student

---

⭐ If you find this project useful, consider giving it a star!