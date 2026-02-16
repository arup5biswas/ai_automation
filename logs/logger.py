import os

def log(entry):
    os.makedirs("logs", exist_ok=True)

    with open("logs/history.log", "a", encoding="utf-8") as f:
        f.write(entry + "\n")
