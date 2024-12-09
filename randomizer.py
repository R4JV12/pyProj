import os, time, random, sys

def clear(): os.system("cls" if os.name == "nt" else "clear")


def randomize(cmd, jar, interval=0, remaining=1, cls=False):
    if not jar:
        print("No choices to pick from!")
        return

    to_remove = len(jar) - remaining
    clear()

    if to_remove > 0:
        for _ in range(to_remove):
            unfaithful = random.choice(jar)
            jar.remove(unfaithful)
            print(f"Removing: {unfaithful}") if len(cmd.split()) >= 2 else print("", end="")
            time.sleep(interval)

    if cls: clear()

    print("\nFinal choice(s):", ", ".join(jar)) if len(cmd.split()) >= 2 else print(f"Final Choice: {jar[0]}")


def main():
    clear()
    jar = []

    while True:
        cmd = input(f"Choice {len(jar) + 1}: ").strip()
        if cmd.lower().startswith("done"):
            try:
                parts = cmd.split()
                interval = float(parts[1]) if len(parts) > 1 else 0
                remaining = int(parts[2]) if len(parts) > 2 else 1
            except ValueError:
                print("Invalid input! type 'help' for assistance.")
                continue
            randomize(cmd, jar, interval, max(1, remaining))
            break
        elif cmd.lower() in ["coin", "toss"]:
            print(random.choice([True, False]))
        elif cmd.lower() == "number":
            print(random.randint(1, 100))
        elif cmd.lower() in ["cls", "clean", "clear"]:
            clear()
        elif cmd.lower() == "exit":
            sys.exit(0)
        else:
            jar.append(cmd)

    input("Enter to restart...")


if __name__ == "__main__":
    while True:
        main()
