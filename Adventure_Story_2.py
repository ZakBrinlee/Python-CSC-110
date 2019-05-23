# North Seattle College, CSC 110
# Week 4 Programming Assignment
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# This program is the start of an adventure game using python
# Currently taking in 4 character attributes and a starting day of the story
# Using multiple variables in multiple places in the story

# Updated with 5 new story choices
# 2 nested but not sure where or what to next
# Parameter STORY_CHOICES is for being able to replay the whole story without user input because each
# response is being tracked. So kept in order the functions can be called to replay the story.

CHARACTER_NAME = ''
CHARACTER_PLANET = ''
CHARACTER_NICKNAME = ''
STARTING_DAY = ''
CHARACTER_CAREER = ''
PLANETS = ['Jupiter', 'Earth', 'Mercury', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Neptune']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
STORY_CHOICES = []


def main():
    # Program intro
    print("\nWelcome to the great Python story teller! Where you create story elements as you go!\nThroughout "
          "the story you will be prompted to decide the direction of the story!\n")
    # input section
    global CHARACTER_NAME
    global CHARACTER_PLANET
    global CHARACTER_NICKNAME
    global STARTING_DAY
    global CHARACTER_CAREER

    CHARACTER_NAME = input("Please enter your character's name: ")
    CHARACTER_PLANET = input("Which of the 8 planets in our solar system is your character from? ")
    validate_string_input(CHARACTER_PLANET, PLANETS)
    CHARACTER_NICKNAME = input("Please enter your character's nickname: ")
    STARTING_DAY = input("Please enter a day of the week: ")
    validate_string_input(STARTING_DAY, DAYS)
    CHARACTER_CAREER = input("Which career would you like for your character? (Engineer/Scientist) ")

    display_prologue(CHARACTER_NAME, CHARACTER_PLANET, CHARACTER_NICKNAME, STARTING_DAY, CHARACTER_CAREER)

    w_or_w = input("Time to choose!\nDo you want your story to be weird or wild? (weird/wild): ")
    STORY_CHOICES.append(validate_string_input(w_or_w, ['weird', 'wild']))
    weird_or_wild(STORY_CHOICES[0])

    f_or_d = input("\nTime to choose!\nDo you want your hero to end up in a forest world or desert world? ("
                   "forest/desert): ")
    STORY_CHOICES.append(validate_string_input(f_or_d, ['forest', 'desert']))
    forest_or_desert(STORY_CHOICES[1])

    r_or_i = input("\nTime to choose!\nDoes your hero run away from the crash or investigate? ("
                   "run/investigate): ")
    STORY_CHOICES.append(validate_string_input(r_or_i, ['run', 'investigate']))
    run_or_investigate(STORY_CHOICES[2])

    problem_difficulty = input("\nSelect one from the 3 difficulty settings (easy, medium, hard): ")
    STORY_CHOICES.append(validate_string_input(problem_difficulty, ["easy", "medium", "hard"]))

    STORY_CHOICES.append(math_problems(STORY_CHOICES[3]))

    STORY_CHOICES.append(check_answer(STORY_CHOICES[4], STORY_CHOICES[3]))

    end_story(STORY_CHOICES[5])


# This function displays the prologue of the story based on first set of input
# parameters: Same as the globals
def display_prologue(c_name, c_planet, c_nickname, starting_day, c_career):
    # output section
    print(" \nOur story starts on a " + starting_day + ", just like every other day.")
    print("Nothing out of the ordinary on the home planet of " + c_planet + ".")
    print("The unlikely hero of our story is the humble " + c_name + ".")
    print(c_name + " worked as a " + c_career + ".")
    print("A very skilled " + c_career + " that was liked by everyone, always friendly, polite and welcomed everywhere "
                                         "around " + c_planet + ".")
    print("Closest friends often called " + c_name + " by " + c_nickname + ".")
    print("An endearing nickname from childhood.\n")


# This function displays the first part of story
# parameters: determines if the next paragraph is sci-fi weird or action wild
def weird_or_wild(w_or_w):
    print()
    if w_or_w == 'weird':
        print(CHARACTER_NAME, "'s work could be summed up in one word: WEIRD.")
        print("Being an", CHARACTER_CAREER, "for a top secret research company often had it's share of weird days.")
        print("Today,", CHARACTER_NAME,
              "was asked to go consult on a new discovery unearthed in the Northern Hemisphere of", CHARACTER_PLANET)
        print("The discovery appeared to be a portal, there was only one way to find out what was through this "
              "portal: and our hero volunteered to go through first!")
    else:
        print(CHARACTER_NAME, "'s work could be summed up in one word: WILD.")
        print("Being an", CHARACTER_CAREER, "for a interstellar research vessel traveling the galaxy often had it's "
                                            "share of wild missions and encounters.")
        print(CHARACTER_NAME, "'s vessel was attacked by the Evil Emporer Zorg's Battleship! A rival of the friendly planet of",
              CHARACTER_PLANET)
        print(
            "The enemy vessel was able to capture and board the research vessel. Our Hero fought against the evil "
            "Zorgians and was forced to flee into an escape pod.")
        print("Barely making it into the pod as a laser beam shoots into the wall just inches past.", CHARACTER_NAME,
              "slams the launch button and grasps for an empty seat.")


# This function displays the next setting of the story
# parameters: forest or desert location
def forest_or_desert(f_or_d):
    print()
    if f_or_d == 'forest':
        print(CHARACTER_NAME, " awoke slowly, mind still in a haze.")
        print("Unable to remember how our hero arrived in this strange place, all", CHARACTER_NAME, "could gather was "
                                                                                                    "it was a vast "
                                                                                                    "and dark forest.")
        print("All the sudden there was a loud CRASH followed by the ground shaking!")
    else:
        print(CHARACTER_NAME, "awoke slowly, mind still in a haze.")
        print("Once our hero was able to shake the haze, the first thing", CHARACTER_NAME, "noticed was the endless "
                                                                                           "desert in every "
                                                                                           "direction.")
        print("All the sudden there was a loud CRASH followed by the ground shaking!")


# This function displays the user's choice for action
# parameters: run or investigate action
def run_or_investigate(r_or_i):
    if r_or_i == 'run':
        print("\nVery quickly,", CHARACTER_NICKNAME, "bolts in the opposite direction of the crash.")
        print(CHARACTER_NAME, "continued to run as something begun to chase.")
        print("Suddenly", CHARACTER_NAME, "came upon a door with a keypad.")
        print("The passcode appears to be a mathematical problem.")

    else:
        print("\n" + CHARACTER_NAME, "slowly walks towards the direction of the crash.")
        print("A short distance away, a unfamiliar type of spaceship is visible.")
        print("Closer inspection shows a door with a keypad")
        print("The passcode appears to be a mathematical problem.")


# This function validates any input against what the options are. If not valid then will prompt again
# parameters: Same as the globals
def validate_string_input(choice, options):
    valid_trigger = False
    user_choice = choice

    while not valid_trigger:
        if user_choice in options:
            return user_choice
        else:
            print("Your input is not accurate.")
            valid_trigger = False
            print("Options: ", *options, sep="\n")
            user_choice = input("Please input your selection from the list of options provided: ")


# This function provides different problems to solve based on user selection
# parameters: Same as the globals
def math_problems(difficulty):
    if difficulty.lower() == 'easy':
        answer = int(input("5 + 3x = 11\nSolve for x: "))
    elif difficulty.lower() == 'medium':
        answer = int(input("The value of x+x(x^x) when x = 2: "))
    else:
        answer = int(input("How many parsec's did Han Solo make the Kessel Run?: "))

    return answer


# This function tests the answers based on the difficulty chosen
# parameters: answer to the question, difficulty of question
def check_answer(answer, d_level):
    if d_level == 'easy':
        if answer == 2:
            happy_ending = True
        else:
            happy_ending = False
    elif d_level == 'medium':
        if answer == 10:
            happy_ending = True
        else:
            happy_ending = False
    else:
        if answer == 12:
            happy_ending = True
        else:
            happy_ending = False

    return happy_ending


# This function displays the ending of the story based on if the user provided the correct answer
# parameters: True, its a dream...False it gets dangerous
def end_story(happy_ending):
    print()
    if happy_ending:
        print("WHOOSH! The mysterious door opened and", CHARACTER_NAME, "wakes up in bed! It was all a dream!")
    else:
        print("BUZZZZ! The answer was not correct! Self-destruct sequence initiated 3..2..1")


main()
