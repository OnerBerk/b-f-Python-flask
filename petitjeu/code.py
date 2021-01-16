number = 7

userInput=input("tape y si tu veux jouer :").lower()
#lower transforme tout en minuscule facilite les comparaison 

if userInput == "y":
    userNumber = int(input("choisi un chiffre entre 0 et 10 :"))
    if userNumber == number:
        print("bravoooooooo !!!!")
    elif abs(number - userNumber) == 1:
        print("presque 1 de difference ")
    else:
        print("reessaye")
else:
    print("tant pis !!!")

