
 
from database import initialize_database
import operations as ops
 
 
def print_header(title):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)
 
 
def main_menu():
    print_header("EXPENSE TRACKER")
    print(" 1. Add Expense")
    print(" 2. Show All Expenses")
    print(" 3. Filter by Month")
    print(" 4. Filter by Category")
    print(" 5. Total Spent")
    print(" 6. Average Expense")
    print(" 7. Highest Expenses")
    print(" 8. Category-wise Report")
    print(" 9. Delete Expense")
    print("10. Exit")
    return input("Select an option: ").strip()
 
 
def run():
    initialize_database()
    while True:
        choice = main_menu()
 
        if choice == "1":
            amount = input("Amount: ").strip()
            category = input("Category (e.g. Food/Travel/Rent): ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            description = input("Description (optional): ").strip()
            ops.add_expense(amount, category, date, description)
 
        elif choice == "2":
            ops.show_all_expenses()
 
        elif choice == "3":
            year_month = input("Enter month (YYYY-MM, e.g. 2026-07): ").strip()
            ops.filter_by_month(year_month)
 
        elif choice == "4":
            category = input("Category to filter by: ").strip()
            ops.filter_by_category(category)
 
        elif choice == "5":
            ops.total_spent()
 
        elif choice == "6":
            ops.average_expense()
 
        elif choice == "7":
            n = input("How many top expenses to show? (default 5): ").strip()
            n = int(n) if n else 5
            ops.highest_expenses(n)
 
        elif choice == "8":
            ops.category_wise_report()
 
        elif choice == "9":
            expense_id = input("Expense ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete expense {expense_id}? (y/n): ").strip().lower()
            if confirm == "y":
                ops.delete_expense(expense_id)
            else:
                print("Cancelled.")
 
        elif choice == "10":
            print("\nGoodbye! 👋")
            break
 
        else:
            print("❌ Invalid option. Please choose 1-10.")
 
 
if __name__ == "__main__":
    run()
 
