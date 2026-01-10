def is_square(n):
    """returns True if n is a perfect square"""
    root = int(n ** 0.5)
    return root * root == n

def is_prime(n):
    """returns True if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def safe_int(prompt):
      """keeps asking until user enters a valid integer"""
      while True:
            val = input(prompt).strip()
            if val == "":              # boş bırakırsa
                  print("You must enter a number.")
                  continue
            try:
                  return int(val)
            except ValueError:
                  print("Please enter a valid integer number.")

"""prime or square but not both"""
stop = False

while not stop:

      print("\nenter 0 0 to quit")

      low = safe_int("enter lower bound: ")
      high = safe_int("enter upper bound: ")

      if low == 0 and high == 0:
            print("bye!")
            stop = True   

      elif low > high:
            print("invalid range\n")

      else:
            count = 0
            total = 0
            print(f"numbers between {low} and {high} that are prime or square but not both:")
            
            for n in range(low, high + 1):
                  square = is_square(n)
                  prime = is_prime(n)
                  if (square or prime) and not (square and prime):
                        print(f"{n}", end="  ")
                        count += 1
                        total += n

            if count == 0:    
                  print("nothing found.")
                        
            else:
                 print(f"\n{count} values found, sum = {total}\n")


