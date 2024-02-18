import tkinter as tk
import encrypt as ec

# Create the main window
window = tk.Tk()

window.title("Password Manager")#Change window title to Password Manager

window.geometry("1280x720")#Change window size to 1280x720

# Create a label
label = tk.Label(window, text="Password Manager")
label.pack()


# Create a password input field
password_field = tk.Entry(window, show="*")
password_field.pack()

# Create a button to encrypt the password
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
    print(password)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_password)
decrypt_button.pack()


# Start the GUI event loop
window.mainloop()