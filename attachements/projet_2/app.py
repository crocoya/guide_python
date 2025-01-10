mot_de_passe = input("Quel est votre mot de passe ?")

if len(mot_de_passe) < 6:
    if len(mot_de_passe) == 0:
       print("Il faut écrire quelque chose")
    else:
      print("Le mot de passe est trop court")
elif mot_de_passe == '123456':
  print("Le mot de passe est bon")
  print("Mais il n'est pas très sécurisé")
else:
  print("Le mot de passe n'est pas bon")

print("Le programme est terminé")