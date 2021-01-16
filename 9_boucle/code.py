number = 7

while True:
    userInput=input("veux tu jouer (Y/n) :")
    if userInput == "n":
        break
    
    userNumber = int(input("choisi un chiffre entre 0 et 10 :"))
    if userNumber == number:
        print("bravoooooooo !!!!")
        break
    elif abs(number - userNumber) == 1:
        print("presque 1 de difference ")
    else:
        print("reessaye")
if userInput == "n":
    print("tant pis !!!")

grades= [25,25,36,1444,12]
total=sum(grades)
quantitédenombre = len(grades)

moyenne= total/quantitédenombre
print(moyenne)