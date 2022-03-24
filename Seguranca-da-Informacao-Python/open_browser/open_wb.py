import webbrowser
from tkinter import Button, Tk

"""
    Abrindo um navegador usando o tkinter
"""
root = Tk()
root.title("Abrir Browser")
root.geometry("300x200")


def google():
    webbrowser.open("www.google.com")


mygoogle = Button(root, text="Abrit o Google", command=google).pack(padx=20)
root.mainloop()
