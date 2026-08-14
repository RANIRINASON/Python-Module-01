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


if __name__ == "__main__":
    plant1 = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end="")
    plant1.show()
    print("\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-1)
    plant1.set_age(-1)
    print("\n")
    print("Current state: ", end="")
    plant1.show()
