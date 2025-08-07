from cryptography.fernet import Fernet #Fernet is the class that allows us to encrypt and decrypt data
from getpass import getpass
import os


def writeKey():
    key = Fernet.generate_key() #Generates a new symmetric encryption key
    with open("key.key", "wb") as keyFile:
        keyFile.write(key) #Key is stored in raw bytes



def loadKey():
    if not os.path.exists("key.key"):
        print("Key not found. Generating a new key...")
        writeKey()

    with open("key.key","rb") as keyFile:
        return keyFile.read()

key=loadKey()
fer=Fernet(key) #Initializes the encryption module

def view():
    try:
        with open("passwords.txt","r") as file:
            lines=file.readlines()
            if not lines:
                print("No passwords saved yet.")
                return #Exits the function

            print("\nSaved Credentials: \n")
            print(f"{'Username':<25}{'Password'}")
            print("-"*45)

            for line in lines:
                data=line.rstrip() #Removes characters from the right end only
                userName, encryptedPassword = data.split("|")
                decryptedPassword = fer.decrypt(encryptedPassword.encode()).decode()

                print(f"{userName:<25}{decryptedPassword}")
    except FileNotFoundError:
        print("No passwords file found!")
    except Exception as e:
        print("An error occurred when reading the passwords:", e)

def add():
    name = input("Account Name: ")
    password=getpass("Password (input hidden): ")

    try:
        encryptedPassword=fer.encrypt(password.encode()).decode()
        with open("passwords.txt","a") as f:
            f.write(name + "|" + encryptedPassword + "\n")
        print(f"Password for {name} has been added!")
    except Exception as e:
        print("An error occurred when saving the password:", e)

def main():
    print("Welcome to the Password Manager")
    while True:
        mode=input("\nWould you like to add a new password or view existing passwords (view/add), press 'q' to quit? : ").lower()
        if mode=="q":
            print("Exiting the Password Manager. Goodbye!")
            break
        elif mode == "view":
            view()
        elif mode=="add":
            add()
        else:
            print("Invalid mode!")
            continue #Brings them back to the while loop


if __name__=="__main__":
    main()
