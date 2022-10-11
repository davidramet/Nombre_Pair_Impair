pair = False

while pair != True:
  nombreAleatoireBis = random.randint(1,100)
  print("Le nombre : ", nombreAleatoireBis)
    if(nombreAleatoireBis % 2 == 0):
      print("Le nombre est pair")
      pair = True
    else:
      print("Le nombre est impair")
      pair = False
print("Le nombre pair est : ", nombreAleatoireBis)    
