import tkinter as tk


def menu_settings(window: tk.Tk, buttons: list):
    window.title("Password Manager")
    window.geometry("1280x720")

    # create a toggle button for switching between black and white theme
    def toggle_theme():
        new_color = "white" if window.cget("bg") == "black" else "black"
        window.configure(bg=new_color)
        #change color of the text in the buttons to opposite of the background
        new_text_color = "black" if new_color == "white" else "white"
        for button in buttons:
            button.config(fg=new_text_color)

        # change the color of the buttons
        for button in buttons:
            button.config(bg=new_color)

    toggle_button = tk.Button(window, text="Toggle Theme", command=toggle_theme)
    toggle_button.pack()
    toggle_button.place(x=0, y=0)
    toggle_button.config(bg="black", fg="white")

    