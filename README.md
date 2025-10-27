# Lab 6: Fuzzing for Input Validation Bugs

## 🧩 Overview
This lab demonstrates how **fuzz testing (using Hypothesis)** can uncover hidden input validation bugs in Python functions.  
The experiment includes writing, testing, and fixing a `processor.py` script that sanitizes strings, parses integer lists, and reverses words.

---

## ⚙️ Setup
```bash
pip install hypothesis pytest
```

---

## 🧪 Testing Results

### Before Fixes
- 3 tests **failed** (`NoneType` errors in all functions).

### After Fixes
- All **3 tests passed** after adding input validation for `None` and invalid values.

```bash
=================== 3 passed in 0.87s ===================
```

---

## 🧠 Reflection
- **Hypothesis** automatically generated edge-case inputs like `None` and `""`, revealing hidden crashes.  
- After applying validation checks, all functions became robust and safe.  
- Fuzzing can be integrated into **CI/CD** to continuously detect such bugs before release.

---

## 📁 Files
- `processor.py` → Final fixed code  
- `test_processor.py` → Hypothesis-based fuzz tests
