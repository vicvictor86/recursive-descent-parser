import tkinter as tk
from recursiveDescentParser import recursiveDescentParser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from lexParser import Lexer

font_style = ("Helvetica", 18)

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
    
    code_text.config(state=tk.NORMAL)
    code_text.delete("1.0", tk.END)
    for char in sql_code:
        code_text.insert(tk.END, char)
        if char == ";":
            code_text.insert(tk.END, "\n")

def analyze_code():
    sql_code = code_text.get("1.0", tk.END)
    sql_code = sql_code.replace("\n", " ")
    lexer = Lexer(sql_code)
    all_tokens = recursiveDescentParser(lexer)
    if all_tokens == True:
        tokens_text.config(state=tk.NORMAL)
        tokens_text.delete("1.0", tk.END)
        
        for token in lexer.tokens:
            tokens_text.insert(tk.END, "{" + f"{token[0]}  >>  {token[1]}" + "}  ")
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
    analyze_button.configure(cursor="hand2")

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Análise de Códigos SQL")
    root.geometry("800x600")
    root.state("zoomed")
    root.configure(bg="#1a1a1a")

    frame = tk.Frame(root, bg="#1a1a1a")
    frame.pack(pady=50)
    
    code_label = tk.Label(
        frame,
        text="Código SQL:",
        font=font_style,
        bg="#1a1a1a",
        fg="white"
    )
    code_label.pack()

    scrollbar = tk.Scrollbar(root)
    # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    code_text = scrolledtext.ScrolledText(
        frame, 
        wrap=tk.WORD, 
        yscrollcommand=scrollbar.set,
        width=80,
        height=12,
        font=("Helvetica", 14)
    )
    scrollbar.config(command=code_text.yview)
    code_text.pack()

    open_button = tk.Button(
        frame,
        text="Abrir Arquivo",
        font=("Helvetica", 14),
        bg="#4682B4",
        fg="white",
        relief="flat",
        padx=27,
        pady=10,
        command=show_code
    )

    open_button.pack(pady=15)
    open_button.bind("<Enter>", change_cursor)

    analyze_button = tk.Button(
        frame,
        text="Analisar Código",
        font=("Helvetica", 14),
        bg="#4682B4",
        fg="white",
        relief="flat",
        padx=15,
        pady=10,
        command=analyze_code
    )
    analyze_button.pack(pady=5)
    analyze_button.bind("<Enter>", change_cursor)

    tokens_frame = tk.Frame(root, bg="#1a1a1a")
    tokens_frame.pack()

    tokens_label = tk.Label(
        tokens_frame,
        text="Tokens:",
        font=font_style,
        bg="#1a1a1a",
        fg="white"
    )
    tokens_label.pack()

    tokens_text = scrolledtext.ScrolledText(
        tokens_frame,
        width=100,
        height=10,
        font=("Helvetica", 12),
        state=tk.DISABLED
    )
    tokens_text.pack(pady=0)
    scrollbar.config(command=code_text.yview)


    root.mainloop()