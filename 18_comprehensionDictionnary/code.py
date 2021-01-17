users=[
    (0,"nimet","bloblo"),
    (1,"ebru","blibli"),
    (2,"berk","bleble"),
    (3,"ali","blublu"),
]
username_mapping = {user[1]: user for user in users}
#va attribuer le 2eme element du tableau comme clé , 
# on peut ensuite acceder a un dictionnaire precis via cette clé
print( username_mapping)
print(username_mapping["berk"])


username_input = input("entrez votre username :")
password_input =input("entrez votre password :")

_,username, password = username_mapping[username_input]
#assigne des variable au element du dictionaire avec la cle passé par l'input

if password_input == password:
    print('password correct')
else:
    print("password incorrect")
