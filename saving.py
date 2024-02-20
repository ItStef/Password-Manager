
import tkinter as tk
import encrypt as ec

def saving_account(window: tk.Tk):
    password_field = tk.Entry(window, show="*")
    password_field.pack()

    def save_password():
        password = password_field.get()
        key = ec.get_key()
        ciphertext = ec.encrypt(password,key = key)
        with open("passwords.txt", "wb") as file:
            file.write(key + b"|KEY-DATA-DEVIDER|" + ciphertext)    #combine key - password pair with devider
        password_field.delete(0, "end")
    save_button = tk.Button(window, text="Save", command=save_password)
    save_button.pack()
    
    # Create a button to decrypt the password
    def decrypt_password():
        with open("passwords.txt", "rb") as file:
            key, ciphertext = file.read().split(b"|KEY-DATA-DEVIDER|")  #split key - password pair with devider
        password = ec.decrypt(ciphertext,key)
    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_password)
    decrypt_button.pack()
