# Programmer: Jordan Gibbs
# Date: 3.12.2024
# Program: Password Generator
# Resources: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os

def hash_password(password, salt):
    # Concatenate the password and salt
    salted_password = password.encode() + salt

    # Hash the salted password using SHA-256 algorithm
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Prompt user to input password
    password = input("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password and salt
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()