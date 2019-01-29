import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class MaleFIS(object):
  def __init__(self):
    #inputs
    self.catch = ctrl.Antecedent(np.arange(58, 70, 0.1), 'Catch Angle')
    self.catch['Novice'] = fuzz.trapmf(self.catch.universe, [0,58,60,61.5])
    self.catch['Intermediate'] = fuzz.gaussmf(self.catch.universe, 63.1, 0.7)
    self.catch['National'] = fuzz.gaussmf(self.catch.universe, 65.7, 0.7)
    self.catch['International'] = fuzz.trapmf(self.catch.universe, [67.6, 68.2, 70, 70])

    self.finish = ctrl.Antecedent(np.arange(38, 46, 0.1), 'Finish Angle')
    self.finish['Novice'] = fuzz.trapmf(self.finish.universe, [0,38,38,38.9])
    self.finish['Intermediate'] = fuzz.gaussmf(self.finish.universe, 40.8, 0.8)
    self.finish['National'] = fuzz.gaussmf(self.finish.universe, 43.1, 0.8)
    self.finish['International'] = fuzz.trapmf(self.finish.universe, [45.1, 45.8, 46, 46])

    self.slip = ctrl.Antecedent(np.arange(2, 8, 0.1), 'slip')
    self.slip['Novice'] = fuzz.trapmf(self.slip.universe, [6.9, 7.4, 8,8])
    self.slip['Intermediate'] = fuzz.gaussmf(self.slip.universe, 5.6, 0.4)
    self.slip['National'] = fuzz.gaussmf(self.slip.universe, 4.1, 0.4)
    self.slip['International'] = fuzz.trapmf(self.slip.universe, [2, 2, 2.2, 2.9])

    self.wash = ctrl.Antecedent(np.arange(9, 20, 0.1), 'wash')
    self.wash['Novice'] = fuzz.trapmf(self.wash.universe, [18.9, 19.4, 20, 20])
    self.wash['Intermediate'] = fuzz.gaussmf(self.wash.universe, 16.8, 1)
    self.wash['National'] = fuzz.gaussmf(self.wash.universe, 14.3, 1)
    self.wash['International'] = fuzz.trapmf(self.wash.universe, [9,9, 10.9,12.5])
    
    self.length = ctrl.Antecedent(np.arange(95, 115, 0.1), 'length')
    self.length['Novice'] = fuzz.trapmf(self.length.universe, [95,95,100.2,102.3])
    self.length['Intermediate'] = fuzz.gaussmf(self.length.universe, 104.7, 1.2)
    self.length['National'] = fuzz.gaussmf(self.length.universe, 108, 1.2)
    self.length['International'] = fuzz.trapmf(self.length.universe, [108.0, 111.4, 115,115])

    #output 
    self.q = ctrl.Consequent(np.arange(0, 101, 0.1), 'Quality %')
    #setting membership functions
    self.q['Intermediate'] = fuzz.gaussmf(self.q.universe, 40, 8)
    self.q['Novice'] = fuzz.gaussmf(self.q.universe, 0, 10)
    self.q['National'] = fuzz.gaussmf(self.q.universe, 60, 8)
    self.q['International'] = fuzz.gaussmf(self.q.universe, 100, 10)


  def ViewPlots(self):
    # plt.subplot(6,1,1)
    # plt.plot(self.catch)

    # plt.subplot(6,1,6)
    # plt.plot(self.q)
    return self.q.view(), self.catch.view(), self.finish.view(), self.slip.view(), self.wash.view(), self.length.view()


fis = MaleFIS()

fis.ViewPlots()

wait = input("PRESS ENTER TO CONTINUE.")






