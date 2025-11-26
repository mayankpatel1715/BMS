# Bank Management System - Learning & Error Documentation

**Project:** Basic Bank Management System (BMS)  
**Developer:** Mayank Patel  
**Date Started:** November 26, 2025  
**Repository:** mayankpatel1715/BMS

---

## Project Overview

A Basic Bank Management System built with Python featuring the following core functionalities:

1. **Bank Account Creation** - Create new customer accounts
2. **View Bank Account** - Display account information
3. **Deposit Money** - Add funds to accounts
4. **Withdraw Money** - Remove funds from accounts
5. **Delete Bank Account** - Remove customer accounts

---

## Development Journey

### Step 1: Project Initialization & Entry Point

**What I Did:**
- Created the main entry point for the application in `main.py`
- Implemented the `main()` function to serve as the application's starting point
- Built a menu-driven interface with a while loop for user interaction
- Added 6 menu options (5 features + exit option)

**Code Structure:**
```python
def main():
    bank_account = load_data()
    
    while True:
        # Display menu options
        # Get user choice
        # Execute corresponding function
```

**Learning:**
- Menu-driven applications need a loop to keep running until user exits
- Entry point functions help organize code flow
- User interaction requires clear prompts and choices

---

### Step 2: Creating the Account Class & Bank Application Form

**What I Did:**
- Created `bank.py` file
- Implemented the `Account` class with constructor to initialize account details
- Built the `bank_app()` method to generate account forms

**Initial Approach (INCORRECT):**
```python
def bank_app(self):
    # Created Account object TWICE - This was wrong!
    acc = Account(self.name, ...)  # First creation
    
    form = {
        "name": acc.name,  # Using acc object
        ...
    }
    
    return form
```

**The Problem:**
- I was creating an Account object inside the `bank_app()` method
- This meant creating the Account object **twice** unnecessarily
- The method was already being called on an existing Account instance (self)
- This was redundant and inefficient

**The Fix (CURRENT SOLUTION):**
```python
def bank_app(self):
    # Use self directly - no need to create new Account object
    form = {
        "account_no": random.randint(1, 100),
        "name": self.name,           # Use self.name directly
        "dob": self.dob,             # Use self.dob directly
        "gender": self.gender,       # Use self.gender directly
        "email": self.email,         # Use self.email directly
        "phone_no": self.phone_no,   # Use self.phone_no directly
        "money": 0
    }
    return form
```

**Key Learning:**
- ✅ When you're inside a class method, `self` already refers to the current instance
- ✅ No need to create another object when you already have access to the instance data
- ✅ Use `self.attribute` to access instance variables directly
- ❌ Avoid creating redundant objects - it wastes memory and processing
- 💡 **Lesson:** Understand the difference between class instances and when to use `self`

---

### Step 3: Implementing Data Persistence with JSON

**What I Did:**
- Created `load_data()` function to read account data from `bank_db.json`
- Implemented JSON file handling to persist data between sessions

**Initial Implementation:**
```python
def load_data():
    with open("bank_db.json", 'r') as file:
        return json.load(file)
```

**The Problem:**
- When the database file (`bank_db.json`) was empty or had no valid JSON
- The program would crash with `json.decoder.JSONDecodeError`
- Application couldn't handle the case when starting fresh with no data

**The Solution (ERROR HANDLING):**
```python
def load_data():
    try:
        with open("bank_db.json", 'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []  # Return empty list if JSON is invalid/empty
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist
```

**Key Learning:**
- ✅ Always handle exceptions when working with file I/O
- ✅ `json.decoder.JSONDecodeError` is raised when JSON is malformed or empty
- ✅ `FileNotFoundError` is raised when the file doesn't exist yet
- ✅ Returning an empty list `[]` allows the program to continue gracefully
- 💡 **Lesson:** Defensive programming - always expect files to be missing or corrupted
- 💡 **Lesson:** Use try-except blocks for robust error handling

**Additional Considerations:**
- Empty database scenario is common when app runs for the first time
- Users shouldn't see error messages for normal first-time operation
- Graceful degradation improves user experience

---

## Code Architecture

### File Structure
```
BMS/
├── main.py           # Entry point, menu system, orchestration
├── bank.py           # Account class and account management logic
├── bank_db.json      # JSON database for storing account data
├── README.md         # Project documentation
└── LEARNING_LOG.md   # This file - errors and learnings
```

### Current Implementation Status

✅ **Completed:**
- Project structure setup
- Entry point with menu system
- Account class with proper use of `self`
- Bank application form generation
- Data loading with error handling
- JSON database integration

⏳ **In Progress/TODO:**
- `save_data()` function implementation
- `account_info()` function implementation
- Deposit money functionality
- Withdraw money functionality
- Delete account functionality
- Complete menu option handlers

---

## Key Takeaways

### 1. Object-Oriented Programming
- Understanding `self` is crucial in Python classes
- Instance methods already have access to instance data through `self`
- Don't create redundant objects when `self` provides what you need

### 2. Error Handling Best Practices
- Always anticipate file operations might fail
- Handle specific exceptions separately for better debugging
- Provide fallback values (like empty lists) for graceful degradation

### 3. Data Persistence
- JSON is simple for small-scale data storage
- Always validate data before using it
- Empty or corrupted files should not crash your application

---

## Git Workflow Reference

For tracking changes and understanding the evolution of this project, refer to:
```bash
git log --oneline --all
```

Current commit history shows the initial implementation with the fixes already applied.

---

## Next Steps

1. Implement `save_data()` to persist new accounts
2. Fix JSON append logic (currently using 'a+' mode which may cause formatting issues)
3. Implement account lookup by account number
4. Add deposit/withdraw transaction logic
5. Implement account deletion
6. Add input validation for all user inputs
7. Consider using list of dictionaries structure for multiple accounts

---

## Notes for Future Reference

- The current `account_creation()` uses `json.dump()` with 'a+' mode
  - This may cause JSON formatting issues with multiple accounts
  - Consider loading all data, appending new account, then writing entire list
- Account numbers use `random.randint(1, 100)` - risk of duplicates exists
  - Should implement unique ID generation or sequential numbering
- No input validation currently - should add validation for:
  - Email format
  - Phone number format
  - Positive numbers for money operations

---

*This document will be updated as development continues and new learnings emerge.*
