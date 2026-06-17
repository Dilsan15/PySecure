# PassPhraser 🔐

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10.5-blue?style=for-the-badge&logo=python&logoColor=white)
![Pyglet](https://img.shields.io/badge/Pyglet-1.5.26-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Open_Source-orange?style=for-the-badge)

**A lightweight, readable password generator that creates secure passphrases using real words**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [How It Works](#how-it-works)

</div>

---

## 📖 Overview

PassPhraser is a readable password generator that creates secure, memorable passwords by combining real words instead of random characters. Perfect for users who want strong passwords that are actually possible to remember!

### Why PassPhraser?

Traditional password generators create passwords like: `h7$mK9#pL2@qR`  
PassPhraser creates passwords like: `Correct-Horse-Battery-Staple`

**Benefits:**
- ✅ Easier to remember
- ✅ Just as secure (with sufficient length)
- ✅ Reduces password writing/storage needs
- ✅ Customizable length and special characters

---

## ✨ Features

- **Readable Passwords**: Uses real words from a dictionary API
- **Customizable Length**: Choose how many words to include
- **Special Character Options**: Add numbers and symbols for extra security
- **User-Friendly GUI**: Simple Pyglet-based interface
- **Input Validation**: Error checking with helpful feedback
- **Easy Copying**: One-click copy to clipboard
- **Lightweight**: Minimal dependencies, fast performance
- **Free & Open Source**: Use anywhere, modify as needed

---

## 🖼️ Demo

```
┌─────────────────────────────────────┐
│        PassPhraser Generator        │
├─────────────────────────────────────┤
│                                     │
│  Password Length: [  4  ]           │
│  Include Numbers:  ☑                │
│  Include Symbols:  ☑                │
│                                     │
│  [ Generate Password ]              │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Sunset-Mountain-River-42!   │   │
│  └─────────────────────────────┘   │
│                                     │
│  [ Copy to Clipboard ]              │
│                                     │
└─────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10.5 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/Dilsan15/PassPhraser.git
cd PassPhraser
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install pyglet==1.5.26
pip install requests
```

3. **Run the application**:
```bash
python src/gen_main_app.py
```

---

## 🎯 Usage

### Basic Usage

1. Launch the application
2. Enter desired password length (number of words)
3. Select options for numbers and special characters
4. Click "Generate Password"
5. Copy the generated password

### Command Line (if supported)

```bash
python src/gen_main_app.py --length 4 --numbers --symbols
```

### API Usage

The generator uses a word API to fetch random words. No API key required for basic usage!

---

## 💡 How It Works

### Password Generation Pipeline

```
┌──────────────┐
│ User Input   │
│ - Length     │
│ - Options    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Input        │
│ Validation   │
│ (gen_error)  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ API Request  │
│ Fetch Words  │
│ (gen_api)    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Password     │
│ Assembly     │
│ (gen_creation)│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Display      │
│ Output       │
│ (main_app)   │
└──────────────┘
```

### Architecture

The project follows a modular MVC-style architecture:

#### **gen_main_app.py**
- Main application controller
- Manages GUI window and user interactions
- Connects all components together
- Handles display of input fields and output

#### **gen_error.py**
- Input validation and error checking
- Displays warnings for invalid inputs
- Ensures password generation requirements are met

#### **gen_api.py**
- Communicates with word dictionary API
- Fetches random words based on user preferences
- Handles API errors and retries

#### **gen_creation.py**
- Core password generation logic
- Assembles words into secure passphrases
- Adds numbers, symbols, and capitalization
- Ensures password meets security standards

---

## 🏗️ Project Structure

```
PassPhraser/
├── src/
│   ├── gen_main_app.py    # Main application & GUI
│   ├── gen_error.py       # Input validation
│   ├── gen_api.py         # API communication
│   └── gen_creation.py    # Password generation logic
├── assets/                # GUI assets (if any)
├── .gitignore
└── README.md
```

---

## 🔒 Security Considerations

### Password Strength

PassPhraser generates strong passwords by:
- Using random word selection from large dictionaries
- Adding optional numbers and symbols
- Capitalizing words for increased complexity
- Ensuring sufficient entropy through word count

### Example Entropy Calculation

For a 4-word passphrase from a 10,000-word dictionary:
- Entropy = log₂(10,000⁴) ≈ **53 bits**
- With numbers and symbols: **~60+ bits**

This is comparable to an 8-character random password and much more memorable!

---

## ⚙️ Configuration

### Customization Options

You can modify the generator by editing configuration values:

```python
# In gen_creation.py
MIN_PASSWORD_LENGTH = 3    # Minimum number of words
MAX_PASSWORD_LENGTH = 8    # Maximum number of words
WORD_SEPARATOR = "-"       # Character between words
```

### Using Different Word Sources

Update the API endpoint in `gen_api.py`:

```python
API_URL = "https://your-word-api.com/random"
```

---

## 🧪 Testing

Run the application with various inputs:

```bash
# Test minimum length
python src/gen_main_app.py

# Test with maximum security
python src/gen_main_app.py --length 8 --numbers --symbols
```

### Test Cases

- ✅ Valid inputs (length 3-8)
- ✅ Invalid inputs (length < 3, length > 8)
- ✅ API failure handling
- ✅ Special character insertion
- ✅ Clipboard functionality

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

### Potential Improvements

- [ ] Add password strength meter
- [ ] Support for multiple languages
- [ ] Save password history (encrypted)
- [ ] Dark mode theme
- [ ] Export passwords to password managers
- [ ] Phonetic spelling output
- [ ] Configurable word sources
- [ ] Browser extension version

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Development Notes

### Project Context

This project was developed as a two-week project for CS 10 (2022 high school course), demonstrating:
- Python programming fundamentals
- API integration
- GUI development with Pyglet
- Software architecture principles
- Error handling and validation

---

## 🐛 Troubleshooting

### Common Issues

**API Connection Errors**
```bash
# Check internet connection
# Verify API endpoint is accessible
```

**Pyglet Installation Issues**
```bash
# Try upgrading pip first
pip install --upgrade pip
pip install pyglet==1.5.26
```

**Module Not Found Errors**
```bash
# Ensure you're in the correct directory
cd PassPhraser
python -m src.gen_main_app
```

---

## 📄 License

This project is **open source** and free to use by anyone. Feel free to modify, distribute, and use it in your own projects!

---

## 👨‍💻 Author

**Dilshaan Sandhu**

- GitHub: [@Dilsan15](https://github.com/Dilsan15)
- Project Link: [https://github.com/Dilsan15/PassPhraser](https://github.com/Dilsan15/PassPhraser)

---

## 🙏 Acknowledgments

- Word dictionary API providers
- Pyglet library maintainers
- The passphrase concept popularized by [XKCD #936](https://xkcd.com/936/)
- CS 10 course for project inspiration

---

## 📚 Resources

- [XKCD: Password Strength](https://xkcd.com/936/)
- [Diceware Passphrases](https://theworld.com/~reinhold/diceware.html)
- [Pyglet Documentation](https://pyglet.readthedocs.io/)

---

<div align="center">

**Secure passwords don't have to be impossible to remember!**

⭐ Star this repo if you find it useful!

</div>
