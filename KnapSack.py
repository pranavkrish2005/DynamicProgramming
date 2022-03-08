class KnapSac :
  Weight = []
  Value = []
  globalValue = 0
  target = 0
  def __init__(self, val, weight, target) :
    self.Value = val
    self.Weight = weight
    self.target = target

  def calcValue(self) :
    WandV = [[0 for x in range(len(self.Weight))]for y in range(2)]
    sumW  = sum(self.Weight)
    sumV  = sum(self.Value)
    for i in range(len(self.Weight)):
      for j in range(len(self.Weight)):
        localW = sumW - self.Weight[j]
        localV = sumV - self.Value[j]
        if localW <= self.target :
          WandV[0][i] = sumW
          WandV[1][i] = sumV
          if localV > self.globalValue :
            self.globalValue = localV
      sumW -= self.Weight[i]
      sumV -= self.Value[i]
  def toString(self):
    return " Value: " + str(self.globalValue)

one = KnapSac([60,70,80,100], [10,20,30,60], 100)
one.calcValue()
print(one.toString())
