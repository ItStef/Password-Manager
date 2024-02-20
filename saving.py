
import tkinter as tk
import encrypt as ec

def saving_account(window: tk.Tk):

    account_for_label = tk.Label(window, text="Account for: ")
    account_for_label.pack()
    account_for_field = tk.Entry(window, text="Account for: ")
    account_for_field.pack()

    username_label = tk.Label(window, text="Username: ")
    username_label.pack()
    username_field = tk.Entry(window, text="Username: ")
    username_field.pack()

    password_label = tk.Label(window, text="Password: ")
    password_label.pack()
    password_field = tk.Entry(window, text= "Password: " ,show="*")
    password_field.pack() 
    
    def save_account():
        account_for = account_for_field.get()
        username = username_field.get()
        password = password_field.get()
        try:
            account_for = account_for.encode()
            username = username.encode()
            key = ec.get_key()
            ciphertext = ec.encrypt(password,key = key)
        except ValueError:
            return "Invalid values in account for, username or password"
        
        # Save the account to a file
        with open("passwords.txt", "wb") as file:
            file.write(account_for + b"|FOR-USER-DEVIDER|" + username+ b"|USER-KEY-DEVIDER|" + key + b"|KEY-DATA-DEVIDER|" + ciphertext)

    save_button = tk.Button(window, text="Save", command=save_account)
    save_button.pack()

    # Create a button to decrypt the password
    def decrypt_password():
        try:
            with open("passwords.txt", "rb") as file:
                line = file.read()
                if b"|FOR-USER-DEVIDER|" and b"|USER-KEY-DEVIDER|" and b"|KEY-DATA-DEVIDER|" in line:
                    
                    account_for, temp_rest = line.split(b"|FOR-USER-DEVIDER|")
                    username, temp_rest = temp_rest.split(b"|USER-KEY-DEVIDER|")
                    key, ciphertext = temp_rest.split(b"|KEY-DATA-DEVIDER|")

                    account_for = account_for.decode()
                    username = username.decode()
                    password = ec.decrypt(ciphertext,key)
                else:
                    return "Invalid file format"

            account_for_label = tk.Label(window, text=account_for)
            account_for_label.pack()
            username_label = tk.Label(window, text=username)
            username_label.pack()
            password_label = tk.Label(window, text=password)
            password_label.pack()

            account_for_label.after(5000, account_for_label.destroy)
            username_label.after(5000, username_label.destroy)
            password_label.after(5000, password_label.destroy)

        except ValueError:
            return "Invalid file format"

    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_password)
    decrypt_button.pack()
