#programme qui divise une liste de mots en 2 listes avec l'une comportant les mots de 
#plus de 6 carateres et l'autre les mots de moins de 6 caracteres
list_l=['jean', 'maximilien','sonia', 'jean-pierre', 'sandra']

longueur=len(list_l)
i=0
plus_6=[]
moins_6=[]

while (i<longueur):
 if (len(list_l[i])>5):
  plus_6.append(list_l[i])
 else:
  moins_6.append(list_l[i])
 i=i+1
print(plus_6)
print(moins_6)
