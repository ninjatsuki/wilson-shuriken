#in this code am gonna create a program that determines if a number is prime or not
import math

while True:
    n = int(input("Enter a number (0 to exit): "))
    if n == 0:
        break
    if (math.factorial(n - 1) + 1) % n == 0:
        print("Prime ✅")
    else:
        print("Not prime ❌")
