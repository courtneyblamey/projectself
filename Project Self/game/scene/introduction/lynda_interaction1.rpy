label lyndainteraction1:

    "You re-enter the building after an evening walk, making most of the remaining daylight at dusk and prepare to climb the stairs. A woman emerges from the stairwell holding a laundry basket."

    "She looks to be in her late 40s, with some hints of grey in her hair wrapped up into a messy bun, though it looks so done with intention that it looks tidy."

    "A set of well-manicured nails peek overtop the laundry basket handle and a gentle smell of lavender lingers in the air."

    l "I thought I heard some chatter this morning outside my window - are you the one I heard telling someone 'no one will steal my stuff from the sidewalk it's 10am'?"

    "You recall a joking exchange between yourself and your friend over ferrying things indoors when they had to leave. They looked guilty, but you didn't want them to worry. Plus, stealing is a night crime, everyone knows that."

    m "Hah, yes that was me."

    "The woman extends her hand out."

    l "Lynda."

    m "<playername>."

    l "Well, welcome to the building, <playername>. I'm glad no one stole your things."

    l "How are you liking it so far?"

menu:
    "I'm adjusting.":
        jump adjusting

        label adjusting:
            m "I'm getting used to it. Once I've spent a few nights here, it'll feel a bit more like home, right?"

            l "Of course! It takes some time"
            $ BuildingPastGood = True
            jump lyndabye1

    "Better than my last place!":
        jump betterthan

        label betterthan:
            m "Well, it's already better than my last place!"

            "A flash of concern flits across Lynda's expression."

            l  "Oh, really? What was wrong with your place before?"

            $ BuildingPastGood = False

            menu:
                "Noisy neighbours":
                    jump noisyneigh

                    label noisyneigh:
                        m "It was a classic thin-walls-EDM-loving-party-neighbours situation. Didn't get much sleep."

                        l "Oh dear… luckily everyone in this building tends to be respectful of volume. Unless there's some kind of sports on. Antony is very into his sports."

                        m "What kind of sports?"

                        l "No idea."

                        "She laughs."

                        l "All I know is if the referee could hear him, they would be blushing."

                        m "Oh… oh dear."

                        m "Well, I moved to avoid it all, so let's hope it'll work out here!"
                        jump lyndabye1
                        
                "General disrepair"
                "Frequent fire alarms"
                "All of the above"





