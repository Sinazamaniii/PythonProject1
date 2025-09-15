from tkinter import *
import tkinter.messagebox as msg

from data_access.database_manager import save_username
from tools.validation import *

def save_click():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        save_username(username.get(),password.get(),nickname.get(), locked.get())
        msg.showinfo("Save", "Person saved")
    except Exception as e:
        msg.showerror("Error", f"{e}")


window = Tk()

window.title("user")
window.geometry("500x300")

# username
username = StringVar()
Label(window, text="Name").place(x=20, y=40)
Entry(window, textvariable=username).place(x=100, y=40)

# password
password = StringVar()
Label(window, text="password").place(x=20, y=60)
Entry(window, textvariable=password, show= "*").place(x=100, y=60)


#nickname
nickname = StringVar()
Label(window, text="Nickname").place(x=20, y=80)
Entry(window, textvariable=nickname).place(x=100, y=80)


# locked
locked = BooleanVar(value=True)
Label(window, text="locked").place(x=20, y=200)
Checkbutton(window, variable=locked).place(x=100, y=200)


Button(window, text="Save", width=15, command= save_click).place(x=70, y=240)

window.mainloop()
