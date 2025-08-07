# 🔑 Password Manager

A simple, secure command-line password manager built in Python that uses Fernet symmetric encryption to safely store your passwords locally.

---

## 📦 Features

- **Secure Encryption**: Uses `cryptography.fernet` for strong symmetric encryption
- **Local Storage**: All passwords are stored locally on your machine
- **Hidden Input**: Password entry is masked for security
- **Simple Interface**: Easy-to-use command-line interface
- **Automatic Key Management**: Generates and manages encryption keys automatically

---

## 🔐 Security Features

- Passwords are encrypted using Fernet
- Master encryption key is automatically generated and stored locally
- Password input is hidden during entry using `getpass`
- All sensitive data is encrypted before being written to disk

---

## ⚙️ Requirements

- Python 3.6 or higher
- `cryptography` library

---

## 🛠️ Installation

1. **Clone or download the script** to your local machine
2. **Install the required dependency**:
   ```bash
   pip install cryptography
   ```

---

## 🚀 Usage

Run the password manager:
```bash
python password_manager.py
```

---

### 👩‍💻 Available Commands

- **`add`**: Add a new password entry
- **`view`**: View all stored passwords (decrypted)
- **`q`**: Quit the application

---

### 🔑 Adding Passwords

1. Choose `add` from the main menu
2. Enter the account name (e.g., "Gmail", "Facebook", "Work Email")
3. Enter the password (input will be hidden)
4. The password will be encrypted and stored

---

### 🔑 Viewing Passwords

1. Choose `view` from the main menu
2. All stored credentials will be displayed in a formatted table
3. Passwords are automatically decrypted for viewing

---

## 🗃️ File Structure

The application creates two files in the same directory:

- **`key.key`**: Contains your encryption key (keep this safe!)
- **`passwords.txt`**: Contains your encrypted password data

---

## ❗Error Handling

The application includes error handling for:
- Missing key files (automatically generates new key)
- Missing password files
- Encryption/decryption errors
- File I/O errors

---

## 🛠️ Potential Improvements

Consider adding these features for enhanced security and usability:
- Master password protection
- Password strength meter
- Password generation utility
- Secure password updates
- Search functionality
- Backup/restore features
- Password expiration reminders

---

## 💡Example Session

```
Welcome to the Password Manager

Would you like to add a new password or view existing passwords (view/add), press 'q' to quit? : add
Account Name: Gmail
Password (input hidden): 
Password for Gmail has been added!

Would you like to add a new password or view existing passwords (view/add), press 'q' to quit? : view

Saved Credentials: 

Username                 Password
---------------------------------------------
Gmail                    mySecretPassword123

Would you like to add a new password or view existing passwords (view/add), press 'q' to quit? : q
Exiting the Password Manager. Goodbye!
```


**Remember**: This is a simple implementation suitable for learning or basic personal use. For production use or storing highly sensitive data, consider using established password managers with additional security features.
