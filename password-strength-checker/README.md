# Password Strength Checker 🔐

A Python command-line tool that analyzes password strength and suggests improvements.

## Features
- Detects weak passwords
- Checks for uppercase, lowercase, digits and special characters
- Suggests a strong password automatically

## Technologies
- Python
- string module
- random module
- getpass module

## Run the program

python password_checker.py

## Example Output

```
Enter a password: hello

Password Strength Score: 1/5
Weak Password Detected ⚠️

Issues Found:
- Too short (minimum 8 characters)
- Missing uppercase letter
- Missing digit
- Missing special character
```