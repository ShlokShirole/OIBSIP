# 🔐 Password Generator

A modern, dark-themed password generator desktop application built with **Python** and **Tkinter**.  
It generates strong, customizable passwords and keeps a history of generated or copied passwords – all in a clean, user-friendly interface.

![Password Generator UI](https://via.placeholder.com/520x700/1a1a24/4a7cf7?text=Password+Generator+UI)  
*(Replace with actual screenshot if available)*

---

## ✨ Features

- **Customizable Password Length** – Slider from 4 to 32 characters.
- **Character Sets** – Toggle uppercase, lowercase, numbers, and symbols.
- **Real-time Strength Evaluation** – Visual bars and a label (Weak / Medium / Strong) based on length and character variety.
- **Copy to Clipboard** – One‑click copy; the password is also saved to history when copied.
- **History Panel** – Shows timestamps and passwords generated or copied (duplicates are not repeated).
- **Dark Theme** – Fully dark interface with accent colours for strength feedback.
- **Modular Code** – Clean separation of logic, UI, and history management.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** (the app uses only the standard library – no external dependencies)

### Installation

1. Clone or download this repository.

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

2. (Optional) Create and activate a virtual environment – though not required since no external packages are used.

### Run the Application

```bash
python app.py
```

The main window will open, and you can start generating passwords immediately.

---

## 📁 Project Structure

```
password_generator/
│
├── app.py                 # Entry point – launches the Tkinter window
├── constants.py           # Character sets and colour definitions
├── core/
│   ├── __init__.py
│   ├── generator.py       # Password generation logic
│   ├── evaluator.py       # Strength evaluation
│   └── history.py         # History management (add, retrieve)
├── ui/
│   ├── __init__.py
│   └── main_window.py     # Main UI class (Tkinter)
└── README.md              # You are here
```

---

## 🧠 How It Works

- **Generation** – A secure random password is built using `secrets` from the chosen character sets.
- **Strength Evaluation** – Scores are calculated based on length and the variety of character types present. The score is mapped to **Weak**, **Medium**, or **Strong**.
- **History** – Passwords are saved **only** when you click the **GENERATE** button or copy the password. Changing the slider or checkboxes updates the displayed password **without** adding it to history, giving you full control over what gets stored.
- **Copy** – Copies the current password to your clipboard and automatically adds it to history.

---

## 🖥️ Usage Guide

1. Adjust the **Character Length** slider to set the desired password length.
2. Check/uncheck the character type boxes to include or exclude specific sets.
3. The password field updates automatically; the strength bars and label reflect the current password.
4. Click **GENERATE** to create a new password and store it in the history.
5. Click the **📋** button to copy the password – it will also be saved in history.
6. The history list shows each saved password with a timestamp.

---

## 📦 Dependencies

- Python standard library only:
  - `tkinter` – GUI framework
  - `secrets` – cryptographically strong random number generator
  - `string`, `datetime` – utility modules

No extra packages need to be installed.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgements

- Inspired by modern password managers and generator tools.
- Built with ❤️ using Python and Tkinter.

---

**Enjoy generating secure passwords!** 🛡️
