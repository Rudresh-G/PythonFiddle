class Numbers:
  def __init__(self, arr=[]):
    self.arr = arr
    self.count = len(self.arr)

  def getPrimeFactors(self):
    factors = []
    
    def primeFactorize(n):
      facs = [1]
      isPrime = False
      for fac in range(2, n+1):
        if n % fac == 0:
          facs.append(fac)
          quotient = n//fac
          sub = primeFactorize(quotient)
          if sub[1]:
            facs.append(quotient)
          else:
            [facs.append(val) for val in sub[0][1:]]
          break
        elif fac == n-1 and facs == [1]:
          isPrime = True
      return [facs, isPrime]
    
    for num in self.arr:
      factors.append(primeFactorize(num)[0])
    return factors

  def getFactors(self):
    factors = []

    def factorize(n):
      facs = [1]
      isPrime = False
      for fac in range(2, n):
        if n % fac == 0:
          facs.append(fac)
          continue
        elif fac == n-1 and facs == [1]:
          isPrime = True
      return [facs, isPrime]

    for num in self.arr:
      factors.append(factorize(num)[0])
    return factors


  def getHCF(self):
    def intersect(fac1, fac2):
      commonFac = [val for val in fac1 if val in fac2]
      return commonFac

    factors = self.getFactors()
    commonFactors = factors[1]
    for pf in factors:
      commonFactors = intersect(commonFactors, pf)
    HCF = max(commonFactors)
    return HCF


  def getLCM(self):
    nums = self.arr
    primeFac = self.getPrimeFactors()
    uniqueFac = set([x for sublist in primeFac for x in sublist])
    occurFreq = {}
    for uf in uniqueFac:
      occurFreq[uf] = max([x.count(uf) for x in primeFac])
    LCM = 1
    for uf, x in occurFreq.items():
      LCM *= uf**x
    return LCM