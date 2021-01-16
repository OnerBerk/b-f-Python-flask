numbers=[1,3,5]
double=[x*2 for x in numbers]
print(double)

friends=["sam","sandra","sylvie","alfonso","Jacques"]
start_s=[friend for friend in friends if friend.startswith("s")]
print(start_s)

print(friends[0] is start_s[0])

print("friends :", id(friends), "startS :", id(start_s) )

#reviens a la meme chose
# for friend in friends:
#     if friend.startswith("s")
#     start_s.append(friend)