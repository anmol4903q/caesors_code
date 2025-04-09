# caesors_code
# 🔐 Caesar Cipher - Encryption & Decryption Tool

Welcome to my **Caesar Cipher** project! This tool is a simple Python program that lets you **encrypt** or **decrypt** messages by shifting letters of the alphabet. It's one of the earliest and most classic techniques in the history of cryptography.

---

## 🪖 Why is this project useful?

This type of encryption was **originally used by the Roman military**, especially by **Julius Caesar**, to send top-secret messages from one place to another without being intercepted or understood by enemies.

Even though it's a basic technique by today’s standards, it shows the foundation of how modern encryption works. This project simulates that ancient system and helps understand the core concept of **symmetric key encryption**.

---

## 📜 How it works

- The Caesar Cipher shifts each letter in the message by a certain number of positions in the alphabet.
- For example, shifting `"a"` by 3 becomes `"d"`.
- The same logic can be reversed to decrypt a message back to its original form.

---

## 🔧 Features

- Encrypt or decrypt messages with any number of letter shifts.
- Keeps non-alphabet characters (spaces, punctuation, numbers) unchanged.
- Handles wrapping from `'z'` to `'a'` using modulo math.
- Allows repeating the process until the user chooses to exit.

---

## ▶️ How to run

1. Make sure you have Python installed (3.x version).
2. Run the script in any Python IDE or terminal:
   ```bash
   python caesar_cipher.py
