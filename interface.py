import tkinter as tk
from main import recursiveDescentParser
from tkinter import filedialog
from tkinter import messagebox
from lexParser import Lexer

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.SQL")])
    if file_path:
        with open(file_path, 'r') as file:
            sql_code = file.read()
            return sql_code
    else:
        return ""

def popup_message(title, message, icon="info"):
    messagebox.showinfo(title, message, icon=icon)

def show_code():
    sql_code = open_file()
    print(sql_code)
    lexer = Lexer(sql_code)
    all_tokens = recursiveDescentParser(lexer)

    if all_tokens == True:
        popup_message("SQL Tokens", "O código SQL é válido.", "info")
        print(lexer.tokens)
    else:
        popup_message("SQL Tokens", "O código SQL não é válido.", "warning")

def change_cursor(event):
    open_button.configure(cursor="hand2")


root = tk.Tk()
root.title("Análise de Códigos SQL")


root.geometry("800x600")
root.state("zoomed")
root.configure(bg="#1a1a1a")

frame = tk.Frame(root, bg="#1a1a1a")
frame.pack(pady=50)

open_button = tk.Button(
        frame,
        text="Abrir Arquivo",
        font=("Arial", 14),
        bg="#4682B4",
        fg="white",
        relief="flat",
        padx=20,
        pady=10, command=show_code)
open_button.pack(side=tk.BOTTOM)
open_button.bind("<Enter>", change_cursor)

# text_widget = tk.Text(root, width=80, height=30)
# text_widget.pack(pady=10)

root.mainloop()
