# For
#Repetição de laços tipo for in ...
notas = [10,55,80,35,75]
 aprovados = 0
      reprovados = 0
  for nota in notas:
     if nota > 50:
       aprovados += 1
     else:
       reprovados += 1
print(aprovados)
print (reprovados)
print("FIM")
