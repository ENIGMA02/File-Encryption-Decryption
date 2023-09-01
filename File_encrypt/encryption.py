import subprocess
import os

def encrypt_file(file_path, recipient=None):
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file.")
        return

    if recipient:
        command = f"gpg --encrypt --recipient {recipient} {file_path}"
    else:
        command = f"gpg --symmetric {file_path}"


    try:
        subprocess.run(command, shell=True, check=True)
        print(f"File '{file_path}' successfully encrypted.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def decrypt_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file.")
        return

    command = f"gpg --decrypt {file_path}"

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"File '{file_path}' successfully decrypted.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    choice = input("Encrypt (e) or decrypt (d) a file? ").lower()

    if choice == "e":
        file_path = input("Enter the path to the file you want to encrypt: ")
        recipient = input("Enter the recipient's key ID (if using asymmetric encryption, leave blank for symmetric encryption): ")
        encrypt_file(file_path, recipient)
    elif choice == "d":
        file_path = input("Enter the path to the file you want to decrypt: ")
        decrypt_file(file_path)
    else:
        print("Invalid choice. Please choose 'e' or 'd'.")
