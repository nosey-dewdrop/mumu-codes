def largestDivisor(n):

      biggest = 1
      divisors = []

      for i in range(1, n) :
            if n % i == 0:
                  print(i, "divides", n, "!")
                  divisors.append(i)
                  if(n > biggest):
                        biggest = i

      print("the largest divisor of", n, "is", biggest)
      print("divisors:", divisors)


largestDivisor(15)
            