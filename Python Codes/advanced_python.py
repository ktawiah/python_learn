class Toy:
    age = 3

    def __init__(self, name) -> None:
        self.name = name

    @property
    def get_name(self):
        return self.name

    @classmethod
    def get_age(cls):
        return cls.age

    @staticmethod
    def get_kelvin_name():
        my_name = Toy.get_age()
        kel_age = 29
        print(my_name)
        return kel_age


if __name__ == "__main__":
    # print(Toy("Loader").get_name())
    toy = Toy("Cinderella")
    print(toy.get_name)
    print(Toy.get_age())
    print(Toy.get_kelvin_name())
