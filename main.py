import tkinter as tk
import encrypt as ec
import saving as sv
import menu as mn

window = tk.Tk()

sv.saving_account(window)

mn.menu_settings(window, sv.list_of_themeable)

# Start the GUI event loop
window.mainloop()