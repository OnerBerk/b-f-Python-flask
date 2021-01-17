student ={"name":"oner", "notes":(18,20,12,15,17)}

def moyenne(sequence):
    return sum(sequence) / len(sequence)

print("la moyenne de", student["name"], "est de :",  moyenne(student["notes"]),"/20" )

#------------------------------------------#
# la meme chose en creant un objet (class) Student grace a la fonction __init__
# que l'ont va assigné a la variable self selon les convention python 

class Student:
    def __init__(self, name, notes):
        self.name = name
        self.notes =notes
    
    def noteMoyenne(self):
        return sum(self.notes) / len(self.notes)


student1 = Student("Oner", (19,20,18,19))
student2 = Student("Simon", (16,15,18,12))

print (f"{student1.name} à la note moyenne de : {student1.noteMoyenne()}/20 ")
print (f"{student2.name} à la note moyenne de : {student2.noteMoyenne()}/20 ")