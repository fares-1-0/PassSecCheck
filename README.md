# PassSecCheck

A simple password auditing tool written in Python.

## Features
- Password strength check (length, upper/lowercase, digits, symbols)
- Check against a list of common weak passwords
- Check against known data breaches using the HaveIBeenPwned API (k-anonymity: the password never leaves your machine)

## Usage
```bash
pip install -r requirements.txt
python3 main.py
```
