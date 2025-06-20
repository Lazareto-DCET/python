import tkinter as tk
from tkinter import ttk, messagebox
import os

RATES_FILE = "rates.txt"
API_URL = "https://api.exchangerate.host/latest?base=USD"

# Try to fetch live rates from the API
def fetch_live_rates():
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()
        rates = data.get("rates", {})
        rates["USD"] = 1.0  # Ensure USD is included
        save_rates_to_file(rates)
        return rates
    except Exception:
        return None

# Save rates to file
def save_rates_to_file(rates):
    try:
        with open(RATES_FILE, "w") as f:
            for code, rate in rates.items():
                f.write(f"{code}={rate}\n")
    except Exception as e:
        messagebox.showerror("File Error", f"Failed to save rates to file.\n{e}")

# Load rates from file
def load_rates_from_file():
    rates = {}
    if not os.path.exists(RATES_FILE):
        return rates
    with open(RATES_FILE, "r") as f:
        for line in f:
            if '=' in line:
                code, rate = line.strip().split('=')
                try:
                    rates[code.upper()] = float(rate)
                except:
                    continue
    return rates

# Try to get live rates, fallback to file if failed
def load_exchange_rates():
    rates = fetch_live_rates()
    if rates:
        return rates
    else:
        messagebox.showinfo("Offline Mode", "Could not fetch live rates. Using saved rates.")
        return load_rates_from_file()

# Currency conversion logic
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_combobox.get()
        to_curr = to_combobox.get()

        if from_curr not in exchange_rates or to_curr not in exchange_rates:
            raise ValueError("Unsupported currency selected.")

        usd_amount = amount / exchange_rates[from_curr]
        converted = usd_amount * exchange_rates[to_curr]

        result_label.config(text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number and select currencies.")

# GUI Setup
root = tk.Tk()
root.title("Smart Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Load exchange rates
exchange_rates = load_exchange_rates()
currency_list = sorted(exchange_rates.keys())

# UI Elements
tk.Label(root, text="Amount:", font=("Arial", 12)).pack(pady=10)
amount_entry = tk.Entry(root, font=("Arial", 12), justify="center")
amount_entry.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
from_combobox = ttk.Combobox(frame, values=currency_list, state="readonly", width=10)
from_combobox.grid(row=0, column=1)
from_combobox.set("USD")

tk.Label(frame, text="To:", font=("Arial", 12)).grid(row=0, column=2, padx=10)
to_combobox = ttk.Combobox(frame, values=currency_list, state="readonly", width=10)
to_combobox.grid(row=0, column=3)
to_combobox.set("EUR")

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_currency)
convert_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
