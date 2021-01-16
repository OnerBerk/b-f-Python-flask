t = 5,12
x,y = t
print(x,y)


friend=[("caro", 29, "serveuse"), ("volkan", 45, "assureur"), ("tarik",43,"informaticien")]

for name,age,profession in friend:
    print({name},{age},{profession})

for person in friend:
    print(f"name :{person[0]}, age :{person[1]}, profession : {person[2]} ")

#si une variable est defini avec _ c'est qu'elle est ignorer qelon le protocol de la communauté

tete, *queue =[1,2,3,4,5,6]
#cette syntaxe permet de separer les valeur * prend tout le rest et laisse la tete 
 
print(tete)
print(queue)