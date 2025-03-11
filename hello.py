print("Hello from both main and feature-2!")
name = input("Enter your name: ").strip()
while not name:
    name = input("Name cannot be empty! Enter your name: ").strip()

print(f"Hello, {name}!")
