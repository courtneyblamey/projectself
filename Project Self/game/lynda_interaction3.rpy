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

m "To the laundry room!"
