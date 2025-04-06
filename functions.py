# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


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


# Hero's Attack Function
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
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
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
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))
    
def hero_events_occur(events_Pass,health_points,combat_strength):
    chance = random.randrange(0,51)
    chance_two = random.randrange(0,2)
    for event in events_Pass:
        if event == "Advice":
            print("You remember an old man giving you some advice: \"Cripple the spleen and you will never go hungry\"")
            print("It'll probably help somehow, Combat strength + 1\n")
            combat_strength += 1
        elif event == "Fish":
            print("You remember trying to do some fishing")
            if chance == 0:
                print("Nothing's biting\n")
            elif chance <= 15:
                print(".....Sardines\n")
                health_points += 1
                print("You gained 1 health points for a total of " + str(health_points)+"\n")
            elif chance > 15 and chance < 50:
                print("Tilapia nice\n")
                health_points += 2
                print("You gained 2 health points for a total of " + str(health_points)+"\n")
            else:
                print("You caught a Salmon! You eat well.")
                health_points += 3
                print("You gained 3 health points for a total of " + str(health_points)+"\n")
        elif event == "Pocket":
            print("You rummage through your pockets and find a pen.....this is irrelevent for your situation\n")
        elif event == "Training":
            print("You do some exercise while you are waiting for a monster to show up, you feel a little stronger\n")
            combat_strength += 1
        elif event == "Food":
            food = random.randrange(1,7)
            print("You recall a kind stranger handing you a sandwich")
            print(f"It was pretty good you get {food} health points\n")
            health_points += food
        elif event == "Forget":
            print("You realized you forgot to bring a helmet before going into battle")
            print("Your overall health is lower\n")
            health_points -= 2
        elif event == "Frog":
            print("You have faint memories of tripping face first into a poison dart frog\n")
            if chance_two == 1:
                print("You lose some health but gain some strength\n")
                health_points -= 3
                combat_strength +=2
            else:
                print("You lose some strength but gain some health\n")
                health_points += 2
                combat_strength -= 3
        elif event == "Egg":
            print("You eat an egg.....rotten -1 everywhere")
            health_points -=1
            combat_strength -=1
    
    return health_points,combat_strength

# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

# Lab 06 - Question 5a
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

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
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


