# 🔐 Monoalphabetic Substitution Cipher in Python

A Python implementation of a classical cryptographic technique that encrypts and decrypts text using a randomly generated monoalphabetic substitution key.

This project was built to strengthen foundational knowledge of encryption mechanisms and understand how early cryptographic systems operated.

---

## 📌 Project Overview

The Monoalphabetic Substitution Cipher replaces each character in the plaintext with a uniquely mapped character from a shuffled character set.

Unlike simple shift ciphers (like Caesar), this approach creates a far larger keyspace, making brute-force attacks significantly harder — while still being vulnerable to frequency analysis.

This project focuses on:

✅ Understanding encryption fundamentals
✅ Learning key generation concepts
✅ Practicing reversible transformations
✅ Writing modular Python code

---

## ⚙️ Features

* Random key generation using Python’s `random` module
* Encryption of plaintext into ciphertext
* Decryption back to original text
* Handles letters, digits, spaces, and punctuation
* Gracefully ignores unsupported characters

---

## 🧠 How It Works

1. A character set is defined containing letters, numbers, spaces, and symbols.
2. The character set is shuffled to generate a substitution key.
3. Each plaintext character is replaced with its mapped cipher character.
4. Decryption reverses the mapping to recover the original message.

This demonstrates the core cryptographic principle:

> **Secure communication requires both the algorithm and the key.**

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.x installed

Check with:

```
python --version
```

---

### ✅ Run the Program

Clone the repository:

```
git clone https://github.com/yourusername/your-repo-name.git
```

Navigate into the folder:

```
cd your-repo-name
```

Run the script:

```
python substitution_cipher.py
```

---

## 💻 Example

```
Enter plain text to encrypt : hello world

plain text : hello world  
cipher text : %A9!k Zq#1d
```

Decryption restores the original message when the same key is used.

---

## 🔐 Security Note

This project implements a **classical cipher** and is intended for educational purposes only.

Monoalphabetic substitution ciphers are **not secure by modern standards** and can be broken using frequency analysis techniques.

However, they remain an excellent way to understand the evolution of cryptography and the importance of strong key management.

---

## 📚 What I Learned

* Foundations of classical cryptography
* Importance of key generation
* Reversible algorithm design
* Python string handling
* Writing clean, modular functions

---

## 🔮 Future Improvements

* Save and load keys from a file
* Add a command-line interface (CLI)
* Support file encryption
* Implement stronger algorithms (AES, RSA)
* Add unit testing

---

## 👨‍💻 Author

**Swarnabha Sharma**
B.Tech Computer Science | Cybersecurity Enthusiast

Focused on building practical security skills in threat detection, encryption concepts, and defensive security.

---

## ⭐ If You Found This Useful
Consider giving the repository a star — it helps others discover the project!

Consider giving the repository a star — it helps others discover the project!
