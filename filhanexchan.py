import os 
try:
    with open("fil1.txt", "r") as file:
        content = file.read()
    with open("fil2.txt", "w") as file:
        file.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print("input or output operation file")
except IOError:
    print("I/O error occurred")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
os.remove("fil2.txt")
print("File deleted successfully.")