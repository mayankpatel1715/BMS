# Bank Management System (BMS) 🏦

A robust, console-based banking application built with Python. This project simulates core banking operations including account creation, deposits, withdrawals, and persistent data storage using JSON.

## 🚀 Features

* **Account Management:** Create, delete, and view account details.
* **Secure Transactions:** Deposit and withdraw funds with real-time validation.
* **Data Persistence:** All user data is saved automatically to `bank_db.json`, so records are not lost when the app closes.
* **Auto-Increment IDs:** Automatically generates unique 4-digit Account IDs (starting from 1001).
* **Input Validation:**
    * **Phone:** strict +91 10-digit validation.
    * **Email:** Regex-based format checking.
    * **Money:** Prevents negative inputs and non-integer values.
    * **Safety:** Prevents withdrawing more money than available balance.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Storage:** JSON (File Handling)
* **Concepts Used:**
    * Object-Oriented Programming (Classes & Objects)
    * Modular Programming (Separation of Concerns)
    * Exception Handling (`try`, `except`, `raise`)
    * Regular Expressions (`re` module)
    * File I/O (`json` module)

## 📂 Project Structure

```text
├── main.py           # Entry point (Controller)
├── operations.py     # Business logic (Deposit, Withdraw, Create)
├── data.py           # Data persistence layer (Load/Save JSON)
├── validation.py     # Input sanitization and Regex checks
├── display.py        # UI/Print formatting
├── bank.py           # Account Class and Model
├── log.py            # Logging configuration
└── bank_db.json      # Database file (Auto-generated)
```

## ⚙️ How to Run
Ensure you have Python installed.

Clone this repository or download the files.

Run the main script:

```Bash
python main.py
Follow the on-screen menu to navigate the bank.
```

## 🔮 Future Improvements
Implement a Transaction History log for each user.

Add password protection/authentication for login.

Integrate the logging module to save errors to file.log.

---

### File 2: `LEARNING_LOG.md`
*Create a file named `LEARNING_LOG.md`. This is for **you** to look back on six months from now.*

```markdown
# My Learning Journey: Bank Management System

## 📝 Project Overview
This is my first major Python project built from scratch without following a tutorial step-by-step. I transitioned from a simple script-based "YouTube Manager" to a fully modular "Bank Management System."

## 🧠 Key Concepts Mastered

### 1. Architecture & Modularization
* **The Shift:** I moved from writing everything in one file (Spaghetti Code) to splitting code into logical modules (`operations`, `data`, `validation`).
* **MVC Pattern:** Unknowingly implemented a version of Model-View-Controller:
    * *Model:* `bank.py` & `data.py`
    * *View:* `display.py`
    * *Controller:* `main.py` & `operations.py`
* **Benefit:** Debugging became easier. If a print statement was wrong, I knew exactly where to look (`display.py`).

### 2. Data Handling (JSON)
* **Persistence:** Learned that variables die when the program ends, but files (`json`) survive.
* **The Process:**
    1.  `load_data()`: Read file -> Convert to List.
    2.  Modify List (Append/Update).
    3.  `save_data()`: Convert List -> Write to file.
* **Analogy:** The "Truck and Warehouse" analogy helped me understand that `w` mode wipes the file, so I must save the *entire* list every time.

### 3. Validation & Regex
* **Trust No One:** Users will enter garbage data. I built "Gatekeepers" in `validation.py`.
* **Regex:** Learned `re.match` for patterns:
    * Email: `^[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,}$`
    * Phone: `^[1-9][0-9]{9}$`
* **Result:** The database remains clean, and the app doesn't crash on bad input.

### 4. Exception Handling
* **Crash Prevention:** Used `try/except` blocks (especially `ValueError`) to catch non-integer inputs.
* **Control Flow:** Used `continue` inside `while True` loops to ask the user to try again instead of stopping the program.
* **Custom Errors:** Learned to use `raise ValueError` when the data type is correct, but the logic is wrong (e.g., negative money).

### 5. Logic Breakthroughs
* **Unique IDs:** Solved the "Duplicate ID" problem by checking the last entry in the database and adding `+1` (Auto-Increment), rather than using random numbers.
* **Search Algorithms:** Created `one_ID` to find a specific user dictionary inside a list of users.

## 🚧 Challenges Faced & Solved
1.  **Circular Imports:** Attempted to cross-import files which caused crashes. Solved by creating a hierarchical structure (Main -> Operations -> Validation).
2.  **Negative Numbers:** Users could deposit `-500`. Solved by adding logic checks (`if cash > 0`).
3.  **UI Consistency:** Print statements were scattered. Solved by creating a dedicated `display.py`.

## 🎯 Next Steps
* Implement `logging` to capture errors in `file.log`.
* Add a "Transaction History" list to the JSON structure.