import re

def validate_gmail(email):
    if not email:
        return "Email cannot be empty."

    first = email[0]

    if first.isdigit():
        return "Invalid email: It must start with a lowercase letter, not a number."
    elif first.isupper():
        return "Invalid email: It must start with a lowercase letter, not a capital letter."
    elif not first.isalpha():
        return "Invalid email: It must start with a lowercase letter, not a symbol."

    if any(char.isupper() for char in email):
        return "Invalid email: Capital letters are not allowed."

    if any(char.isspace() for char in email):
        return "Invalid email: Spaces are not allowed."

    if not email.endswith("@gmail.com"):
        return "Invalid email: It must end with @gmail.com."

    username = email[:-10]  # Remove "@gmail.com"

    if not username:
        return "Invalid email: Add a username before @gmail.com."

    if not re.fullmatch(r"[a-z0-9._%+-]+", username):
        return "Invalid email: The username contains a symbol that is not allowed."

    return "Valid email address."


email = input("Enter the email ID: ")
print(validate_gmail(email))