import os, time, random, sys

def clear(): os.system("cls" if os.name == "nt" else "clear")


def randomize(choices, interval=0, remaining=1, cls=False):
    if not choices:
        print("No choices to pick from!")
        return

    to_remove = len(choices) - remaining
    clear()

    if to_remove > 0:
        for _ in range(to_remove):
            unfaithful = random.choice(choices)
            choices.remove(unfaithful)
            print(f"Removing: {unfaithful}")
            time.sleep(interval)

    if cls: clear()

    print("\nFinal choice(s):", ", ".join(choices))


def main():
    clear()
    choices = []

    while True:
        cmd = input(f"Choice {len(choices) + 1}: ").strip()
        if cmd.lower().startswith("done"):
            try:
                parts = cmd.split()
                interval = float(parts[1]) if len(parts) > 1 else 0
                remaining = int(parts[2]) if len(parts) > 2 else 1
            except ValueError:
                print("Invalid input! type 'help' for assistance.")
                continue
            randomize(choices, interval, max(1, remaining))
            break
        elif cmd.lower() in ["coin", "toss"]:
            print(random.choice(["Heads", "Tails"]))
        elif cmd.lower() == "number":
            print(random.randint(1, 100))
        elif cmd.lower() in ["cls", "clean", "clear"]:
            clear()
        elif cmd.lower() == "exit":
            sys.exit(0)
        else:
            choices.append(cmd)

    input("Enter to restart...")


if __name__ == "__main__":
    while True:
        main()
