#le smethod magic sont cell qui coimmence et se termine par __
#donc __init__ , __str__, __repr__
# on a pas besoi de leur nom pour les appelé dans le code 

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        #str renvoi un string
        return f"cette personne s'appelle {self.name} et à {self.age} ans"
    
    def __repr__(self):
        #repr renvoie une representation de l'objet (pour le debug)
        return f"<Person('{self.name}',{self.age})>"

Oner = Person("Oner", 42)

print(Oner)
print(Oner.__repr__())