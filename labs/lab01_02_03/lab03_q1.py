def divisible(m, n):
      """Returns True if m is a multiple of n, else False."""
      return m % n == 0

def safe_int(prompt):
      """keeps asking until user enters a valid integer"""
      while True:
            val = input(prompt).strip()
            if val == "":            
                  print("you must enter a number.")
                  continue
            try:
                  return int(val)
            except ValueError:
                  print("please enter a valid integer number.")
 
pairs = []
proceed = True

while proceed:
      a = safe_int("first: ")
      b = safe_int("second: ")
      if(a>0 and b>0):
            pairs.append((a, b))   
      else:
            proceed = False

print(pairs)

divisible_count = 0
for(a, b) in pairs:
      if divisible(a, b):
            print(f"{a} is a multiple of {b}")
            divisible_count += 1
      else:
            print(f"{a} is not a multiple of {b}")

if pairs:
    percentage = (divisible_count / len(pairs)) * 100
    print(f"\n{percentage:.2f}% of the pairs are divisible.")
    
else:
    print("No pairs entered.")