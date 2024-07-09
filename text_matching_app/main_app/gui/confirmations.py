from tkinter import messagebox


def error_message(*, title='error', error: str) -> str:
    return messagebox.showerror(title=title.title(), message=error.upper())


def confirm(custom_message: str):
    title = 'confirmation'
    message = 'Do you want to proceed\n'

    final_message = message + custom_message + '??'

    return messagebox.askyesno(title=title, message=final_message.upper())


"""

askokcancel
askquestion
askretrycancel
askyesno
askyesnocancel
showerror
showinfo
showwarning

"""
