# 🔐 Substitution Cipher

A Python implementation of a substitution cipher for encrypting and decrypting text messages. This project demonstrates classical cryptography techniques using randomized character mapping.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Technical Details](#technical-details)
- [Security Note](#security-note)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

A **substitution cipher** is a method of encryption where each character in the plaintext is replaced with another character according to a fixed mapping (key). This implementation creates a random substitution key and uses it to encrypt and decrypt messages.

### What is a Substitution Cipher?

In a substitution cipher:
- Each character is mapped to exactly one other character
- The mapping is defined by a "key" 
- The same plaintext character always maps to the same ciphertext character
- Decryption reverses the process using the same key

---

## ✨ Features

- 🎲 **Random Key Generation** - Creates unique substitution keys
- 🔒 **Text Encryption** - Convert plaintext to ciphertext
- 🔓 **Text Decryption** - Convert ciphertext back to plaintext
- 📝 **Support for Multiple Character Types**:
  - Uppercase and lowercase letters
  - Numbers
  - Punctuation marks
  - Special characters
  - Spaces

---

## 🔧 How It Works

### Encryption Process

1. **Key Generation**: A random substitution key is created by shuffling all possible characters
2. **Character Mapping**: Each character in the plaintext is looked up in the original character set
3. **Substitution**: The character at that position is replaced with the character at the same position in the shuffled key
4. **Result**: Encrypted ciphertext is produced

### Decryption Process

1. **Reverse Lookup**: Each character in the ciphertext is found in the shuffled key
2. **Original Character**: The original character is retrieved from the same position in the original character set
3. **Result**: Original plaintext is recovered

---

## 📥 Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/substitution-cipher.git
cd substitution-cipher
```

2. **No additional dependencies required** - Uses only Python standard library!

---

## 🚀 Usage

### Running the Program

```bash
python substitution_cipher.py
```

### Interactive Mode

The program will prompt you to:

1. **Enter plaintext** to encrypt
2. **View encrypted ciphertext**
3. **Enter ciphertext** to decrypt (or use the one just generated)
4. **View decrypted plaintext**

### Example Session

```
Enter plain text to encrypt: Hello World!
Encrypted: Xczz3 i3mz5!

Enter cipher text to decrypt: Xczz3 i3mz5!
Decrypted: Hello World!
```

---

## 💡 Example

### Python Script Usage

```python
from substitution_cipher import encrypt, decrypt, gen_key

# Generate a substitution key
key, chars = gen_key()

# Encrypt a message
plaintext = "Secret Message"
ciphertext = encrypt(plaintext, key, chars)
print(f"Encrypted: {ciphertext}")

# Decrypt the message
decrypted = decrypt(ciphertext, key, chars)
print(f"Decrypted: {decrypted}")
```

### Sample Output

```
Original:  The quick brown fox jumps over the lazy dog
Encrypted: Kz< n@7oe p23y) g3V w@d+x 3!<2 Kz< z8fw 53q
Decrypted: The quick brown fox jumps over the lazy dog
```

---

## 🔍 Technical Details

### Character Set

The cipher supports the following character types:

```python
chars = " " + string.ascii_letters + string.digits + string.punctuation
```

- **Spaces**
- **Letters**: A-Z, a-z (52 letters)
- **Digits**: 0-9 (10 digits)
- **Punctuation**: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (32 symbols)

**Total**: ~95 unique characters

### Algorithm Complexity

- **Time Complexity**: O(n) - where n is the length of the input text
- **Space Complexity**: O(m) - where m is the size of the character set (~95 characters)

### Key Generation

The substitution key is created by:
1. Creating a list of all supported characters
2. Creating a copy of this list
3. Shuffling the copy using `random.shuffle()`
4. The shuffled list becomes the substitution key

---

## ⚠️ Security Note

**This is an educational implementation and should NOT be used for real-world security purposes.**

### Vulnerabilities

- ❌ **Frequency Analysis**: Substitution ciphers are vulnerable to statistical attacks
- ❌ **No Key Management**: Key is generated randomly but not securely stored or shared
- ❌ **Pattern Preservation**: Word lengths and patterns remain visible
- ❌ **Not Cryptographically Secure**: Uses Python's `random` module (not cryptographically secure)

### Why It's Weak

```
Original:  "attack at dawn"
Encrypted: "8kk8oe 8k 58y)"
           ↓ ↓ ↓  ↓ ↓
        Pattern preserved: XX XYXZ
```

An attacker can:
- Analyze letter frequency (E is most common in English)
- Look for common words (THE, AND, etc.)
- Detect patterns (double letters, word lengths)

### For Real Security, Use:

- ✅ **AES (Advanced Encryption Standard)**
- ✅ **RSA** for asymmetric encryption
- ✅ **Modern cryptographic libraries** (e.g., `cryptography` in Python)

---

## 🎓 Learning Objectives

This project demonstrates:

- Classical cryptography concepts
- String manipulation in Python
- Randomization and shuffling algorithms
- Function design and modularity
- Basic encryption/decryption workflows

---

## 🐛 Known Issues & Improvements

### Current Limitations

1. **No Key Persistence**: Key is regenerated each run (encryption/decryption won't match)
2. **No Key Sharing**: No mechanism to share the key between sender and receiver
3. **No Input Validation**: Doesn't handle unsupported characters gracefully

### Potential Improvements

- [ ] Save/load keys to/from files
- [ ] Add key sharing mechanism
- [ ] Support for key generation from a passphrase
- [ ] GUI interface
- [ ] File encryption/decryption
- [ ] Multiple encryption modes (Caesar, Vigenère)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions

- Add unit tests
- Implement key management
- Create a GUI
- Add more cipher types
- Improve error handling
- Add command-line arguments

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Swarnabha Sharma**

- 📧 Email: [swarnabha.sharma2005@gmail.com](mailto:swarnabha.sharma2005@gmail.com)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/swarnabha-sharma)
- 🐙 GitHub: [@SwarnabhaSharma](https://github.com/SwarnabhaSharma)

---

## 📚 Additional Resources

### Learn More About Cryptography

- [Cryptography Basics - Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Classical Ciphers - Wikipedia](https://en.wikipedia.org/wiki/Classical_cipher)
- [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis)

### Python Cryptography

- [Python `cryptography` library](https://cryptography.io/)
- [Practical Cryptography with Python](https://www.pythonforbeginners.com/code-snippets-source-code/python-encryption)

---

## 🎯 Project Status

![Status](https://img.shields.io/badge/Status-Educational-blue)
![Python](https://img.shields.io/badge/Python-3.6+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

---

<div align="center">

**⚠️ For Educational Purposes Only ⚠️**

*This is a learning project demonstrating classical cryptography concepts.*  
*Do not use for actual security needs!*

---

Made with 🔐 by Swarnabha Sharma

</div>
