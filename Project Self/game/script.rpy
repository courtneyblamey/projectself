# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lynda", color="#1bd033")
define m = Character("Me", color="#8be6ea")
image lynda placeholder = "lynda_placeholder.png"
image bg lobby = "bg_lobby.jpg"

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

    return
