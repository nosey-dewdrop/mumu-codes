# CS115 - Lab04
# Files and Modules (single file version)
# Author: Damla Su Bilge 💙

# -------------------------------
# 1. Fonksiyonlar
# -------------------------------

def displayMenu():
    while True:
        print("\nMenu:")
        print("(a) Find email by domain")
        print("(b) Display numeric userNames by domain")
        print("(c) EXIT")
        choice = input("Enter choice: ").lower().strip()
        if choice in ['a', 'b', 'c']:
            return choice
        else:
            print("Invalid input, try again.")


def findEmailByDomain(domain, infile):
    """Girilen domain'e ait kullanıcı adlarını bulur ve domain.txt dosyasına yazar."""
    count = 0

    try:
        with open(infile, "r") as f, open(f"{domain}.txt", "w") as out:
            for line in f:
                line = line.strip()
                if "@" in line:
                    user, rest = line.split("@")
                    dom = rest.split(".")[0]
                    if dom == domain:
                        out.write(user + "\n")
                        print(user)
                        count += 1
                        
        print(f"{count} users exist in {domain} domain")

    except FileNotFoundError:
        print("Input file not found.")


def displayUsersHavingNumeric(domain):
    try:
        with open(f"{domain}.txt", "r") as f:
            found = False
            for line in f:
                user = line.strip()
                if any(ch.isdigit() for ch in user):
                    print(user)
                    found = True
            if not found:
                print("No users with numeric characters.")

    except FileNotFoundError:
        print("No such file exists")


# -------------------------------
# 2. Ana Program
# -------------------------------

def main():
    while True:
        choice = displayMenu()

        if choice == 'a':
            domain = input("Enter domain to search: ").strip()
            findEmailByDomain(domain, "emails.txt")

        elif choice == 'b':
            domain = input("Enter domain to search: ").strip()
            displayUsersHavingNumeric(domain)

        elif choice == 'c':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()