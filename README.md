# 🖼️ Image Code Steganography

This project demonstrates a simple way to **embed Python code into an image file** and later **extract & execute it**.  
It is intended for **educational and security research purposes only** (e.g., showing students how hidden code works).  

⚠️ Do **not** use this project to distribute malware or run untrusted code.  

---

## 🚀 Features
- Hide Python scripts inside any image (`.png`, `.jpg`, etc.)
- Extract hidden code from the image
- Automatically execute the extracted code

---

## 📂 Repository Structure
embed_code.py → Script to hide Python code in an image /n
auto_extract_and_run.py → Script to extract and run hidden code
example.png → Example carrier image
README.md → Documentation
LICENSE → MIT license

---

## 🛠️ Usage

### 1. Embed Code into an Image
```bash
python embed_code.py example.png secret_code.py infected.png
```
Takes example.png and a Python file (secret_code.py)
Embeds the code inside the image
Produces a new image (infected.png) that still opens normally

### 2. Extract & Execute Automatically
```bash
python auto_extract_and_run.py infected.png
```
Reads the specified image (infected.png)
Extracts the hidden Python code
Executes it immediately

---

##⚡ Notes

The hidden code is simply appended to the image file.
The image still works as an image, but if you open it in a hex editor, you can see the hidden data.
For true pixel-based steganography, more advanced methods are needed.

