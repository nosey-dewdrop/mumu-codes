
for i in range(5):
      print(i)
print("\n")

for i in range(5, 10):
      print(i)
print("\n")

for i in range(5, 10, 2):
      print(i)

print("\n")
for i in range(5):
      print(i, end=' ')

print("\n")

sum = 0
for i in range(1, 11):
      sum += i
      print(sum, end=' ')
print(f"\nsum: {sum}")
print("\n")

a = 1
b = 1
print(a, end=' ')
print(b, end=' ')

for _ in range(5) :
      c = a + b
      print(c, end=' ')
      a = b
      b = c

