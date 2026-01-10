""" page 63 """
def square_root(x):
      if x < 0:
            print("dne")

      else:
            epsilon = 0.01
            low = 0
            high = max(1, x)

            answer = (high+low)/2

            while abs(answer**2 - x) >= epsilon:
                  if answer**2 < x:
                        low = answer
                  else:
                        high = answer
                  answer = (high + low) / 2
                  
            print(f"Square root of {x} is about {answer:.4f}")

proceed = True    
while proceed:
      x = input("\nenter a number (q to quit): ")
      if(x != "q"):
            square_root(int(x))
      else:
            proceed = False

