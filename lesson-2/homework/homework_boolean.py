def validate_user():
    print("Valid" if input("Enter username: ") and input("Enter password: ") else "Invalid")

def check_numbers_equal():
    print("Equal" if int(input("Enter first number: ")) == int(input("Enter second number: ")) else "Not equal")

def check_positive_even():
    num = int(input("Enter a number: "))
    print("Positive and even" if num > 0 and num % 2 == 0 else "Not both")

def check_all_different():
    nums = {int(input(f"Enter number {i+1}: ")) for i in range(3)}
    print("All different" if len(nums) == 3 else "Not all different")

def check_same_length():
    print("Same length" if len(input("Enter first string: ")) == len(input("Enter second string: ")) else "Different lengths")

def check_divisible_3_5():
    num = int(input("Enter a number: "))
    print("Divisible by 3 and 5" if num % 3 == 0 and num % 5 == 0 else "Not divisible")

def sum_greater_50():
    print("Greater than 50" if int(input("Enter first number: ")) + int(input("Enter second number: ")) > 50 else "Not greater")

def check_range():
    print("In range" if 10 <= int(input("Enter a number: ")) <= 20 else "Out of range")
