import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading

# === Voice Function (Non-blocking + Delayed callback) ===
def speak_wait(text, callback=None, delay=1000):  # delay in ms
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        if callback:
            root.after(delay, callback)
    threading.Thread(target=run, daemon=True).start()

def speak_async(text):  # Optional: background speaking without waiting
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

# === User Data ===
users = {
    "1234": {"pin": "0000", "balance": 5000},
    "1111": {"pin": "2222", "balance": 10000}
}

current_user = None

# === ATM App ===
class ATMApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.master.geometry("800x600")
        self.welcome_screen()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def welcome_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Welcome to ATM Machine", font=("Arial", 30)).pack(pady=100)
        speak_wait("Welcome to ATM machine. Insert your card.", self.create_login_screen)

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="ATM Login", font=("Arial", 28)).pack(pady=20)

        tk.Label(self.master, text="Account Number", font=("Arial", 18)).pack(pady=10)
        self.acc_entry = tk.Entry(self.master, font=("Arial", 18), width=20)
        self.acc_entry.pack()

        tk.Label(self.master, text="PIN", font=("Arial", 18)).pack(pady=10)
        self.pin_entry = tk.Entry(self.master, font=("Arial", 18), width=20, show="*")
        self.pin_entry.pack()

        tk.Button(self.master, text="Login", font=("Arial", 18), command=self.handle_login, width=10).pack(pady=30)

    def handle_login(self):
        acc = self.acc_entry.get()
        pin = self.pin_entry.get()
        speak_wait("Please wait", lambda: self.show_wait_and_check_login(acc, pin))

    def show_wait_and_check_login(self, acc, pin):
        self.clear_screen()
        tk.Label(self.master, text="Please wait...", font=("Arial", 28)).pack(pady=200)
        self.master.update()
        speak_wait("while your passbook and barcode are being verified", lambda: self.verify_login(acc, pin))

    def verify_login(self, acc, pin):
        if acc in users and users[acc]["pin"] == pin:
            global current_user
            current_user = acc
            speak_wait("Login successful", self.create_main_menu)
        else:
            speak_wait("Invalid account number or PIN", self.show_invalid_login)

    def show_invalid_login(self):
        messagebox.showerror("Error", "Invalid login credentials")
        self.create_login_screen()

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.master, text="ATM Main Menu", font=("Arial", 28)).pack(pady=30)
        speak_wait("Please choose an option")

        options = {
            "Check Balance": self.check_balance,
            "Deposit": self.deposit_screen,
            "Withdraw": self.withdraw_screen,
            "Logout": self.logout
        }

        for label, action in options.items():
            tk.Button(self.master, text=label, font=("Arial", 18), command=action, width=20, height=2).pack(pady=10)

    def check_balance(self):
        balance = users[current_user]["balance"]
        speak_wait(f"Your balance is {balance} rupees")
        messagebox.showinfo("Balance", f"Your current balance is ₹{balance}")

    def deposit_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Deposit Amount", font=("Arial", 28)).pack(pady=30)
        self.dep_entry = tk.Entry(self.master, font=("Arial", 20), width=15)
        self.dep_entry.pack()
        tk.Button(self.master, text="Submit", font=("Arial", 18), command=self.deposit).pack(pady=20)
        tk.Button(self.master, text="Back", font=("Arial", 14), command=self.create_main_menu).pack()
        speak_wait("Enter the amount to deposit")

    def deposit(self):
        try:
            amount = float(self.dep_entry.get())
            users[current_user]["balance"] += amount
            speak_wait(f"{amount} rupees deposited successfully", self.create_main_menu)
            messagebox.showinfo("Success", f"Deposited ₹{amount}")
        except:
            speak_wait("Invalid amount entered")
            messagebox.showerror("Error", "Please enter a valid amount")

    def withdraw_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Withdraw Amount", font=("Arial", 28)).pack(pady=30)
        self.wd_entry = tk.Entry(self.master, font=("Arial", 20), width=15)
        self.wd_entry.pack()
        tk.Button(self.master, text="Submit", font=("Arial", 18), command=self.withdraw).pack(pady=20)
        tk.Button(self.master, text="Back", font=("Arial", 14), command=self.create_main_menu).pack()
        speak_wait("Enter the amount to withdraw")

    def withdraw(self):
        try:
            amount = float(self.wd_entry.get())
            if amount <= users[current_user]["balance"]:
                users[current_user]["balance"] -= amount
                speak_wait(f"{amount} rupees withdrawn successfully", self.create_main_menu)
                messagebox.showinfo("Success", f"Withdrawn ₹{amount}")
            else:
                speak_wait("Insufficient balance")
                messagebox.showerror("Error", "Not enough balance")
        except:
            speak_wait("Invalid amount entered")
            messagebox.showerror("Error", "Please enter a valid amount")

    def logout(self):
        speak_wait("You have been logged out. Please take your card. Thank you", self.create_login_screen)

# === Launch App ===
root = tk.Tk()
app = ATMApp(root)
root.mainloop()
