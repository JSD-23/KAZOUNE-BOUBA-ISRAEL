def maxprofit(prix):
  mes_achats = prix[0]
  profits = 0
  #contrôle si on  peut/non  realiser le profit
  if not prix:
    return 0
  for i in range(1, len(prix)):
    if prix[i] < mes_achats:
      mes_achats = prix[i]
    else:
      profit = max(profits, prix[i] - mes_achats)
    return profits
#maxprofit([7,1,5,3,6,4])
