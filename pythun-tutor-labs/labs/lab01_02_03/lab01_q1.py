import math

print("quadratic Equation: ax² + bx + c = 0")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b ** 2) - (4 * a * c)
print(f"discriminant (b² - 4ac): {d}")

if (d < 0):
      print("no real roots")

elif (d == 0):
      x = -b / (2 * a)
      print(f"one real root: {x:.2f}")

else:
      x1 = (-b + math.sqrt(d)) / (2 * a)
      x2 = (-b - math.sqrt(d)) / (2 * a)
      print(f"Roots are: {x1:.2f} and {x2:.2f}")
