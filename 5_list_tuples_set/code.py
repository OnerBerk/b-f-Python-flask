listt=["Oner","Caroline","Gomni"]
#peut etre modifier
tupplee=("Oner","Caroline","Gomni")
#ne peut pas etre modifier  
sett={"bob","karl","math"}
#ne peut pas dupliquer les vatiable a l'interieyr et l'ordre de rendu n'es pas definis

print(listt[0])

listt[0]="Park huen"
print(listt)

listt.append("Saitama")
print(listt)

listt.remove('Gomni')
print(listt)

sett.add("lichtell")
#dans le set ce n'est pas append mais add pour ajouter un element 
print(sett)