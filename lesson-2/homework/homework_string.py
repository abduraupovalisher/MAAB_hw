def name_age():
    name, birth_year = input("Enter your name: "), int(input("Enter your birth year: "))
    print(f"Hello {name}, your age is {2024 - birth_year}")

def extract_car_names():
    txt = 'LMaasleitbtui'
    print("Car names extracted: ", txt[::2])

def string_operations():
    s = input("Enter a string: ")
    print(f"Length: {len(s)}, Uppercase: {s.upper()}, Lowercase: {s.lower()}")

def palindrome_check():
    s = input("Enter a string: ")
    print("Palindrome" if s == s[::-1] else "Not a palindrome")

def count_vowels_consonants():
    s = input("Enter a string: ").lower()
    vowels = sum(1 for c in s if c in "aeiou")
    consonants = sum(1 for c in s if c.isalpha() and c not in "aeiou")
    print(f"Vowels: {vowels}, Consonants: {consonants}")

def substring_check():
    s1, s2 = input("Enter first string: "), input("Enter second string: ")
    print("Contained" if s2 in s1 else "Not contained")

def replace_word():
    sentence, old, new = input("Enter sentence: "), input("Word to replace: "), input("New word: ")
    print(sentence.replace(old, new))

def first_last_chars():
    s = input("Enter a string: ")
    print(f"First: {s[0]}, Last: {s[-1]}")

def reverse_string():
    print(input("Enter a string: ")[::-1])

def count_words():
    print(f"Word count: {len(input('Enter a sentence: ').split())}")

def contains_digits():
    print("Contains digit" if any(c.isdigit() for c in input("Enter a string: ")) else "No digits")

def join_words():
    words = input("Enter words separated by space: ").split()
    print("-".join(words))

def remove_spaces():
    print(input("Enter a string: ").replace(" ", ""))

def check_strings_equal():
    print("Equal" if input("Enter first string: ") == input("Enter second string: ") else "Not equal")

def create_acronym():
    print("".join([word[0].upper() for word in input("Enter a sentence: ").split()]))

def remove_character():
    s, char = input("Enter a string: "), input("Enter character to remove: ")
    print(s.replace(char, ""))

def replace_vowels():
    print("".join(["*" if c in "aeiouAEIOU" else c for c in input("Enter a string: ")]))

def check_start_end():
    s, start, end = input("Enter a string: "), input("Start word: "), input("End word: ")
    print("Valid" if s.startswith(start) and s.endswith(end) else "Invalid")

