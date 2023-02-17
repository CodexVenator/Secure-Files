from gui import popupgui
from encrypt import EncryptTransactions
import sys

def main():
    gui_object = popupgui()
    encrypt_object = EncryptTransactions()
    filename = gui_object.get_file_path()
    if filename is None:
        sys.exit()
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    if choice in ['E', 'e']:
        password = encrypt_object.get_password()
        if encrypt_object.password_check(password):
            encrypt_object.encrypt_file(filename, encrypt_object.get_key(password))
            print("Done.")
        else:
            print("Please choose a more secure password for your important files.")
    elif choice in ['D', 'd']:
        password = input("Password: ")
        encrypt_object.decrypt_file(filename, encrypt_object.get_key(password))
        print("Done.")
    else:
        print("Closing...")

if __name__ == "__main__":
    main()

