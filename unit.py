class length:
  def __init__(self):  # many kinds of length unit to mm
    self.result = 0
    self.list = {}
    self.list['nm'] = 0.000000000001
    self.list['um'] = 0.000000001
    self.list['mm'] = 0.000001
    self.list['cm'] = 0.00001
    self.list['inch'] = 0.000039370079
    self.list['ja'] = 0.000303030303
    self.list['ft'] = 0.0003048
    self.list['yd'] = 0.0009144
    self.list['m'] = 0.001
    self.list['gan'] = 0.00181818182
    self.list['jung'] = 0.109090909
    self.list['re'] = 0.392727273
    self.list['km'] = 1
    self.list['mile'] = 1.609344
    self.list['he_re'] = 1.852
    self.list['au'] = 149597870.7
    self.list['light day'] = 25880431631.1
    self.list['light year'] = 9446357545315
    self.a = 0         #unit1
    self.b = 0         #unit2
    self.c = 0         #ratio of unit1 and unit2
   
  def calc(self, unit1, unit2, count):     #calculate unit1 to unit2
      self.a = self.list.get(unit1)
      self.b = self.list.get(unit2)
   
  
      self.c = self.a / self.b    #calculate ratio
      self.a = count;       #define if unit1 is count
      self.b = self.a * self.c      #multiply ratio and unit1
      self.result = self.b      
      return self.result       
