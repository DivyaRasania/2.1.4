import tkinter as ttk
from tkinter import *
from tkinter.constants import CENTER, LEFT, RIGHT
def one():
    print('Password = admin')
    def test_my_button():
        answer = ent_password.get()
        if answer == 'admin':
            frame_authy.tkraise()
        else:
            frame_authn.tkraise()
        
        if answer == 'admin':
            lbl_answery.config(text='You entered corret answer: ' + answer)
        else:
            lbl_answern.config(text='Incorrect. You entered wrong answer: ' + answer)

    # main window
    root = Tk()
    root.geometry('250x150')
    root.title('Authorization')
    root.columnconfigure(0, weight=10)
    root.rowconfigure(0, weight=10)

    # create empty frame
    frame_login = Frame(root)
    frame_login.grid(row=0, column=0, sticky='news')

    lbl_username = Label(frame_login, text='Username:', bg='cyan', justify=CENTER)
    lbl_username.pack(side=TOP, padx=94, pady=8)

    ent_username = Entry(frame_login, bd=3)
    ent_username.pack(pady=5)

    lbl_password = Label(frame_login, text='Password: ', bg='cyan')
    lbl_password.pack()

    ent_password = Entry(frame_login, bd=3, show='*')
    ent_password.pack(pady=5)

    btn_login = Button(frame_login, text="Log In", fg='black', bg='yellow', command=test_my_button, cursor='hand2')
    btn_login.pack()

    frame_authy = ttk.Frame(root)
    frame_authy.grid(row=0, column=0, sticky='news')
    frame_authy['bg'] = 'lime'
    lbl_answery = Label(frame_authy, text='You are now authorized', bg='lime')
    lbl_answery.pack()
    frame_authn = ttk.Frame(root)
    frame_authn.grid(row=0, column=0, sticky='news')
    frame_authn['bg'] = 'red'
    lbl_answern = Label(frame_authn, text='Invalid Password', bg='red')
    lbl_answern.pack()
    frame_login.tkraise()

    #root.resizable(0, 0)
    root.mainloop()

def two():
    root = Tk()
    root.geometry('256x256')
    root.title('Arranging Widgets in a Grid')

    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    color_blue = Label(root, bg='blue')
    color_blue.grid(column=0, row=0, sticky='news')

    color_lime = Label(root, bg='lime')
    color_lime.grid(column=1, row=0, sticky='news')

    color_red = Label(root, bg='red')
    color_red.grid(column=0, row=1, sticky='news')

    color_yellow = Label(root, bg='yellow')
    color_yellow.grid(column=1, row=1, sticky='news')

    root.mainloop()

