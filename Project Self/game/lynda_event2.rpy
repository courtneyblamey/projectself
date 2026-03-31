label lyndaevent2:

scene pc apartment at bg_fit

    "It's a quiet and grey afternoon, you decide to:"

    menu:
        "Bake some cookies":
            $ Baking = True

            "You put on some tunes and get to baking!"
            m "Hmm… what kind of cookies do I make…"

            menu:
                "Apple pie":
                    $ CookieType = "apple pie"
                "Pumpkin pecan":
                    $ CookieType = "pumpkin pecan"
                "Double chocolate":
                    $ CookieType = "double chocolate"

            "The scent of baked goods slowly fills the air as you pull the tray of cookies out of the oven."
            "A sudden knock at the door startles you."

            jump lyndabean1

        "Put on a comfort series":
            $ TVOn = True

            "You launch yourself onto the couch and bundle up in blankets."
            m "Ehehehehe."
            "You kick your feet excitedly as your streaming app boots up."
            "As the opening title rolls, there's a sudden knock at the door."

            jump lyndabean1

        "Curl up and play a game":
            $ GamingOn = True

            "You grab your controller and cocoon into some blankets."
            m "Yes. E x c e l l e n t."
            "As the console powers on, there's a sudden knock at the door."

            jump lyndabean1

label lyndabean1:

    "You open your door to a very stressed out Lynda."

    if lynda_rating > 2:
        show lynda sad at char_center
        l "Oh, thank god you're home!"
        m "Lynda, you okay?"
        l "No, no not really. Bean is missing."
        m "What?!"

        "Lynda walks into your apartment, pacing frantically."

        if Baking:

            l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- Oh my god it smells amazing in here."

            m "Want one?"
            "You offer a cookie to Lynda."

            l "I won't say no."

            "She shoves the cookie in her mouth and continues to pace."

            l "I domphn't know howmph Bean eshcaped."
            l "Sorry *ahem*, I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

            l "Can you help me look?"
            m "Of course!"
            show lynda neutral at char_center
            l "Thank you thank you thank you. I'm going to check the apartment one last time and then look around the upstairs area."

            "She dusts the crumbs off of herself and pats you on the arm."
            show lynda sad at char_center
            l "Wait, no, I'm sorry, I feel like I'm intruding on your afternoon."

            jump findbeanchoice

        elif TVOn:

            l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and-"
            l "Oh I'm catching up on that season too."

            l "Sorry, distracted - I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

            l "Can you help me look?"
            m "Of course!"
            show lynda neutral at char_center
            l "Thank you thank you thank you. I'm going to check the apartment one last time and then look around the upstairs area."

            "Some characters begin to argue on the TV."

            show lynda sad at char_center

            l "Oh! I'm sorry, I realise I'm intruding on your afternoon."

            jump findbeanchoice

        elif GamingOn:

            l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and-"

            "The start menu is blaring music in the background."

            m "Lemme just…"
            "You turn it down."
            show lynda neutral at char_center
            m "Sorry, new game in a series I love, you were saying?"
            show lynda sad at char_center
            l "No I'm sorry! I feel like I'm intruding on your afternoon."

            jump findbeanchoice

    else:

        if Baking:

            l "I was doing something for work tomorrow and I went to feed him and- wow something smells good."

            m "Want one?"
            "You offer a cookie to Lynda."
            show lynda neutral at char_center
            l "Umm… no it's okay, but thanks."

            l "I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

            l "I'm sorry to ask but could you help me look?"
            m "Of course!"

            l "I really appreciate it. I'm going to check the apartment one last time and then look around the upstairs area."
            show lynda sad at char_center
            l "Wait, no, I'm sorry, I feel like I'm intruding on your afternoon."

            jump findbeanchoice

        elif TVOn:

            l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and-"
            show lynda neutral at char_center
            l "Oh I'm catching up on that season too."

            l "Sorry, distracted - I don't know how Bean escaped…"
            show lynda sad at char_center
            l "Can you help me look?"
            m "Of course!"
            show lynda neutral at char_center
            l "Thank you thank you thank you."

            "Some characters begin to argue on the TV."

            l "Oh! I'm sorry, I realise I'm intruding on your afternoon."

            jump findbeanchoice

        elif GamingOn:

            l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and-"

            "The start menu is blaring music in the background."

            m "Lemme just…"
            "You turn it down."

            m "Sorry, new game in a series I love, you were saying?"

            l "No I'm sorry! I feel like I'm intruding on your afternoon."

            jump findbeanchoice

label findbeanchoice:

    menu:
        "Yeah, a little, but it's okay!":
            jump yeahbutbean

        "No, it's okay.":
            jump noitsbean

        "Gaze longingly at your afternoon plans.":
            jump gameoverbean

label gameoverbean:
    show lynda sad at char_center
    $ HelpLynda -= 2

    $ lynda_rating -=2

    m "I mean…."

    if GamingOn:
        "You look over at the bouncing title screen. You don't get a lot of free time, and you were *really* looking forward to being a couch gremlin."

    elif Baking:
        "You think about whether the cookie dough would be fine in the fridge for a bit."

    elif TVOn:
        "This season has had so much hype around it, and right now two of your favourite characters are getting into a heated argume- OH THEY'RE KISSING."

    m "You're sure Bean isn't just hiding in the apartment?"
    show lynda unsure at char_center
    l "I'll go look again… if you see or hear him, would you look?"
    m "Sure, yeah."

    "Lynda walks out and shuts the door behind her."
    hide lynda unsure
    jump gameoverbeanend

label yeahbutbean:

    m "A little, but it's okay! Bean is missing. That takes priority."

    jump lyndabean2

label noitsbean:

    m "No, it's okay. Bean got out?"

    jump lyndabean2

label lyndabean2:
    show lynda annoyed at char_center
    l "I just don't know how he got out!"

    l "He's normally so lazy that at any time I'll find him passed out in blankets or my bed, but today when I finished prepping he was nowhere."
    show lynda unsure at char_center
    m "A sudden burst of adventure, maybe?"

    l "Maybe… but he's still my dopey boy and I want him home."

    m "Of course! I can look around if you want to check your place again?"

    l "Sure."
    show lynda neutral at char_center
    "Time to split the party and find this furry escape artist."
    hide lynda neutral

    jump beansearch

label beansearch:

    if bean_location is None:
        $ bean_location = renpy.random.choice([
            "outside",
            "lobby",
            "laundry",
            "balcony",
            "bedroom"
        ])

"Where should you look?"

menu:

    "Inside the building":
        $ checked_lobby = False
        $ checked_mail = False
        $ checked_planters = False
        $ checked_stairwells = False
        $ checked_laundry = False
        jump beaninbuilding

    "Outside the building":
        $ checked_bushes = False
        $ checked_bins = False
        $ checked_cars = False
        jump beanoutbuilding

    "Check your apartment":
        $ checked_balcony = False
        $ checked_bedroom = False
        jump beaninapartment

label beanoutbuilding:

scene bg outside at bg_fit

    if checked_bushes and checked_bins and checked_cars:
        "You've checked everywhere outside… Bean must be somewhere else."
        jump beansearch

    "You head outside of the building, bundling up against the crisp breeze."

    m "Beaaaaan!"

    "The wind picks up a bit as you wander around the outside of the building."

    if bean_location == "outside":

        "Where do you check?"

        menu:

            "Check bushes" if not checked_bushes:
                $ checked_bushes = True

                m "Maybe the bushes?"

                "You approach the group of bushes at the side of the building and begin to peer through the branches."

                m "Bean~?"
                b "{size=-10}mrow{/size}"

                m "Beaaaan~?"
                b "m r o w w w"

                m "Bean!"

                show bean at char_center

                "A pair of eyes peer back at you through the branches. Bean is curled up tight and trembling."

                m "Oh, buddy!"

                "You take off your scarf and bundle him up in it. He's not game initially, but soon succumbs to the woollen burrito."

                hide bean with dissolve

                jump foundbean

            "Check garbage bins" if not checked_bins:
                $ checked_bins = True

                m "He does love cardboard, maybe near the bins?"

                "You head around the back of the building to the bins."

                m "Beaaan?"
                m "Beaaaaaaan!"

                "After some kissy sounds and searching, there's no sign of Bean."

                m "Darn."

                jump beanoutbuilding

            "Check under cars" if not checked_cars:
                $ checked_cars = True

                m "Let's check cars."

                "You kneel down and look under the cars parked at the front of the building."

                m "Beanie boyyyy?"

                "...nothing."

                "You hear some rustling under a red car."

                m "Bean?"

                "A bunch of fallen leaves whirl out from under the car and hit you in the face."

                m "ACK."
                m "Bleugh."

                "You brush your face off and sigh."

                m "Not here…"

                jump beanoutbuilding

    else:

        "Where do you check?"

        menu:
            "Check bushes" if not checked_bushes:
                $ checked_bushes = True

                m "Maybe the bushes?"

                "You approach the group of bushes at the side of the building and begin to peer through the branches."

                m "Bean~?"

                "A bunch of litter is stuck amongst the branches."

                m "Mm, nice."

                "You climb slightly into the bushes to check Bean isn't hiding in one of them."

                m "Bean??"

                "There's no sign of Bean here."

                m "Where are you?"

                jump beanoutbuilding

            "Check garbage bins" if not checked_bins:
                $ checked_bins = True

                m "He does love cardboard, maybe near the bins?"

                "You head around the back of the building to the bins."

                m "Beaaan?"
                m "Beaaaaaaan!"

                "After some kissy sounds and searching, there's no sign of Bean."

                m "Darn."

                jump beanoutbuilding

            "Check under cars" if not checked_cars:
                $ checked_cars = True

                m "Let's check cars."

                "You kneel down and look under the cars parked at the front of the building."

                m "Beanie boyyyy?"

                "...nothing."

                "You hear some rustling under a red car."

                m "Bean?"

                "A bunch of fallen leaves whirl out from under the car and hit you in the face."

                m "ACK."
                m "Bleugh."

                "You brush your face off and sigh."

                m "Not here…"

                jump beanoutbuilding

label beaninbuilding:

    if checked_lobby and checked_laundry:
        "You've checked everywhere inside the building… Bean must be somewhere else."
        jump beansearch
    
    "Where should you check?"

    menu:
        "Check the lobby" if not checked_lobby:
            $ checkled_lobby = True
            jump beanlobby

        "Check the laundry room" if not checked_laundry:
            $ checked_laundry = True
            jump beanlaundry

label beanlobby:
scene bg lobby at bg_fit
    if checked_mail and checked_planters and checked_stairwells:
        "You've checked everything in the lobby… Bean must not be here."
        jump beaninbuilding

    if bean_location == "lobby":

            "Where do you check?"

            menu:
                "Check the mailbox area" if not checked_mail:
                    $ checked_mail = True

                    "You investigate the mailbox area."

                    "...it's not likely that Bean climbed into one of the mailboxes."

                    m "Why give me the option then?!"

                    jump beanlobby

                "Check planters" if not checked_planters:
                    $ checked_planters = True

                    "There's a few planters in the lobby. Some are easily large enough to hide a furry escapee."

                    "You check them out one by one when - a wild Bean appears!"

                    show bean at char_center

                    "Curled up and content, Bean is snoozing in one of the plant pots, with some shreds of cardboard from someone's delivery parcel."

                    m "Ohhh, you little stinker."

                    m "Your mum is worried sick about you."

                    "You scoop him up, despite his complaining, and carry him back to Lynda's apartment."

                    hide bean with dissolve

                    jump foundbean

                "Check stairwells" if not checked_stairwells:
                    $ checked_stairwells = True

                    m "Maybe he managed to get into the stairwell…"

                    "The door creaks open."

                    m "Beany boy~?"

                    "You check around the different exits at each floor, clambering up a couple flights of stairs."

                    m "Ugggggghhh."

                    m "Thank god there's only a couple floors."

                    "Stairs are the only form of cardio that you cannot train to be better at."

                    m "Bean~?"

                    "Your voice echoes in the stairwell."

                    "No sign of Bean."

                    m "Where the heck are you?"

                    jump beanlobby

    else:

            "Where do you check?"

            menu:
                "Check the mailbox area" if not checked_mail:
                    $ checked_mail = True

                    "You investigate the mailbox area."

                    "...it's not likely that Bean climbed into one of the mailboxes."

                    m "Why give me the option then?!"

                    jump beanlobby

                "Check planters" if not checked_planters:
                    $ checked_planters = True

                    "There's a few planters in the lobby. Some are easily large enough to hide a furry escapee."

                    "You check them out one by one."

                    m "Achoo!"

                    "Ironically, most of these are plastic plants."

                    m "Must be the dust."

                    "No napping cat in any of them."

                    m "Where did you sneak off too you little stinker?"

                    jump beanlobby

                "Check stairwells" if not checked_stairwells:
                    $ checked_stairwells = True

                    m "Maybe he managed to get into the stairwell…"

                    "The door creaks open."

                    m "Beany boy~?"

                    "You check around the different exits at each floor, clambering up a couple flights of stairs."

                    m "Ugggggghhh."

                    m "Thank god there's only a couple floors."

                    "Stairs are the only form of cardio that you cannot train to be better at."

                    m "Bean~?"

                    "Your voice echoes in the stairwell."

                    "No sign of Bean."

                    m "Where the heck are you?"

                    jump beanlobby

label beanlaundry:
scene bg laundry at bg_fit
    if checked_laundry:
        "You've already checked the laundry room thoroughly… Bean doesn't seem to be here."
        jump beaninbuilding

    "You wander into the laundry room. The smell of floral laundry detergent and dryer sheets wafts in the air."

    m "Well, this is a cosy spot for a mischievous cat."

    if bean_location == "laundry":

        "A couple of the machines rumble as you search around for Bean."

        m "Beaaaan~?"
        m "Are you hiding in here?"

        b "{size=-10}Prrp.{/size}"

        m "Bean?"

        "You spot a pile of orange fur snuggled up in someone's laundry basket."

        show bean at char_center

        "Bean is belly up snoring away in some freshly laundered bedsheets. Truly a cat that got the cream… sheets."

        m "Excuse me, sir."

        b "Prrrp?"

        m "Sorry to disturb your slumber but *someone* is very worried about you."

        "Bean sighs and stretches and begins to snore again."

        m "Right."

        "You scoop Bean up in your arms. He's too lazy to fight back and flops around instead of resisting. Truly orange cat behaviour."

        hide bean with dissolve

        jump foundbean

    else:

        m "Beaaaan~?"
        m "Are you hiding in here?"

        "A couple of the machines rumble as you search around for Bean."

        "No sneaky cat napping in any baskets or piles of laundry."

        m "Not here, it seems…"

        jump beaninbuilding

label beaninapartment:
scene bg pc apartment at bg_fit 
    if checked_balcony and checked_bedroom:
        "You've checked everywhere in your apartment… Bean must not be here."
        jump beansearch

    m "There's no way he managed to sneak in here right? I only popped out a couple times to do some laundry."

    "Where do you check?"

    menu:

        "Check balcony" if not checked_balcony:
            $ checked_balcony = True
            jump beanbalcony

        "Check bedroom" if not checked_bedroom:
            $ checked_bedroom = True
            jump beanbedroom

label beanbalcony:

    if bean_location == "balcony":

        $ bean_escape = "window"

        m "I will eat my shoe if he's on the balcony."

        "You open the balcony door and a flash of orange streaks across your apartment."

        b "{size=+10}MROWWW!!!{/size}"

        show bean at char_center

        "A very spooked Bean hides under your coffee table."

        m "Oh, buddy!"

        "You shut the balcony door."

        m "...guess I'm eating a shoe…"

        m "How the hell did you get out there?!"

        b "merp"

        "You lean down onto the floor to meet him at his level."

        m "You okay? That must've been scary."

        "Bean emerges from under the table."

        m "Let's get you back home."

        hide bean with dissolve

        jump foundbean

    else:

        m "I will eat my shoe if he's on the balcony."

        "You open the balcony door and peer out and around."

        m "No sign of him here… and I *don't* have to eat a shoe. Double win?"

        jump beaninapartment

label beanbedroom:

    if bean_location == "bedroom":

        $ bean_escape = "door"

        "You flick on your bedroom light to see if Bean has somehow made his way into your apartment."

        show bean at char_center

        "Right in the middle is a very content, but now rudely awakened, orange blob of fur."

        b "Mrow?"

        "Bean folds his face into his paws trying to block out the light and grunts."

        m "Ohhh you little stinker."

        "You then spot a shredded box next to him on the bed."

        m "You really do have a penchant for cardboard eh, Bean?"

        m "C'mon, let's get you back home."

        "Luckily, as an orange cat Bean offers little resistance to being scooped up by a relative stranger."

        hide bean with dissolve

        jump foundbean

    else:

        "You flick on your bedroom light to see if Bean has somehow made his way into your apartment."

        "Looking around the room you see nothing out of place beyond your usual clutter."

        m "Phew… if he'd have been in here the whole time I would have been a *little* surprised."

        jump beaninapartment

label foundbean:

    "You make your way up to Lynda's apartment with Bean in your arms and knock on her door."

scene bg lynda apartment at bg_fit
    m "Guess who~?"

    show lynda sad at char_center

    "Lynda opens the door - she's clearly been crying."

    show lynda laugh at char_center

    l "BEAN!!!!"

    show bean at char_center

    "She grabs him from you and showers him in kisses."

    l "You stupid, sweet, dumb, silly, beautiful cat!!!"

    show lynda sad at char_center

    "She holds him out at arms length and scolds him. Bean blinks out of sync."

    show lynda annoyed at char_center

    l "How did you get {i}out{/i}?!"

    l "Ugh who cares, I'm just glad you're back home."

    "Bean jumps from Lynda's arms and struts around the apartment."

    hide bean with dissolve

    jump beanhome

label gameoverbeanend:

scene pc apartment at bg_fit

    "SOMETIME LATER"

    if GamingOn or TVOn:

        "You blink and your eyes feel as dry as the Sahara."

        m "Oof. Maybe I should take a break."

        "You stand up and stretch - a few things pop - and you realise it's dark out."

    elif Baking:

        "You put away the last batch of cookies into a container."

        m "Ahh, procrasti-baking… My favourite pastime."

        m "Now I just need to figure out what to do with all these cookies… I hadn't thought that bit through."

        "You stretch - a few things pop - and you realise it's dark out."

    m "I wonder if Lynda's found Bean…"

    "You decide to go upstairs and check in on Lynda."

    "You knock on her door, and there's a brief pause before she opens it."

    scene lynda apartment at bg_fit

    show lynda neutral at char_center

    l "Oh, hey [player_name]."

    m "Hey, I just wanted to check if you found Bean?"

    "Lynda sighs with a light chuckle."

    l "Yeah, I did in the end. It took a good couple hours of searching. He decided he'd curl up in Jasper's laundry basket in the laundry room. Little shit. He looked at me like I was disturbing him with my snotty tears."

    m "That's good! Well, not the snotty tears but, finding Bean."

    show lynda unsure at char_center

    l "Yeah - still don't know how he got out though."

    jump beanhome

label beanhome:

    menu:

        "You can always leave out food and something that smells like you.":

            m "I've read before that leaving out food and something that smells like home helps guide them back."

            show lynda neutral at char_center

            l "Oh, that's good to know. Hopefully he won't be breaking out again anytime soon."

            show bean at char_left

            b "Meow."

            l "Yeah, you."

            hide bean with dissolve

            "You both chuckle and bid each other good night."

            hide lynda neutral

            jump beanconvinceend


        "Maybe a collar would be good in case he does it again?":

            $ HelpLynda -= 1

            m "I mean, he doesn't have a collar, that's something you should probably look into getting for him."

            show lynda annoyed at char_center

            l "Yeah, do you have a cat?"

            m "No…"

            l "Then you don't know the struggle of putting anything on them. It is like wrestling a coat onto a toddler."

            m "Ah, gotcha."

            show bean at char_left

            b "Mrowww."

            "Bean flomps near the doorway."

            l "You and I are *not* friends right now, mister."

            b "Purrrmeow."

            "You both chuckle while Bean rolls around."

            l "I gotta be up early so, night [player_name]."

            m "Night!"

            hide bean with dissolve

            hide lynda annoyed

            jump beanconvinceend


        "Want me to look around and see if I can spot anything?":

            $ HelpLynda += 1

            m "I could check and see where he maybe got out?"

            show lynda unsure at char_center

            l "Honestly, sure, I cannot for the life of me figure out how."

            "You head into Lynda's apartment."

            "Bean and Maple stalk you as you move around, looking for any signs of escape."

            hide lynda unsure

            if AttentionSkill >= 2:

                if bean_escape == "door":

                    "After a scan of the apartment, you can't see any evidence of cat mischievousness. You turn to let Lynda know when you spot the door is ajar."

                    m "Uh, Lynda?"

                    show lynda neutral at char_center

                    l "Yeah?"

                    m "Did you mean to leave the door open?"

                    show lynda sad at char_center

                    l "What?!"

                    "She strolls over and goes to shut and latch it."

                    "It pops open."

                    show lynda annoyed at char_center

                    l "Oh, you're kidding me."

                    "She tries again."

                    "It pops open."

                    "Frustration builds on her face."

                    jump lyndabeanconvince1

                elif bean_escape == "window":

                    "After a scan of the apartment, you can't see any evidence of cat mischievousness. You turn to let Lynda know when you spot a missing chunk of window screen in one of the windows."

                    m "Uh, Lynda?"

                    show lynda neutral at char_center

                    l "Yeah?"

                    m "Has that always had a, uh, Bean sized hole in it?"

                    l "You're {i}kidding{/i}."

                    "Lynda moves over to investigate."

                    show lynda annoyed at char_center

                    l "Urgh! This was the loose panel I messaged the damn management about weeks ago!!"

                    l "Great, now I have a HOLE in my WINDOW MESH."

                    jump lyndabeanconvince2

            else:

                if bean_escape == "door":

                    "After peering around the apartment, you're unable to find where Bean got out."

                    show lynda unsure at char_center

                    l "Any luck?"

                    m "No… sorry, I thought I could help with that at least."

                    l "Ah, it's okay."

                    m "Hope your presentation goes okay tomorrow."

                    show lynda laugh at char_center

                    l "Thanks [player_name]."

                    hide lynda laugh

                    "You roll out and Lynda shuts the door behind you."

                    "It pops back open."

                    m "Yeah?"

                    show lynda neutral at char_center

                    l "Hmm? I didn't say anythi- why is this open?"

                    "She goes to shut it again. *click* it creaks ajar."

                    show lynda_annoyed at char_center

                    l "Oh, you're kidding me."

                    "She tries again."

                    "And again."

                    "It won't shut."

                    "Frustration builds on her face."

                    jump lyndabeanconvince1

                elif bean_escape == "window":

                    "After peering around the apartment, you're unable to find where Bean got out."

                    show lynda neutral at char_center

                    l "Any luck?"

                    m "No… sorry, I thought I could help with that at least."

                    l "Ah, it's okay."

                    m "Hope your presentation goes okay tomorrow."

                    l "Thanks [player_name]."

                    "As you turn to leave a gust of wind blows through Lynda's apartment."

                    show lynda unsure at char_center

                    l "Oh my, I must have left a window open!"

                    "She saunters over and stops."

                    l "Oh for- I know how Bean got out…"

                    show lynda annoyed at char_center

                    "Lynda points to a missing mesh panel in the window pane."

                    l "Urgh! This was the loose panel I messaged the damn management about weeks ago!!"

                    l "Great, now I have a HOLE in my WINDOW MESH."

                    jump lyndabeanconvince2

label lyndabeanconvince1:

    "A door that won't lock is a pretty convincing argument for Lynda to join the association…"

    menu:
        "Convince Lynda":
            
            m "That's not good."

            m "This is why I think we really should start a tenancy association. There are clearly issues around the whole building."

            # -------------------------
            # POSITIVE RELATIONSHIP
            # -------------------------
            if lynda_rating >= 5:

                if lynda_convince >= 2:

                    $ lynda_convince +=2

                    show lynda neutral at char_center

                    "Lynda faffs with the door latch."

                    l "Y'know, the argument is kinda making itself at this point."

                    "The latch pops out properly."

                    show lynda laugh at char_center

                    l "Ah-HA. Fixed it."

                    show lynda neutral at char_center

                    l "But seriously, I am still considering it. I am just not sure what I could contribute to it, honestly."

                    m "It's more about numbers than anything. To show enough of us care and will fight."

                    l "I hear you."

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    l "I think I'm getting a handle on some of the jargon and acronyms."

                    show lynda unsure at char_center

                    l "I think…"

                    l "I've got pages of notes so…"

                    show lynda laugh at char_center

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    hide lynda laugh

                    jump beanconvincegood


                elif lynda_convince == 1:

                    $ lynda_convince += 1

                    show lynda neutral at char_center

                    "Lynda faffs with the door latch."

                    l "I know, I know, I'm just so busy. I don't think I have time right now."

                    m "It doesn't have to be right now. It'll take a little time to be official anyway."

                    show lynda unsure at char_center

                    l "Oh, fair point."

                    l "Let me think some more on it."

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    show lynda laugh at char_center

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    hide lynda laugh

                    jump beanconvincegood


                else:

                    $ lynda_convince += 2
                    
                    "Lynda faffs with the door latch."

                    show lynda annoyed at char_center

                    l "Last time you brought this up it annoyed the hell out of me… but I am starting to see your point."

                    show lynda neutral at char_center

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    hide lynda neutral

                    jump beanconvincegood


            # -------------------------
            # NEUTRAL RELATIONSHIP
            # -------------------------
            elif lynda_rating >= 3:

                if lynda_convince >= 2:

                    show lynda unsure at char_center

                    l "I hear you, I hear you. I just need things to settle at work and then we can talk, 'kay?"

                    l "Anyway, I gotta crack on with some more work now that Bean's secured."

                    show lynda neutral at char_center

                    m "Yeah, of course. Night, Lynda!"

                    $ lynda_convince += 1

                    hide lynda neutral

                    jump beanconvinceneut


                elif lynda_convince == 1:

                    show lynda annoyed at char_center

                    l "Yeah, I just don't know about timing right now, but we can talk about it another time, 'kay?"

                    l "Anyway, I gotta crack on with some more work now that Bean's secured."

                    m "Yeah, of course. Night, Lynda!"

                    hide lynda annoyed 

                    $ lynda_convince += 1

                    jump beanconvinceneut


                else:

                    "Lynda sighs."

                    show lynda unsure at char_center

                    l "I can understand where you're coming from."

                    show lynda annoyed at char_center

                    l "More than last time."

                    show lynda neutral at char_center

                    m "Eheh… sorry."

                    l "We can talk about it some other time."

                    l "For now, I gotta figure out how to sort this out and then get back to prepping for tomorrow."

                    m "Yeah, of course. Night Lynda!"

                    hide lynda neutral

                    $ lynda_convince += 1

                    jump beanconvinceneut


            # -------------------------
            # NEGATIVE RELATIONSHIP
            # -------------------------
            else:

                if lynda_convince >= 2:

                    show lynda annoyed at char_center

                    l "You know, I got where you were coming from before, but this really isn't going to make a difference."

                    l "Respectfully, I love that you have the free time to deal with this, I just don't."

                    l "I have too much on to be thinking about this right now."

                    l "Speaking of which, I need to get on with my prep work for tomorrow."

                    m "Yeah, no, I'll head out."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


                elif lynda_convince == 1:

                    show lynda annoyed at char_center

                    l "While I understand your ambition, between the sink and now Bean escaping, I'm starting to get very over this apartment complex in general."

                    "Lynda sighs deeply."

                    l "I gotta get on with some things."

                    m "Yeah, no, I'll head out."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


                else:

                    show lynda annoyed at char_center

                    l "Oh my GOD [player_name], will you let it be? Can't you see, once again, this is not the time?"

                    l "I am up to my eyeballs in work things, trying to learn everything I can in prep for every meeting."

                    l "Joining a tenancy association is the LOWEST thing on my priority list."

                    l "So, no, thank you."

                    m "Yeah, no, I'll head out."
                    m "Sorry."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


        "Don't push it":
            m "…Maybe another time."
            jump beanconvinceneut

label lyndabeanconvince2:

    "A loose mesh and now window… hole? is a pretty convincing argument for Lynda to join the association…"

    menu:
        "Convince Lynda":

            m "That's not good."
            m "This is why I think we really should start a tenancy association. There are clearly issues around the whole building."

            # -------------------------
            # POSITIVE RELATIONSHIP
            # -------------------------
            if lynda_rating >= 5:

                if lynda_convince >= 2:

                    "Lynda faffs with the window."

                    show lynda unsure at char_center

                    l "Y'know, the argument is kinda making itself at this point."

                    l "But seriously, I am still considering it. I am just not sure what I could contribute to it, honestly."

                    m "It's more about numbers than anything. To show enough of us care and will fight."

                    l "I hear you."

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    show lynda neutral at char_center

                    l "I think I'm getting a handle on some of the jargon and acronyms."

                    l "I think…"

                    l "I've got pages of notes so…"

                    show lynda laugh at char_center

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    hide lynda laugh

                    $ lynda_convince += 2

                    jump beanconvincegood


                elif lynda_convince == 1:

                    "Lynda faffs with the window."

                    show lynda neutral at char_center

                    l "I know, I know, I'm just so busy. I don't think I have time right now."

                    m "It doesn't have to be right now. It'll take a little time to be official anyway."

                    show lynda unsure at char_center

                    l "Oh, fair point."

                    l "Let me think some more on it."

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    hide lynda unsure

                    $ lynda_convince += 2

                    jump beanconvincegood


                else:

                    "Lynda faffs with the window."

                    show lynda neutral

                    l "Last time you brought this up it annoyed the hell out of me… but I am starting to see your point."

                    l "For now, I gotta get back to researching for my meeting tomorrow."

                    l "Anyway, good night!"

                    m "Night, Lynda!"

                    $ lynda_convince += 2

                    jump beanconvincegood


            # -------------------------
            # NEUTRAL RELATIONSHIP
            # -------------------------
            elif lynda_rating >= 3:

                if lynda_convince >= 2:

                    show lynda neutral at char_center

                    l "I hear you, I hear you. I just need things to settle at work and then we can talk, 'kay?"

                    l "Anyway, I gotta crack on with some more work now that Bean's secured."

                    m "Yeah, of course. Night, Lynda!"

                    hide lynda neutral

                    $ lynda_convince += 1

                    jump beanconvinceneut


                elif lynda_convince == 1:
                    show lynda unsure at char_center

                    l "Yeah, I just don't know about timing right now, but we can talk about it another time, 'kay?"

                    l "Anyway, I gotta crack on with some more work now that Bean's secured."

                    m "Yeah, of course. Night, Lynda!"

                    hide lynda unsure

                    $ lynda_convince += 1

                    jump beanconvinceneut


                else:

                    "Lynda sighs."

                    show lynda unsure at char_center

                    l "I can understand where you're coming from."

                    l "More than last time."

                    m "Eheh… sorry."

                    l "We can talk about it some other time."

                    show lynda neutral at char_center

                    l "For now, I gotta figure out how to sort this out and then get back to prepping for tomorrow."

                    m "Yeah, of course. Night Lynda!"

                    hide lynda neutral

                    $ lynda_convince += 1

                    jump beanconvinceneut


            # -------------------------
            # NEGATIVE RELATIONSHIP
            # -------------------------
            else:

                if lynda_convince >= 2:

                    show lynda annoyed at char_center

                    l "You know, I got where you were coming from before, but this really isn't going to make a difference."

                    l "Respectfully, I love that you have the free time to deal with this, I just don't."

                    l "I have too much on to be thinking about this right now."

                    l "Speaking of which, I need to get on with my prep work for tomorrow."

                    m "Yeah, no, I'll head out."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


                elif lynda_convince == 1:

                    show lynda annoyed at char_center

                    l "While I understand your ambition, between the sink and now Bean escaping, I'm starting to get very over this apartment complex in general."

                    "Lynda sighs deeply."

                    l "I gotta get on with some things."

                    m "Yeah, no, I'll head out."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


                else:

                    show lynda annoyed at char_center

                    l "Oh my GOD [player_name], will you let it be? Can't you see, once again, this is not the time?"

                    l "I am up to my eyeballs in work things, trying to learn everything I can in prep for every meeting."

                    l "Joining a tenancy association is the LOWEST thing on my priority list."

                    l "So, no, thank you."

                    m "Yeah, no, I'll head out."
                    m "Sorry."

                    l "I'll see you 'round, [player_name]."

                    hide lynda annoyed

                    jump beanconvincebad


        "Don't push it":
            m "…Maybe another time."
            jump beanconvinceneut

label beanconvincegood:

    scene pc apartment at bg_fit

    "You head back downstairs. You're making progress with Lynda, you can feel it."

    m "Though hopefully less cat and sink issues for now…"

    "Time to settle in for the night."

    jump beanconvinceend


label beanconvinceneut:

    scene pc apartment at bg_fit

    "You head back downstairs. Maybe you can still convince Lynda. She didn't seem uninterested."

    "Time to settle in for the night."

    jump beanconvinceend


label beanconvincebad:
    scene pc apartment at bg_fit

    "You head back downstairs."

    m "...well, that was rough. Lynda seemed particularly annoyed at me."

    m "I hope she still wants to go out like we planned."

    "Time to settle in for the night."

    jump beanconvinceend


label beanconvinceend:

    jump lyndainteraction4check
