# This file contains all the important setup to run the game.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#IMAGES#
image bg lobby = "lobby_environment.png"
image bg lynda apartment = "lynda_apartment_environment.png"
image bg pc apartment = "pc_apartment_environment.png"
image bg laundry = "laundry_environment.png"
image bg bar = "bar_environment.png"
image bg cafe = "cafe_environment.png"
image bg park = "park_environment.png"
image lynda annoyed = "Lynda_Annoyed.png"
image lynda neutral = "Lynda_Neutral.png"
image lynda unsure = "Lynda_Unsure.png"
image lynda laugh = "Lynda_Laughing.png"
image lynda sad = "Lynda_Sad.png"
image lynda wink = "Lynda_Wink.png"
image maple = "Maple.png"
image bean = "Bean.png"
image anna annoyed = "Anna_Annoyed.png"
image anna concern = "Anna_Concerned.png"
image anna happy = "Anna_Happy.png"
image anna neutral = "Anna_Neutral.png"

init:
    transform bg_fit:
        fit "contain"
        xalign 0.5
        yalign 0.5
            
init:
    transform char_left:
        zoom 0.35
        xalign 0.25
        yalign 0.5

    transform char_center:
        zoom 0.35
        xalign 0.5
        yalign 0.5

    transform char_right:
        zoom 0.35
        xalign 0.75
        yalign 0.5

#VARIABLES#

#Character Variables
default lynda_rating = 1
default Money = 1

#Misc Variables
default CarryBox = False
default BoxIntense = False
default LyndaDrink = False
default BuildingPastGood = False
default DiligentLaundry = False
default ChaosLaundry = False
default BowlMoney = False
default CoatMoney = False
default read_laundry = False
default read_disposal = False
default read_pipes = False
default read_noise = False
default AttentionSkill = 0
default SinkTimer = 0

#Skill Variables
default TechSkill = 1
default TidySkill = 1
default HandsonSkill = 1
default StrengthSkill = 1
default ShareSkill = 1

default player_name = "Maria"

# The game starts here. And this is me testing that the push works.



## This is the start of the proper demo scene which (with some edits) will be in the game. It is the second event that takes place between the PC and Lynda.
label start:
    "Before we begin..."

    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Maria"

    "Nice to meet you, [player_name]."

    jump lyndainteraction1


        
        

