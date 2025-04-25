label lyndainteraction1:
    scene bg lobby
    with dissolve
    
    "You re-enter the building after an evening walk, making most of the remaining daylight at dusk and prepare to climb the stairs. A woman emerges from the stairwell holding a laundry basket."

    show lynda neutral at truecenter

    "She looks to be in her late 40s, with some hints of grey in her hair wrapped up into a messy bun, though it looks so done with intention that it looks tidy."

    "A set of well-manicured nails peek overtop the laundry basket handle and a gentle smell of lavender lingers in the air."

    l "I thought I heard some chatter this morning outside my window - are you the one I heard telling someone 'no one will steal my stuff from the sidewalk it's 10am'?"

    "You recall a joking exchange between yourself and your friend over ferrying things indoors when they had to leave. They looked guilty, but you didn't want them to worry. Plus, stealing is a night crime, everyone knows that."

    m "Hah, yes that was me."

    "The woman extends her hand out."
    show lynda joy at truecenter
    l "Lynda."

    m "<playername>."

    l "Well, welcome to the building, <playername>. I'm glad no one stole your things."
    show lynda neutral at truecenter
    l "How are you liking it so far?"

menu:
    "I'm adjusting.":
        jump adjusting

        label adjusting:
            m "I'm getting used to it. Once I've spent a few nights here, it'll feel a bit more like home, right?"
            show lynda content at truecenter
            l "Of course! It takes some time"
            $ BuildingPastGood = True
            jump lyndabye1

    "Better than my last place!":
        jump betterthan

        label betterthan:
            m "Well, it's already better than my last place!"
            show lynda surprise at truecenter
            "A flash of concern flits across Lynda's expression."

            l  "Oh, really? What was wrong with your place before?"

            $ BuildingPastGood = False

            menu:
                "Noisy neighbours":
                    jump noisyneigh

                    label noisyneigh:
                        m "It was a classic thin-walls-EDM-loving-party-neighbours situation. Didn't get much sleep."
                        show lynda unsure at truecenter
                        l "Oh dear… luckily everyone in this building tends to be respectful of volume. Unless there's some kind of sports on. Antony is very into his sports."

                        m "What kind of sports?"

                        l "No idea."
                        show lynda joy at truecenter
                        "She laughs."

                        l "All I know is if the referee could hear him, they would be blushing."

                        m "Oh… oh dear."

                        m "Well, I moved to avoid it all, so let's hope it'll work out here!"
                        jump lyndabye1

                "General disrepair":
                    jump generaldisrepair

                    label generaldisrepair:
                        m "I think the building was held together with duct tape and dreams by the time I left…"
                        show lynda furrow at truecenter
                        "Another look of concern from Lynda."

                        m  "What?"
                        show lynda neutral at truecenter
                        l  "Hm? No, nothing, I just- this building has its quirks."

                        m "As in, sometimes the doors get stuck in the summer, or more, we've had multiple gas leaks? Because my old place existed across that spectrum of experiences."
                        show lynda joy at truecenter
                        l "...then you'll be fine!"

                        m "Well, I moved to avoid it all, so let's hope so!"
                        jump lyndabye1

                "Frequent fire alarms":
                    jump firealarms

                    label firealarms:
                        m  "I think I've stood in rain, snow, and shine multiple times due to people setting off the fire alarm with toast or cigarettes or one time a birthday cake candle situation"
                        show lynda neutral at truecenter
                        l  "You won't have to worry about that here, the last time it was set off was months ago with a very real fire, but they contained it quickly. Someone left something on the stove and it was a warning and reminder enough to us all to be vigilant."

                        m "Yikes."

                        m "Well, I moved to avoid that kind of thing, so I'm looking forward to not waking up to beeping!"
                        jump lyndabye1

                "All of the above":
                    jump allabove

                    label allabove:
                        m "I mean, the building may as well have been Grey Sloan Memorial Hospital with the amount of tragedies that hit it."
                        show lynda unsure at truecenter
                        l "Oh dear… well then I think you'll be just fine here!"

                        m "Well, I moved to avoid it all, so let's hope so!"
                        jump lyndabye1

label lyndabye1:

if BuildingPastGood:
    show lynda content at truecenter
    l "Well, nice to meet you, and see you around the building!"

    m "Nice to meet you, Lynda!"

    "You both head off to your apartments for the night."

    jump lyndainteraction2
else:
    show lynda content at truecenter
    l "It's been nice chatting, <playername> but this laundry isn't going to fold itself, unfortunately."

    m "No worries at all."

    l "See you around the building!"

    "You both head off to your apartments for the night."

    jump lyndainteraction2







