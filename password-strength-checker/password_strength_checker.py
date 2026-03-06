"""
Password Strength Checker 🔐

A command-line Python tool that:
- Checks password strength
- Identifies missing security requirements
- Suggests a strong password

Author: Shrestha
"""
import string
import random
import getpass

def check_password_strength(password):
    score = 0
    issues=[]
    if len(password) >= 8:
        score += 1
    else:
        issues.append("Too short (minimum 8 characters)")
    if any(c.islower() for c in password):
        score += 1
    else:
        issues.append("Missing lowercase letter")
    if any(c.isupper() for c in password):
        score += 1
    else:
        issues.append("Missing uppercase letter")
    if any(c.isdigit() for c in password):
        score +=1
    else:
        issues.append("Missing digit")
    if any(c in string.punctuation for c in password):
        score +=1
    else:
        issues.append("Missing special character")
    return score, issues

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def main():
    password = getpass.getpass("Enter a password: ")
    if not password:
        print("⚠️Password cannot be empty.")
    else:
        score, issues = check_password_strength(password)

    print(f"Password Strength Score: {score}/5")

    if not issues:
        print("Strong password! you are good to go")
    else:
        print("Weak Password Detected ⚠ \nIssues found:")
        for issue in issues:
            print(f"- {issue}")

    suggestion = generate_strong_password()
    print("\n Suggested Strong Password🔑")
    print(suggestion)

if __name__ == "__main__":
    main()