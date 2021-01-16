friend =["oner","sam","fredon"]
print("oner"in friend)
print("golum" in friend)


movieVu={"matrix","parasite","green book", "la soupe aux chou"}
tesFilm = input("quel film a tu vu :")
print(tesFilm in movieVu)

if tesFilm in movieVu:
    print( f"deja vu {tesFilm} !!")
else:
    print(f'cool jamais vu {tesFilm}')
