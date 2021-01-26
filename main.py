from cryptography.fernet import Fernet
import sys


def get_key():
    key = Fernet.generate_key()
    return key


def input_key():
    print("Enter your key which we gave you: ")
    key = input()
    return key


def input_password():
    password = input("Enter the password you want to encrypt: ")
    return password


def input_encrypted_password():
    encrypted_password = input("Enter the encrypted hash:")
    return encrypted_password


def encrypt_password(key, password):
    password = password.encode()
    f = Fernet(key)
    encrypted_password = f.encrypt(password)
    return encrypted_password


def decrypt_password(key, encrypted_password):
    f = Fernet(key.encode("utf-8"))
    decrypted_password = f.decrypt(encrypted_password.encode("utf-8"))
    return decrypted_password


while True:
    print('Choose: \n 1. Encrypt password \n 2. Decrypt existing hash \n 3. exit')
    choice = input()
    if choice == '1':
        print("Do not forget this key: ")
        key = get_key()
        print(key.decode("utf-8"))
        password = input_password()
        encrypted_password = encrypt_password(key, password)
        print('Your encrypted password is: ')
        print(encrypted_password.decode("utf-8"))
    if choice == '2':
        key = input_key()
        encrypted_password = input_encrypted_password()
        decrypted_password = decrypt_password(key, encrypted_password)
        print("Your decrypted password is: "+decrypted_password.decode("utf-8"))
    if choice == '3':
        sys.exit()
