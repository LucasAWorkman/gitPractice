from math import sqrt, floor
userName = input("What is your name")
print(f"Hello, {userName}")
userNumber = int(input("What is your lucky number"))
print(f"I guess that your lucky number is {userNumber}")

def UserNum(n):
    return n * 100

def UserNumPrime(n):
    for i in range(2, floor(sqrt(n)) + 1):
            if n % i == 0:
              return False
    return True


print(UserNum(userNumber),"is your number multiplied by 100")

primeValue = UserNumPrime(userNumber)

if primeValue:
    print("Your Number is prime")
else:
    print("Your number is not prime")
    
