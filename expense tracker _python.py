#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import json


expenses = []


categories = ['Food', 'Transportation', 'Entertainment', 'Bills', 'Miscellaneous']


def add_expense():
    """
    Function to add a new expense to the expenses list.
    """
    print("\nAdding Expense:")
    description = input("Enter a brief description: ")
    while True:
        try:
            amount = float(input("Enter the amount spent ($): "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid number.")

    print("Select a category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:
        try:
            category_index = int(input("Enter category number: "))
            if category_index < 1 or category_index > len(categories):
                raise ValueError("Invalid category number.")
            selected_category = categories[category_index - 1]
            break
        except (ValueError, IndexError):
            print("Invalid category number. Please enter a valid number.")

    timestamp = datetime.datetime.now()
    expense = {
        'timestamp': timestamp,
        'description': description,
        'amount': amount,
        'category': selected_category
    }
    expenses.append(expense)
    print("Expense added successfully.")


def edit_expense():
    """
    Function to edit an existing expense.
    """
    print("\nEditing Expense:")
    print_expenses()
    try:
        index = int(input("Enter the index of the expense to edit: "))
        if index < 1 or index > len(expenses):
            raise IndexError("Invalid expense index.")
        
        expense = expenses[index - 1]
        print(f"Editing expense #{index}:")
        print(f"Description: {expense['description']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        
     
        new_description = input("Enter new description (leave blank to keep current): ")
        if new_description.strip():
            expense['description'] = new_description.strip()
        
        while True:
            try:
                new_amount = float(input(f"Enter new amount ($), current: ${expense['amount']:.2f}: "))
                if new_amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                expense['amount'] = new_amount
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please enter a valid number.")
        
        print("Select a new category:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        
        while True:
            try:
                category_index = int(input("Enter category number: "))
                if category_index < 1 or category_index > len(categories):
                    raise ValueError("Invalid category number.")
                expense['category'] = categories[category_index - 1]
                break
            except (ValueError, IndexError):
                print("Invalid category number. Please enter a valid number.")
        
        expense['timestamp'] = datetime.datetime.now()
        print("Expense edited successfully.")
    
    except (IndexError, ValueError) as e:
        print(f"Error editing expense: {str(e)}")


def delete_expense():
    """
    Function to delete an existing expense.
    """
    print("\nDeleting Expense:")
    print_expenses()
    try:
        index = int(input("Enter the index of the expense to delete: "))
        if index < 1 or index > len(expenses):
            raise IndexError("Invalid expense index.")
        
        expense = expenses.pop(index - 1)
        print(f"Expense #{index} deleted successfully:")
        print(f"Description: {expense['description']}")
        print(f"Amount: ${expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
    
    except (IndexError, ValueError) as e:
        print(f"Error deleting expense: {str(e)}")


def monthly_summary():
    """
    Function to display a monthly summary of expenses.
    """
    today = datetime.date.today()
    current_month = today.month
    current_year = today.year

    total_expense = 0
    for expense in expenses:
        if expense['timestamp'].month == current_month and expense['timestamp'].year == current_year:
            total_expense += expense['amount']

    print(f"\n----- Monthly Summary: {today.strftime('%B %Y')} -----")
    print(f"Total expenses: ${total_expense:.2f}")


def category_summary():
    """
    Function to display a category-wise summary of expenses.
    """
    print("\nCategory-wise Summary:")
    category_totals = {category: 0 for category in categories}
    for expense in expenses:
        category_totals[expense['category']] += expense['amount']

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


def print_expenses():
    """
    Function to print all existing expenses.
    """
    if not expenses:
        print("No expenses to display.")
        return
    
    print("\nCurrent Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f} - {expense['category']}")


def display_menu():
    """
    Function to display the main menu of the expense tracker.
    """
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Edit Expense")
    print("3. Delete Expense")
    print("4. View Monthly Summary")
    print("5. View Category-wise Summary")
    print("6. Exit")


def save_data():
    """
    Function to save the current expenses list to a JSON file.
    """
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, default=str)
    print("Expense data saved successfully.")


def load_data():
    """
    Function to load expenses from a JSON file into the expenses list.
    """
    global expenses
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
        print("Expense data loaded successfully.")
    except FileNotFoundError:
        print("No existing expense data found.")


def main():
    """
    Main function to run the expense tracker application.
    """
    print("Welcome to the Expense Tracker App!")
    load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            edit_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            category_summary()
        elif choice == '6':
            save_data()  # Save data before exiting
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()


# # Functionality: This script includes all essential features:
# 
# Add Expense: Allows users to input a new expense with description, amount, and category.
# Edit Expense: Enables users to edit an existing expense's description, amount, and category.
# Delete Expense: Allows users to delete an existing expense from the list.
# Monthly Summary: Displays the total expenses for the current month.
# Category-wise Summary: Displays the total expenses categorized by predefined categories.
# User Interface: Presents a command-line interface (CLI) with a main menu for user interaction.
# Error Handling: Basic error handling is implemented to manage unexpected user inputs.
# Data Storage: Saves and loads expense data to/from a JSON file (expenses.json) for persistence across sessions.
# Documentation: Each function is documented with docstrings to explain its purpose and usage.

# In[ ]:




