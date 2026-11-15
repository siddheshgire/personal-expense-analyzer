import json
import os


def display_menu():    
    print("-" * 30)
    print("Personal Expense Tracker")
    print("-" * 30)

    print(" 1. Add Expense")
    print(" 2. View Expenses")
    print(" 3. Calculate total Spending")
    print(" 4. Find Highest Expense")
    print(" 5. Exit")
    print(" 6. Filter Expenses")

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json",'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open("expenses.json", 'w') as file:
        json.dump(expenses, file, indent = 4)

def filter_expenses(expenses, minimum_amount):
    found = False
    for expense in expenses:
        if expense['amount'] > minimum_amount:
            print("-" * 15)
            print(f"{expense['name']} - ₹{expense['amount']:.2f}")
            found = True
    if not found:
        print("No Expenses found above this amount!")


def add_expense(expenses):
    while True:
        name = input("Expense Name: ").strip()
        if name == "":
            print("Invalid name! Please enter a name.")
            continue
        break

    while True:
        try:
            amount = float(input("Expense Amount: "))
            if amount <= 0:
                print("Amount must be greater that 0")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number")
    while True:
        category = input("Expense Category: ").strip()
        if category == "":
            print("Invalid Category! Please Try again")
            continue
        break


    expense = {
        "name" : name,
        "amount" : amount,
        "category" : category
    }
    expenses.append(expense)
    return expenses





def view_expenses(expenses):
    if not expenses:
        print("No expenses Found..!")
    else:
        print("\n" + "-" * 40)
        print("           ALL EXPENSES")
        print("-" * 40)

        for index, expense in enumerate(expenses, start = 1):
            print(f"{index}.  {expense['name']}")
            print(f"    Amount: ₹{expense['amount']:.2f}")
            print(f"    Category: {expense['category']}")
            print("-" * 40)


def calculate_total(expenses):
    if not expenses:
        return 0

    total = 0

    for expense in expenses:
        total = total + expense['amount']

    return total




def find_highest_expense(expenses):
    if not expenses:
        return None

    
    highest_expense = expenses[0]
    for expense in expenses:
        if expense['amount'] > highest_expense['amount']:
            highest_expense = expense

    return highest_expense



def main():
    expenses = load_expenses()


    while True:
        display_menu()
        choice = input("Enter Your Choice: ")
        if choice == '1':
            expenses = add_expense(expenses)
            save_expenses(expenses)

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            total = calculate_total(expenses)

            print("-" * 30)        
            print(f"Total Spending:₹{total:.2f}")
            print("-" * 30)

        elif choice == '4':
            highest = find_highest_expense(expenses)

            if highest is None:
                print("No expenses found")
            else:
                print(f"-------Highest Expense-------")
                print(f"Expense Name: {highest['name']}")
                print(f"Amount: ₹{highest['amount']:.2f}")
                print(f"Category: {highest['category']}")
                


          
        elif choice == '5':
            print("Thank you for using Personal Expense Tracker!")
            break

        elif choice == '6':
            while True:
                try:
                    minimum_amount = float(input("Enter minimum amount: "))
                    if minimum_amount <= 0:
                        print("invalid amount!!")
                        continue
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
            filter_expenses(expenses, minimum_amount)


if __name__ == "__main__":
    main()  