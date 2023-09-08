import tkinter as tk
from tkinter import ttk

def hitungtotal():
    harga = float(harga_entry.get())
    kuantias = int(kuantitas_entry.get())
    hasil=harga*kuantias
    hasilVar.set(f"Total : Rp{hasil:.2f}")


window = tk.Tk()
window.title("Program Kasir")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

harga_label = ttk.Label(input_frame, text="Harga: ")
harga_label.grid(row=0, column=0, sticky="W")
harga_entry = ttk.Entry(input_frame)
harga_entry.grid(row=0, column=1)

kuantitas_label = ttk.Label(input_frame, text="Kuantitas: ")
kuantitas_label.grid(row=1, column=0, sticky="W")
kuantitas_entry = ttk.Entry(input_frame)
kuantitas_entry.grid(row=1, column=1)

tombol = ttk.Button(input_frame, text="Hitung", command=hitungtotal)
tombol.grid(row=3, column=0, columnspan=2)

hasilVar= tk.StringVar()
hasilVar.set("Total : Rp0.00")
hasil_label=ttk.Label(window,textvariable=hasilVar)
hasil_label.pack()

window.mainloop()