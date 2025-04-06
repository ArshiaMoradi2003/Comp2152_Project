import random


class Shop:
    def __init__(self):
        self.items = self.generate_items()

    def generate_items(self):
        """Generates random items with random stats and prices."""
        items = [
            {"name": "Health Potion", "type": "health", "boost": random.randint(5, 20),
             "price": random.randint(10, 30)},
            {"name": "Strength Elixir", "type": "combat", "boost": random.randint(2, 10),
             "price": random.randint(15, 35)},
            {"name": "Magic Shield", "type": "health", "boost": random.randint(10, 30),
             "price": random.randint(20, 50)},
            {"name": "Sword of Valor", "type": "combat", "boost": random.randint(5, 15),
             "price": random.randint(25, 60)}
        ]
        return items

    def display_items(self):
        """Displays available items in the shop."""
        print("\n🏪 Magic Shop Items:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['name']} (+{item['boost']} {item['type']}) - {item['price']} gold")

    def purchase(self, hero, item_index):
        """Allows the hero to purchase an item if they have enough gold."""
        if item_index < 1 or item_index > len(self.items):
            print("❌ Invalid selection.")
            return

        item = self.items[item_index - 1]

        if hero.gold >= item['price']:
            hero.gold -= item['price']

            if item['type'] == 'health':
                hero.health_points += item['boost']
                print(f"✅ {item['name']} purchased! +{item['boost']} HP.")

            elif item['type'] == 'combat':
                hero.combat_strength += item['boost']
                print(f"✅ {item['name']} purchased! +{item['boost']} Combat Strength.")
        else:
            print("❌ Not enough gold!")
