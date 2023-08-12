from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Weapon:
    damage: int


@dataclass
class Defense:
    shield: int


@dataclass
class Spell:
    damage: int
    mana_cost: int


@dataclass
class GameCharacter:
    name: str
    hp: int
    level: int
    mana: int = 100
    defenses: list[Defense] = field(default_factory=list)

    @property
    def defense_shield(self) -> int:
        return sum([defense.shield for defense in self.defenses])

    @property
    def damage(self) -> int:
        return self.level * 10

    def attack(
        self,
        target: GameCharacter,
        weapon: Weapon | None = None,
        spell: Spell | None = None,
    ) -> None:
        damage = self.damage
        if weapon:
            damage += weapon.damage
        elif spell and spell.mana_cost <= self.mana:
            damage += spell.damage
            self.mana -= spell.mana_cost
        target.hp -= damage - target.defense_shield
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.hp <= 0:
            print(f"{target.name} has been defeated!")


def main() -> None:
    knight = GameCharacter("Sir Foo", 1000, 10, defenses=[Defense(100)])
    wizard = GameCharacter("Archibald", 1000, 5)
    sword = Weapon(100)
    fire_spell = Spell(100, 100)
    knight.attack(wizard, weapon=sword)
    wizard.attack(knight, spell=fire_spell)
    knight.attack(wizard, weapon=sword)
    wizard.attack(knight, spell=fire_spell)
    knight.attack(wizard, weapon=sword)
    wizard.attack(knight, spell=fire_spell)
    knight.attack(wizard, weapon=sword)
    wizard.attack(knight, spell=fire_spell)
    knight.attack(wizard, weapon=sword)


if __name__ == "__main__":
    main()
