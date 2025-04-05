import os
if os.path.exists("fil1.txt"):
    with open("fil1.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print("File does not exist.")

    