def displayMenu():
    while True:
        print("\nMenu:")
        print("(a) Find email by domain")
        print("(b) Display numeric userNames by domain")
        print("(c) EXIT")
        choice = input("Enter choice: ").lower().strip()
        
        if choice == 'a' or  choice == 'b' or choice ==  'c':
            return choice
        else:
            print("Invalid choice, try again.")


def findEmailByDomain(emails, domain):
#email is in format userName@domain
      count = 0 
      try:
            with open(emails, "r") as file:
                  for line in file:
                        line = line.strip()
                        if "@" in line:
                              user, rest = line.split("@")
                              dom = rest.split(".")[0]
                              if dom == domain:
                                    with open(f"{domain}.txt", "w") as newFile:
                                         newFile.write(user + "\n")
                                         print(f"{user} has a domain of {domain}")
                                         count += 1

            print(f"{count} users exist in {domain} domain")
      except FileNotFoundError:
            print(f"error: The file {emails} was not found.")

def displayUsersHavingNumeric(domain):
      try:
            with open(f"{domain}.txt", "r") as file:
                  found = False
                  for line in file:
                        user = line.strip()
                        if any(ch.isdigit() for ch in user):
                              print(user)
                              found = True
                        if not found:
                              print(f"No numeric usernames found in {domain} domain.")
      except FileNotFoundError:
            print("No such file exists")
                              
                  