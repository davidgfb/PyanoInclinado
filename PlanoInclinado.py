from math import cos, radians

def uPlanoInclinadoRoz(alfa): # en equilibrio, a = 0, Px = Fr
    return cos(radians(90 - alfa))

def aPlanoInclinadoRoz(g, u, alfa): # rampa, Fap + Px > Fr 
    return abs(g * (u - uPlanoInclinadoRoz(alfa)))

def vPlanoInclinadoRoz(g, u, alfa, t):
    return abs(aPlanoInclinadoRoz(g, u, alfa) * t) # v = a * t 

#PROBADOR
g, u, alfa, t = 9.81, 0.1, 30, 1 # m/s^2, º, s
print(round(aPlanoInclinadoRoz(g, u, alfa), 2),\
      "debe ser 3.92 m/s^2\n",\
      round(uPlanoInclinadoRoz(alfa), 2), "debe ser 0.5\n",\
      round(vPlanoInclinadoRoz(g, u, alfa, t), 2),\
      "debe ser 3.92 s")
