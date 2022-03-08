{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b265b83e-e338-40e9-aaae-5948b3fc95ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Value: 240\n"
     ]
    }
   ],
   "source": [
    "class KnapSac :\n",
    "  Weight = []\n",
    "  Value = []\n",
    "  globalValue = 0\n",
    "  target = 0\n",
    "  def __init__(self, val, weight, target) :\n",
    "    self.Value = val\n",
    "    self.Weight = weight\n",
    "    self.target = target\n",
    "\n",
    "  def calcValue(self) :\n",
    "    WandV = [[0 for x in range(len(self.Weight))]for y in range(2)]\n",
    "    sumW  = sum(self.Weight)\n",
    "    sumV  = sum(self.Value)\n",
    "    for i in range(len(self.Weight)):\n",
    "      for j in range(len(self.Weight)):\n",
    "        localW = sumW - self.Weight[j]\n",
    "        localV = sumV - self.Value[j]\n",
    "        if localW <= self.target :\n",
    "          WandV[0][i] = sumW\n",
    "          WandV[1][i] = sumV\n",
    "          if localV > self.globalValue :\n",
    "            self.globalValue = localV\n",
    "      sumW -= self.Weight[i]\n",
    "      sumV -= self.Value[i]\n",
    "  def toString(self):\n",
    "    return \" Value: \" + str(self.globalValue)\n",
    "\n",
    "one = KnapSac([60,70,80,100], [10,20,30,60], 100)\n",
    "one.calcValue()\n",
    "print(one.toString())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "030e67c8-a807-4665-8a92-a6a5ec37b516",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
