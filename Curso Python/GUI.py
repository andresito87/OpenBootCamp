# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.


import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(background="white", width=1000, height=1000, padx=50, pady=50, relief="sunken", borderwidth=10,
                 cursor="arrow", takefocus=True, highlightbackground="black", highlightcolor="black", highlightthickness=1)
window.anchor("center")
window.resizable(0, 0)
window.title("GUI - Python")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)


selected = tk.StringVar()
radioButton1 = ttk.Radiobutton(
    window, text="Opción 1", value=1, variable=selected, state="normal", takefocus=True)
radioButton2 = ttk.Radiobutton(
    window, text="Opción 2", value=2, variable=selected, state="normal", takefocus=True)
radioButton3 = ttk.Radiobutton(
    window, text="Opción 3", value=3, variable=selected, state="normal", takefocus=True)
radioButton4 = ttk.Radiobutton(
    window, text="Opción 4", value=4, variable=selected, state="normal", takefocus=True)
radioButton5 = ttk.Radiobutton(
    window, text="Opción 5", value=5, variable=selected, state="normal", takefocus=True)

radioButton1.grid(row=1, column=0)
radioButton2.grid(row=2, column=0)
radioButton3.grid(row=3, column=0)
radioButton4.grid(row=4, column=0)
radioButton5.grid(row=5, column=0)


radioButtonreset = tk.Button(
    window, text="Reiniciar", command=lambda: selected.set(""))

radioButtonreset.grid(row=0, column=1)

quit = tk.Button(window, text="Salir", command=window.destroy)

quit.grid(row=5, column=1)
window.mainloop()
