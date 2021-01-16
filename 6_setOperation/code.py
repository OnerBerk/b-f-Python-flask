amis={"Elise", "Mahir", "Volkan"}
Abroad={"Elise","Mahir"}
other={"Yurri","Monica","Litchell"}

localfriend = amis.difference(Abroad)
print(localfriend)

friends=amis.union(other)
#union lie les 2 sets
print(friends)

art={'sai',"ali","matt","franck"}
techno={"sai","franck","yusuf","emma"}
both =art.intersection(techno)
#intersation compare et renvoie les entrer similaire  
print(both)