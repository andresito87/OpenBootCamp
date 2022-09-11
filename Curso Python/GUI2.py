# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

from cProfile import label
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(background="white", width=1000, height=1000, padx=50, pady=50, relief="sunken", borderwidth=10,
                 cursor="arrow", takefocus=True, highlightbackground="black", highlightcolor="black", highlightthickness=1)
window.title("GUI List - Python")
window.geometry("500x500")


window.columnconfigure(0, weight=1)

list = ["Python", "Java", "Javascript", "C++", "C#", "PHP", "Ruby", "Perl", "Swift", "Go",
        "TypeScript", "Kotlin", "Scala", "Rust", "Haskell", "Lua", "Julia", "Elixir", "Clojure"]
list_items = tk.StringVar(value=list)
listbox = tk.Listbox(window, selectmode="multiple",
                     height=10, width=20, listvariable=list_items)
listbox.grid(row=1, column=0)

label = tk.Label(window, text="Selecciona un lenguaje de programación")

label.grid(row=0, column=0)


quit = tk.Button(window, text="Salir", command=window.destroy)

quit.grid(row=5, column=1)
window.mainloop()
