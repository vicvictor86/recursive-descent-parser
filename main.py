import tkinter as tk
from recursiveDescentParser import recursiveDescentParser
from tkinter import filedialog
from tkinter import messagebox
from lexParser import Lexer

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.SQL")])
    sql_code = ""
    if file_path:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    index = line.index('\n')
                    line = line[:index]
                except:
                    pass
                sql_code += line
            return sql_code
    else:
        return sql_code

def popup_message(title, message, icon="info"):
    messagebox.showinfo(title, message, icon=icon)

def show_code():
    sql_code = open_file()
    lexer = Lexer(sql_code)
    all_tokens = recursiveDescentParser(lexer)

    if all_tokens == True:
        tokens_text.config(state=tk.NORMAL)
        tokens_text.delete("1.0", tk.END)
        
        for token in lexer.tokens:
            token_str = str(token) + " "
            tokens_text.insert(tk.END, token_str)
            if token[0] == ";":
                tokens_text.insert(tk.END, "\n")
        tokens_text.config(state=tk.DISABLED)
        popup_message("SQL Tokens", "O código SQL é válido.", "info")
    else:
        tokens_text.config(state=tk.NORMAL)
        tokens_text.delete("1.0", tk.END)
        tokens_text.insert(tk.END, lexer.tokens)
        tokens_text.config(state=tk.DISABLED)
        popup_message("SQL Tokens", "O código SQL não é válido.", "warning")

def change_cursor(event):
    open_button.configure(cursor="hand2")

if __name__ == "__main__":

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
        pady=10,
        command=show_code
    )
    open_button.pack(side=tk.BOTTOM)
    open_button.bind("<Enter>", change_cursor)

    tokens_frame = tk.Frame(root, bg="#1a1a1a")
    tokens_frame.pack()

    tokens_label = tk.Label(
        tokens_frame,
        text="Tokens:",
        font=("Arial", 16),
        bg="#1a1a1a",
        fg="white"
    )
    tokens_label.pack(pady=10)

    tokens_text = tk.Text(
        tokens_frame,
        width=80,
        height=30,
        font=("Arial", 12),
        state=tk.DISABLED
    )
    tokens_text.pack()

    root.mainloop()