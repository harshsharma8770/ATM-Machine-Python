# 🏧 ATM Machine - Python

A Python-based ATM Machine desktop application built with **Tkinter** and **pyttsx3**, featuring a graphical interface and voice assistance.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Voice](https://img.shields.io/badge/Voice-pyttsx3-green)

## 📌 Overview

This project simulates a basic ATM system using Python. Users can log in with an account number and PIN, check their balance, deposit money, withdraw money, and log out.

The application also provides voice feedback using `pyttsx3` and uses background threads so voice operations do not block the graphical interface.

## ✨ Features

- 🔐 Account number and PIN authentication
- 💰 Check account balance
- 💵 Deposit money
- 💸 Withdraw money
- 🔊 Voice assistance
- ⏳ Login verification screen
- 🚪 Logout functionality
- 🖥️ Graphical User Interface using Tkinter
- ⚡ Background voice processing using threading

## 🛠️ Technologies Used

- **Python**
- **Tkinter** — GUI development
- **pyttsx3** — Text-to-speech
- **Threading** — Background voice processing

## 📂 Project Structure

```text
ATM-Machine-Python/
│
├── ATM.py
├── README.md
├── requirements.txt
├── .gitignore
└── Screenshots/
    ├── Welcome.png
    ├── Login.png
    └── Main-menu.png
```

## 📸 Application Screenshots

### 🏧 Welcome Screen

![ATM Welcome Screen](Screenshots/Welcome.png)

### 🔐 Login Screen

![ATM Login Screen](Screenshots/Login.png)

### 💳 Main Menu

![ATM Main Menu](Screenshots/Main-menu.png)

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshsharma8770/ATM-Machine-Python.git
```

### 2. Navigate to the project

```bash
cd ATM-Machine-Python
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python ATM.py
```

## 🔑 Demo Credentials

The application currently contains demo users for testing:

| Account Number | PIN | Initial Balance |
|---|---|---:|
| `1234` | `0000` | ₹5,000 |
| `1111` | `2222` | ₹10,000 |

> ⚠️ These are demonstration credentials only. This project is not connected to a real banking system.

## 💳 ATM Operations

After successful login, users can:

1. **Check Balance** — View the current account balance.
2. **Deposit** — Add money to the account.
3. **Withdraw** — Withdraw money if sufficient balance is available.
4. **Logout** — Return to the login screen.

## 🔊 Voice Assistance

The application uses `pyttsx3` to provide voice feedback for events such as:

- Welcome message
- Login verification
- Successful login
- Invalid credentials
- Balance information
- Deposit confirmation
- Withdrawal confirmation
- Logout message

## 🎯 Learning Outcomes

This project helped demonstrate practical use of:

- Python programming
- Object-oriented programming
- Tkinter GUI development
- Event-driven programming
- Dictionaries for storing user data
- Exception handling
- Multithreading
- Text-to-speech integration

## 🚀 Future Improvements

- 🗄️ Add SQLite/MySQL database integration
- 🧾 Add transaction history
- 🔐 Hash and securely store PINs
- 👤 Add account creation
- 💳 Add ATM card simulation
- 🧾 Generate transaction receipts
- 🎨 Improve the GUI design
- 🛡️ Add stronger input validation
- 📊 Add transaction statements

## ⚠️ Disclaimer

This is an educational/demo ATM simulation created for learning purposes. It does not connect to real bank accounts, banking networks, or financial services.

## 👨‍💻 Author

**Harsh Sharma**

GitHub: [@harshsharma8770](https://github.com/harshsharma8770)