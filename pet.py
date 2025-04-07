# pet.py
class Pet:
    def __init__(self, name, ability, cooldown=3):
        self.name = name
        self.ability = ability
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use_ability(self, combat_strength, m_combat_strength, health_points):
        if self.current_cooldown > 0:
            print(f"    |    {self.name}'s ability is on cooldown ({self.current_cooldown} turn(s) left)")
            return combat_strength, m_combat_strength, health_points

        print(f"    |    {self.name} uses its {self.ability} ability!")

        if self.ability == "heal":
            health_points = min(20,health_points +  5)
            print(f"    |    {self.name} heals you. Health is now {health_points}")
        elif self.ability == "boost":
            combat_strength += 1
            print(f"    |    {self.name} boosts your strength. Combat Strength is now {combat_strength}")
        elif self.ability == "weaken":
            m_combat_strength = max(1, m_combat_strength - 1)
            print(f"    |    {self.name} weakens the monster. Monster strength is now {m_combat_strength}")

        self.current_cooldown = self.cooldown
        return combat_strength, m_combat_strength, health_points

    def tick(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
