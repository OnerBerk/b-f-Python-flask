add=lambda x,y:x+y
print(add(5,7))
#comme les fonctions lambda n'ont pas de nom on les lie a une variable

print((lambda x,y: x+y)(6,8))
#ou ont definis l'action et les les argument sur la meme ligne

def double(x):
    return x * 2

sequence =[1,3,5,7]
doubler = [double(x) for x in sequence]
#code classic


doubled= list(map(double, sequence))
# map permet d'utiliser une function au element d'un tableau ...boucle
doubled2 = list(map(lambda x: x *2, sequence))
# meme fonction en version lambda

print(doubler)
print(doubled)
print(doubled2)