def read_lines(filename):
    with open(filename, "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line.rstrip()}")


if __name__ == "__main__":
    # create sample file for testing
    with open("data.txt", "w") as f:
        f.write("Apple\nBanana\nCherry")

    read_lines("data.txt")
