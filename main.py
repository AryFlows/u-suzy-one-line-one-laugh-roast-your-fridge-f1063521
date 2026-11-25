import os

ROAST = "My fridge is the only roommate who never pays rent, never cleans, and still judges me every time I open the door at 2am."


def main():
    # The gate allows 1-200 characters; refuse to write an out-of-gate line.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast line is %d characters, outside the 1-200 gate" % len(ROAST))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
