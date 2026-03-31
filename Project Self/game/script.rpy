# This file contains all the important setup to run the game.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#IMAGES#
image bg lobby = "lobby_environment.png"
image bg outside = "bg_doorway.png"
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
image maple = Transform("Maple.png", zoom=0.5)
image bean = Transform("Bean.png", zoom=0.5)
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
default lynda_convince = 0

#Misc Variables

#Lynda Interaction 1
default read_laundry = False
default read_disposal = False
default read_pipes = False
default read_noise = False
default BuildingPastGood = False

#Lynda Interaction 2
default CarryBox = False
default BoxIntense = False
default LyndaDrink = False

#Lynda Interaction 3
default DiligentLaundry = False
default ChaosLaundry = False
default BowlMoney = False
default CoatMoney = False

#Lynda Event 1
default SinkTimer = 0

#Lynda Event 2
default bean_location = None
default checked_bushes = False
default checked_bins = False
default checked_cars = False
default checked_lobby = False
default checked_laundry = False
default checked_mail = False
default checked_planters = False
default checked_stairwells = False
default checked_balcony = False
default checked_bedroom = False
default bean_escape = None

#Skill Variables
default TechSkill = 1
default TidySkill = 1
default HandsonSkill = 1
default StrengthSkill = 1
default ShareSkill = 1
default AttentionSkill = 1

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


        
        

