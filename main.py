from cryptography.fernet import Fernet


def write_key():
    # This function generates a unique key that we will be using in this file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username: ", username, "\t\tPassword: ",
                  fer.decrypt(password.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input("Type \n"
                 "add to add a new password \n"
                 "view to view existing ones\n"
                 "q to quit\n").lower().strip().lstrip().rstrip()
    print("\n")

    if mode == "q":
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid Mode")
        continue
