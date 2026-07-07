def read_from_position(filename, position):
    with open(filename, "r") as f:
        f.seek(position)
        print(f.read())


if __name__ == "__main__":
    # create sample file for testing
    with open("hello.txt", "w") as f:
        f.write("Hello, World!")

    read_from_position("hello.txt", 7)
