import wikipedia, sys, os

def clear(): os.system("cls" if os.name == "nt" else "clear")

clear()
while True:
    cmd = input("~$ ").strip()
    if cmd.lower() == "exit": sys.exit("Goodbye!")
    if cmd.lower() in ["clear", "cls"]: clear(); continue
    
    try:
        page = wikipedia.page(cmd)

        print(f"Title: {page.title}")
        print(f"\nSummary:\n{page.summary}")
        print(f"\nFull Article: {page.url}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n")
