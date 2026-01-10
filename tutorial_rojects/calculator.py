def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b):
    if(b != 0):
        return a/b
    else:
        return "error"

def show_menu():
    print("\n=== CALCULATOR MENU ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers!")

def perform(choice):
    a, b = get_numbers()
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice.")

def run_calculator():
    
    while True:
        show_menu()
        choice = input("Select (1-5): ").strip()
        if choice == "5":
            print("Goodbye! 👋")
            return
        perform(choice)

# run it
run_calculator()

