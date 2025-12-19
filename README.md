

# Cipher 🔐
**A lightweight, file-based encryption tool written in Python**

Cipher is an open-source command-line application for securely encrypting and decrypting messages using symmetric cryptography. It is designed to be simple, reliable, and resistant to common terminal copy-paste issues by storing encrypted data directly in files.

---

## ✨ Features
- Secure key generation and management
- File-based message encryption (`message.enc`)
- Safe decryption using the same key
- No copy-paste of encrypted text
- Offline, fast, and lightweight
- Clean and beginner-friendly CLI menu

---

## 🔐 Cryptography Overview
Cipher uses **Fernet** from the `cryptography` library. Fernet is a high-level symmetric encryption scheme that provides:

- **Confidentiality** using AES encryption  
- **Integrity and authenticity** using HMAC  
- Protection against message tampering  

> ⚠️ Cipher uses symmetric encryption. Anyone with access to `secret.key` can decrypt the message.

---

## 🛠 Requirements
- Python **3.8+**
- `cryptography` library

Install the dependency:
```bash
pip install cryptography
````

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cipher.git
cd cipher
```

---

## ▶️ Usage

Run the application:

```bash
python cipher.py
```

You will see an interactive menu:

```
1) Generate New Key
2) Encrypt Message → file
3) Decrypt Message ← file
4) Exit
```

---

## ⚙️ How It Works

### 1. Key Generation

* Cipher generates a secure random symmetric key using Fernet.
* The key is saved locally as `secret.key`.
* This key is required for both encryption and decryption.

### 2. Encryption

* The user enters a plaintext message.
* Cipher encrypts the message using the loaded key.
* The encrypted output is written to `message.enc`.

### 3. Decryption

* Cipher reads the encrypted data from `message.enc`.
* The same key (`secret.key`) is used to decrypt the message.
* If the key or encrypted file has been altered, decryption fails safely.

This file-based workflow avoids copy-paste errors and ensures consistent encryption behavior.

---

## 📁 Generated Files

| File          | Description                   |
| ------------- | ----------------------------- |
| `secret.key`  | Encryption key (KEEP PRIVATE) |
| `message.enc` | Encrypted message file        |

Both files are created in the directory where the program is executed.

---

## 🧭 Typical Workflow

1. Generate a key (option 1)
2. Encrypt a message (option 2)
3. Decrypt the message later (option 3)

---

## 🚨 Common Issues

### Decryption Failed

Possible causes:

* `secret.key` was overwritten after encryption
* `message.enc` was edited or corrupted
* Key and encrypted file are from different directories

### File Not Found

* Encryption was not performed before decryption
* The program was run from a different folder

---

## 🔒 Security Considerations

* Never share `secret.key`
* Back up the key securely
* Losing the key permanently locks the encrypted message
* Cipher encrypts one message at a time (new encryption overwrites `message.enc`)

---

## 🧪 Intended Use

Cipher is intended for:

* Learning cryptography fundamentals
* Secure local message storage
* Educational and personal projects

It is not intended for enterprise or production-grade security systems.

---

## 🛣 Roadmap

* Encrypt and decrypt any file type (PDFs, images, text files)
* Password-based key derivation (PBKDF2 or scrypt)
* Support multiple encrypted messages
* CLI arguments (non-interactive mode)
* Cross-platform packaging

---

## 🤝 Contributing

Contributions are welcome.

* Fork the repository
* Create a feature branch
* Commit your changes
* Open a pull request

---

## 📄 License

This project is open-source and free to use for educational and personal projects.

---

## 👤 Author

Built as a Python cryptography learning project.

```


