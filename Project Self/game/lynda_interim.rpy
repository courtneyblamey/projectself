label lynda_interim:

    #this scene goes between interaction 1 and 2 to set up the premise that no one turns up to the first tenant's meeting.

    scene bg lobby at bg_fit
    with dissolve
    "During your walk home you scroll through some articles on how to approach forming a tenant association. Many recommend forming genuine connections with each other to help with organising and delegating leadership to one or two people to help efficiency."

    m "Guess I self-elect as leader?"

    "Other sites suggest finding common issues in the building to help leverage interest from fellow tenants."

    m "Yeah, that makes sense."

    "You open the building door and spot your sign up list on the bulletin board."

    "{i}Are you bothered by issues in your apartment? Sign up to help form a tenants association so we can work together and hold our building managers accountable!/{i}"

    "{i}First meeting Apt 101 next Tuesday evening, snacks provided!/{i}"

    "About ten signatures are scrawled on the paper."

    m "That's 50% of folks signed up!"

    m "This is going to be easier than I thought."
    
    "You take down the list and carry your bag of snacks and sodas up to your apartment."

    scene pc apartment at bg_fit
    with dissolve

    "You set up the space and unbolt the door so folks can head on in."

    "The chip bowls have tongs in them to prevent any double dip ick, and a small stack of holiday themed paper plates sit to the side."

    m "They were on sale."

    "You also laid out a variety of sodas, both caffeinated and non-caffeinated, and some crudites."

    m "Pronounced {i} crew-di-tay {/i} not {i} crud-ite, apparently."

    m "That was an embarrassing night."

    menu:
        "Pace about the apartment.":
            jump paceapartment

            label paceapartment:
                "You stroll around your small front room. awaiting the first arrival."
                jump waiting
        "Check through the peephole.":
            jump peephole

            label peephole:
                "You peer through the peephole to nothing but an empty corridor."
                jump waiting

label waiting:
    "About 10 or 15 minutes pass by, with no one arriving."

    "Then, a sound at the door."

    m "Oh! Come in!"

    "..."

    "Silence."

    m "I swear I heard something."

    "You pop up and open the door."

    "Down the corridor an apartment door closes. It must have been their movement that rattled the door."

    m "Sigh."

    "Another 10 minutes tick by."

    menu:
        "Shovel chips into your face.":
            "You pick up one of the chip bowls and begin to cram them into your mouth."
            m "At least I got flavours I like..."
            jump stillwaiting
        "Drink a sparkling water.":
            "Choosing carefully, you crack a can of raspberry flavoured sparkling water and sip it."
            m "Some people call it rock water, but I like it."
            jump stillwaiting
        "Drink a soda.":
            "You grab a can of cola and slam half of it."
            m "Aaah... that's crispy."
            jump stillwaiting

label stillwaiting:
    "A full hour goes by."

    m "I don't think anyone is coming... why sign up if you won't turn up?"

    "A pang of frustration hits. Then, realisation."

    m "I sign up for things and don't turn up hoping that others will be there..."

    m "...I need to convince them it is {i}worth{/i} participating. That a difference can come from this."

    "You clear your coffee table and write a new sign for the bulletin board."

    "{i} Thanks to all who came tonight! We'll meet again next month to discuss grievances in the building we want dealt with! We already have water pressure as one of them. And if you haven't signed up, you can still!"

    scene bg lobby at bg_fit

    "You trot downstairs with new determination and pin up the sheet."

    m "Okay, now all I need to do is spend some time convincing folks... shouldn't be that hard, right?"

    "..."

    m "Right?"

    "Right."

    jump lyndainteraction2
