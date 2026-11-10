"""Student Toolkit: calculator, marks percentage, and password generator."""
import secrets
import string

def calculator():
    try:
        a = float(input("First number: "))
        op = input("Operator (+, -, *, /): ").strip()
        b = float(input("Second number: "))
        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/":
            if b == 0:
                print("Cannot divide by zero."); return
            result = a / b
        else:
            print("Unknown operator."); return
        print(f"Result: {result:g}")
    except ValueError:
        print("Please enter valid numbers.")

def marks_percentage():
    try:
        obtained = float(input("Marks obtained: "))
        maximum = float(input("Maximum marks: "))
        if maximum <= 0 or obtained < 0 or obtained > maximum:
            print("Check the marks entered."); return
        print(f"Percentage: {obtained / maximum * 100:.2f}%")
    except ValueError:
        print("Please enter valid numbers.")

def password_generator():
    try:
        length = int(input("Password length (8-64): "))
        if not 8 <= length <= 64:
            print("Choose a length from 8 to 64."); return
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        print("Generated password:", "".join(secrets.choice(alphabet) for _ in range(length)))
        print("Store it safely; do not share it.")
    except ValueError:
        print("Enter a whole number.")

def main():
    actions = {"1": calculator, "2": marks_percentage, "3": password_generator}
    while True:
        print("\n=== STUDENT TOOLKIT ===\n1. Calculator\n2. Marks percentage\n3. Password generator\n0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!"); break
        action = actions.get(choice)
        if action: action()
        else: print("Choose 0, 1, 2, or 3.")

if __name__ == "__main__":
    main()
