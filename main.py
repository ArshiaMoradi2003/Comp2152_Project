# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions


# Define Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Monster Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Get combat strengths from user input
i = 0
input_invalid = True

while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    combat_strength = input("    Enter your combat Strength (1-6): ")
    m_combat_strength = input("    Enter the monster's combat Strength (1-6): ")

    if not (combat_strength.isnumeric() and m_combat_strength.isnumeric()):
        print("    |    Invalid input. Please enter integer numbers for Combat Strength.")
        i += 1
        continue

    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    if combat_strength not in range(1, 7) or m_combat_strength not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only.")
        i += 1
        continue

    input_invalid = False

if not input_invalid:
    input("    Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, combat_strength + weapon_roll)
    print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    input("    Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("    |    --- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("    |    --- Your weapon is meh")
    else:
        print("    |    --- Nice weapon, friend!")

    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    input("    Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print(f"    |    Player rolled {health_points} health points")

    input("    Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print(f"    |    Player rolled {m_health_points} health points for the monster")

    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    input("    Roll for first item (enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)

    input("    Roll for second item (enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)

    belt.sort()
    print("    |    Your belt: ", belt)
    belt, health_points = functions.use_loot(belt, health_points)

    input("    Analyze the roll (Press enter)")
    print(f"    |    --- You are matched in strength: {combat_strength == m_combat_strength}")
    print(f"    |    --- You have a strong player: {(combat_strength + health_points) >= 15}")

    input("    Roll for Monster's Magic Power (Press enter)")
    power_roll = random.choice(list(monster_powers.keys()))
    m_combat_strength = min(6, m_combat_strength + monster_powers[power_roll])
    print(f"    |    The monster's combat strength is now {m_combat_strength} using the {power_roll} magic power")

    # Dream Level Logic
    num_dream_lvls = -1
    while num_dream_lvls < 0 or num_dream_lvls > 3:
        num_dream_lvls = input("    |    How many dream levels do you want to go down? (Enter a number 0-3): ")
        if not num_dream_lvls.isdigit():
            print("    |    Invalid input. Try again.")
            num_dream_lvls = -1
            continue
        num_dream_lvls = int(num_dream_lvls)
        if 0 < num_dream_lvls <= 3:
            health_points -= 1
            crazy_level = functions.inception_dream(num_dream_lvls)
            combat_strength += crazy_level
            print("    |    After the dream, your stats:")
            print(f"    |    Combat strength: {combat_strength}")
            print(f"    |    Health points: {health_points}")

    # Fight Sequence
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    num_stars = 0
    while m_health_points > 0 and health_points > 0:
        input("    |    Roll to see who strikes first (Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 == 1:  # Hero attacks first
            input("    |    You strike! (Enter)")
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                num_stars = 3
                print("    |    Monster is defeated! You find some drops:")
                belt = functions.monster_drops(belt)
                break

            input("    |    The monster strikes! (Enter)")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                num_stars = 1
                break
            else:
                num_stars = 2

        else:  # Monster attacks first
            input("    |    The Monster strikes! (Enter)")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                num_stars = 1
                break

            input("    |    The hero strikes!! (Enter)")
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                num_stars = 3
                print("    |    Monster is defeated! You find some drops:")
                belt = functions.monster_drops(belt)
                break
            else:
                num_stars = 2

    winner = "Hero" if m_health_points <= 0 else "Monster"

    # Get Hero Name
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        hero_name = input("    |    Enter your Hero's name (in two words): ")
        name = hero_name.split()
        if len(name) != 2 or not (name[0].isalpha() and name[1].isalpha()):
            print("    |    Please enter a valid name with two alphabetic parts.")
            tries += 1
        else:
            short_name = name[0][:2] + name[1][:1]
            print("    |    I'm going to call you " + short_name + " for short")
            input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print(f"    |    Hero {short_name} gets <{stars_display}> stars")
        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)

