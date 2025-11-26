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

## Step 4: The Critical Data Structure Problem - JSON Architecture Breakdown

### 🔍 Overview

The Bank Management System (BMS) is intended to support:
- ✅ Creating new accounts
- ✅ Storing them persistently
- ✅ Fetching account information
- ✅ Updating account balance
- ✅ Deleting accounts

To achieve this, the program uses a JSON file (`bank_db.json`) as a database.

**However**, the current JSON structure and logic do not support multiple accounts, which leads to:
- ❌ Broken search functions
- ❌ Overwriting data
- ❌ KeyErrors
- ❌ TypeError exceptions
- ❌ Only storing one account at a time

This section explains:
1. What went wrong
2. Why it happened
3. What the correct data model should be
4. How the YouTube Manager example already does the right thing
5. The conceptual fixes needed

---

### 📋 Finding 1 — Incorrect JSON Structure

#### ❌ What I Did Wrong

My BMS database contains a **single dictionary**:
```json
{
  "account_no": 83,
  "name": "dsas",
  "dob": "12/12/12",
  "gender": "M",
  "email": "dsad@gmail.com",
  "phone_no": 1234567890,
  "money": 0
}
```

This means the file represents **ONE account**, not a list of accounts.

But my program behaves as if the JSON contains:
```python
[ account1, account2, account3, ... ]
```

**This mismatch breaks everything that depends on list behavior.**

#### ✅ What Is Correct

A multi-account system **MUST** use a JSON list:
```json
[
    {
        "account_no": 83,
        "name": "John Doe",
        "dob": "01/01/1990",
        "gender": "M",
        "email": "john@example.com",
        "phone_no": 1234567890,
        "money": 1000
    },
    {
        "account_no": 12,
        "name": "Jane Smith",
        "dob": "15/05/1995",
        "gender": "F",
        "email": "jane@example.com",
        "phone_no": 9876543210,
        "money": 2500
    },
    {
        "account_no": 77,
        "name": "Bob Wilson",
        "dob": "22/08/1988",
        "gender": "M",
        "email": "bob@example.com",
        "phone_no": 5551234567,
        "money": 500
    }
]
```

This is the **ONLY** structure that supports:
- ➕ Appending new accounts
- 🔍 Searching multiple accounts
- ✏️ Updating individual accounts
- 🗑️ Removing an account

**Analogy:**
```
A list is the database TABLE.
Each dictionary is a ROW.
```

#### 📊 Visual Representation

**Wrong Structure (Current):**
```
bank_db.json
     ↓
┌─────────────────┐
│  Single Dict    │  ← Only 1 account
│  {account_no:83}│
└─────────────────┘
```

**Correct Structure (Needed):**
```
bank_db.json
     ↓
┌──────────────────────────────┐
│  List of Dictionaries        │
├──────────────────────────────┤
│  [                           │
│    {account_no: 83},    ← Row 1
│    {account_no: 12},    ← Row 2
│    {account_no: 77}     ← Row 3
│  ]                           │
└──────────────────────────────┘
```

---

### 📋 Finding 2 — Overwriting Data Instead of Appending

#### ❌ What I Did Wrong

When creating a new account:
```python
save_data(bank_account)
```

But since the file is **not a list**, every save operation:
1. **Replaces** the entire file
2. Leaves **only the last created account**
3. **Deletes all previous accounts**

This is why the JSON always contains just **ONE record**.

#### 🔄 The Overwrite Cycle (Visual Flow)

```
User creates Account A
     ↓
bank_db.json = {account_no: 1, name: "Alice"}
     ↓
User creates Account B
     ↓
bank_db.json = {account_no: 2, name: "Bob"}  ← Alice is GONE!
     ↓
User creates Account C
     ↓
bank_db.json = {account_no: 3, name: "Charlie"}  ← Bob is GONE!
```

#### ✅ Correct Concept

Every CRUD system with JSON must follow this sequence:

```
┌─────────────────────────────────────────┐
│  CORRECT SAVE PATTERN                   │
├─────────────────────────────────────────┤
│  1. Load existing list from file        │
│     ↓                                   │
│  2. Append new dictionary to list       │
│     ↓                                   │
│  3. Save entire list back to file       │
└─────────────────────────────────────────┘
```

**Code Pattern:**
```python
# Step 1: Load
accounts = load_data()  # Returns []

# Step 2: Append
new_account = {"account_no": 83, "name": "John", ...}
accounts.append(new_account)

# Step 3: Save
save_data(accounts)  # Writes entire list
```

**Comparison with YouTube Manager:**

My YouTube Manager app already does it correctly:
- ✅ Load → Modify → Save pattern
- ✅ Uses a list structure
- ✅ Never overwrites, always appends

**My BMS must follow the same architecture.**

---

### 📋 Finding 3 — Wrong `account_info()` Logic

#### ❌ What I Did Wrong

My code attempted:
```python
def account_info(bank_account):
    acc_id = int(input("Enter your account ID: "))
    
    for account in bank_account:
        return bank_account[account]  # WRONG!
```

**Logical Errors:**
1. ❌ The loop returns immediately → only first iteration happens
2. ❌ `account` is treated as an index or key → but it's not
3. ❌ Never compare `account_no` with user input
4. ❌ Data is actually a dict, not a list → so iteration is wrong
5. ❌ `bank_account[account]` results in **KeyError**

**Everything fails because the structure is wrong.**

#### ✅ Correct Conceptual Logic

Fetching one account requires:

```
┌────────────────────────────────────────┐
│  ACCOUNT SEARCH ALGORITHM              │
├────────────────────────────────────────┤
│  1. Get account_no from user input     │
│     ↓                                  │
│  2. Iterate through the LIST           │
│     ↓                                  │
│  3. Each element is a DICTIONARY       │
│     ↓                                  │
│  4. Check if element["account_no"]     │
│     matches user input                 │
│     ↓                                  │
│  5. If match → return that dictionary  │
│     ↓                                  │
│  6. If no match → "Account not found"  │
└────────────────────────────────────────┘
```

**Correct Code Pattern:**
```python
def account_info(bank_account):
    acc_id = int(input("Enter your account ID: "))
    
    for account in bank_account:  # Each account is a dict
        if account["account_no"] == acc_id:  # Compare account_no
            return account  # Return the matched account
    
    return None  # Not found
```

**This requires the JSON to be a list of dictionaries, not a single dictionary.**

#### 🔍 Visual Search Process

**Correct Search Flow:**
```
User inputs: account_no = 12

bank_account = [
    {"account_no": 83, "name": "Alice"},  ← Check: 83 != 12, skip
    {"account_no": 12, "name": "Bob"},    ← Check: 12 == 12, FOUND!
    {"account_no": 77, "name": "Charlie"} ← Never reached
]

Return: {"account_no": 12, "name": "Bob"}
```

---

### 📋 Finding 4 — Misunderstanding JSON vs TXT in YouTube Manager

#### ❌ What I Thought

"I saved data in `.txt` in `yt_manager.py` — how can JSON be saved as a list?"

#### ✅ Reality

**A `.json` file is just a text file.**

My YouTube Manager code already saves JSON correctly:
- ✅ It loads a list
- ✅ It appends new items to that list
- ✅ It writes the entire list back as JSON text

**The file extension does not matter — JSON is text.**

#### 🔑 Key Understanding

```
┌──────────────────────────────────────┐
│  File Type Comparison                │
├──────────────────────────────────────┤
│  .txt file  →  Plain text            │
│  .json file →  Plain text with       │
│                JSON structure         │
└──────────────────────────────────────┘

Both are TEXT files.
Both can store lists.
Both are read/written the same way.
```

**My confusion came from:**

| YouTube Manager | BMS |
|----------------|-----|
| List of objects | Single object |
| `[video1, video2, ...]` | `{account1}` |
| ✅ Correct structure | ❌ Wrong structure |

**That's the whole difference.**

---

### 🎯 Root Cause Summary

The entire BMS failure is due to **ONE ISSUE**:

```
╔════════════════════════════════════════╗
║  THE ROOT CAUSE                        ║
║                                        ║
║  Your JSON file was NOT structured     ║
║  as a LIST.                            ║
╚════════════════════════════════════════╝
```

This caused:
- ❌ KeyError
- ❌ TypeError
- ❌ Incorrect iteration
- ❌ Incorrect data loading
- ❌ Incorrect saving
- ❌ Overwriting data
- ❌ `account_info()` never working

**Everything else is a downstream symptom.**

---

### 🏗️ Correct Conceptual Model for the BMS

#### 1️⃣ The Database Should Be a List

```json
[
  {account-1},
  {account-2},
  {account-3}
]
```

#### 2️⃣ Account Creation (CRUD - Create)

```
┌─────────────────────────────────┐
│  CREATE NEW ACCOUNT             │
├─────────────────────────────────┤
│  accounts = load_data()         │  ← Load existing list
│     ↓                           │
│  new_acc = create_account()     │  ← Build new dict
│     ↓                           │
│  accounts.append(new_acc)       │  ← Add to list
│     ↓                           │
│  save_data(accounts)            │  ← Save entire list
└─────────────────────────────────┘
```

#### 3️⃣ Fetching Account Info (CRUD - Read)

```
┌─────────────────────────────────┐
│  FETCH ACCOUNT INFO             │
├─────────────────────────────────┤
│  accounts = load_data()         │  ← Load list
│     ↓                           │
│  for account in accounts:       │  ← Loop through
│      if account["account_no"]   │
│         == user_input:          │  ← Compare
│          return account         │  ← Return match
└─────────────────────────────────┘
```

#### 4️⃣ Updating Balance (CRUD - Update)

```
┌─────────────────────────────────┐
│  UPDATE ACCOUNT BALANCE         │
├─────────────────────────────────┤
│  accounts = load_data()         │  ← Load list
│     ↓                           │
│  for account in accounts:       │  ← Loop through
│      if account["account_no"]   │
│         == user_input:          │  ← Find match
│          account["money"] += x  │  ← Modify
│     ↓                           │
│  save_data(accounts)            │  ← Save entire list
└─────────────────────────────────┘
```

#### 5️⃣ Deleting Account (CRUD - Delete)

```
┌─────────────────────────────────┐
│  DELETE ACCOUNT                 │
├─────────────────────────────────┤
│  accounts = load_data()         │  ← Load list
│     ↓                           │
│  for account in accounts:       │  ← Loop through
│      if account["account_no"]   │
│         == user_input:          │  ← Find match
│          accounts.remove(account)│ ← Remove from list
│     ↓                           │
│  save_data(accounts)            │  ← Save updated list
└─────────────────────────────────┘
```

#### 6️⃣ JSON = Text

```
┌──────────────────────────────────────┐
│  JSON IS JUST TEXT                   │
├──────────────────────────────────────┤
│  Saving JSON list is the same as     │
│  saving text.                        │
│                                      │
│  YouTube Manager already uses        │
│  the correct approach.               │
└──────────────────────────────────────┘
```

---

### 🎓 Why Understanding This Matters

**I am learning how to build a backend.**

The **list-of-dicts JSON structure** is the foundation of:
- 📝 CRUD apps
- 🌐 APIs
- 🗄️ NoSQL databases
- 💾 Local storage systems
- 🖥️ Small backend projects

Once I master this pattern, I can build:
- ✍️ Blog engines
- 🏦 Banking apps
- 📦 Inventory systems
- 📔 Notes apps
- 🔐 Authentication systems
- 🗃️ File-based databases

**This is the core skill.**

---

### 📊 Complete Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                    BMS DATA FLOW                             │
└──────────────────────────────────────────────────────────────┘

    USER ACTION
        ↓
┌───────────────┐
│  main() Menu  │
└───────┬───────┘
        ↓
┌───────────────────────────────────────────────────┐
│               Choose Operation                    │
├────────┬────────┬────────┬────────┬──────────────┤
│ Create │  View  │Deposit │Withdraw│    Delete    │
└────┬───┴───┬────┴───┬────┴───┬────┴──────┬───────┘
     ↓       ↓        ↓        ↓           ↓
     
┌─────────────────────────────────────────────────────────┐
│               LOAD DATA (Always First)                  │
│  accounts = load_data()  # Returns LIST                 │
│  → [account1, account2, account3, ...]                  │
└─────────────────┬───────────────────────────────────────┘
                  ↓
                  
┌─────────────────────────────────────────────────────────┐
│                 MODIFY THE LIST                         │
├─────────────────────────────────────────────────────────┤
│  CREATE:   accounts.append(new_account)                 │
│  VIEW:     find account where account_no matches        │
│  DEPOSIT:  find + modify account["money"] += amount     │
│  WITHDRAW: find + modify account["money"] -= amount     │
│  DELETE:   accounts.remove(found_account)               │
└─────────────────┬───────────────────────────────────────┘
                  ↓
                  
┌─────────────────────────────────────────────────────────┐
│              SAVE DATA (If Modified)                    │
│  save_data(accounts)  # Writes entire LIST              │
│  → Persists to bank_db.json                             │
└─────────────────────────────────────────────────────────┘

```

---

### 🔄 Comparison: Wrong vs Right Architecture

```
╔══════════════════════════════════════════════════════════════╗
║                    WRONG ARCHITECTURE                        ║
╠══════════════════════════════════════════════════════════════╣
║  bank_db.json → Single Dict                                  ║
║       ↓                                                      ║
║  load_data() returns → Dict (not List)                       ║
║       ↓                                                      ║
║  for account in dict → Loops over KEYS (wrong)               ║
║       ↓                                                      ║
║  save_data(dict) → Overwrites entire file                    ║
║       ↓                                                      ║
║  RESULT: KeyError, data loss, broken search                  ║
╚══════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════╗
║                    RIGHT ARCHITECTURE                        ║
╠══════════════════════════════════════════════════════════════╣
║  bank_db.json → List of Dicts                                ║
║       ↓                                                      ║
║  load_data() returns → List of account objects               ║
║       ↓                                                      ║
║  for account in list → Loops over ACCOUNTS (correct)         ║
║       ↓                                                      ║
║  accounts.append() → Adds to list                            ║
║       ↓                                                      ║
║  save_data(list) → Saves all accounts                        ║
║       ↓                                                      ║
║  RESULT: ✅ All operations work correctly                    ║
╚══════════════════════════════════════════════════════════════╝
```

---

### ✅ Final Conclusion

My BMS failed because the **JSON file structure did not match the program's expectations**.

Fixing the structure enables everything:

```
┌────────────────────────────────────────┐
│  WHAT FIXING THE STRUCTURE GIVES YOU   │
├────────────────────────────────────────┤
│  ✅ Multiple accounts                  │
│  ✅ Correct search                     │
│  ✅ Correct update                     │
│  ✅ Correct delete                     │
│  ✅ No KeyError                        │
│  ✅ Proper persistence                 │
│  ✅ Professional-grade CRUD operations │
└────────────────────────────────────────┘
```

**The Fix is Simple:**
```python
# Initialize empty database
bank_db.json → []

# Not this
bank_db.json → {}
```

That one character change makes everything work.

---

## Next Steps

1. ✅ **Fix JSON structure** - Change `bank_db.json` to use list format `[]`
2. ✅ **Update `save_data()`** - Implement proper load-modify-save pattern
3. ✅ **Fix `account_info()`** - Use correct search logic with list iteration
4. Add deposit/withdraw transaction logic
5. Implement account deletion with list.remove()
6. Add input validation for all user inputs
7. Implement unique account number generation

---

## Notes for Future Reference

- ⚠️ The current `account_creation()` uses `json.dump()` with 'a+' mode
  - This causes JSON formatting issues with multiple accounts
  - **Must use** load → append → save pattern instead
  
- ⚠️ Account numbers use `random.randint(1, 100)` - risk of duplicates exists
  - Should implement unique ID generation or sequential numbering
  - Consider: `max([acc["account_no"] for acc in accounts]) + 1`
  
- ⚠️ No input validation currently - should add validation for:
  - Email format (regex)
  - Phone number format (10 digits)
  - Positive numbers for money operations
  - Account number existence before operations

---

*This document will be updated as development continues and new learnings emerge.*
