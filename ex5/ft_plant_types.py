#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

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
        print(f"{self.name}: {float(self._height)}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = self._height + 0.8
        self._height = round(self._height, 2)

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.bloom_track = 0
        self.color = color

    def bloom(self) -> None:
        self.bloom_track += 1

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloom_track == 0:
            print(" Rose has not bloomed yet")
            print(f"[asking the {(self.name.lower())} to bloom]")
        else:
            print("Rose is blooming beautifully!")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.tree_track = 0

    def show(self) -> None:

        if self.tree_track == 0:
            super().show()
            print(f" Trunk diameter: {float(self.trunk_diameter)}cm")
            print(f"[asking the {self.name.lower()} to produce shade]")
        else:
            print(f"Tree {self.name} now produces a shade of "
                  f"{float(self._height)}cm"
                  f" long and {float(self.trunk_diameter)}cm wide.")

    def produce_shade(self) -> None:
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


if __name__ == "__main__":
    flower1 = Flower("Rose", 15, 10, "Red")
    tree1 = Tree("Oak", 200, 365, 5)
    vegetable1 = Vegetable("Tomato", 5, 10, 0, 20)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1.show()
    flower1.bloom()
    flower1.show()
    print("\n")

    print("=== Tree")
    tree1.show()
    tree1.produce_shade()
    tree1.show()
    print("\n")

    print("=== Vegetable")
    vegetable1.show()
    vegetable1.grow()
    vegetable1.age()
    vegetable1.show()
