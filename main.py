
# menu
import random
import pyperclip
from user import User
from credential import Credential
import login


def menu():
    print("="*35)
    print("\nPlease select an Option")
    print("\tWelcome To The Vault")
    print("1. Store User credentials")
    print("2. Password Generator ")
    print("3. Exit")

# password generator


def password_generator():
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
    number_of_passwords = int(
        input("\nHow many passwords would you like? :"))
    length_of_password = int(input("\nLength of password? :"))

    for p in range(number_of_passwords):
        password = ''
        for c in range(length_of_password):
            password += random.choice(characters)
        pyperclip.copy(password)
        password = pyperclip.paste()
        print(password)


def store_accounts():
    # list to hold user input
    credentials = []
    no_of_accounts = int(
        input("How many accounts would you like to enter? "))
    # input account credentials
    for n in range(no_of_accounts):

        service_provider = input("\nEnter the service provider: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        # create instance of Credential  class
        credential = Credential(service_provider, username, password)
        credentials.append(credential)

    # output
    print("\nYour credential credentials have been stored")
    print("="*15)
    for credential in credentials:
        print("\nService: {}, Username: {},Password:{}".format(
            credential.service_provider, credential.username, credential.password))


# no of accounts
menu()
while True:
    print("="*15)
    menu_choice = int(input("Please select your option (1,2 or 3) "))
    if menu_choice == 1:
        print("\nStore account credentials")
        print("="*15)
        store_accounts()
        menu()
    elif menu_choice == 2:
        print("\nPassword Generator")
        print("="*15)
        password_generator()
    elif menu_choice == 3:
        break
    else:
        print("Please enter a number between 1 and 3")
        menu()
