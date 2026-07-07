def add_log(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")


if __name__ == "__main__":
    add_log("User logged in")
    add_log("File uploaded")

    # verify
    with open("log.txt", "r") as f:
        print(f.read())
