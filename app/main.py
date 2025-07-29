from typing import List, Union


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def _check_health(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Union[Herbivore, Animal]) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_health()
