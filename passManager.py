import random, shlex ;from os import name, system
symbols, letters, digits = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "'", '"', "<", ">", "?", ".", ",", "/", "~", "`"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"), ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
def clear(): system("cls" if name == "nt" else "clear")
def helper(): print("\ncheck, stren, rate - Check the strength of a password\nexit, quit - Exit the program\nclear, cls - Clear the screen\nhelp, h - Show this message\n")    

def check_needed_char(needed, password):
    for char in needed: 
        if char in password: return True
    return False

def check_pass_strength(password):
    try:
        if len(password) >= 8 and check_needed_char(symbols, password) and check_needed_char(letters, password) and check_needed_char(digits, password): return "Strong"
        elif len(password) == 8 and (check_needed_char(symbols, password) or check_needed_char(letters, password) or check_needed_char(digits, password)): return "Moderate"
        else: return "Weak"
    except Exception as e: return e

def generate_password(length, sym, let, dig):
    password = ""
    if length < 1: return "Error! length is too short"
    
    available_types = []
    if sym: available_types.append(symbols)
    if let: available_types.append(letters)
    if dig: available_types.append(digits)
    if not available_types: return "Error! At least one character type must be selected."

    while length > 0:
        password += random.choice(random.choice(available_types))
        length -= 1
    
    print(f"Your Password: {password}\nStrength: {check_pass_strength(password)}")


def main():
    clear()
    while True:
        cmd = shlex.split(input("~$ ").lower())
        if cmd[0] in ["check", "stren", "rate"] and len(cmd) == 2: print(check_pass_strength(cmd[1])) 
        elif cmd[0] in ["gen", "new"] and len(cmd) >= 3 and len(cmd) <= 5 and cmd[1].isdigit(): generate_password(int(cmd[1]), "sym" in cmd, "let" in cmd, "dig" in cmd)
        elif cmd[0] in ["exit", "quit"]: exit()
        elif cmd[0] in ["clear", "cls"]: clear()
        elif "help" in cmd[0]: helper()
        else: print("Invalid command.")

if __name__ == "__main__": main()
