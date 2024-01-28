import os
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(iv + ciphertext)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    original_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
    with open(original_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def get_user_password():
    password = getpass.getpass("Enter your encryption password: ")
    password_confirm = getpass.getpass("Confirm your encryption password: ")

    if password != password_confirm:
        print("Passwords do not match. Exiting.")
        exit()

    return password

def prompt_for_file_path():
    file_path = input("Enter the path of the file: ")

    if not os.path.isfile(file_path):
        print("File not found. Exiting.")
        exit()

    return file_path

def main():
    password = get_user_password()
    salt = os.urandom(16)
    key = generate_key(password, salt)

    print("Choose an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        file_path = prompt_for_file_path()
        encrypt_file(file_path, key)
        print(f"File encrypted successfully: {file_path}.enc")

    elif choice == "2":
        encrypted_file_path = prompt_for_file_path()
        decrypt_file(encrypted_file_path, key)
        print(f"File decrypted successfully: {encrypted_file_path[:-4]}")

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
