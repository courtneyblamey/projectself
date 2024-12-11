# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#CHARACTERS#
define l = Character("Lynda", color="#1bd033")
define m = Character("Me", color="#8be6ea")

#IMAGES#
image lynda placeholder = "lynda_placeholder.png"
image bg lobby = "bg_lobby.jpg"

#VARIABLES#

#Character Variables
default lynda_rating = 1

#Misc Variables
$ CarryBox = True
$ BoxIntense = False
$ LyndaDrink = False

#Skill Variables
$ TechSkill = 0

# The game starts here. And this is me testing that the push works.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lobby

    "It was another day in the building. The vent was still making that weird noise that stopped if you kicked it just hard enough."

    "Lynda appears from around the corner."

    show lynda placeholder at center

    # These display lines of dialogue.

    l "Oh hey! Don't mind me, I'm just a placeholder."

    m "Hey! Me too, I guess..."

    "You stare off into the distance, reconciling with your newfound self-awareness and fourth wall breaking."

    l "Can I help you?"

menu:
    
    "No I think I'm okay for now...":
        jump stop

    "Actually, yes, I wanted to ask you something!":
        jump question 

label stop:

    m "I think I'm good for now, but thanks."

    l "No problem, you know where to find me!"

    return

label question:

    m "Yes, can I ask you something?"

    l "Sure, what's up?"

menu:

    "What do you know about Jasper?":
        jump jasperwho
    "What do you know about Antony?":
        jump antonywho
    "What do you know about Sasha?":
        jump sashawho

label jasperwho:

    l "Oh not much, they seem like a sweet kid if a little scattered at times. 
    They bring down their laundry at all hours and it's somehow always a small mountain."
    jump afterwho 

label antonywho:

    l "Antony is a busy man - barista and bartender. I don't know how he does it honestly."
    jump afterwho

label sashawho:

    l "Sasha? She's lovely! And so funny. You should ask about her artwork sometime."
    jump afterwho

label afterwho:

    m "Good to know!"

    l "No problem. Anyway, my couch and cats are calling me, see you around the building."

    # This ends the game.

    jump lyndaevent2


## This is the start of the proper demo scene which (with some edits) will be in the game. It is the second event that takes place between the PC and Lynda.

label lyndaevent2:

"As you are headed back home you spot Lynda wrangling a pair of boxes through the building’s front door."

"You quicken your approach to meet her at the door and go to hold it open."

l "Oh thank you!"

"She fumbles with the boxes and shimmies through the doorway."

"Partway through, the door jams."

l "You're kidding me."

menu:

    "Give the door a shove.":
        jump doorshove

        label doorshove:

            $ lynda_rating += 1
            "With some gumption, you give the door a swift boot. It pops back with force and slams against the doorway causing an echo down the corridor. BUT it is open. You see a shoe print on the (luckily) glazed glass."
            jump postdoor

    "Kick the door.":
        jump doorkick

        label doorkick:

            "You give the door a hefty shove and it scrapes against the ground in protest before finally giving - swinging back on its hinges."

            l "Nicely done!"

            "She readjusts the boxes in he arms and carries on through the doorway."
            jump postdoor

    "Yell at the door.":
        jump dooryell

        label dooryell:

            $ lynda_rating -= 1
            m "CMON DOOR."
            "..."
            "The door remains stuck."
            "Lynda leans into it and it scoots past its sticking point, finally swinging freely on its hinges once more."
            l "I like the enthusiasm?"
            "She nearly drops the boxes she’s holding, but manages to adjust her grip and carries on through the doorway."
            jump postdoor

        label postdoor:
            m "[lynda_rating]"
            l "That door keeps getting stuck... I hope it doesn't properly jam one of thse days."


        
        

