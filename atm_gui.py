import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Sample account storage
accounts = {
    'john': {'pin': '1234', 'balance': 1000.0, 'history': []},
    'jane': {'pin': '4321', 'balance': 500.0, 'history': []}
}

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python ATM")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.current_user = None
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login to ATM", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="PIN").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack()

        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)
        tk.Button(self.root, text="Create New Account", command=self.create_register_screen).pack()

    def create_register_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Create Account", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="New Username").pack()
        self.reg_username_entry = tk.Entry(self.root)
        self.reg_username_entry.pack()

        tk.Label(self.root, text="New PIN").pack()
        self.reg_pin_entry = tk.Entry(self.root, show="*")
        self.reg_pin_entry.pack()

        tk.Button(self.root, text="Register", command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.create_login_screen).pack()

    def register_user(self):
        username = self.reg_username_entry.get().strip()
        pin = self.reg_pin_entry.get().strip()

        if not username or not pin:
            messagebox.showerror("Error", "All fields are required.")
        elif username in accounts:
            messagebox.showerror("Error", "Username already exists.")
        elif not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number.")
        else:
            accounts[username] = {'pin': pin, 'balance': 0.0, 'history': []}
            messagebox.showinfo("Success", "Account created successfully!")
            self.create_login_screen()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Check Balance", command=self.show_balance, width=22).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit_screen, width=22).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen, width=22).pack(pady=5)
        tk.Button(self.root, text="Transaction History", command=self.show_history, width=22).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout, width=22).pack(pady=5)

    def show_balance(self):
        user = accounts[self.current_user]
        messagebox.showinfo("Balance", f"Your balance is: ₱{user['balance']:.2f}")

    def deposit_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to deposit", font=("Arial", 12)).pack(pady=10)
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=self.deposit).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def withdraw_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to withdraw", font=("Arial", 12)).pack(pady=10)
        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=self.withdraw).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def show_history(self):
        self.clear_screen()
        user = accounts[self.current_user]
        tk.Label(self.root, text="Transaction History", font=("Arial", 14)).pack(pady=5)
        history_box = tk.Text(self.root, height=10, width=35)
        history_box.pack(pady=5)
        history_box.insert(tk.END, "\n".join(user['history'][-10:]) or "No transactions yet.")
        history_box.config(state='disabled')
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError
            user = accounts[self.current_user]
            user['balance'] += amount
            self.add_to_history("Deposit", amount)
            messagebox.showinfo("Deposit", f"₱{amount:.2f} deposited successfully.")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            user = accounts[self.current_user]
            if amount <= 0 or amount > user['balance']:
                raise ValueError
            user['balance'] -= amount
            self.add_to_history("Withdraw", amount)
            messagebox.showinfo("Withdraw", f"₱{amount:.2f} withdrawn successfully.")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount or insufficient balance.")

    def add_to_history(self, transaction_type, amount):
        user = accounts[self.current_user]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {transaction_type}: ₱{amount:.2f}"
        user['history'].append(entry)

    def authenticate(self):
        username = self.username_entry.get().strip()
        pin = self.pin_entry.get().strip()
        if username in accounts and accounts[username]['pin'] == pin:
            self.current_user = username
            self.create_main_menu()
        else:
            messagebox.showerror("Authentication Failed", "Invalid username or PIN.")

    def logout(self):
        self.current_user = None
        self.create_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
