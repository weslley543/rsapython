import math 
class Rsa:
  def __init__(self, messageReceived):
    self.message = len(messageReceived.encode('utf-8'))
    self.p = 11
    self.q = 7
    self.e = 3
  
  def encript(self):
    n = self.p*self.q

    phi = (self.p-1)*(self.q-1)
    while math.gcd(phi, self.e) > 1:
      e = e + 2
    
    self.d = math.pow(e, -1, phi)

    encripted = math.pow(self.message, e, n)


