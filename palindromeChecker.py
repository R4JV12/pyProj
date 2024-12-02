while True: exit() if (cmd := input("~$ ")).lower() == "exit" else print("It's a palindrome" if cmd == cmd[::-1] else "Not a palindrome")
