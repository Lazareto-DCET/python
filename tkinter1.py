import tkinter as tk
from tkinter import ttk, messagebox

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "INR": 83.2,
    "JPY": 110.5,
    "CAD": 1.35,
    "AUD": 1.5,
    "CNY": 7.2,
    "MXN": 17.1,
    "BRL": 5.4,
    "ZAR": 18.3,
    "CHF": 0.91,
    "SEK": 10.5,
    "PHP": 58.3,
    "NOK": 10.3,
    "KRW": 1300.0,
    "SGD": 1.36,
    "NZD": 1.61,
    "HKD": 7.82,
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_combobox.get()
        to_curr = to_combobox.get()

        if from_curr not in exchange_rates or to_curr not in exchange_rates:
            raise ValueError("Unsupported currency selected.")

        usd_amount = amount / exchange_rates[from_curr]
        converted = usd_amount * exchange_rates[to_curr]

        result_label.config(
            text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number and select currencies.")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Amount:", font=("Arial", 12)).pack(pady=10)
amount_entry = tk.Entry(root, font=("Arial", 12), justify="center")
amount_entry.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
from_combobox = ttk.Combobox(frame, values=list(exchange_rates.keys()), state="readonly", width=10)
from_combobox.grid(row=0, column=1)
from_combobox.set("PHP")

tk.Label(frame, text="To:", font=("Arial", 12)).grid(row=0, column=2, padx=10)
to_combobox = ttk.Combobox(frame, values=list(exchange_rates.keys()), state="readonly", width=10)
to_combobox.grid(row=0, column=3)
to_combobox.set("USD")

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_currency)
convert_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
