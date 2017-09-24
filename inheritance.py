class Animal():
    '''동물'''
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

class Human(Animal):
    '''인간'''
    def wave(self):
        print('손을 흔든다')


class Dog(Animal):
    '''개'''
    def wave(self):
        print('꼬리를 흔든다')


person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wave()
