#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        self.height = self.height + 0.8
        self.height = round(self.height, 2)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {float(self.height)}cm, {self._age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    initial_height = plant1.height
    print("=== Garden Plant Growth ===")
    plant1.show()
    for day in range(1, 8):
        print(f"=== day {day} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    final_height = plant1.height
    print(f"Growth this week: {round((final_height-initial_height), 2)}cm")
