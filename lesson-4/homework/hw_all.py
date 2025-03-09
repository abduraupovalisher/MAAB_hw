from random import randint

def uncommon_elements(list1, list2):
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []
    
    for key in set(list1 + list2):
        if key in count1 and key in count2:
            count_diff = abs(count1[key] - count2[key])
            result.extend([key] * count_diff)
        else:
            result.extend([key] * (count1[key] if key in count1 else count2[key]))
    return result

def squares_less_than_n(n):
    for i in range(1, n):
        print(i * i)

def format_text(txt):
    result = []
    i = 0
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0:
            if i + 1 < len(txt) and txt[i + 1] in "aeiou":
                result.append(txt[i + 1])
                i += 1
            result.append("_")
        i += 1
    return "".join(result)

def number_guessing_game():
    while True:
        number = randint(1, 100)
        attempts = 10
        
        while attempts > 0:
            guess = int(input("Enter your guess: "))
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return
            attempts -= 1
        
        print("You lost. Want to play again?")
        retry = input().lower()
        if retry not in ['y', 'yes', 'ok']:
            break

def password_checker():
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password is too short.")
    elif not any(c.isupper() for c in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

def prime_numbers():
    for num in range(2, 101):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            print(num, end=" ")
    print()


