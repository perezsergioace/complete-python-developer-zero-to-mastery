# OOP

# creating our own objects


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.age = age
            self.name = name  # attributes

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('sergio', 22)
print(player1.shout())
