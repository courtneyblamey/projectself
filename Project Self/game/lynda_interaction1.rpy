label lyndainteraction1:
    scene bg lobby at bg_fit
    with dissolve
    
    "You re-enter the building after an evening walk, making most of the remaining daylight at dusk and prepare to climb the stairs."
    "There's a notice board in the entrance littered with 'for sale' furniture posters, business cards, and a couple hand-scrawled notes."

    label notice_menu:

        # If all have been read, continue automatically
        if read_laundry and read_disposal and read_pipes and read_noise:
            jump notice_after

        menu:
            "What do you read?"

            "Read 'laundry room'" if not read_laundry:
                $ read_laundry = True
                jump notice_laundry

            "Read 'disposal of goods'" if not read_disposal:
                $ read_disposal = True
                jump notice_disposal

            "Read 'pipe issues'" if not read_pipes:
                $ read_pipes = True
                jump notice_pipes

            "Read 'noise notice'" if not read_noise:
                $ read_noise = True
                jump notice_noise

            "Step away from the board":
                jump notice_after


label notice_laundry:

    "{i}Dear tenants, as of the new rent cycle please be advised that the cost of laundry will increase by 1$. We have installed a new change machine to assist in this adjustment.{/i}"
    "Scrawled beneath it reads: {i}don't bother, none of the machines work anyway!!!!{/i}"

    m "Uh oh."

    jump notice_menu


label notice_disposal:

    "{i}Can we get some more garbage bins?! We're having to pile laundry in the garage and the raccoons are having a field day with all the bags.{/i}"

    m "Raccoons are criminals, but cute and hungry tiny criminals."

    jump notice_menu


label notice_pipes:

    "{i}Has anyone else noticed weird groaning sounds when running their sink? Come knock at apartment 7 - Lynda{/i}"

    jump notice_menu


label notice_noise:

    "{i}Dear tenants, we have been made aware that there is a beeping noise coming from inside the electrical room of the building. This is nothing to be concerned about and nothing can be done to silence it. With that in mind please do not email us about the beeping.{/i}"

    "A slight concern rises in your stomach."

    jump notice_menu


label notice_after:

    "A woman emerges from the stairwell holding a laundry basket, startling you."

    m "OH!"

    show lynda laugh at char_center

    l "Oh no, sorry!"

    m "No, I'm sorry, I was just checking out this board and got lost reading."

    show lynda neutral at char_center

    "She looks to be in her late 40s, with some hints of grey in her hair wrapped up into a messy bun, though it looks so done with intention that it looks tidy."

    "A set of well-manicured nails peek overtop the laundry basket handle and a gentle smell of laundry detergent hangs in the air."

    l "I thought I heard some chatter this morning outside my window - are you the one I heard telling someone 'no one will steal my stuff from the sidewalk it's 10am'?"

    "You recall a joking exchange between yourself and your friend over ferrying things indoors when they had to leave. They looked guilty, but you didn't want them to worry. Plus, stealing is a night crime, everyone knows that."

    m "Hah, yes that was me."

    "The woman extends her hand out."

    l "Lynda."

    m "[player_name]."

    l "Well, welcome to the building, [player_name]. I'm glad no one stole your things."
    show lynda neutral at char_center
    l "How are you liking it so far?"

menu:
    "I'm adjusting.":
        jump adjusting

        label adjusting:
            m "I'm getting used to it. Once I've spent a few nights here, it'll feel a bit more like home, right?"
            show lynda unsure at char_center
            l "Of course! It takes some time"
            $ BuildingPastGood = True
            jump lyndabye1

    "Better than my last place!":
        jump betterthan

        label betterthan:
            m "Well, it's already better than my last place!"
            show lynda annoyed at char_center
            "A flash of concern flits across Lynda's expression."

            l  "Oh, really? What was wrong with your place before?"

            $ BuildingPastGood = False

            menu:
                "Noisy neighbours":
                    jump noisyneigh

                    label noisyneigh:
                        m "It was a classic thin-walls-EDM-loving-party-neighbours situation. Didn't get much sleep."
                        show lynda unsure at char_center
                        l "Oh dear… luckily everyone in this building tends to be respectful of volume. Unless there's some kind of sports on. Antony is very into his sports."

                        m "What kind of sports?"

                        l "No idea."
                        show lynda laugh at char_center
                        "She laughs."

                        l "All I know is if the referee could hear him, they would be blushing."

                        m "Oh… oh dear."

                        m "Well, I moved to avoid it all, so let's hope it'll work out here!"
                        jump lyndabye1

                "General disrepair":
                    jump generaldisrepair

                    label generaldisrepair:
                        m "I think the building was held together with duct tape and dreams by the time I left…"
                        show lynda sad at char_center
                        "Another look of concern from Lynda."

                        m  "What?"
                        show lynda neutral at char_center
                        l  "Hm? No, nothing, I just- this building has its quirks."

                        m "As in, sometimes the doors get stuck in the summer, or more, we've had multiple gas leaks? Because my old place existed across that spectrum of experiences."
                        show lynda laugh at char_center
                        l "...then you'll be fine!"

                        m "Well, I moved to avoid it all, so let's hope so!"
                        jump lyndabye1

                "Frequent fire alarms":
                    jump firealarms

                    label firealarms:
                        m  "I think I've stood in rain, snow, and shine multiple times due to people setting off the fire alarm with toast or cigarettes or one time a birthday cake candle situation"
                        show lynda neutral at char_center
                        l  "You won't have to worry about that here, the last time it was set off was months ago with a very real fire, but they contained it quickly. Someone left something on the stove and it was a warning and reminder enough to us all to be vigilant."

                        m "Yikes."

                        m "Well, I moved to avoid that kind of thing, so I'm looking forward to not waking up to beeping!"
                        jump lyndabye1

                "All of the above":
                    jump allabove

                    label allabove:
                        m "I mean, the building may as well have been Grey Sloan Memorial Hospital with the amount of tragedies that hit it."
                        show lynda unsure at char_center
                        l "Oh dear… well then I think you'll be just fine here!"

                        m "Well, I moved to avoid it all, so let's hope so!"
                        jump lyndabye1

label lyndabye1:

if BuildingPastGood:
    show lynda neutral at char_center
    l "Well, nice to meet you, and see you around the building!"

    m "Nice to meet you, Lynda!"

    "Lynda starts to walk away, but pivots back to you."

    show lynda unsure at char_center

    l "Hey, uh, if you have any issues in the building, I just want to warn you that building management isn't great at dealing with things."

    m "Oh, really? We had a tenant's association in my last building, which helped with that."

    l "Like a union?"

    m "Sort of! Collective action and power to deal with an absentee landlord."

    l "Huh. Honestly, that might not be a bad thing for here."

    m "Hmm… Well, hopefully it isn't necessary!"

    "There's a pause."
    
    show lynda neutral

    l "Okay, well, see you round! Laundry still not folding itself."

    m "See ya!"

    hide lynda neutral

    "You both head off to your apartments for the night."

    scene bg pc apartment at  bg_fit

    "You close your new apartment door behind you and take in your new space again. Some of your boxes still need unpacking but the bed is made and you're feeling ready to sleep."

    m "Shower first. Fresh sheets, new apartment, clean pyjamas. The perfect rest trifecta."

    "You undress and crank the shower on."

    "The water dribbles out."

    m "Maybe it needs a second."

    "The pressure remains the same."

    m "Ooookay then."

    "You get into the shower and lather up. Upon rinsing some soap from your eyes, you look up and clock a patch of mould across the ceiling."

    m "Not ideal."

    "Finally, as you exit the shower, you reach for your towel and the rail falls out of the wall fixture."

    m "...COOL."

    "You dry off and open up your laptop, typing in the search 'how to start a tenants association' with gusto."

    m "Okay, how many signatures do I need?"

    "{i}It is recommended to get 50\% of tenants signed up to have bargaining power, however, you can start an association with as little as two tenants.{/i}"

    m "Okay… so I just need one person to start?"

    m "Lynda suggested this, maybe she'd be interested… I'll bring it up when I next see her."

    "You spend the rest of the evening checking out how to run the association and details on tenants' rights in general. There's a sense of excitement, even if it means trying to persuade some total strangers to join you on the journey."

    jump lyndainteraction2
else:
    show lynda neutral at char_center
    l "It's been nice chatting, [player_name] but this laundry isn't going to fold itself, unfortunately."

    m "No worries at all."

    l "See you around the building!"

    "Lynda starts to walk away, but pivots back to you."

    show lynda unsure at char_center

    l "Hey, uh, if you have any issues in the building, I just want to warn you that building management isn't great at dealing with things."

    m "Oh, really? We had a tenant's association in my last building, which helped with that."

    l "Like a union?"

    m "Sort of! Collective action and power to deal with an absentee landlord."

    l "Huh. Honestly, that might not be a bad thing for here."

    m "Hmm… Well, hopefully it isn't necessary!"

    "There's a pause."

    show lynda neutral at char_center

    l "Okay, well, see you round! Laundry still not folding itself."

    m "See ya!"

    hide lynda neutral

    "You both head off to your apartments for the night."

    "You close your new apartment door behind you and take in your new space again. Some of your boxes still need unpacking but the bed is made and you're feeling ready to sleep."

    m "Shower first. Fresh sheets, new apartment, clean pyjamas. The perfect rest trifecta."

    "You undress and crank the shower on."

    "The water dribbles out."

    m "Maybe it needs a second."

    "The pressure remains the same."

    m "Ooookay then."

    "You get into the shower and lather up. Upon rinsing some soap from your eyes, you look up and clock a patch of mould across the ceiling."

    m "Not ideal."

    "Finally, as you exit the shower, you reach for your towel and the rail falls out of the wall fixture."

    m "...COOL."

    "You dry off and open up your laptop, typing in the search 'how to start a tenants association' with gusto."

    m "Okay, how many signatures do I need?"

    "{i}It is recommended to get 50\% of tenants signed up to have bargaining power, however, you can start an association with as little as two tenants.{/i}"

    m "Okay… so I just need one person to start?"

    m "...maybe Lynda? I'll bring it up when I next see her."

    "You spend the rest of the evening checking out how to run the association and details on tenants' rights in general. There's a sense of excitement, even if it means trying to persuade some total strangers to join you on the journey."

    jump lyndainteraction2







