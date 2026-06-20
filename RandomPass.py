import random
import string

def generate_password():
    chars = string.ascii_lowercase + string.digits

    password = ""

    for i in range(8):
        password += random.choice(chars)

    return password

def save_password(username, password):
    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"{username} : {password}\n")

def main():
    username = input("Enter username: ")

    while True:
        password = generate_password()

        print("\nSuggested password:")
        print(password)

        choice = input(
            "\nClick 's' for saving password, and click anything else to remake password: "
        )

        if choice.lower() == "s":
            save_password(username, password)
            print("Password saved.")
            break

main()