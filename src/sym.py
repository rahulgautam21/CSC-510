from re import S
import math

class Sym():

  _has = {}
  n = 0

  def __init__ (self, s = "", c = 0):
    self.name = s
    self.c = c

  # at = c
  # name = s 


  def add (self, v):
    if (v != "?"):
      self.n = self.n + 1

      if v in self._has:
        self._has[v] += 1
      else :
        self._has[v] = 1

    return self._has

    
  def mid (self, mode = 0, most = -1):
    # most = -1

    for k, v in self._has.items():
      if v > most :
        mode, most = k, v

    return mode

  def div (self, e = 0):
    self.e = 0
    sum = 0

    for (_, n) in self._has.items():
      sum += n

    for (_, n) in self._has.items():
      # e = e - fun(n / self.n)
      p = n/sum
      e += p * math.log(p,2)

    return -e 