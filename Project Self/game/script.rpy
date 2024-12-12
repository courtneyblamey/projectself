# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#CHARACTERS#
define l = Character("Lynda", color="#1bd033")
define m = Character("Me", color="#8be6ea")

#IMAGES#
image lynda placeholder = "lynda_placeholder.png"
image bg lobby = "bg_lobby.jpg"
image bg doorway = "bg_doorway.jpg"
image lynda anger = "Lynda_Anger.png"
image lynda furrow = "Lynda_Furrow.png"
image lynda neutral = "Lynda_Neutral.png"
image lynda surprise = "Lynda_Surprise.png"
image lynda unsure = "Lynda_Unsure.png"
#VARIABLES#

#Character Variables
default lynda_rating = 1

#Misc Variables
$ CarryBox = True
$ BoxIntense = False
$ LyndaDrink = False

#Skill Variables
default TechSkill = 0

# The game starts here. And this is me testing that the push works.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lobby

    "It was another day in the building. The vent was still making that weird noise that stopped if you kicked it just hard enough."

    "Lynda appears from around the corner."

    show lynda neutral at center

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

    hide lynda placeholder

    jump lyndaevent2


## This is the start of the proper demo scene which (with some edits) will be in the game. It is the second event that takes place between the PC and Lynda.

label lyndaevent2:
    
    scene bg doorway
    with dissolve

    "As you are headed back home you spot Lynda wrangling a pair of boxes through the building's front door."

    "You quicken your approach to meet her at the door and go to hold it open."

    show lynda_placeholder

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
            "She nearly drops the boxes she's holding, but manages to adjust her grip and carries on through the doorway."
            jump postdoor

        label postdoor:
            m "[lynda_rating]"
            l "That door keeps getting stuck... I hope it doesn't properly jam one of thse days."
            "She shrugs and moves further into the lobby."
            m "What have you got there?"
            l "Oh, some things from work I need to try out."
            "She sighs placing the boxes down to stretch out her back."
            l "It's a new product they want us to get to know."
            "Lynda looks down at them with a grimace."

            menu:
                "Sounds fun?":
                    $ BoxIntense = False
                    l "Yeah." 
                    "She lets out a soft sound through her nose."
                    l "Super fun."
                    "Lynda looks at you deadpan."
                    l "I know nothing about tech, <playername>."
                    l "Well, that's not fair actually. I know how to run apps and find which HDMI my devices are hiding on, but this?"
                    "She indicates the boxes."
                    l "Nothing."
                    jump boxdetails
                "You want me to carry them up for you?":
                    $ BoxIntense = False
                    $ CarryBox = True
                    $ lynda_rating += 1
                    "Lynda's eyes widen."
                    l "Are you sure? These things are heavy! Which is ironic."
                    m "Yeah, I got this!"
                    "You lift up the boxes from the ground. They're certainly heavy, but you know you can make it to Lynda's apartment thanks to the elevator."
                    "As you walk towards the elevator Lynda peels off a loose label on the top of the box with a sigh."
                    jump boxdetails
                "WHAT'S IN THE BOX.":
                    $ BoxIntense = True
                    jump boxdetails

            label boxdetails:
                if BoxIntense:
                    $ lynda_rating -= 1
                    m "WHAT'S IN THE BOOOOOX"
                    "Lynda blinks at you."
                    l "Great film."
                    l "Specifically? Uh, some kind of holographic thing? There's some kind of app with it… They're pitching it for kid's bedtime stories."
                else:
                    l "They want us to test and play with some kind of holographic thing. It has an app integration too. Apparently they think it will be the next big thing in 'Kids Bedtime Tech Peripherals'"
                    "You both continue along to the elevator."
                    "There's a palpable silence before Lynda turns to you."
                    l "Are you good at tech-y things?"
                    "You see a glimmer of anxiety in her eyes."

            menu:
                "I'm not, but we can suffer together?":
                    $ TechSkill += 1
                    m "I'm not amazing with it but we can suffer together in it?"
                    "Lynda's eyes light up."
                    l "Really?"
                    l "I really appreciate it <playername>! I'm feeling a little out of my depth here."
                "I'm pretty good with tech-y things!":
                    $ TechSkill =+ 2
                    m "Actually, I do know a decent amount about tech."
                    "Lynda's shoulders seem to relax as she smiles at you."
                    l "Would you help me out in setting this thing up?"
                    m "Of course! Lead the way!"
                "I will break whatever you hand me.":
                    m "Candidly, I will break whatever this is in record time."
                    "Lynda's shoulders slump in defeat."
                    l 'Damn it. Okay.'
                    "Lynda looks at the boxes once more."
                    l "Guess it's you, me, tutorial videos, and a tall glass of wine."
                    jump lyndaboxfinal

            if CarryBox and TechSkill == 0:
                "You carry the boxes up to Lynda's apartment and wish her a good evening with her tech adventure and head home for the night."
                jump lyndaboxend
            elif CarryBox and TechSkill != 0:
                "You chat with Lynda on the way to her apartment, carrying the boxes along the way."
            else:
                jump lyndaboxapartment
        label lyndaboxapartment:
            $ lynda_rating += 1
            "You reach her door, decorated with a minimalistic doormat stating REAL FRIENDS BRING WINE, and a fall wreath of brightly coloured leaves and pinecones."
            "Lynda notices you scanning the doorway and nods to the wreath."
            l "Sasha made me this!"
            "And points to the doormat."
            l "*That* was a dumb online purchase, but I stand by it."
            "She unlocks the door and flicks on the lights to the apartment."
            if CarryBox:
                l "You can place the boxes right here on the counter."
                "You prop them up and onto the counter, trying very carefully to not drop them, noticing the VERY LARGE 'FRAGILE THIS WAY UP' label on the side."
            else:
                "Lynda grunts as she places the boxes on top of the countertop."
                l "Alright, can I get you something to drink before we get into this?"
        menu:
            "No, I'm good for now.":
                $ LyndaDrink = False
                m "No, I think I'm okay for now, but thanks."
                jump lyndaopenbox
            "Yeah, some water would be great!":
                m "Just some water for now, thanks."
                "Lynda smiles from behind a heavily painted white cabinet door."
                l "On it!"
                jump lyndaopenbox
            "I'd love some tea.":
                $ LyndaDrink = True
                m "I'd love some tea. actually."
                l "Sure thing! Let me get it brewed for you and we'll get into it."
                jump lyndaopenbox
            "Some wine, perchance?":
                $ lynda_rating += 1
                $ LyndaDrink = True
                m "I know great friends bring wine, but maybe you have some already to share?"
                "Lynda peers from behind a heavily painted white cabinet door, wine glasses in hand."
                l "Already on it!"
                jump lyndaopenbox
        
        label lyndaopenbox:
            if LyndaDrink:
                "Lynda sets down the drinks and begins to open the box."
            else:
                "Lynda sets down her drink and begins to open the box."

            "You look into the boxes to see a short tangle of wires, an odd looking box with angled windows, and various cubes reading: Alice in Wonderland, The Gruffalo, Ferdinand the Bull, and more."
            "Lynda pulls out and sets everything down on the countertop, throwing the boxes into the front room."
            "Within moments, two cats appear and hop into each of them respectively. One a mottled grey, orange, and white, and the other a slim black cat."
            l "They're cardboard box fiends. Give it a second and you'll see Bean just start chomping it."
            "Sure enough, the black cat begins to move along the box, biting it. Leaving a trail of bite marks as it goes."
            l "We found him behind a restaurant with a bunch of empty bean tins and boxes. You can take cat out of the street but-"
            "Bean continues his holepunching tirade against the box's edges."
            l "…anyway. Where to start with this thing."
            "She looks with dismay at the tech in front of her."

            if TechSkill == 1:
                "You also look down at the tech in front of you."
                m "Is there an instruction booklet?"
                "Lynda fishes around in the box and produces a paper booklet with a flourish."
                l "Yes, there is!"
                "You both read over the instructions, which are relatively well-written, if a bit over-written."
                l "Wow, these are kinda idiot-proof."
                l "Maybe I could have done this myself. Now I feel bad for asking for help."
                
                menu:
                    "You want me to leave you to get on with it?":
                        jump lyndaleaveearly
                    "I can stay, I don't mind.":
                        jump lyndastayearly
                
                label lyndaleaveearly:
                    $ lynda_rating += 1
                    "Lynda flicks through the instructions with neon painted nails."
                    l "Yeah, actually, I think I got this!"
                    l "Thanks anyway. I'll let you know how it goes."
                    if LyndaDrink:
                        "You finish up your drink as Lynda gets to work and head back home for the evening. You sense she's feeling a little more confident in herself as she sets up the tech on your way out."
                        l "See ya, <playername>!"
                        jump lyndaboxend
                    else:
                        "You wish Lynda luck in deciphering the device and head home for the evening. You sense a new level of confidence in her as she begins to set up the pieces of tech."
                        "See ya, <playername>!"
                        jump lyndaboxend
                
                label lyndastayearly:
                    "Lynda flicks through the instructions with neon painted nails."
                    l "You know, I wouldn't hate the help…"
                    m "Sure! Let's figure it out."
                    "You each begin to take turns following the instructions, setting up the base, power source, and fetching the different story cubes."
                    l "It's so comforting to know I'm not the only one moderately afraid of technology like this."
                    m "I mean, this is pretty high-tech. I think you're allowed to be a little intimidated by it."
                    l "I do feel a bit out of my depth. I moved to this job from the beauty industry, and it's just…"
                    "Lynda slots a piece of the device in place."
                    l "It's very different sometimes."
                    l "I guess I didn't think I'd feel like this still at this point in my career."
                    "She chuckles softly to herself and flicks on the device."
                    m "Feel like what?"
                    l "I don't really know how to describe it other than out of my depth."
                    "The images of Alice in Wonderland begin to faintly appear on the holographic part of the device."
                    l "Oh look at that!"
                    "Over the next couple minutes, the images get brighter and words begin to appear, telling the story of a girl growing too fast after eating a cake."
                    m "Not going to lie, that is pretty cool."
                    "Lynda stares at the holograph with a slightly furrowed brow."
                    l "This could be used for more than just storytime, right?"
                    m "Probably? The concept can do lots of things."
                    "Lynda grabs a notebook off of her desk and begins to scribble down notes."
                    "She looks up at you after a moment with a soft smile."
                    l "<player name> you have no idea how much this has helped me out."

                    menu:
                        "I think you know more than you realise.":
                            jump lyndalearn
                        "I'm happy to help!":
                            jump playertech
                        "I really enjoyed playing with this thing. It's cool.":
                            jump playertech
                
                label lyndalearn:
                    $ lynda_rating += 1
                    m "You know, I think you actually know more than you're giving yourself credit, Lynda."
                    "Lynda's face drops for a moment."
                    l "You think so? Huh."
                    m "Considering we both went into this a little unsure- we made it, and it works!"
                    "She looks over the device, now clearly playing colourful sequences from Alice in Wonderland."
                    l "I feel like the team is just so adept and knowledgeable about these things compared to me."
                    "She looks at you with a smile and a wink."
                    l "Maybe that's just me getting older."
                    l "Anyway, I've kept you long enough. I'm sure you'd like some of your evening to yourself!"
                    "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                    jump lyndaboxend
            
            if TechSkill == 2:
                "You pick up the cables and untangle them, plugging in the power source, and opening the instructions."
                m "Okay so, this is the base. You just have to make sure it is plugged into the outlet. And then…"
                "You reach for one of the cubes."
                m "This goes into the base."
                l "Okay, this makes sense."
                "You then pick up the box of angled windows and place it overtop, slowly piecing together the device, as Lynda watches on chewing her rosy pink stained lip."
                "You talk her through each phase, ensuring she's following along and answering her questions. She slowly becomes more and more inquisitive as you get ready to boot up the device."
                l "Okay and so this then refracts? the projection to make it look 3D?"
                m "Exactly, yeah! And each of these cubes holds the data of the images and words that will play."
                m "Wanna boot it up?"
                l "YES!"
                "You flick on the device and it whirs to life."
                "After a couple minutes, you begin to faintly see the outlines of a girl growing too big for a doorway. Alice in Wonderland is playing on the holographic projector."
                m "Weird, there's no sound…"
                l "Oh! They told us they're working on the audio component right now. But the words appear on the screen- well holograph, too."
                "You both continue to watch as the projector warms up and the colours become more vibrant and words clearly display alongside the pictures."
                l "So, this could actually be used for more than just storytime, right?"
                m "Probably? The concept can do lots of things."
                "Lynda grabs a notebook off of her desk and begins to scribble down notes."
                "She looks up at you after a moment with a soft smile."
                l "<player name> you have no idea how much this has helped me out."

                menu:
                    "I think you know more than you realise.":
                        jump lyndapride
                    "I'm happy to help!":
                        jump playertech
                    "I really enjoyed playing with this thing. It's cool.":
                        jump playertech
                
                label lyndapride:
                    $ lynda_rating += 1
                    m "You know, I think you actually know more than you're giving yourself credit, Lynda."
                    "Lynda's face drops for a moment."
                    l "You think so? Huh."
                    "She looks over the device, now clearly playing colourful sequences from Alice in Wonderland."
                    l "I feel like the team is just so adept and knowledgeable about these things compared to me."
                    "She looks at you with a smile and a wink."
                    l "Maybe that's just me getting older."
                    l "Anyway, I've kept you long enough. I'm sure you'd like some of your evening to yourself!"
                    "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                    jump lyndaboxend
            
            label playertech:
                m "No problem! I enjoyed it."
                l "Me too. It was less daunting than I expected in the end."
                "Treacle comes to investigate the quietly whirring device. Lynda switches it off and shoos her away from the ever-tempting-to-cat-brain cubes."
                l "I've kept you for enough of your evening, you should head home - but thank you, again."
                "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                jump lyndaboxend

label lyndaboxend:
    m "This is a sneaky peeky into the back-end, you're rating with Lynda is [lynda_rating]."
    "Thanks for playing this sequence!"
    return


        
        

