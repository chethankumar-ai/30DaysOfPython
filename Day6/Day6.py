# Generate a random 8-character password
import random
def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password()
print(f"Generated password: {password}")