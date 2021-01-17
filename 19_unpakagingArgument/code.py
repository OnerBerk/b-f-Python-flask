def multiply(*args):
# recuperer tous les arguments passé et en fait un tupple
    total=1
    for arg in args:
        total=total * arg
    return total
print( multiply(2,3,5))


def add(x,y):
    return x+y

nums = [5,5]
print(add(*nums))
# * va destructurer la liste num,
#  ce qui permet d'attribuer chaques valeurs aux argument de add

num = [
    {"x":10, "y":20},
    {"x":24, "y":32}
    ]
print(add(**num[1]))
# parametre etant x et y ** va chercher les cles x et y dans le dictionnaire num



def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    # on met une etoile car la fonction de base a une etoile aussi en argument
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator provided"

print("A",apply(1,5,8,4,6, operator="+"))
print("B",apply(1,5,8,4,6, operator="*"))
print("C", apply(1,5,8,4,6, operator="-"))