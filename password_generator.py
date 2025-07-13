import random
import string
#calculating password strength
def calculate_password_strength(password):
    length = len(password)
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
#different char types
    #selecting according to provided option
    char_types = sum([has_lowercase, has_uppercase, has_digit, has_symbol])
    score += char_types

    if score >= 6:
        return "Strong"
    elif score >= 4:
        return "Medium"
    else:
        return "Weak"
#generating password
def generate_password(length, include_uppercase, include_digits, include_symbols, exclude_ambiguous):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    ambiguous_chars = 'lIO0'

    all_possible_chars = []
    required_chars = []
#uppercase
    if include_uppercase:
        chars_to_add = [c for c in uppercase_chars if not (exclude_ambiguous and c in ambiguous_chars)]
        all_possible_chars.extend(chars_to_add)
        if chars_to_add:
            required_chars.append(random.choice(chars_to_add))
#digits
    if include_digits:
        chars_to_add = [c for c in digit_chars if not (exclude_ambiguous and c in ambiguous_chars)]
        all_possible_chars.extend(chars_to_add)
        if chars_to_add:
            required_chars.append(random.choice(chars_to_add))

    if include_symbols:
        chars_to_add = [c for c in symbol_chars if not (exclude_ambiguous and c in ambiguous_chars)]
        all_possible_chars.extend(chars_to_add)
        if chars_to_add:
            required_chars.append(random.choice(chars_to_add))

    base_lowercase_chars = [c for c in lowercase_chars if not (exclude_ambiguous and c in ambiguous_chars)]
    all_possible_chars.extend(base_lowercase_chars)
    
    if not required_chars and length > 0 and base_lowercase_chars:
        required_chars.append(random.choice(base_lowercase_chars))

    #all possible charaters
    all_possible_chars = list(set(all_possible_chars))

    if not all_possible_chars:
        print("Warning: No valid characters to generate password based on your criteria. Using all lowercase as fallback.")
        all_possible_chars = list(lowercase_chars)

    if len(required_chars) > length:
        return "".join(random.sample(required_chars, length))

    password_chars = required_chars[:]
    for _ in range(length - len(required_chars)):
        password_chars.append(random.choice(all_possible_chars))

    random.shuffle(password_chars)

    return "".join(password_chars)

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def main():
    print("--- Welcome to the Advanced Random Password Generator ---")
    print("Create strong and secure passwords tailored to your needs.\n")

    while True:
        while True:
            try:
                length = int(input("Enter desired password length (minimum recommended 8, e.g., 12): "))
                if length <= 0:
                    print("Password length must be a positive number.")
                elif length < 8:
                    print("Warning: For better security, a minimum length of 8 characters is strongly recommended.")
                    if length < 4 and length > 0:
                        print("A length this short will result in a very weak password.")
                    break
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for length.")

        include_uppercase = get_yes_no_input("Include uppercase letters? (yes/no): ")
        include_digits = get_yes_no_input("Include numbers? (yes/no): ")
        include_symbols = get_yes_no_input("Include symbols? (yes/no): ")
        
        exclude_ambiguous = get_yes_no_input("Exclude ambiguous characters (e.g., 'l', 'I', 'O', '0')? (yes/no): ")

        if not (include_uppercase or include_digits or include_symbols):
            if length > 0:
                print("Warning: No character types selected except lowercase. The generated password will only contain lowercase letters.")
            else:
                print("Warning: Password length is 0. No password will be generated.")
                if not get_yes_no_input("Do you want to try again with a valid length? (yes/no): "):
                    break
                else:
                    continue

        #change according to condition
        while True:
            try:
                num_passwords = int(input("How many passwords do you want to generate? (e.g., 1): "))
                if num_passwords <= 0:
                    print("Please enter a positive number for the quantity.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("\n--- Generated Passwords ---")
        for i in range(num_passwords):
            password = generate_password(length, include_uppercase, include_digits, include_symbols, exclude_ambiguous)
            strength = calculate_password_strength(password)
            print(f"Password {i+1}: {password} (Strength: {strength})")
        print("---------------------------\n")

        generate_again = get_yes_no_input("Generate more passwords? (yes/no): ")
        if not generate_again:
            break

if __name__ == "__main__":
    main()
    print("Thank you for using the password generator! Stay secure.")

if __name__ == "__main__":
    main()
