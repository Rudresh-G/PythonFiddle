# check whether a input number is prime or not
def checkFactors(num):
    factors = []
    isPrime = False
    for fac in range(2, num):
      if num % fac == 0:
        factors.append(fac)
        continue
      elif fac == num-1 and factors == []:
        isPrime = True
    return factors, isPrime

print('----CHECK FOR PRIME NUMBER----')
number = int(input('input number to check:'))
print(checkFactors(number))