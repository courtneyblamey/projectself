label lyndainteraction3:
     
    scene bg pc_apartment
    with dissolve

    "After scrolling social media for the morning, you roll over to spot your mountain of clothes bursting out of your laundry basket."

    m "I should probably deal with that."

    "You get up and make a coffee to sip."

    menu:
        "Sort the laundry.":
            jump sortlaundry
        
            label sortlaundry:
                $ DiligentLaundry = True
                $ TidySkill += 1

                "You dutifully separate out your laundry into piles."

                m "No bleeding colours or shrinking sweaters on my watch!"

                "You pile some of it into the basket and drop it by the front door."

                jump changesearch

        "INTO THE BASKET YOU GO.":
            jump basketchaos

            label basketchaos:
                $ ChaosLaundry = True
                $ TidySkill -= 1

                "You wrap your arms around the laundry mountain, and like a claw machine, decant it into your laundry basket."

                m "Y e e t."
                jump changesearch

label changesearch:

    "You search around the apartment for some change."

    m "I know I saw a pile of quarters somewhere around here..."
    #this code uses a list to remove choices once you've selected them!
    $ menu1 = []
    menu laundry_money:
        set menu1
        "Check the bowl by the door.":
                "You shuffle around some mail and loyalty cards to find a smattering of coins."
                $ Money =+5
                jump laundry_money
        "Check your coat pockets.":
                "You fish around in some coat pockets and find a stash of coins."
                $ Money =+2
                jump laundry_money

"You grab the basket and head downstairs to the laundry room."

scene bg_laundry
with dissolve

"As you reach the door, you notice someone filling the dryer."

l "Oh hey, <playername>, sorry I'm just finishing this load and then I'm outta here."

"Lynda subtly dabs her eye with a sock and throws it into the drum. She slots her change in as you dump your laundry into the machine."

if ChaosLaundry:
    l "Wow, you just throw it all together."

    "You shrug."

    m "I think separating laundry is a conspiracy made up by detergent companies to make us run more loads."
    "You watch Lynda think for a moment."

    l "Huh."

    jump lyndaokay
else:
    $ lynda_rating =+1
    l "Ah, you're a fellow laundry sorter are you?"

    m "I want my stuff to stay soft!"

    l "Not judging! Admiring, really."
    jump lyndaokay

label lyndaokay:
    "You notice Lynda's eyes are tinged pink."

    m "Hey, are you okay?"

    l "What? Me?"

    "She takes a deep breath."

    l "I was hoping to have my silly feelings contained by this age."

    "Lynda looks at you and tears brim in her eyes."

    l "Long distance is just really tough sometimes."

    l "Don't get me wrong, it was worth it, the money is relatively good, and she'll probably move out here once I know how good a fit this role is, but…"

    "She trails off, picking at a loose corner of a 'INSERT COINS HERE' sticker on the machine."

    m "You miss her."

    l "Yeah. And sometimes, I'm not sure I should even be trying to make this job work, I had a good one back home, but this one seemed so good for developing my skillset and-"

    if TechSkill == 1:
        l  "Anyway, I am going to go back upstairs while this dries and have a nice glass of wine."

        jump invitelynda
    else:
        l "Sorry, I've already blabbed to you about all this before."

        menu:
            "You can blab more, it's okay.":
                $ lynda_rating =+2

                m "You can blab more, I don't mind."

                l "You're sweet, but I won't subject you to all of-"

                "She gestures to her wet eyes."

                l "-this."

                m "Really, sometimes it's good to vent."

                "Lynda sighs again and wipes away some smudged eyeliner."

                l "I am one of the very lucky people on this planet who has found their person."

                l "And I *never* subscribed to that idea until I met her."

                l "Cliche, I know."

                l "She has wholeheartedly supported my ambitions, and I've supported hers, don't get me wrong. Just, this last endeavour has me wondering if I made the right choice."

                menu:
                    "Why's that?":
                        m "What has you wondering?"

                        if lynda_rating >= 4:

                            l "I just don't think I fit in at the office at all. Like we talked about the other day, I hear all these acronyms and everyone nodding in the room like it is something I should know, but I really don't."

                            m "Do you mean with the people or like, the work itself?"

                            "Lynda stares at the rumbling dryer."

                            l "That is a good question…"

                            "She looks lost in thought."

                            jump invitelynda
                        else: 
                            "Lynda picks at some loose skin on her lip, lost in thought."

                            jump invitelynda
                    "Maybe I've pried enough...":
                        "Maybe that's enough questions for this evening."

                        jump invitelynda

            "I get it, it's tough.":
                $ lynda_rating =+ 1

                m "I get it. It's tough."

                l "Yeah, yeah it is."

                "She wipes away a slight smear of eyeliner."

                jump invitelynda

label invitelynda:
    menu:
        "Offer a coffee hang.":
            $ lynda_rating =+1
            m "Do you wanna grab coffee sometime?"
            "Lynda smiles at you."

            l "You know what? That would be nice."

            l "And Antony owes me one anyway for saving his dried laundry from being thrown onto the floor."

            m "Okay! Then let's plan a time and we'll grab some."

            jump endlyndainteraction3

        "Offer a picnic in the park":
            $ lynda_rating =-1
            m "Are you a fan of picnics?"

            l "Uhhh…"

            l "Sure!"

            m "Okay! I make a mean spinach dip. We can find a time and go to the park nearby?"
            #small smile here

            l "That sounds lovely."

            jump endlyndainteraction3

        "Offer drinks at a local bar.":
            $ lynda_rating =+2
            m "Do you want to grab a casual drink sometime?"

            "Lynda's eyes light up."

            l "Oh, I'd love that."

            l "I haven't had a drink outside of my place in a hot minute."

            l "I've forgotten what it is like to be overcharged for an ounce of liquor."

            m "Then we shall correct this and refresh your memory so that you remember why you drink at home instead!"

            l "Perfect!"

            l "I'll let you know when works for me and vice versa, 'kay?"

            m "Sure!"

            jump endlyndainteraction3
label endlyndainteraction3:
    "Lynda wiggles her fingers goodbye to you as she heads out of the laundry room. You don't see her again when you go to move over your own laundry."

    if lynda_rating >= 5:
        "As you re-enter the laundry room you realise that the dryer is already running with your clothes in it. Lynda must have moved them over when she collected hers."

        if ChaosLaundry == True:
            "You decide to scroll on your phone for the last five minutes of the cycle and collect them, heading back upstairs for the night."
        else:
            "You load your next batch of clothes and head back upstairs. Eventually completing your laundry just in time for a reasonable bedtime."
            jump lyndainteraction4

    elif lynda_rating <5 and ChaosLaundry == True:
        "You throw the load into the dryer and return upstairs while it finishes the dry cycle. You grab it once it is done and watch some TV while folding it before heading off to bed."
        jump lyndainteraction4
    elif lynda_rating <5 and DiligentLaundry == True:
        "You move over the current load and prep the next one, which you do one more time for the delicates, before bringing the last load upstairs. You lay out your delicates to dry, realising you should have done them first, and fold the remaining laundry while watching TV. Eventually, you sort it all away and flomp into bed for the night."
        jump lyndainteraction4
    else:
        jump lyndainteraction4







