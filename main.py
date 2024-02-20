import tkinter as tk
import encrypt as ec
import saving as sv
import menu as mn

window = tk.Tk()
window.title("Password Manager")
window.geometry("1280x720")

sv.saving_account(window)


# Start the GUI event loop
window.mainloop()