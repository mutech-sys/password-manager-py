
# 🔐 Simple Password Manager (Python CLI)

A beginner-friendly command-line **Password Manager** built with Python. It allows you to **add** and **view** saved usernames and passwords stored in a local text file.

---

## 📌 Features

- ➕ Add username-password entries
- 📄 View saved credentials
- 💾 Stores data locally in `passed.txt`
- 🧠 Simple and minimal logic using file handling

---

## 📂 Files

- `password_manager.py` – main script for managing passwords
- `passed.txt` – auto-created file to store username-password pairs (in plain text)

---

## ▶️ How to Run

Make sure you have **Python 3** installed. Then run:

```bash
python password_manager.py
````

You'll be prompted to choose an action:

* Type `add` → to save a new username-password pair
* Type `view` → to view all stored credentials
* Type `q` → to quit the program

---

## 🖥️ Sample Output

```bash
What do you intend to do? (view, add) Or 'q' to quit : add
ENTER THE USERNAME: johndoe
ENTER THE PASSWORD: 12345secure

What do you intend to do? (view, add) Or 'q' to quit : view
USERNAME: johndoe, PASSWORD: 12345secure

What do you intend to do? (view, add) Or 'q' to quit : q
```

---

## ⚠️ Disclaimer

> ⚠️ This tool **does not encrypt or hash passwords** — they are stored in plain text inside `passed.txt`. For educational purposes only.

---

## 🔐 Future Improvements I have in mind

* Encrypt or hash passwords
* Implement password masking while typing

---

## 🤝 Contributing

Have suggestions or want to help improve this project? Fork it and submit a PR!

---

