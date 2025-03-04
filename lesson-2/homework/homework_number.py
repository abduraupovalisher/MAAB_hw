def round_float():
    num = float(input("Enter a float number: "))
    print(f"Rounded to 2 decimal places: {round(num, 2)}")

def find_min_max():
    nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
    print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

def km_to_m_cm():
    km = float(input("Enter kilometers: "))
    print(f"Meters: {km * 1000}, Centimeters: {km * 100000}")

def integer_division():
    a, b = int(input("Enter first number: ")), int(input("Enter second number: "))
    print(f"Quotient: {a // b}, Remainder: {a % b}")

def celsius_to_fahrenheit():
    c = float(input("Enter Celsius temperature: "))
    print(f"Fahrenheit: {(c * 9/5) + 32}")

def last_digit():
    num = int(input("Enter a number: "))
    print(f"Last digit: {num % 10}")

def check_even():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")
