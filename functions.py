# Import the random library to use for the dice later
import random
from random import choice

# Magic Shop
def magic_shop(belt, gold, combat_strength):
    # Define available items
    items = {
        "Fireball Scroll": {"cost": 5, "combat_strength": 3, "health_points": 0},
        "Healing Potion": {"cost": 3, "combat_strength": 0, "health_points": 5},
        "Shield Charm": {"cost": 4, "combat_strength": 0, "health_points": 0},
    }

    print("\n🌟 Welcome to Magic Shop! 🌟")
    print(f"You have {gold} gold coins\n")

    print("🛒 Items available:")
    for idx, (item_name, item_data) in enumerate(items.items(), start=1):
        print(f" {idx}. {item_name}: +{item_data['combat_strength']} Combat Strength, +{item_data['health_points']} Health Points (Cost: {item_data['cost']} gold)")

    while True:
        print("\nEnter the item you want to buy (or 'exit' to leave):")
        choice_input = input().strip().lower()

        if choice_input == 'exit':
            print("You leave the Magic Shop.")
            break

        if choice_input.isdigit() and 1 <= int(choice_input) <= len(items):
            item_choice = int(choice_input) - 1
            item_name = list(items.keys())[item_choice]
            item_data = items[item_name]

            if gold >= item_data["cost"]:
                gold -= item_data["cost"]
                belt.append(item_name)
                combat_strength += item_data["combat_strength"]
                print(f"\nYou bought a {item_name}!")
                print(f"Remaining gold: {gold}")
                print(f"New Combat Strength: {combat_strength}")
                print(f"Your belt: {belt}")
            else:
                print("You don’t have enough gold for that item.")
        else:
            print("Invalid choice. Please enter a valid item number or 'exit' to leave.")

    return belt, gold, combat_strength


# Use Loot
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")

    if belt:
        first_item = belt.pop(0)
    else:
        print("    |    Your belt is empty!")
        return belt, health_points

    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print(f"    |    You used {first_item} to increase your health to {health_points}")
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print(f"    |    You used {first_item} but it harmed you. Health: {health_points}")
    elif first_item == "Fireball Scroll":
        print("🔥 You unleash a powerful Fireball Scroll! +3 Combat Strength for this battle.")
    elif first_item == "Shield Charm":
        print("🛡️ Shield Charm activated! You will take half damage next hit.")
    else:
        print(f"    |    You used {first_item}, but it had no effect.")

    return belt, health_points


# Collect Loot
def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Hero's Attack
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                            
      (     @*&@  ,                          
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                 
               @       /                    
                %         @                  
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points


# Recursion
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Save Game
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")


# Load Game
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None


# Adjust Combat Strength
def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
    return combat_strength, m_combat_strength


# Monster Drops
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]

def monster_drops(belt):
    drop = random.choice(loot_options)
    belt.append(drop)
    print(f"    |    The monster drops: {drop}")
    return belt
