import re

def check_password_strength(password):
    # Minimum length
    length_error = len(password) < 8

    # Check for uppercase, lowercase, numbers, and special characters
    uppercase_error = not re.search(r'[A-Z]', password)
    lowercase_error = not re.search(r'[a-z]', password)
    digit_error = not re.search(r'\d', password)
    special_char_error = not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Evaluate overall strength
    password_strong = not (length_error or uppercase_error or lowercase_error or digit_error or special_char_error)

    # Return the result
    return {
        'password_strong': password_strong,
        'length_error': length_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'digit_error': digit_error,
        'special_char_error': special_char_error
    }

def main():
    # Get password from the user
    password = input("Enter your password: ")

    # Check password strength
    result = check_password_strength(password)

    # Display the result
    if result['password_strong']:
        print("Password is strong!")
    else:
        print("Password is weak. Please address the following issues:")
        if result['length_error']:
            print("- Minimum password length should be 8 characters.")
        if result['uppercase_error']:
            print("- Include at least one uppercase letter.")
        if result['lowercase_error']:
            print("- Include at least one lowercase letter.")
        if result['digit_error']:
            print("- Include at least one digit.")
        if result['special_char_error']:
            print("- Include at least one special character.")

if __name__ == "__main__":
    main()
