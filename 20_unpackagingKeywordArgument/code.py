#----------#
def named(**kwargs):
    print(kwargs)

named(name="oner", age=25)
# les double etoiles va creer un dictionnaire 


#----------#
def named1(name, age):
    print("D",name, age)

detail={"name":"oner", "age":42}

named1(**detail)
# les 2 etoiles va destructurer detail et va les attribuer selon les clé du dictionnaire 

#----------#

def printPropre(**kwargs):
    for arg, value in kwargs.items():
        print("E",f"{arg}:{value} ")

printPropre(name=" oner", age=" 42")

#----------#

def both(*args, **kwargs):
    # on va spliter automatiquement les argument en tupple et les cle valur en dictionnaire 
    print(args)
    print(kwargs)

both(1, 2, 3, 4, 5, id=0, name="berk", age=42)

