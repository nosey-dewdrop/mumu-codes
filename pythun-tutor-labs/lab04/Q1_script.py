from Q1_module import displayMenu, findEmailByDomain, displayUsersHavingNumeric

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