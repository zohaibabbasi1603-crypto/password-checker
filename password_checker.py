import re

SPECIAL_CHARS = r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]/\\~`~]"


def check_strength(password):
    password = "" if password is None else str(password)
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(SPECIAL_CHARS, password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score >= 5:
        level = "Strong"
    elif score >= 4:
        level = "Good"
    elif score >= 3:
        level = "Medium"
    else:
        level = "Weak"

    return level, feedback


if __name__ == "__main__":
    pwd = input("Enter a password: ")
    level, tips = check_strength(pwd)
    print(f"Strength: {level}")
    if tips:
        print("Suggestions:")
    for tip in tips:
        print(" -", tip)
