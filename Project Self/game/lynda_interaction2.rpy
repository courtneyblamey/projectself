label lyndainteraction2:
    
    scene bg lobby at bg_fit
    with dissolve

    "As you are headed back home you spot Lynda wrangling a pair of boxes through the building's front door."

    "You quicken your approach to meet her at the door and go to hold it open."

    show lynda laugh at char_center

    l "Oh thank you!"

    "She fumbles with the boxes and shimmies through the doorway."

    "Partway through, the door jams."

    show lynda annoyed at char_center

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

            show lynda laugh at char_center

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
            show lynda annoyed at char_center
            l "That door keeps getting stuck... I hope it doesn't properly jam one of thse days."
            "She shrugs and moves further into the lobby."
            show lynda neutral at char_center
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
                    show lynda unsure at char_center
                    l "I know nothing about tech, [player_name]."
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
                    show lynda annoyed at char_center
                    "Lynda blinks at you."
                    show lynda neutral at char_center
                    l "Great film."
                    l "Specifically? Uh, some kind of holographic thing? There's some kind of app with it… They're pitching it for kid's bedtime stories."
                else:
                    show lynda neutral at char_center
                    l "They want us to test and play with some kind of holographic thing. It has an app integration too. Apparently they think it will be the next big thing in 'Kids Bedtime Tech Peripherals'"
                    "You both continue along to the elevator."
                    "There's a palpable silence before Lynda turns to you."
                    l "Are you good at tech-y things?"
                    "You see a glimmer of anxiety in her eyes."

            menu:
                "I'm not, but we can suffer together?":
                    $ TechSkill += 1
                    m "I'm not amazing with it but we can suffer together in it?"
                    show lynda neutral at char_center
                    "Lynda's eyes light up."
                    l "Really?"
                    l "I really appreciate it [player_name]! I'm feeling a little out of my depth here."
                "I'm pretty good with tech-y things!":
                    $ TechSkill =+ 2
                    m "Actually, I do know a decent amount about tech."
                    "Lynda's shoulders seem to relax as she smiles at you."
                    show lynda unsure at char_center
                    l "Would you help me out in setting this thing up?"
                    m "Of course! Lead the way!"
                "I will break whatever you hand me.":
                    m "Candidly, I will break whatever this is in record time."
                    "Lynda's shoulders slump in defeat."
                    l 'Damn it. Okay.'
                    "Lynda looks at the boxes once more."
                    show lynda unsure at char_center
                    l "Guess it's you, me, tutorial videos, and a tall glass of wine."
                    jump carryboxchoice

        label carryboxchoice:
            if CarryBox and TechSkill == 1:
                "You carry the boxes up to Lynda's apartment and wish her a good evening with her tech adventure and head home for the night."
                jump lyndalastbox
            elif CarryBox and TechSkill != 1:
                "You chat with Lynda on the way to her apartment, carrying the boxes along the way."
                jump lyndaboxapartment
            elif TechSkill == 1:
                "You say your farewells to Lynda and head to your own apartment for the night."
                jump lyndalastbox
            else:
                jump lyndaboxapartment
        label lyndaboxapartment:
            show lynda neutral at char_center
            $ lynda_rating += 1
            "You reach her door, decorated with a minimalistic doormat stating REAL FRIENDS BRING WINE, and a fall wreath of brightly coloured leaves and pinecones."
            "Lynda notices you scanning the doorway and nods to the wreath."
            l "Sasha made me this!"
            "And points to the doormat."
            show lynda wink at char_center
            l "*That* was a dumb online purchase, but I stand by it."
            show lynda neutral
            "She unlocks the door and flicks on the lights to the apartment."
            scene bg lynda apartment at bg_fit
            with dissolve
            if CarryBox:
                show lynda neutral at char_center
                l "You can place the boxes right here on the counter."
                "You prop them up and onto the counter, trying very carefully to not drop them, noticing the VERY LARGE 'FRAGILE THIS WAY UP' label on the side."
                l "Can I get you something to drink?"
            else:
                show lynda annoyed at char_center
                "Lynda grunts as she places the boxes on top of the countertop."
                show lynda neutral at char_center
                l "Alright, can I get you something to drink before we get into this?"
        menu:
            "No, I'm good for now.":
                $ LyndaDrink = False
                $ drinkchoice = "none"
                m "No, I think I'm okay for now, but thanks."
                jump lyndaopenbox
            "Yeah, some water would be great!":
                $ drinkchoice = "water"
                m "Just some water for now, thanks."
                show lynda laugh at char_center
                "Lynda smiles from behind a heavily painted white cabinet door."
                l "On it!"
                jump lyndaopenbox
            "I'd love some tea.":
                $ LyndaDrink = True
                $ drinkchoice = "tea"
                m "I'd love some tea. actually."
                show lynda laugh at char_center 
                l "Sure thing! Let me get it brewed for you and we'll get into it."
                jump lyndaopenbox
            "Some wine, perchance?":
                $ lynda_rating += 1
                $ LyndaDrink = True
                $ drinkchoice = "wine"
                m "I know great friends bring wine, but maybe you have some already to share?"
                show lynda wink at char_center
                "Lynda peers from behind a heavily painted white cabinet door, wine glasses in hand."
                l "Already on it!"
                jump lyndaopenbox
        
        label lyndaopenbox:
            if LyndaDrink:
                show lynda neutral at char_center
                "Lynda sets down the drinks and begins to open the box."
            else:
                show lynda neutral at char_center
                "Lynda sets down her drink and begins to open the box."

            "You look into the boxes to see a short tangle of wires, an odd looking box with angled windows, and various cubes reading: Alice in Wonderland, The Gruffalo, Ferdinand the Bull, and more."
            "Lynda pulls out and sets everything down on the countertop, throwing the boxes into the front room."
            "Within moments, two cats appear and hop into each of them respectively. One a mottled grey, orange, and white, and the other a large orange cat."
            show lynda unsure at char_center
            l "They're cardboard box fiends. Give it a second and you'll see Bean just start chomping it."
            show bean at left
            show maple at right
            "Sure enough, the orange cat begins to move along the box, biting it. Leaving a trail of bite marks as it goes."
            l "We found him behind a restaurant with a bunch of empty bean tins and boxes. You can take cat out of the street but-"
            "Bean continues his holepunching tirade against the box's edges."
            show lynda neutral at char_center
            l "…anyway. Where to start with this thing."
            "She looks with dismay at the tech in front of her."
            hide bean with dissolve
            hide maple with dissolve

            if TechSkill == 1:
                "You also look down at the tech in front of you."
                m "Is there an instruction booklet?"
                "Lynda fishes around in the box and produces a paper booklet with a flourish."
                show lynda neutral at char_center
                l "Yes, there is!"
                "You both read over the instructions, which are relatively well-written, if a bit over-written."
                show lynda unsure at char_center
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
                    show lynda unsure at char_center
                    l "Yeah, actually, I think I got this!"
                    l "Thanks anyway. I'll let you know how it goes."
                    show lynda neutral at char_center
                    if LyndaDrink:
                        "You finish up your drink as Lynda gets to work and head back home for the evening. You sense she's feeling a little more confident in herself as she sets up the tech on your way out."
                        l "See ya, [player_name]!"
                        hide lynda neutral
                        jump lyndalastbox
                    else:
                        "You wish Lynda luck in deciphering the device and head home for the evening. You sense a new level of confidence in her as she begins to set up the pieces of tech."
                        "See ya, [player_name]!"
                        hide lynda neutral
                        jump lyndalastbox
                
                label lyndastayearly:
                    "Lynda flicks through the instructions with neon painted nails."
                    show lynda unsure at char_center
                    l "You know, I wouldn't hate the help…"
                    m "Sure! Let's figure it out."
                    show lynda neutral at char_center
                    "You each begin to take turns following the instructions, setting up the base, power source, and fetching the different story cubes."
                    l "It's so comforting to know I'm not the only one moderately afraid of technology like this."
                    m "I mean, this is pretty high-tech. I think you're allowed to be a little intimidated by it."
                    l "I do feel a bit out of my depth. I moved to this job from the beauty industry, and it's just…"
                    "Lynda slots a piece of the device in place."
                    show lynda sad at char_center
                    l "It's very different sometimes."
                    l "I guess I didn't think I'd feel like this still at this point in my career."
                    "She chuckles softly to herself and flicks on the device."
                    m "Feel like what?"
                    show lynda unsure at char_center
                    l "I don't really know how to describe it other than out of my depth."
                    "The images of Alice in Wonderland begin to faintly appear on the holographic part of the device."
                    show lynda laugh at char_center
                    l "Oh look at that!"
                    "Over the next couple minutes, the images get brighter and words begin to appear, telling the story of a girl growing too fast after eating a cake."
                    m "Not going to lie, that is pretty cool."
                    "Lynda stares at the holograph with a slightly furrowed brow."
                    show lynda unsure at char_center
                    l "This could be used for more than just storytime, right?"
                    m "Probably? The concept can do lots of things."
                    "Lynda grabs a notebook off of her desk and begins to scribble down notes."
                    show lynda neutral at char_center
                    "She looks up at you after a moment with a soft smile."
                    l "[player_name] you have no idea how much this has helped me out."

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
                    show lynda sad at char_center
                    "Lynda's face drops for a moment."
                    l "You think so? Huh."
                    show lynda neutral at char_center
                    m "Considering we both went into this a little unsure- we made it, and it works!"
                    "She looks over the device, now clearly playing colourful sequences from Alice in Wonderland."
                    l "I feel like the team is just so adept and knowledgeable about these things compared to me."
                    show lynda wink at char_center
                    "She looks at you with a smile and a wink."
                    l "Maybe that's just me getting older."
                    show lynda neutral at char_center
                    l "Anyway, I've kept you long enough. I'm sure you'd like some of your evening to yourself!"
                    "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                    hide lynda neutral
                    jump lyndalastbox
            
            if TechSkill == 2:
                show lynda neutral at char_center
                "You pick up the cables and untangle them, plugging in the power source, and opening the instructions."
                m "Okay so, this is the base. You just have to make sure it is plugged into the outlet. And then…"
                "You reach for one of the cubes."
                m "This goes into the base."
                l "Okay, this makes sense."
                "You then pick up the box of angled windows and place it overtop, slowly piecing together the device, as Lynda watches on chewing her rosy pink stained lip."
                "You talk her through each phase, ensuring she's following along and answering her questions. She slowly becomes more and more inquisitive as you get ready to boot up the device."
                show lynda unsure at char_center
                l "Okay and so this then refracts? the projection to make it look 3D?"
                m "Exactly, yeah! And each of these cubes holds the data of the images and words that will play."
                m "Wanna boot it up?"
                show lynda laugh at char_center
                l "YES!"
                "You flick on the device and it whirs to life."
                "After a couple minutes, you begin to faintly see the outlines of a girl growing too big for a doorway. Alice in Wonderland is playing on the holographic projector."
                m "Weird, there's no sound…"
                show lynda unsure at char_center
                l "Oh! They told us they're working on the audio component right now. But the words appear on the screen- well holograph, too."
                "You both continue to watch as the projector warms up and the colours become more vibrant and words clearly display alongside the pictures."
                show lynda neutral at char_center
                l "So, this could actually be used for more than just storytime, right?"
                m "Probably? The concept can do lots of things."
                "Lynda grabs a notebook off of her desk and begins to scribble down notes."
                "She looks up at you after a moment with a soft smile."
                l "[player_name] you have no idea how much this has helped me out."

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
                    show lynda sad at char_center
                    "Lynda's face drops for a moment."
                    l "You think so? Huh."
                    show lynda neutral at char_center
                    "She looks over the device, now clearly playing colourful sequences from Alice in Wonderland."
                    l "I feel like the team is just so adept and knowledgeable about these things compared to me."
                    "She looks at you with a smile and a wink."
                    show lynda wink at char_center
                    l "Maybe that's just me getting older."
                    show lynda neutral at char_center
                    l "Anyway, I've kept you long enough. I'm sure you'd like some of your evening to yourself!"
                    "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                    hide lynda neutral
                    jump lyndalastbox
            
            label playertech:
                m "No problem! I enjoyed it."
                show lynda laugh at char_center
                l "Me too. It was less daunting than I expected in the end."
                "Maple comes to investigate the quietly whirring device. Lynda switches it off and shoos her away from the ever-tempting-to-cat-brain cubes."
                l "I've kept you for enough of your evening, you should head home - but thank you, again."
                "You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her."
                hide lynda laugh 
                jump lyndalastbox

label lyndalastbox:
    "You head off to your apartment for the night."
    jump lyndaevent1