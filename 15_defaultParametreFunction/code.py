def add(x, y=8):
    print(x+y)

add(5)
add(4, y=5)



defaultY=5
def add2(x, defaultY):
    print(x+y)

add(5)
defaultY=8
#en une variable avec une valeur dans la fonction on ne peut plus la modifier 
add(5)