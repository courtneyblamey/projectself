

label gameendingbad:
    hide black_overlay 
    scene bg pc apartment at bg_fit
    with Dissolve(3.0)
    "A MONTH LATER."
    "As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."
    "Today must be the day Lynda moves out."
    "A flicker of frustration courses through you before you let out a sigh."
    m "Well, guess it's time to chat with the other tenants."
    jump lyndareflectiontime

label gameendingneut:
    scene bg pc apartment at bg_fit
    with Dissolve(3.0)
    "A MONTH LATER."
    "As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."
    "Today must be the day Lynda moves out."
    "A wave of sadness hits."
    "While Lynda's departure makes sense, you can't help but be sad to see her go. Partly because of the rapport you both built over the last couple months, but equally because you'd hoped she would be your helper with the association."
    m "Guess it's time to chat with the other tenants."
    jump lyndareflectiontime

label gameendinggood:
    scene bg lobby at bg_fit
    with Dissolve(3.0)
    "A MONTH LATER."
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
    "Lynda jogs over."
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
    scene bg pc apartment at bg_fit 
    with dissolve
    "As you get back into your apartment, you get to tidying up from the first meeting with actual attendees from last night. Even if it was just Lynda."
    "But that's proof you can get others on board."
    m "Guess it's time to chat with the other tenants."
    jump lyndareflectiontime


label lyndareflectiontime:
    play music "audio/Pamela Yuen - Dream Diary.mp3" fadeout 2.0 fadein 2.0
    scene bg black at bg_fit
    with Dissolve(5.0)
    "Our choices matter. We're often told this in games especially. So let's take a moment to reflect."
    "If the following section becomes too much for you, please feel free to save and exit the game."
    "Some big questions for you [player_name]:"
    
    "Do you ever doubt your skills?"
    menu:
        "Yes":
            jump yesdoubtskills
        "No":
            jump nodoubtskills
    
label yesdoubtskills:
    if EndCredit:
        "When Lynda doubted her skills dealing with the tech she brought from work you told her 'I think you know more than you realise.'"
        "That stayed with Lynda. She gained a little more confidence in what she could do."
        "As for you, what made you reassure her skills? Perhaps she was being too hard on herself? Or denied herself of what her capability is?"
        "Next question..."
        #confidence marker for lynda in next iteration?
        jump struggle
    else:
        "Both Lynda and yourself experience the same worries. Lynda wasn't sure she could get enough of a hold on the technological side of her role."
        "What do you feel unsure of? Have others said things to make you feel such a way? Or does the pressure come from within?"
        "Next question..."
        jump struggle

label nodoubtskills:
    if EndCredit:
        "When Lynda doubted her skills dealing with the tech she brought from work you told her 'I think you know more than you realise.'"
        "It helped her feel more secure in her own knowledge about things."
        "What from your own confidence made you reassure her skills? Perhaps she was being too hard on herself? Or denied herself of what her capability is?"
        "Next question..."
        jump struggle
    else:
        "Wonderful! What helps you feel assured in your skills? Is it tangible expertise, like degrees or projects? Or is it comments from others? Or does it come from within?"
        "Next question..."
        jump struggle

label struggle:
    "Do you talk with people when you're struggling?"
    menu:
        "Yes":
            jump talkstruggle
        "No":
            jump notalkstruggle
    
label talkstruggle:
    if lynda_blab:
        "When Lynda was struggling with the long-distance nature of her relationship you gave her the chance to blab! Sometimes blabbing about feelings can help us externalise things."
        "You offered an ear for her, just like you ask of others."
        "Next question..."
        jump harder
    elif lynda_validate:
        "When Lynda was struggling with the long-distance nature of her relationship you validated her struggles. Just as others, hopefully, validate yours."
        "Next question..."
        jump harder
    else:
        "Next question..."
        jump harder

label notalkstruggle:
    if lynda_blab:
        "When Lynda was struggling with the long-distance nature of her relationship you gave her the chance to blab! Sometimes blabbing about feelings can help us externalise things."
        "You offered an ear for her."
        "It's okay to ask that of others when you feel overwhelmed."
        "Next question..."
        jump harder
    elif lynda_validate:
        "When Lynda was struggling with the long-distance nature of her relationship you validated her struggles." 
        "What is it the makes you not want to share with others? Is it trust or vulnerability?"
        "You are likely rarely alone in how you're feeling. You might even find advice where you least expect it."
        "Next question..."
        jump harder
    else:
        "What is it the makes you not want to share with others? Is it trust or vulnerability?"
        "Or do you not want to do that emotional work for others, so sharing feels unfair?"
        "It is okay to not always share how you're doing or feeling. But sometimes not having an outlet can make things feel so lonely."
        "You don't have to be alone in things."
        "Next question..."
        jump harder

label harder:
    "Are you harder on yourself than you should be?"
    menu:
        "Yes":
            jump yesharder
        "No":
            jump noharder

label yesharder:
    if lynda_blame:
        "When Bean escaped, Lynda felt wholly responsible for his escapade." 
        "You reminded her to not blame herself. Some things are beyond our control, and beating yourself up over a misstep is not kind to yourself."
        jump lyndareflectionend
    elif lynda_overwork:
        "When Bean escaped, Lynda felt wholly responsible for his escapade." 
        "You pointed out she worked too much. Not as a critique, but as a concern. Lynda spends a lot of time overpreparing for work meetings and presentations, and you helped her realise she could ease off a little bit."
        jump lyndareflectionend
    else:
        "Giving ourselves permission to be gentler to ourselves is hard."
        "Sometimes it can be as small as ending a work day a little earlier, or externalising our inner critic to hear it aloud, but it is no easy task."
        jump lyndareflectionend

label noharder:
    "When Bean escaped, Lynda felt wholly responsible for his escapade." 
    if lynda_blame:
        "You reminded her to not blame herself. Some things are beyond our control, and beating yourself up over a misstep is not kind to yourself."
        jump lyndareflectionend
    elif lynda_overwork:
        "You pointed out she worked too much. Not as a critique, but as a concern. Lynda spends a lot of time overpreparing for work meetings and presentations, and you helped her realise she could ease off a little bit."
        jump lyndareflectionend
    else:
        "Finding the balance of not being our own worst critic, while also accepting of criticism is no easy feat. Check in with those around you."
    jump lyndareflectionend

label lyndareflectionend:
    if imposter:
        "You identified with Lynda."
    else:
        "You did not necessarily identify aspects of yourself in Lynda."
        "After this, does that still hold true?"

    "Sometimes, it is easier to give advice than take it."

    "Sometimes, it is easy to forget that we're not so alone in our feelings. Even though it can feel like it at times."

    "And sometimes... the weight of the world and others can rest on us in ways we don't expect."

    "I never really know how to end things."

    "But I hope, for a moment, that you can see your kind words towards Lynda, someone who isn't real, as things you can say to yourself or to others around you. To grant yourself and others the same generosity and care."

    "Maybe you didn't pick those options, perhaps you were curious what certain options might bring you, or maybe you just didn't vibe with Lynda."

    "However it went, be grateful you took a moment for yourself."

    "We all need more of those."
    
    "Thank you for playing <3."

    "This was for No One in Particular."

    "CREDITS!"

    "Background Art: Kira Fountain"

    "Character Artist: Tuana Bicakci"

    "Title and Reflection Music: Come As You Are and Dream Diary by Pamela Yuen"

    "Main Game Theme: DJ Possum by Stijn van Wakeren"

    "QA: Tiff, Jules, and Michael - thank you all <3"

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

