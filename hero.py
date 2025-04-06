import random
from character import Character
from shop import Shop

class Hero(Character):
    def __init__(self):
        combat_strength = random.randint(5, 15)
        health_points = random.randint(20, 50)
        super().__init__(combat_strength, health_points)
        self.gold = random.randint(50, 150)  # Hero starts with random gold

    def hero_attacks(self):
        return random.randint(1, self.combat_strength)

    def visit_shop(self):
        """Allows the hero to visit and interact with the shop."""
        shop = Shop()
        shop.display_items()

        print(f"\n💰 Your Gold: {self.gold}")
        choice = input("Enter the item number to buy or 'q' to quit: ")

        if choice.lower() == 'q':
            print("🚪 Leaving the shop.")
            return

        if choice.isdigit():
            item_index = int(choice)
            shop.purchase(self, item_index)
        else:
            print("❌ Invalid input.")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()
