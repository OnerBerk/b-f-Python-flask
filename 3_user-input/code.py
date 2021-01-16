name=input("enter your name : ")
gretting=f"Salut {name} "
print(gretting)

size_input=input("combien de pied de long fait votre maison :")
pied=int(size_input)
metre=pied/10.8
print(f"{pied} Pied font {metre:.2f} metre")
# :.2f permet de n'affher que 2 decimal 
