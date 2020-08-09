from abc import ABCMeta, abstractmethod
from enum import Enum

class Type(Enum):
    食肉 = 1
    食草 = 2

class Shape(Enum):
    小 = 1
    中等 = 2
    大型 = 3

class Character(Enum):
    温顺 = 1
    凶猛 = 2

class Zoo(object):
    def __init__(self, name):
        self.animals = {}
        self.name = name

    def add_animal(self, instance):
        if type(instance).__name__ in self.__dict__:
            pass
        else:
            self.__dict__[type(instance).__name__] = True
        if instance.name in self.animals:
            print(f'{instance.name} 已经录入系统，请勿重复添加！')
        else:
            self.animals[instance.name] = instance

    def get_animal(self, animalname):
        if animalname in self.animals:
            return self.animals[animalname]
        else:
            print(f'{animalname} 尚未录入系统！')

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, shape, character):
        self.type = type
        self.shape = shape
        self.character = character
        if self.type == Type.食肉 and self.shape in (Shape.中等, Shape.大型) and self.character == Character.凶猛:
            self.isFerociousAnimal = True
        else:
            self.isFerociousAnimal = False


class Cat(Animal):
    voice = 'miao miao miao ~'

    def __init__(self, name, type, shape, character):
        super().__init__(type, shape, character)
        self.name = name
        self.isPet = True


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', Type.食肉, Shape.小, Character.温顺)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(f'----------------------查询是否存在猫这种动物----------------------')
    print(f'是否存在猫这种动物：{have_cat}')
    print(f'----------------------查询“大花猫1”这种动物----------------------')
    mcat = z.get_animal('大花猫 1')
    print(f'动物名字：{mcat.name}')
    print(f'动物动作：{mcat.voice}')
    print(f'是否宠物：{mcat.isPet}')
    print(f'是否属于凶猛动物：{mcat.isFerociousAnimal}')
    print(f'----------------------重复添加“大花猫1”----------------------')
    cat2 = Cat('大花猫 1', Type.食肉, Shape.小, Character.温顺)
    # 增加一只猫到动物园
    z.add_animal(cat2)
