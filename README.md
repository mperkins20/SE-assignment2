# SE-assignment2

## 📌 Project Description
This is a simple Python project that prints a user-friendly greeting. The program prompts the user to enter their name and responds with a personalized message.

## 🛠 Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/mperkins20/SE-assignment2.git

## 🤝 Contributing to This Project
We welcome contributions! Follow these steps to contribute:
1. **Fork the repository** (Click "Fork" at the top right of this page).
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/mperkins20/SE-assignment2.git

---

## 🚀 Issues and Resolutions
Below are documented issues encountered in the project and their resolutions.

### **Issue #1: Input Validation Problem**
- **Problem:** The script allowed empty names, leading to blank greetings.
- **Resolution:** Implemented a `while` loop to repeatedly prompt the user until they enter a valid name.

#### **Updated Code in `hello.py`**
```python
name = input("Enter your name: ").strip()
while not name:
    name = input("Name cannot be empty! Enter your name: ").strip()

print(f"Hello, {name}!")
