﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#IMAGES#
image lynda placeholder = "lynda_placeholder.png"
image bg lobby = "bg_lobby.png"
image bg doorway = "bg_doorway.png"
image bg apartment = "bg_lyndaapt.png"
image bg pc_apartment = "bg_pcapart.png"
image bg laundry = "bg_laundry.png"
image lynda anger = "Lynda_Neutral.png"
image lynda furrow = "Lynda_Neutral.png"
image lynda neutral = "Lynda_Neutral.png"
image lynda surprise = "Lynda_Neutral.png"
image lynda unsure = "Lynda_Neutral.png"
image lynda content = "Lynda_Neutral.png"
image lynda joy = "Lynda_Neutral.png"

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

#Skill Variables
default TechSkill = 1
default TidySkill = 1

# The game starts here. And this is me testing that the push works.



## This is the start of the proper demo scene which (with some edits) will be in the game. It is the second event that takes place between the PC and Lynda.
label start:
    jump lyndainteraction1


        
        

