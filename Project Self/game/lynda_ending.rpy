

label gameendingbad:
    hide black_overlay:
        linear 1.0 alpha 0.0
    scene bg pc apartment at bg_fit
    with dissolve
    "A FEW WEEKS LATER."
    "As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."
    "Today must be the day Lynda moves out."
    "A flicker of irritation courses through you."
    "While she might not have joined your cause, now's the time to start thinking about the others."
    m "Guess it's time to chat with the other tenants."
    jump lyndareflectiontime

label gameendingneut:
    scene bg pc apartment at bg_fit
    with dissolve
    "A FEW WEEKS LATER."
    "As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."
    "Today must be the day Lynda moves out."
    "A wave of sadness hits."
    "While Lynda's departure makes sense, you can't help but be sad to see her go. Partly because of the rapport you both built over the last couple months, but equally because you'd hoped she would be your helper with the association."
    m "Guess it's time to chat with the other tenants."
    jump lyndareflectiontime

label gameendinggood:
    scene bg lobby at bg_fit
    with dissolve
    "A FEW WEEKS LATER."
    show lynda neutral at char_center
    l "Yeah, just stack them here for now!"
    "You lug some moving boxes over to the lobby doorway."
    m "My god, what do you have in this one?"
    show lynda annoyed at char_center
    l "Fashion magazines from the 90s."
    m "Bricks would be lighter."
    show lynda laugh at char_center
    "You plonk it down and grab another box with an open top."
    show lynda neutral at char_center
    m "Oh, this one needs taping shut!"
    l "Oh! Actually!"
    "Lynda trots over."
    show lynda wink at char_center
    l "That's for you!"
    show lynda neutral at char_center
    m "Me?"
    "You peer into the box."
    "There's another box in there labelled 'The Story Cube'"
    l "It's the actual product I was trying to figure out way back! This is one of the first ones manufactured that we're showcasing soon."
    l "I thought it might be a silly gift. I know it's bedtime stories, but-"
    m "No, that's very wholesome, thank you."
    "You place the box to the side and hug Lynda."
    show lynda unsure at char_center
    l "I chatted with Antony and Sasha about the association, so hopefully they'll have a little more intrigue than before."
    show lynda neutral at char_center
    m "Thank you."
    show lynda neutral at char_left
    show anna concern at char_right
    a "Lynda, my love, the movers said they'd grab the rest and we should drive ahead to the new place."
    show anna annoyed at char_right
    a "Also, I think Bean and Maple might lose it if we leave them outside the car in their carriers much longer."
    show anna neutral at char_right
    a "The kitty Xanax hasn't kicked in yet it seems."
    l "Alright."
    "Lynda squeezes your arm."
    l "Best of luck with it all [player_name]."
    "You wave bye to Lynda and Anna as they head out."
    scene bg pc apartment at bg_fit with dissolve
    "As you get back into your apartment, you get to tidying up from the first meeting with actual attendees from last night. Even if it was just Lynda."
    "But that's proof you can get others on board."
    m "Guess it's time to chat with the other tenants."
    jump lyndareflectiontime


label lyndareflectiontime:
    "Our choices matter. We're often told this in games especially. So let's tale a moment to reflect."
    show black_overlay onlayer overlay:
        alpha 0.0
        linear 1.0 alpha 1.0
    "Do I ever doubt my skills?"
    menu:
        "Yes":
            jump doubtskills
        "No":
            jump nodoubtskills
    
label doubtskills:
    if EndCredit:
        "When Lynda doubted her skills you told her 'I think you know more than you realise.'"
    else:
        jump struggle

label nodoubtskills:
    if EndCredit:
        "When Lynda doubted her skills you told her 'I think you know more than you realise.'"
        "It helped her feel more secure in her own knowledge about things."
        jump struggle
    else:
        jump struggle

label struggle:
    "Do I talk with people when I'm struggling?"
    menu:
        "Yes":
            jump talkstruggle
        "No":
            jump notalkstruggle
    
label talkstruggle:
    if lynda_blab:
        "When Lynda was struggling with the long-distance nature of her relationship you gave her the chance to blab! Sometimes blabbing about feelings can help us externalise things."
        "You offered an ear for her, just like you ask of others."
    elif lynda_validate:
        "When Lynda was struggling with the long-distance nature of her relationship you validated her struggles. Just as others validate yours."
    else:
        jump harder

label notalkstruggle:
    if lynda_blab:
        "When Lynda was struggling with the long-distance nature of her relationship you gave her the chance to blab! Sometimes blabbing about feelings can help us externalise things."
        "You offered an ear for her. It's okay to ask that of others."
    elif lynda_validate:
        "When Lynda was struggling with the long-distance nature of her relationship you validated her struggles. You are likely rarely alone in how you're feeling."
    else:
        jump harder

label harder:
    "Am I harder on myself than I should be?"
    menu:
        "Yes":
            jump yesharder
        "No":
            jump noharder

label yesharder:
    "When Bean escaped, Lynda felt wholly responsible for his escapade." 
    if lynda_blame:
        "You reminded her to not blame herself. Some things are beyond our control, and beating yourself up over a misstep is not kind to yourself."
    elif lynda_overwork:
        "You pointed out she worked too much. Not as a critique, but as a concern. Lynda spends a lot of time overpreparing for work meetings and presentations, and you helped her realise she could ease off a little bit."
    else:
        jump lyndareflectionend

label noharder:
"When Bean escaped, Lynda felt wholly responsible for his escapade." 
    if lynda_blame:
        "You reminded her to not blame herself. Some things are beyond our control, and beating yourself up over a misstep is not kind to yourself."
    elif lynda_overwork:
        "You pointed out she worked too much. Not as a critique, but as a concern. Lynda spends a lot of time overpreparing for work meetings and presentations, and you helped her realise she could ease off a little bit."
    else:
        jump lyndareflectionend

label lyndareflectionend:
    if imposter:
        "You identified with Lynda."
    else:
        "You did not necessarily see yourself in Lynda."
        "After this, does that still hold true?"
    "Sometimes, it is easier to give advice than take it."

    "But I hope, for a moment, that you can see your kindness towards Lynda, someone who isn't real, as things you can say to yourself. To grant yourself the same level of kindness."

    "If you didn't pick these options, perhaps you were curious what certain options might bring you, or maybe you just didn't vibe with Lynda."

    "However it went, I'm grateful you took a moment to reflect. Thank you for playing."

    "This was for No One in Particular."

    return



#label lyndaending:
#if imposter:
#    else:
#        jump 
#   
#   if EndCredit:
#       m "I told Lynda she shouldn't doubt her knowledge."
#   if EndMistake:
#       "You told Lynda [EndMistake]."

#label lyndareflection:
#   if lynda_reflection = "instincts":
#   elif lynda_reflection = "kinder":
#   elif lynda_reflection = "work":
#   else:
#       jump reflectionend

#label reflectionend

