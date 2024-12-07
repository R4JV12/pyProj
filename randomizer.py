import os, random, time, sys

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def randomize(jar, parts, cls, interval=0, remaining_choices=1):
    if not jar: 
        print("No choices to pick from!")
        return
    removals = len(jar) - remaining_choices
    executed = False
    clear()
    if removals > 0 and remaining_choices != 0:
        for _ in range(removals):
            unfaithful = random.choice(jar)
            jar.remove(unfaithful)

            if not cls: 
                print(f"'{unfaithful}' is out of the game!")
                time.sleep(interval)
        executed = True
    if cls: clear()
    if jar and executed: 
        if len(parts) == 3: 
            print(f"Final choices: \n{',\n'.join(jar)}")
        else: 
            print(f"Final choice: {jar[0]}")
    if not executed: 
        print("Error!")

clear()

jar = []

while True:
    cmd = input(f"Choice {len(jar) + 1}: ").strip()
    if cmd.lower().startswith("done"):
        parts = cmd.split()
        try:
            randomize(jar, parts, len(parts) == 1, float(parts[1]), int(parts[2]))
        except Exception:
            print("Error Occurred!")
        break
    elif cmd.lower() in ["coin", "flip", "toss"]: 
        time.sleep(random.uniform(1, 2))
        print(random.choice(["Heads", "Tails"]))
    elif cmd.lower() == "number": 
        print(random.randint())
    elif cmd.lower() in ["cls", "clean", "clear"]: 
        clear()
    elif cmd.lower() == "exit": 
        sys.exit(0)
    else: 
        jar.append(cmd)
