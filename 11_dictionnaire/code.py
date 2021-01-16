friend_ages = {"elise" : 35, "Caroline": 29, "Mahir":41}
#un dictionnnaire ce compose de cle et de valeur 

friends = [
    {"name":"elise", "age":37, "ville":"Nice"},
    {"name":"Mahir", "age":42, "ville":"Avignon"},
    {"name":"Volkan", "age":45, "ville":"Creteil"}
]

print(friends[0]["ville"])

for friend, age in friend_ages.items():
    print(f"{friend}: {age}")
# cle valeur stocker ds les variable friend et age pendnat la boucle

friends_values = friend_ages.values()
moyenne_dage = sum(friends_values) / len(friend_ages)
print(moyenne_dage)


