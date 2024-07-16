import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert():
    try:
        suhu = float(entry_suhu.get())
        pilihan = combo_box.get()

        if pilihan == "Celcius ke Fahrenheit":
            hasil = celsius_to_fahrenheit(suhu)
            unit = "Fahrenheit"
        elif pilihan == "Fahrenheit ke Celcius":
            hasil = fahrenheit_to_celsius(suhu)
            unit = "Celcius"
        elif pilihan == "Celcius ke Kelvin":
            hasil = celsius_to_kelvin(suhu)
            unit = "Kelvin"
        elif pilihan == "Kelvin ke Celcius":
            hasil = kelvin_to_celsius(suhu)
            unit = "Celcius"
        elif pilihan == "Fahrenheit ke Kelvin":
            hasil = fahrenheit_to_kelvin(suhu)
            unit = "Kelvin"
        elif pilihan == "Kelvin ke Fahrenheit":
            hasil = kelvin_to_fahrenheit(suhu)
            unit = "Fahrenheit"
        else:
            messagebox.showerror("Error", "Pilihan tidak valid")
            return
        
        label_hasil.config(text=f"Hasil: {hasil:.2f} {unit}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai suhu yang valid")

# Inisialisasi GUI
root = tk.Tk()
root.title("Konversi Suhu")

# Label
label_pilih = tk.Label(root, text="Pilih konversi suhu:")
label_pilih.grid(column=0, row=0, padx=10, pady=10)

# Combobox
options = ["Celcius ke Fahrenheit", "Fahrenheit ke Celcius", "Celcius ke Kelvin", "Kelvin ke Celcius", "Fahrenheit ke Kelvin", "Kelvin ke Fahrenheit"]
combo_box = ttk.Combobox(root, values=options, state="readonly")
combo_box.grid(column=1, row=0, padx=10, pady=10)
combo_box.current(0)

# Label dan Entry untuk suhu
label_suhu = tk.Label(root, text="Masukkan suhu:")
label_suhu.grid(column=0, row=1, padx=10, pady=10)

entry_suhu = tk.Entry(root)
entry_suhu.grid(column=1, row=1, padx=10, pady=10)

# Tombol konversi
button_convert = tk.Button(root, text="Konversi", command=convert)
button_convert.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Menjalankan GUI
root.mainloop()
