# Read numbers from a file and handle errors gracefully
try:
    with open(r'/Users/hchethankumar/Desktop/python_workspace/Day10/file.txt', 'r') as var:
        content = var.read()
        for line in content.splitlines():
            try:
                number = int(line.strip())
                print(f"Number: {number}")
            except ValueError:
                print(f"Invalid number found: {line.strip()}")
    print("File read successfully.")  

except FileNotFoundError:
    print("File not found. Please check the file path.") 

except Exception as e:
    print(f"An unexpected error occurred: {e}")