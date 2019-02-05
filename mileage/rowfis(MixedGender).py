import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class RowingFIS(object):
  def __init__(self):
    #inputs
    self.catch = ctrl.Antecedent(np.arange(56, 70, 0.1), 'Catch')
    self.catch['Novice'] = fuzz.trapmf(self.catch.universe, [56,56,59.2,61])
    self.catch['Intermediate'] = fuzz.gaussmf(self.catch.universe, 62, 0.7)
    self.catch['National'] = fuzz.gaussmf(self.catch.universe, 64.7, 0.7)
    self.catch['International'] = fuzz.trapmf(self.catch.universe, [66.1, 68.2, 70, 70])

    self.finish = ctrl.Antecedent(np.arange(36, 46, 0.1), 'Finish')
    self.finish['Novice'] = fuzz.trapmf(self.finish.universe, [0,36,36,38.9])
    self.finish['Intermediate'] = fuzz.gaussmf(self.finish.universe, 40.4, 0.8)
    self.finish['National'] = fuzz.gaussmf(self.finish.universe, 42.7, 0.8)
    self.finish['International'] = fuzz.trapmf(self.finish.universe, [43.6, 45.8, 46, 46])

    self.slip = ctrl.Antecedent(np.arange(2, 10, 0.1), 'Slip')
    self.slip['Novice'] = fuzz.trapmf(self.slip.universe, [6.9, 8.8, 10,10])
    self.slip['Intermediate'] = fuzz.gaussmf(self.slip.universe, 6.2, 0.4)
    self.slip['National'] = fuzz.gaussmf(self.slip.universe, 4.6, 0.4)
    self.slip['International'] = fuzz.trapmf(self.slip.universe, [2, 2, 2.2, 3])

    self.wash = ctrl.Antecedent(np.arange(9, 30, 0.1), 'Wash')
    self.wash['Novice'] = fuzz.trapmf(self.wash.universe, [18.9, 23.1, 30, 30])
    self.wash['Intermediate'] = fuzz.gaussmf(self.wash.universe, 20.2, 1.2)
    self.wash['National'] = fuzz.gaussmf(self.wash.universe, 17.2, 1.2)
    self.wash['International'] = fuzz.trapmf(self.wash.universe, [9,9, 10.9,18.3])
    
    self.length = ctrl.Antecedent(np.arange(92, 115, 0.1), 'Length')
    self.length['Novice'] = fuzz.trapmf(self.length.universe, [92,92,100.2,102.3])
    self.length['Intermediate'] = fuzz.gaussmf(self.length.universe, 103.2, 1.2)
    self.length['National'] = fuzz.gaussmf(self.length.universe, 106.6, 1.2)
    self.length['International'] = fuzz.trapmf(self.length.universe, [107.7, 112.2, 115,115])

    #output 
    self.quality = ctrl.Consequent(np.arange(0, 101, 0.1), 'Quality')
    #setting membership functions
    self.quality['Novice'] = fuzz.gaussmf(self.quality.universe, 0, 10)
    self.quality['Intermediate'] = fuzz.gaussmf(self.quality.universe, 40, 8)
    self.quality['National'] = fuzz.gaussmf(self.quality.universe, 60, 8)
    self.quality['International'] = fuzz.gaussmf(self.quality.universe, 100, 10)

    #catch 
    rule1 = ctrl.Rule(self.catch['Novice'], self.quality['Novice'])
    rule2 = ctrl.Rule(self.catch['Intermediate'], self.quality['Intermediate'])
    rule3 = ctrl.Rule(self.catch['National'], self.quality['National'])
    rule4 = ctrl.Rule(self.catch['International'], self.quality['International'])
    #finish
    rule5 = ctrl.Rule(self.finish['Novice'], self.quality['Novice'])
    rule6 = ctrl.Rule(self.finish['Intermediate'], self.quality['Intermediate'])
    rule7 = ctrl.Rule(self.finish['National'], self.quality['National'])
    rule8 = ctrl.Rule(self.finish['International'], self.quality['International'])
    #slip
    rule9  = ctrl.Rule(self.slip['Novice'], self.quality['Novice'])
    rule10 = ctrl.Rule(self.slip['Intermediate'], self.quality['Intermediate'])
    rule11 = ctrl.Rule(self.slip['National'], self.quality['National'])
    rule12 = ctrl.Rule(self.slip['International'], self.quality['International'])
    #wash
    rule13 = ctrl.Rule(self.wash['Novice'], self.quality['Novice'])
    rule14 = ctrl.Rule(self.wash['Intermediate'], self.quality['Intermediate'])
    rule15 = ctrl.Rule(self.wash['National'], self.quality['National'])
    rule16 = ctrl.Rule(self.wash['International'], self.quality['International'])
    #length
    rule17 = ctrl.Rule(self.length['Novice'], self.quality['Novice'])
    rule18 = ctrl.Rule(self.length['Intermediate'], self.quality['Intermediate'])
    rule19 = ctrl.Rule(self.length['National'], self.quality['National'])
    rule20 = ctrl.Rule(self.length['International'], self.quality['International'])

    rowingFIS_ctrl = ctrl.ControlSystem([
      rule1, rule2, rule3, rule4, #catch
      rule5, rule6, rule7, rule8,#finish
      rule9, rule10, rule11, rule12,#slip
      rule13, rule14, rule15, rule16,#wash
      rule17, rule18, rule19, rule20#length
    ])

    self.rowingFis = ctrl.ControlSystemSimulation(rowingFIS_ctrl)

  def EvalStroke(self, catch, finish, slip, wash, length):
    self.rowingFis.input['Catch'] = catch
    self.rowingFis.input['Finish'] = finish
    self.rowingFis.input['Slip'] = slip
    self.rowingFis.input['Wash'] = wash
    self.rowingFis.input['Length'] = length  
    self.rowingFis.compute()
    self.quality.view(sim=self.rowingFis)
    return self.rowingFis.output['Quality']

  def ViewPlots(self):
    return self.quality.view(), self.catch.view(), self.finish.view(), self.slip.view(), self.wash.view(), self.length.view()



fis = RowingFIS()

#fis.ViewPlots()
print(fis.EvalStroke(69,46,2,12,111)) #international man
print(fis.EvalStroke(65.7,43.1,4.1,14.3,108)) #national man
print(fis.EvalStroke(63.4,41.5,5.5,21.5,104.2)) #national women

wait = input("PRESS ENTER TO CONTINUE.")





