# import controller
#
# if __name__ == '__main__':
#     controller.start()
#

class Human:
    def __init__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work

    def greetings(self):
        print(f'{self.name} говорит "Привет"')

    def good_bye(self, name: str):
        print(f'{self.name} прощается с {name}')

    def __str__(self):
        return f'Это человек с именем {self.name}, возраста {self.age}'


stone = Human('Кирилл', 38, True)
rudolf = Human('Рудольф', 18, True )

print(stone.name)
stone.greetings()
rudolf.greetings()
stone.good_bye('Рудольфом')
rudolf.good_bye('Кириллом')
print(stone)
print(rudolf)