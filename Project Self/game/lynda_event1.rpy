label lyndaevent1:

scene bg pc apartment at bg_fit

"You're settled on your couch for the evening scrolling through a streaming service for SOMETHING good to watch."

menu:
    "While you totally scroll on your phone at the same time.":
        $ AttentionSkill += 1
        $ SinkTimer += 3

        "You select something mindless that fades into the background as you scroll through social media, also mindlessly."
        "Sometimes brain overload feels good."

        "{i}beep boop{/i}"

        "The electrical room below you beeps."

        m "That sound is going to get real annoying."

        jump scroll_sequence

    "Your attention can handle one screen.":
        $ AttentionSkill += 5
        $ SinkTimer += 1

        "You flick through some videos."

        m "I'm pretty sure I've hit the end of all the content that ever existed."

        jump focused_menu


# -------------------------
# SCROLL SEQUENCE - needs scroll choice in top sequence
# -------------------------
label scroll_sequence:

    "A cute video of a dog. Aww, he's chasing something in his sleep."

    menu:
        "Scroll":
            pass

    "How to make girl dinner actually nutritious."

    menu:
        "Scroll":
            pass

    "Why is everyone so obsessed with protein?"

    menu:
        "Scroll":
            pass

    "Did you know, that when you know, you know things?"

    menu:
        "Scroll":
            pass

    "Do I smell burnt toast?"

    menu:
        "Scroll":
            pass

    "You hearing thumping upstairs from Lynda's apartment."

    m "Oh, she must be home."

    menu:
        "Scroll":
            pass

    "Come with me to check out this cute new spot in the city."

    menu:
        "Scroll":
            pass

    "More thumping from upstairs."

    menu:
        "Scroll":
            pass

    "Silence."


    menu:
        "Continue scrolling":
            $ SinkTimer += 5

            "You continue to scroll your feed."

            "10 signs that your cat loves you! Has your cat ever slow blinked at you? That could mean-"

            "A crash from upstairs."

            jump scroll_followup

        "Pause scrolling and listen":
            $ SinkTimer += 4

            "You stop the video and listen."

            "{size=-10}Muffled shouts{/size}"

            "{size=-5}Less muffled shouts{/size}"

            "You head upstairs to investigate."

            jump goupstairs


label scroll_followup:

    menu:
        "Continue scrolling":
            $ SinkTimer += 6

            "You continue to scroll."

            "Whatever was on in the background ends and pulls up some recommendations."

            "You select the next thing to watch and notice some water drops on the coffee table."

            "You notice that something is dripping into the water drops."

            "Something is dripping a LOT into the water drops."

            "You look up to see that the water is coming from the ceiling."

            m "Oh shit"

            "You rush upstairs."

            jump goupstairspanic

        "Stop scrolling and investigate":
            jump goupstairs


# -------------------------
# FOCUSED PATH
# -------------------------

label focused_menu:

    menu:
        "Give up and just pick something at random":
            "You give up scrolling and select the 'surprise me' button."

            "The opening credits to a 90s romcom roll across the screen, and you settle in to watch something that probably hasn't aged well."

            jump upstairsnoise

        "Maybe a nature documentary?":
            "You pick a nature doc and settle in to the gentle voiceover of David Attenborough."

            jump upstairsnoise

        "Ooh, latest episode of a dating show":
            m "Ooh, I forgot there's a new episode of Attraction Isle."

            "You tune in to your guilty pleasure."

            jump upstairsnoise


label upstairsnoise:

    "You feel your eyes starting to drift shut when you hear some stomping upstairs."

    menu:
        "Shrug it off and make some tea":
            $ SinkTimer += 1

            "Lynda does love a one-woman dance party. You swear you can hear music. She might not have rhythm, but the woman loves to groove."

            "You get up to make an herbal tea. In filling the kettle you notice the flow of water is off."

            m "Huh, the water pressure's weird."

            "Eventually, the kettle fills and you set it to boil."

            "You collect a mug and select your tea when-"

            "{size=+10} C R A S H {/size}"

            "A loud noise from upstairs."

            m "Uh oh."

            jump goupstairspanic

        "Listen to check":
            "Lynda is typically quite light on her feet."

            "You pause your show to listen in."

            l "{size=-10}motherfuc-{/size}"

            "More crashing."

            jump goupstairs


# -------------------------
# UPSTAIRS
# -------------------------

label goupstairs:

    "As you round the corridor, you hear banging. Lynda's door is ajar, and a handful of swears echo down the hallway."

    jump enteraptsink


label goupstairspanic:

    "You skid around the corner to see Lynda's door open and run to it."

    scene bg lynda apartment at bg_fit

    show lynda sad at char_center

    l "Ohhhhh noooooo! Stop!!!"

    "Lynda sits in front of her sink, slinging towels under it to prevent the jettison of water from going any further."

    jump enteraptsink


# -------------------------
# SINK EVENT
# -------------------------

label enteraptsink:
    scene bg lynda apartment at bg_fit

    show lynda sad at char_center

    "You step into Lynda's apartment to see her sink tap spraying water in the air and a small flood emerging under the sink."

    menu:
        "PANIC AS WELL":
            $ HandsonSkill += 1
            $ lynda_rating -= 1

            m "UH OH."

            transform fly_left_to_right:
                zoom 0.7
                xpos -500
                yalign 0.5
                linear 0.9 xpos config.screen_width + 500

            transform fly_right_to_left:
                zoom 0.7
                xpos config.screen_width + 500
                yalign 0.5
                linear 0.9 xpos -500

            show maple at fly_left_to_right
            pause 0.2
            show bean at fly_right_to_left

            "Bean and Maple scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

            show lynda sad at char_center

            l "h e l p"

            m "What do I do?!"

            show lynda annoyed at char_center

            l "I don't know!!!"

            show lynda sad at char_center

            l "It won't stop!!!"

            "You move towards the sink, trying not to slip on the floor."

            "Both you and Lynda desperately try to block the flow of water."

            l "Oh my godddd."

            l "There has to be a way to turn this off!!!"

            "Lynda reaches in and fumbles at the back of the pipes."

            l "Ah HA!"

            show lynda laugh at char_center

            "You watch her twist something. With a *clunk*, the water flow ebbs from a jet to a trickle."

            show lynda neutral at char_center

            "You both wipe the water off your faces and adjust yourselves."

            m "Well, that sucked."

            jump investigatefaucet1

        "Grab more towels to help!":
            $ HandsonSkill += 3
            $ lynda_rating += 1

            transform fly_left_to_right:
                zoom 0.7
                xpos -500
                yalign 0.5
                linear 0.9 xpos config.screen_width + 500

            transform fly_right_to_left:
                zoom 0.7
                xpos config.screen_width + 500
                yalign 0.5
                linear 0.9 xpos -500

            show maple at fly_left_to_right
            pause 0.2
            show bean at fly_right_to_left

            "Bean and Maple scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

            show lynda sad at char_center

            l "h e l p"

            m "Where are some other towels?!"

            l "In the bathroom!"

            "You rush to grab more towels and sprint back to the kitchen."

            "Lynda grabs one of the towels out of your hand."

            show lynda annoyed at char_center

            l "WAIT NOT THIS ONE."

            "She clutches a red towel with a cat chasing leaves embroidered on it."

            show lynda unsure at char_center

            l "...its decorative."

            "She throws it away from the flood of water and pulls the other towels off of you to jam under the sink."

            "You create a barrier out of the remaining towels to prevent the water from spreading further."

            show lynda sad at char_center

            l "There has to be a way to turn this off!!!"

            "Lynda reaches in and fumbles at the back of the pipes."

            l "Ah HA!"

            show lynda laugh at char_center

            "You watch her twist something. With a *clunk*, the water flow ebbs from a jet to a trickle."

            show lynda neutral at char_center

            "You both wipe the water off your faces and adjust yourselves."

            jump investigatefaucet1

        "Dive under the sink.":
            $ HandsonSkill += 5
            $ lynda_rating += 1

            m "Move!"

            transform fly_left_to_right:
                zoom 0.7
                xpos -500
                yalign 0.5
                linear 0.9 xpos config.screen_width + 500

            transform fly_right_to_left:
                zoom 0.7
                xpos config.screen_width + 500
                yalign 0.5
                linear 0.9 xpos -500

            show maple at fly_left_to_right
            pause 0.2
            show bean at fly_right_to_left

            "Bean and Maple scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

            show lynda sad at char_center

            l "h e l p"

            if TechSkill == 2:

                "You dive under the sink, moving Lynda out of the way, and reach for the stop valve."

                "With a creak, the jet of water finally ebbs to a trickle."

            else:

                $ SinkTimer += 1
                $ lynda_rating -= 1

                "You dive under the sink."

                m "I got this! Just keep the water from getting everywhere!"

                "Water sprays you in the face."

                "You reach in to try and figure out what is causing the leak."

                "Water continues to spray you in the face."

                "You realise that maybe… you don't got this."

                "Lynda clocks you fumbling around."

                show lynda annoyed at char_center

                l "Oh hell, now *you* move."

                "Lynda pushes you out of the way and gets under the sink once more."

                "You hear a *thunk* and the water finally ceases flowing across the kitchen."

                "She emerges, equally as soaked as you."

                show lynda neutral at char_center

                l "I appreciate your enthusiasm to help."

                m "Sorry…"

            jump investigatefaucet1


# -------------------------
# INVESTIGATION
# -------------------------

label investigatefaucet1:

    if lynda_rating >= 1:

        show lynda neutral at char_center

        "The two of you take a moment to catch your breath and look at each other. Lynda's makeup is all over her face and your shirt is drenched."

        show lynda laugh at char_center

        l "Pfft."

        "Lynda begins to laugh."

        l "Ahahaha!"

        l "Oh, I'm so sorry, but we're a STATE."

    else:

        show lynda neutral at char_center

        "You both stand in silence with only the quiet dripping of the remaining water in the background."

    jump investigatefaucet2


label investigatefaucet2:

    m "What the hell caused the sink to explode like that?"

    show lynda annoyed at char_center

    l "I don't know, I was just washing my dishes when the water pressure dipped and then-"

    "She gestures at the flood around you both."

    "You check out the sink."

    "The taps turn no issue, and the pipes seem fine too..."
    
    menu:
        "Check the faucet":
            jump investigatefaucet3


label investigatefaucet3:
    show lynda neutral at char_center

    m "Well, there's your problem."

    "You turn holding the faucet."

    m "This thing's corroded to hell."

    show lynda annoyed at char_center

    l "Oh GOD. How long has it been like THAT?!"

    "She takes the faucet head from you and looks it over."

    l "This has to have been going on for ages."

    show lynda unsure at char_center

    l "Well… hell."

    l "Sasha had a similar problem next door, not quite as bad, and it took nearly two or three weeks before someone came to fix it."

    show lynda sad at char_center

    l "I need a faucet [player_name]! My partner is coming to visit soon!"

    "Well, this is what a tenant association is good for… shall I suggest it to Lynda?"

    menu:
        "Ask Lynda":
            jump lyndaassociation1

        "Leave it be":
            jump lyndatidyup


label lyndaassociation1:

    if lynda_rating >= 1 and SinkTimer > 5:

        $ lynda_convince += 2

        m "You know… I mentioned that tenancy association before. This is the kind of thing that it could help with."

        show lynda neutral at char_center

        l "I really do appreciate the sentiment [player_name]... let me think on it, okay?"

        show lynda unsure at char_center

        l "I do think it's a good idea."

    elif lynda_rating >= 1:

        $ lynda_convince += 1
        
        show lynda neutral at char_center

        m "You know… I mentioned that tenancy association before. This is the kind of thing that it could help with."

        show lynda unsure at char_center

        l "Yeah, I know. You make a good point. Just… let me think about it, okay? I just have so much on right now."

        m "I understand."

    else:
        show lynda neutral at char_center 
        
        m "You know… I mentioned that tenancy association before. This is the kind of thing that it could help with."

        show lynda annoyed at char_center

        l "Right now is not the time [player_name]!"

        "Lynda starts tidying."

        m "Okay..."

    jump lyndatidyup


label lyndatidyup:

    show lynda neutral at char_center
    
    "Lynda starts sorting out the area around the sink."

    m "Can I help?"

    l "No, no, its okay I can manage."

    m "Yeah, but I'd like to help."

    show lynda unsure at char_center

    l "Sure then, thanks."

    if lynda_rating >= 1:
        show lynda neutral at char_center

        "You both get to mopping up the kitchen, chatting and laughing, before you head home for the night."
    
    else:
        show lynda neutral at char_center

        "You both get to mopping up the kitchen, in a slightly awkward silence, before heading back home for the night."


    jump lyndainteraction3