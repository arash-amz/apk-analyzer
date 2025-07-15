# APK Static Analyzer

This project is a Python-based **static analysis tool** for Android APK files. It was entirely developed by **Arash Amoozandeh** to help inspect Android applications for security and code transparency.

It uses:
- [`jadx`](https://github.com/skylot/jadx) to decompile APKs
- [`androguard`](https://github.com/androguard/androguard) to extract app metadata

---

## ✨ Written by

**👨‍💻 Arash Amoozandeh**  
GitHub: [https://github.com/arash-amz](https://github.com/arash-amz)  
Email: arash.amoozandeh@gmail.com

> 📌 *This tool was fully written and documented by Arash Amoozandeh as part of his interest in Android reverse engineering and static analysis.*

---

## 🚀 Features

- APK decompilation via `jadx`
- Extracts:
  - App package name, version info
  - All declared permissions (with warning for dangerous ones)
  - Activities and services
  - Hardcoded URLs and IP addresses
  - Sensitive strings like tokens, API keys, passwords
  - Libraries and dependencies used
- Results saved in readable `.txt` reports

## ⚙️ Setup

1. Install Python 3.7+  
2. Install dependencies:
   ```bash
   pip install androguard
