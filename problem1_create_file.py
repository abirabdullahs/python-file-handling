def create_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    create_file("notes.txt", "Hello, this is my first file.")

    # verify
    with open("notes.txt", "r") as f:
        print(f.read())
