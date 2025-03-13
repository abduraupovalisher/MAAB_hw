from functools import wraps
import os
import string
from collections import Counter

def check(func):
    """Decorator to ensure denominator is not zero."""
    @wraps(func)
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Employee Records Manager
EMPLOYEE_FILE = "employees.txt"

def add_employee():
    with open(EMPLOYEE_FILE, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!")

def view_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.")
        return
    with open(EMPLOYEE_FILE, "r") as file:
        print("\nEmployee Records:")
        print(file.read())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(EMPLOYEE_FILE, "r") as file:
        for line in file:
            if line.startswith(emp_id):
                print("Employee Found:", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    with open(EMPLOYEE_FILE, "r") as file:
        for line in file:
            data = line.strip().split(", ")
            if data[0] == emp_id:
                name = input("Enter New Name: ") or data[1]
                position = input("Enter New Position: ") or data[2]
                salary = input("Enter New Salary: ") or data[3]
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(line)
    if found:
        with open(EMPLOYEE_FILE, "w") as file:
            file.writelines(updated_records)
        print("Employee record updated.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open(EMPLOYEE_FILE, "r") as file:
        for line in file:
            if not line.startswith(emp_id):
                updated_records.append(line)
            else:
                found = True
    if found:
        with open(EMPLOYEE_FILE, "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted.")
    else:
        print("Employee not found.")

def employee_menu():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add Employee\n2. View Employees\n3. Search Employee\n4. Update Employee\n5. Delete Employee\n6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# Word Frequency Counter
def process_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def word_frequency():
    file_name = "sample.txt"
    if not os.path.exists(file_name):
        print("File does not exist. Please create one.")
        with open(file_name, "w") as file:
            file.write(input("Enter text to create sample.txt: ") + "\n")
    
    with open(file_name, "r") as file:
        content = file.read()
    words = process_text(content)
    word_count = Counter(words)
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)
    
    print(f"\nTotal words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")
    
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")
    print("Word count report saved to word_count_report.txt")

# Run the employee menu
if __name__ == "__main__":
    employee_menu()
    word_frequency()

