class Plant:
    class Statistics:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_show_call(self):
            self._show_calls += 1

        def add_age_call(self):
            self._age_calls += 1

        def add_grow_call(self):
            self._grow_calls += 1

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._statistics = Plant.Statistics()

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = float(height)
            print(f"Height updated: {self._height} cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def show(self) -> None:
        print(f" {self.name}: {float(self._height)}cm, {self._age} days old")
        self._statistics.add_show_call()

    def grow(self) -> None:
        self._height = self._height + 0.8
        self._height = round(self._height, 2)
        self._statistics.add_grow_call()

    def age(self) -> None:
        self._age += 1
        self._statistics.add_age_call()

    @staticmethod
    def is_older_than_one(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.bloom_track = False
        self.color = color

    def bloom(self) -> None:
        self.bloom_track = True

    def show(self) -> None:
        super().show()
        print(f"  Color: {self.color}")
        if not self.bloom_track:
            print(f"  {self.name} has not bloomed yet")     
        else:
            print(f"  {self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0
        self.bloom_track = False

    def bloom(self):
        super().bloom()
        self.seed_count += 42


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.tree_track = 0
        self._shade_calls = 0

    def show(self) -> None:

        if self.tree_track == 0:
            super().show()
            print(f"  Trunk diameter: {float(self.trunk_diameter)}cm")
        else:
            print(f" Tree {self.name} now produces a shade of "
                  f"{float(self._height)}cm"
                  f" long and {float(self.trunk_diameter)}cm wide.")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        self.tree_track += 1


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 nutritional_value: int,
                 harvest_season: int) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = 0
        self.delay = 0

    def show(self) -> None:
        if not self.harvest_season:
            super().show()
            print(" Harvest season: April")
            print(f" Nutritional value: {self.nutritional_value}")
            self.harvest_season += 1
        else:
            print(f"[make {self.name.lower()} "
                  f"grow and age for {self.delay} days]")
            super().show()
            print(" Harvest season: April")
            print(f" Nutritional value :{self.nutritional_value}")

    def age(self) -> None:
        self.delay = self._age
        super().age()
        self.nutritional_value += 5
        self.delay = self._age - self.delay

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 15


def display(plant: Plant) -> None:
    if plant.__class__.__name__ == "Seed" and not seed1.bloom_track:
        print(f"  Seeds: {seed1.seed_count}")
        return
    if plant.__class__.__name__ == "Seed" and seed1.bloom_track:
        print(f"  Seeds: {seed1.seed_count}")
    print(f" [statistics for {plant.name.capitalize()}]")
    print(
            f" Stats: {plant._statistics._grow_calls} grow, "
            f"{plant._statistics._age_calls} age, "
            f"{plant._statistics._show_calls} show"
        )
    if (plant.__class__.__name__ == "Tree"):
        print(f"  {tree1._shade_calls} shade")


if __name__ == "__main__":

    flower1 = Flower("Rose", 15, 10, "red")
    seed1 = Seed("Sunflower", 80, 45, "yellow")
    tree1 = Tree("Oak", 200, 365, 5)
    anonymous1 = Plant.anonymous()
    print(' === Garden statistics ===')
    print(' === Check year-old')
    print(f' Is 30 days more than a year? -> {Plant.is_older_than_one(30)}')
    print(f' Is 400 days more than a year? -> {Plant.is_older_than_one(400)}')
    print("\n")
    print(" === Flower")
    flower1.show()
    display(flower1)
    print(f" [asking the {(flower1.name.lower())} to grow and bloom]")
    flower1.bloom()
    flower1.grow()
    flower1.show()
    display(flower1)
    print("\n")
    print(" === Tree")
    tree1.show()
    display(tree1)
    print(f" [asking the {tree1.name.lower()} to produce shade]")
    tree1.produce_shade()
    tree1.show()
    display(tree1)
    print("\n")
    print(" === Seed")
    seed1.show()
    display(seed1)
    print(f" [make {(seed1.name.lower())} to grow, age and bloom]")
    seed1.bloom()
    seed1.grow()
    seed1.age()
    seed1.show()
    display(seed1)
    print("\n")
    print(" === Anonymous")
    anonymous1.show()
    display(anonymous1)