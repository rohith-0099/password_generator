import random
import string

def generate_password(length, include_uppercase, include_digits, include_symbols):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    characters = list(lowercase_chars)
    password = []

    if include_uppercase:
        characters.extend(list(uppercase_chars))
        password.append(random.choice(uppercase_chars))
    if include_digits:
        characters.extend(list(digit_chars))
        password.append(random.choice(digit_chars))
    if include_symbols:
        characters.extend(list(symbol_chars))
        password.append(random.choice(symbol_chars))

    if not include_uppercase and not include_digits and not include_symbols and length > 0:
        password.append(random.choice(lowercase_chars))

    if length < len(password):
        return "".join(password[:length])

    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

def main():
    print("--- Random Password Generator ---")

    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for length.")

    while True:
        include_uppercase_str = input("Include uppercase letters? (yes/no): ").lower()
        if include_uppercase_str in ['yes', 'y']:
            include_uppercase = True
            break
        elif include_uppercase_str in ['no', 'n']:
            include_uppercase = False
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    while True:
        include_digits_str = input("Include numbers? (yes/no): ").lower()
        if include_digits_str in ['yes', 'y']:
            include_digits = True
            break
        elif include_digits_str in ['no', 'n']:
            include_digits = False
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    while True:
        include_symbols_str = input("Include symbols? (yes/no): ").lower()
        if include_symbols_str in ['yes', 'y']:
            include_symbols = True
            break
        elif include_symbols_str in ['no', 'n']:
            include_symbols = False
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if not include_uppercase and not include_digits and not include_symbols:
        print("Warning: No character types selected except lowercase. The password will only contain lowercase letters.")
        if length > 0:
            print("To ensure a password is generated, lowercase letters will be included.")

    password = generate_password(length, include_uppercase, include_digits, include_symbols)

    print(f"\nGenerated Password: {password}")
    print("-------------------------------")

if __name__ == "__main__":
    main()
