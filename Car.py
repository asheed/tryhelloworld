class Car():
    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def run(self):
        print("{} {}이 달립니다.".format(self.capacity, self.name))

    def load(self):
        print("짐을 실었습니다.")

car = Car("카")
car.load()

truck = Truck("트럭", "10톤")
truck.run()