def safe_read(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        content = f.read()
        print(content)
        f.close()
    finally:
        print("Operation complete.")


if __name__ == "__main__":
    safe_read("missing.txt")
    print()

    # create sample file for testing
    with open("hello.txt", "w") as f:
        f.write("Hello, World!")

    safe_read("hello.txt")
