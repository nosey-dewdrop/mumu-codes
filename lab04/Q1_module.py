import os

def get_path(filename):
    """
    Returns an absolute file path based on the current file's directory.
    This ensures that files can be found regardless of where the code is executed.
    """
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)


def displayMenu():
    """
    Displays the menu until a valid choice (a, b, c) is entered.
    Returns the lowercase letter chosen.
    """
    while True:
        print("\nMenu:")
        print("(a) Find email by domain")
        print("(b) Display numeric userNames by domain")
        print("(c) EXIT")

        choice = input("Enter choice: ").strip().lower()
        if choice in ['a', 'b', 'c']:
            return choice
        else:
            print("\nInvalid choice! Please enter a, b, or c.")


def findEmailByDomain(domain, filename):
    """
    Reads all emails from 'filename', filters by domain,
    and writes usernames to '<domain>.txt'.
    """
    input_path = get_path(filename)
    output_path = get_path(f"{domain}.txt")

    count = 0
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            line = line.strip()
            if "@" not in line:
                continue

            # example: userOne@cs.bilkent.edu.tr
            at_index = line.find("@")
            dot_index = line.find(".", at_index)

            current_domain = line[at_index + 1:dot_index]
            username = line[:at_index]

            if current_domain == domain:
                outfile.write(username + "\n")
                count += 1

    print(f"{count} users exist in {domain} domain")


def displayUsersHavingNumeric(domain):
    """
    Reads the <domain>.txt file and prints usernames that contain a numeric character.
    If file not found, handles it gracefully.
    """
    file_path = get_path(f"{domain}.txt")

    try:
        with open(file_path, "r") as f:
            found = False
            for line in f:
                user = line.strip()
                if any(ch.isdigit() for ch in user):
                    print(user)
                    found = True
            if not found:
                print("No usernames with numeric characters found.")
    except FileNotFoundError:
        print("No such file exists.")