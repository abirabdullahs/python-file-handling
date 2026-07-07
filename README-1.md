# 🗓 Practice Day Sheet
## Module 3.5 — File Handling & Exception Handling

**Topics:** File Basics · Read · Write/Append · File Pointer · Try/Except/Else/Finally

---

## Problem 1: Create and Write to a File

Write a function `create_file(filename, content)` that creates a new text file with the given filename and writes the content into it. Call it using positional arguments.

**📥 Sample Input:**
```
"notes.txt", "Hello, this is my first file."
```

**📤 Sample Output (notes.txt will contain):**
```
Hello, this is my first file.
```

---

## Problem 2: Read Lines with Line Numbers

Write a function `read_lines(filename)` that reads a text file and prints each line with its line number.

**📥 Sample Input (file: data.txt):**
```
Apple
Banana
Cherry
```

**📤 Sample Output:**
```
1: Apple
2: Banana
3: Cherry
```

---

## Problem 3: Append Log Entries to a File

Given a filename `log.txt`, use file append mode to add a new log entry each time the function `add_log(message)` is called. Each message should appear on a new line.

**📥 Sample Input:**
```
add_log("User logged in")
add_log("File uploaded")
```

**📤 Sample Output (log.txt will contain):**
```
User logged in
File uploaded
```

---

## Problem 4: Read from a Specific File Pointer Position

Write a function `read_from_position(filename, position)` that uses the file pointer to start reading a file from a given byte position and prints the remaining content.

**📥 Sample Input:**
```
filename = "hello.txt"  # contains: "Hello, World!"
position = 7
```

**📤 Sample Output:**
```
World!
```

---

## Problem 5 ⭐ (Conceptual Session): Safe File Read with Full Exception Handling

Write a function `safe_read(filename)` that tries to open and read a file. Use `try`, `except`, `else`, and `finally` blocks:
- Print file content if successful (else block)
- Handle the case where file does not exist (except block)
- Always print "Operation complete." at the end (finally block)

**📥 Sample Input 1:**
```
safe_read("missing.txt")
```

**📤 Sample Output 1:**
```
Error: File not found.
Operation complete.
```

**📥 Sample Input 2:**
```
safe_read("hello.txt")  # contains: "Hello, World!"
```

**📤 Sample Output 2:**
```
Hello, World!
Operation complete.
```
