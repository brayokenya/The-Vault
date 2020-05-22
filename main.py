

# menu
from user import User


def menu():
    print("Please select an Option")
    print("\tWelcome To The Vault")
    print("1. Store User credentials")
    print("2. Password Generator ")
    print("3. Exit")
# password generator


def password_generator():
    pass


def store_accounts():
    no_of_accounts = int(input("How many accounts would you like to enter? "))
    # input account credentials
    for n in range(no_of_accounts):
        # list to hold user input
        accounts = []
        service_provider = input("\nEnter the service provider: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        # create instance of Account class
        account = User(service_provider, username, password)
        accounts.append(account)
    # output
    for i in accounts:
        print("\nService: {}, Username: {},Password:{}".format(
            account.service_provider, account.username, account.password))
        print("\nYour account credentials have been stored")
        print("="*15)


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
