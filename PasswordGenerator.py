# Programmer: Jordan Gibbs
# Date: 3.12.2024
# Program: Password Generator
# Resources: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os

def hash_password_with_salt(password, salt):
    # Concatenate the password and salt
    salted_password = password.encode() + salt

    # Hash the salted password using SHA-256 algorithm
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def getpass(prompt="Password: "):
    if os.name == 'nt':
        import msvcrt
    else:
        import tty
        import sys

    print(prompt, end='', flush=True)
    password = b''
    while True:
        char = msvcrt.getch() if os.name == 'nt' else sys.stdin.buffer.read(1)
        if char in {b'\n', b'\r'}:
            print()
            break
        elif char in {b'\x7f', b'\b'}:  # Backspace/Delete
            if password:
                password = password[:-1]
                sys.stdout.write('\b \b')  # Erase the last character
        else:
            password += char
            sys.stdout.write('*')  # Print '*' instead of the character
    return password.decode()

def main():
    # Prompt user to input password without showing characters
    password = getpass("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password with the salt
    hashed_password = hash_password_with_salt(password, salt)

    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()