label lyndainteraction4check:

    if lynda_rating <= 0:
        jump lyndanoshow
    else:
        jump lyndainteraction4


label lyndanoshow:
scene bg pc apartment at bg_fit
    "Another day rolls by. It is a crisp fall morning, and the sunlight cascades upon your windowsi-"

    "Oh, that's kinda dusty."

    "You run your finger over the windowsill."

    m "Oh, ew."
    m "I should probably clean today."
    m "Good way to kill time before hanging with Lynda later."

    "You set out to make breakfast and your source of caffeine for the morning. Then, the Cleaning Game Plan."

    if TidySkill == 1:

        m "Okay, first dusting, then vacuum and mop. Next, wash the bedding, and clean the bathroom while the laundry is on."

        "Your phone pings."

        m "Oh, it's Lynda."

        l "Hi [player_name]. Sorry… something's come up and I can't hang out like we planned.. Lynda."

        "You stare at the text, deciding what to respond."

        menu:
            "Be disappointed":
                m "Awh. That's a bummer. I was looking forward to it… Guess it's a cleaning and couch day today."
                jump lyndanoshowend

            "Be understanding":
                m "All good, it happens! Hope all is okay."
                jump lyndanoshowend

            "Be annoyed":
                $ lynda_rating -= 1
                m "Oh. Okay. I wish you'd have let me know a little sooner?"
                jump lyndanoshowend

    else:

        m "Hmm…"
        "You gaze around the apartment."
        m "I have no idea where to start."

        "Your phone pings."

        m "Oh, it's Lynda."

        l "Hi [player_name]. Sorry… something's come up and I can't hang out like we planned.."

        "You stare at the text, deciding what to respond."

        menu:
            "Be disappointed":
                m "Awh. That's a bummer. I was looking forward to it… Guess it's a couch day today."
                jump lyndanoshowend

            "Be understanding":
                m "All good, it happens! Hope all is okay?"
                jump lyndanoshowend

            "Be annoyed":
                $ lynda_rating -= 1
                m "Oh. Okay. I wish you'd have let me know a little sooner?"
                jump lyndanoshowend


label lyndanoshowend:

    "You meander around the apartment cleaning for the next couple of hours."

    "Another ping from your phone. It's an email with a coupon. You check out your text to Lynda."

    m "She left me on read?"
    m "...rude."
    m "Or is this an older person thing?"
    m "..."
    m "It's still rude."

    "You put your phone away and focus back on cleaning, wondering what caused such a last-minute cancellation from Lynda."

    jump lyndaevent3

label lyndainteraction4:

    if hangout_location == "bar":
        jump lyndabartime

    elif hangout_location == "park":
        jump lyndaparktime

    elif hangout_location == "cafe":
        jump lyndacafetime

##BAR HANG ##

label lyndabartime:
scene bg bar at bg_fit
    "You arrive at the bar where you agreed to meet Lynda for a drink."

    "She is already sitting at the bar with a glass of wine."

    show lynda laugh at char_center

    l "[player_name]! Over here!"
    "She waves at you."

    l "Come, come, grab a seat."

    "She pats the barstool next to her and you sit down."

    show lynda neutral at char_center

    if drink_choice == "wine":

        l "I hope its alright, I ordered you a glass too."

        "Lynda points to the freshly poured glass of wine."

        m "Oh, thanks!"

        "You take a sip. Lynda has good taste in wines, clearly, as it goes down *smooth*."

    else:

        l "I wasn't sure what you'd like so I'll let you order for yourself."

        m "All good!"

        "The bartender saunters over to take your order."

        menu:
            "A beer":
                m "I'll take a beer, please."
                m "Something light."
                "The bartender pours you an amber beer."
                $ Alcohol = True
                jump lyndabar1

            "A glass of wine":
                m "Same as hers, thanks."
                "The bartender pours a glass."
                $ Alcohol = True
                jump lyndabar1

            "A mocktail":
                m "Oh, I'll take a mocktail, please."
                $ Alcohol = False
                jump lyndabar1

            "A glass of water":
                m "Just a water, thanks."
                l "Really?"
                m "Yeah."
                $ Alcohol = False
                jump lyndabar1

label lyndabar1:

    "Lynda sighs wistfully after taking a sip of her wine."

    show lynda neutral at char_center

    l "I appreciate this invite out. I don't think I realised how much I've missed doing things that aren't just *work*."
    l "Or rotting on my couch."
    l "While thinking about work."

    "Lynda raises her glass."

    show lynda laugh at char_center

    l "Cheers!"
    m "Cheers!"

    show lynda neutral at char_center

    menu:
        "Slam the drink":
            "You grasp the glass, throw your head back and open your throat, sending it back."

            if Alcohol:

                "It burns ever so slightly, and you signal the bartender for another."

                show lynda laugh at char_center

                l "So it's that kinda drinking session?"

                "Lynda smiles at the bartender and taps her wine glass lightly."

                l "Hi - I'll take a bottle of this then, please."

                jump lyndadrank1

            else:

                "How hydrating."

                "You signal the bartender for another."

                show lynda laugh at char_center

                l "Thirsty, huh?"

                jump lyndabar2

        "Drink it normally":
            "You take a healthy sip and place the drink back down."
            jump lyndabar2

label lyndadrank1:

    show lynda neutral at char_center

    $ drunk_level += 1

    l "I didn't take you for a chugger."

    m "Nah, I just like to do that with my first drink, means I spend less for the rest of the night, hahaha."

    "Lynda raises an eyebrow."

    show lynda unsure at char_center

    l "It's certainly a choice."

    l "I'm not one to shy away from a good night of drinks, but be warned, I have a strong constitution and a work from home day tomorrow so…"

    show lynda neutral at char_center

    "The bartender places your next drink in front of you."

    menu:
        "Slam this one too":
            $ drunk_level += 1

            "You grab the glass once more and neck it."

            show lynda laugh at char_center

            l "Alright, now I gotta catch up!"

            "Lynda slams her glass of wine and grimaces."

            show lynda annoyed at char_center

            l "bleugh… I wouldn't have got the nicer wine if this was how we were going to drink."

            show lynda neutral at char_center

            jump lyndadrank2

        "Maybe don't?":

            show lynda neutral at char_center
            "You decide to take this one slower. Lynda looks like she's willing to compete with you. Maybe it is best not to encourage that."

            jump lyndadrank2

label lyndadrank2:

    if drunk_level == 2:

        show lynda laugh at char_center
        l "Oooh, shall we get some shots?"

        menu:
            "Yes":
                m "Abso-LUTELY!"
                show lynda neutral at char_center
                "Lynda flags down the bartender and orders a couple shots for each of you."

                "You both slam them down with a clink of your glasses."

                $ drunk_level += 2

                if drunk_level >= 3:
                    jump lyndadrunkbar2
                else:
                    jump lyndabar2

            "Yes and LOTS":
                m "Abso-LUTELY!"
                show lynda neutral at char_center
                "Lynda flags down the bartender and orders a couple shots for each of you."

                "You both slam them down with a clink of your glasses."

                $ drunk_level += 4

                if drunk_level >= 3:
                    jump lyndadrunkbar2
                else:
                    jump lyndabar2

            "NOOO":
                m "Maybe let's not escalate *that* quickly."
                show lynda wink at char_center
                l "Coward."
                show lynda neutral at char_center
                if drunk_level >= 3:
                    jump lyndadrunkbar2
                else:
                    jump lyndabar2

    else:
        jump lyndabar2

label lyndabar2:
    show lynda neutral at char_center
    m "How are things going?"

    l "Well, you know, work is busy as usual."

    l "I'm prepping for my partner Anna to come visit also!"

    m "That's fun! Has she been to visit yet?"

    show lynda laugh at char_center

    l "No, not yet, she's been busy with her own work with an art collective. I'm excited to show her around town and have her finally see the place and not just virtually."

    m "Wait, how long have you been apart and not seen each other?"

    show lynda neutral at char_center

    l "Oh! I still travel back to our home every month or so. I think Bean and Maple would lose it if they didn't see her for long periods of time."

    l "Though wrangling them into the car and giving them their 'chill out' pill leaves something to be desired."

    l "But they love their other mama, so who am I to deny them?"

    m "Especially when they're so cute."

    l "Even when one of them escapes like an ungrateful asshole."

    m "I just know he's snoring on your couch right now as we speak."

    l "Oh, absolutely, look-"

    "Lynda pulls out her phone and opens a pet camera."

    show lynda laugh at char_center

    l "Bean, Maple~"

    b "mrow?"
    t "mewww~"

    "You both burst into giggles."

    l "I'll just shoot them some treats and they'll be happy."

    show lynda neutral at char_center

    menu:
        "You seem to be getting the hang of tech things!":

            m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

            show lynda laugh at char_center

            "Lynda flaps her hand at you."

            l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

            show lynda neutral at char_center

            l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

            m "Look at you, having opinions on *technology*."

            l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought. 'You've gone to the dark side, darling.' She's ridiculous."

            jump lyndabar3


        "Those cameras can be hacked, you know.":

            $ HelpLynda -= 1

            m "You know, those cameras are easily hacked these days."

            show lynda sad at char_center

            l "What?!"

            m "Yeah, I've seen videos of them being hacked."

            show lynda annoyed at char_center

            l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

            l "And me fighting with an exploding sink."

            l "Hmm, I could charge for that level of entertainment."

            show lynda neutral at char_center

            jump lyndabar3


        "Look at those faces, I can't.":

            "The two cats scatter and chase down the dispensed treats."

            show lynda laugh at char_center

            m "I can't even with them, they're so cute."

            show lynda unsure at char_center

            l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

            m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

            "Lynda elbows you playfully."

            show lynda neutral at char_center

            l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Maple gained 2lbs because I didn't realise the setting was giving her double portions."

            jump lyndabar3

label lyndadrunkbar2:
    show lynda laugh at char_center
    m "[say_drunk('How are things going?')]"

    l "[say_drunk('Well, you know, work is busy as usual.')]"

    l "[say_drunk('I am prepping for my partner Anna to come visit also!')]"

    m "[say_drunk('That is fun! Has she been to visit yet?')]"

    l "[say_drunk('No, not yet, she has been busy with her own work with an art collective.')]"

    l "[say_drunk('I am excited to show her around town and have her finally see the place.')]"

    m "[say_drunk('Wait, how long have you been apart?')]"

    l "[say_drunk('Oh! I still travel back home every month or so.')]"

    l "[say_drunk('I think Bean and Maple would lose it otherwise.')]"

    l "[say_drunk('Wrangling them into the car is... a lot.')]"

    m "[say_drunk('Especially when they are so cute.')]"

    l "[say_drunk('Even when one of them escapes like an ungrateful asshole.')]"

    m "[say_drunk('He is probably snoring right now.')]"

    l "[say_drunk('Oh, absolutely, look-')]"

    "Lynda pulls out her phone and opens a pet camera."

    l "[say_drunk('Bean, Maple~')]"

    b "mrow?"
    t "mewww~"

    "You both burst into giggles."

    l "[say_drunk('I will just give them treats.')]"

    menu:
        "You seem to be getting the hang of tech things!":
            jump lyndadrunkbar3

        "Those cameras can be hacked, you know.":
            $ HelpLynda -= 1
            jump lyndadrunkbar3

        "Look at those faces, I can't.":
            jump lyndadrunkbar3

label lyndadrunkbar3:
show lynda laugh at char_center
    if lynda_rating >= 4:
        jump lyndaconfession

    "[say_drunk('You both continue talking for a while.')]"

    l "[say_drunk('This has been fun... but I should go.')]"

    l "[say_drunk('I am not used to being out on a school night.')]"

    "Lynda flags down the bartender."

    l "[say_drunk('This is on me... do not argue.')]"

    m "[say_drunk('But-')]"

    l "[say_drunk('Nope.')]"

    "She taps her card."

    l "[say_drunk('Let us do this again sometime?')]"

    m "[say_drunk('Yeah... yeah that sounds good.')]"

    "You both grab your coats and head out."

    jump lyndagoodend4

label lyndabar3:

    if lynda_rating >= 4:
        jump lyndaconfession

    else:
        show lynda neutral at char_center
        "You both continue to share anecdotes and small talk over the next couple of hours."

        l "Well, this has been fun, [player_name], but I should probably get going. I'm not used to being out on a school night as it were, and I'm an early bedtime kinda person."

        "Lynda flags down the bartender and produces her card."

        show lynda annoyed at char_center

        l "This is on me, don't try and fight me on it."

        m "But-"

        l "Nope."

        "She taps her card."

        show lynda laugh at char_center

        l "This was really lovely, let's do it again sometime?"

        m "Sure!"

        "You both grab your coats and head out into the evening."

        hide lynda laugh 

        jump lyndagoodend4


## PARK HANG ##

label lyndaparktime:
scene bg park at bg_fit
    "You arrive at the park, picnic basket in hand (well, a tote bag with a pithy catchphrase on it - the contemporary picnic basket), and look out for a good spot."

    "Luckily, even though there's a chill in the air, the sun is beaming across the park."

    m "Okayyy, where to set up?"

    menu:
        "A spot near the pond":
            jump lyndapond

        "A spot near some trees":
            jump lyndatrees

        "A spot in the gazebo":
            $ lynda_rating += 1
            $ Gazebo = True
            jump lyndagazebo

label lyndapond:

    "You make your way over to the pond. Now that summer has passed, you don't have to worry too much about mosquitoes or that funky pond smell."

    "Some ducks wade across the water. It's quite tranquil."

    m "Perfect!"

    "You lay out a tartan blanket and set up the food on it."

    show lynda laugh at char_center

    l "Hey!"

    m "Oh, hey!"

    show lynda neutral at char_center

    "Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses too."

    show lynda unsure at char_center

    l "Oh god, are we sitting on the ground? I'm going to have to do my physio later."

    m "Sorry, I thought being by the pond was nice."

    show lynda neutral at char_center

    l "It's cute!"

    l "The ducks will feast well off of any crumbs left behind."

    jump lyndapark1

label lyndatrees:

    "There's a picturesque spot near some trees. Some leaves are floating off of them, but their vibrant colours make for a lovely canopy over a picnic."

    "You wander over and set up next to one of the trees. You lay out a tartan blanket and start to set food up on it."

    show lynda laugh at char_center

    l "Hey!"

    m "Oh, hey!"

    show lynda neutral at char_center

    "Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses, too."

    l "Oh god, are we sitting on the ground? I'm going to have to do my physio later."

    m "My bad! I just love being around the trees this time of year."

    l "No bother, it's pretty."

    jump lyndapark1

label lyndagazebo:

    m "Ooh, the gazebo is empty. And there are no events on, it seems."

    "You stroll over to the gazebo and climb its brief steps. From here, there's a wonderful view of the park, and *chairs*."

    "There's even a folded table left behind from a previous event."

    "You throw your tartan picnic blanket over the table and set up the picnic."

    show lynda laugh at char_center

    l "Hey!"

    m "Oh, hey!"
    
    show lynda neutral at char_center

    "Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses, too."

    l "Oh, see now *this* is my kind of picnic. It's dining al fresco!"

    l "I don't have to worry about bugs in my food."

    m "I'm glad you like it."

    jump lyndapark1

label lyndapark1:

    "You both take in the fresh air while you graze on fruits, cheese, crackers, and crudites."

    if Gazebo:
        show lynda laugh
        l "You know, I was not super enthralled by the idea of a park picnic, but now… now I see the appeal."
        l "And this is good spinach dip."
    else:
        l "Okay, yeah, this is a good spinach dip."

    m "You wouldn't believe how much it cost to make."

    show lynda sad at char_center

    l "What?! It's spinach and artichoke, no?"

    m "If I showed you the receipt, you'd have an aneurysm."

    show lynda neutral at char_center

    "There's a brief pause."

    m "How are things going?"

    l "Well, you know, work is busy as usual."

    l "I'm prepping for my partner Anna to come visit also!"

    show lynda laugh at char_center

    m "That's fun! Has she been to visit yet?"

    l "No, not yet, she's been busy with her own work with an art collective."

    l "I'm excited to show her around town and have her finally see the place and not just virtually."

    show lynda neutral at char_center

    m "Wait, how long have you been apart and not seen each other?"

    l "Oh! I still travel back to our home every month or so."

    show lynda sad at char_center

    l "I think Bean and Maple would lose it if they didn't see her for long periods of time."

    l "Though wrangling them into the car and giving them their 'chill out' pill leaves something to be desired."

    show lynda laugh at char_center

    l "But they love their other mama, so who am I to deny them?"

    m "Especially when they're so cute."

    show lynda annoyed at char_center

    l "Even when one of them escapes like an ungrateful asshole."

    show lynda neutral at char_center

    m "I just know he's snoring on your couch right now as we speak."

    l "Oh, absolutely, look-"

    "Lynda pulls out her phone and opens a pet camera."

    l "Bean, Maple~"

    b "mrow?"
    t "mewww~"

    show lynda laugh at char_center

    "You both burst into giggles."

    l "I'll just shoot them some treats and they'll be happy."

    show lynda neutral at char_center

    menu:
        "You seem to be getting the hang of tech things!":
            jump techpark

        "Those cameras can be hacked, you know.":
            $ HelpLynda -= 1
            jump camerahackpark

        "Look at those faces, I can't.":
            jump cutefacespark

label techpark:
    m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

    show lynda unsure at char_center

    "Lynda flaps her hand at you."

    l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

    l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

    m "Look at you, having opinions on *technology*."

    show lynda annoyed at char_center

    l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought."

    show lynda laugh at char_center

    l "'You've gone to the dark side, darling.' She's ridiculous."
    jump lyndapark2
label camerahackpark:
    m "You know, those cameras are easily hacked these days."
    show lynda annoyed at char_center
    l "What?!"

    m "Yeah, I've seen videos of them being hacked."
    show lynda unsure at char_center
    l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

    l "And me fighting with an exploding sink."

    l "Hmm, I could charge for that level of entertainment."
    show lynda neutral at char_center
    jump lyndapark2
label cutefacespark:
    show lynda neutral at char_center
    "The two cats scatter and chase down the dispensed treats."

    m "I can't even with them, they're so cute."

    l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

    m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

    "Lynda elbows you playfully."

    l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Maple gained 2lbs because I didn't realise the setting was giving her double portions."

    "{i}}beep boop{/i}"
    show lynda annoyed at char_center
    l "Oh my god, you can even hear that damn beeping through the camera."
    show lynda neutral at char_center

    jump lyndapark2

label lyndapark2:

    if lynda_rating >= 4:
        jump lyndaconfession

    show lynda neutral at char_center

    "You both continue to share anecdotes and small talk over the next couple of hours."

    l "Well, this has been fun, [player_name], but I should probably get going."

    l "Thank you for making such a lovely spread. I am *not* going to need dinner tonight, that's for sure."

    l "Next time, I'll take you to a place I like."

    m "A park?"

    show lynda laugh at char_center

    l "Noooo, haha - it's a place with a nice dining patio. Best of both worlds."

    "Lynda helps you pack up the picnic debris."

    "You walk back to the building together, taking in the fall sunshine."

    show lynda neutral at char_center

    l "See you around, [player_name]."

    m "Likewise!"

    hide lynda neutral

    jump lyndagoodend4

## CAFE HANG ##

label lyndacafetime:
scene bg cafe at bg_fit
    "You arrive at the neighbourhood cafe."

    "The walls are littered with event posters, business cards, and some local artist prints to purchase."

    "The smell of freshly ground coffee beans wafts by the counter."

    "There is a large selection of sweet and savoury pastries stored in a display section."

    "It all looks good."
    
    show lynda laugh at char_center

    l "[player_name]! Over here!"

    "You spot Lynda seated at a small table and make your way over."

    show lynda neutral at char_center

    "She already has a drink in hand."

    "You order yourself..."

    menu:
        "A latte":
            $ DrinkChoice = "latte"

            m "I'll take a latte, please."

            "The barista nods and starts steaming milk."

            "A moment later, a warm latte is placed in front of you, foam art and all."

            jump lyndacafe1


        "A black coffee":
            $ DrinkChoice = "coffee"

            m "Just a black coffee, please."

            "The barista pours a fresh cup."

            "The aroma is wonderful."

            jump lyndacafe1


        "Just a tea":
            $ DrinkChoice = "tea"

            m "I'll just have a tea, please."

            "The barista gestures to cute list of different options."

            "You pick something that sounds vaguely calming."

            jump lyndacafe1

label lyndacafe1:

    show lynda neutral at char_center

    "You join Lynda at the table"

    l "Hey, [player_name]. Thanks for the invite, this is nice."

    m "Of course! How are things going?"

    l "Well, you know, work is busy as usual."

    show lynda laugh at char_center

    l "I'm prepping for my partner Anna to come visit also!"

    m "That's fun! Has she been to visit yet?"

    l "No, not yet, she's been busy with her own work with an art collective."

    l "I'm excited to show her around town and have her finally see the place and not just virtually."

    show lynda neutral at char_center

    m "Wait, how long have you been apart and not seen each other?"

    l "Oh! I still travel back to our home every month or so."

    show lynda sad at char_center

    l "I think Bean and Maple would lose it if they didn't see her for long periods of time."

    l "Though wrangling them into the car and giving them their 'chill out' pill leaves something to be desired."

    show lynda unsure at char_center

    l "But they love their other mama, so who am I to deny them?"

    m "Especially when they're so cute."

    show lynda annoyed at at char_center

    l "Even when one of them escapes like an ungrateful asshole."

    m "I just know he's snoring on your couch right now as we speak."

    show lynda neutral at char_center

    l "Oh, absolutely, look-"

    "Lynda pulls out her phone and opens a pet camera."

    l "Bean, Maple~"

    b "mrow?"
    t "mewww~"

    "You both burst into giggles."

    show lynda laugh at char_center

    l "I'll just shoot them some treats and they'll be happy."

    show lynda neutral at char_center

    menu:
        "You seem to be getting the hang of tech things!":
            jump techcafe

        "Those cameras can be hacked, you know.":
            $ HelpLynda -= 1
            jump camerahack

        "Look at those faces, I can't.":
            jump cutefaces

label techcafe:
    m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

    show lynda unsure at at char_center

    "Lynda flaps her hand at you."

    l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

    show lynda neutral at char_center

    l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

    m "Look at you, having opinions on *technology*."

    l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought."

    l "'You've gone to the dark side, darling.' She's ridiculous."
    jump lyndacafe3
label camerahack:
    m "You know, those cameras are easily hacked these days."

    show lynda sad at char_center

    l "What?!"

    m "Yeah, I've seen videos of them being hacked."

    l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

    show lynda neutral at char_center

    l "And me fighting with an exploding sink."

    l "Hmm, I could charge for that level of entertainment."
    jump lyndacafe3
label cutefaces:
    show lynda neutral
    
    "The two cats scatter and chase down the dispensed treats."

    m "I can't even with them, they're so cute."

    l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

    m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

    "Lynda elbows you playfully."

    l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Maple gained 2lbs because I didn't realise the setting was giving her double portions."

    "{i}beep boop{/i}"

    show lynda annoyed at char_center

    l "Oh my god, you can even hear that damn beeping through the camera."

    show lynda neutral at char_center

    jump lyndacafe3

label lyndacafe3:

    if lynda_rating >= 4:
        jump lyndaconfession

    show lynda neutral at char_center

    "You both continue to share anecdotes and small talk over the next couple of hours."

    l "Well, this has been fun, [player_name], but I should probably get going."

    m "So soon?"

    l "Yeah, I have to do some more prep for a client meeting next week."

    l "I've bought a stack of books and I plan to get through them!"

    m "Of course, of course. I understand."

    l "Thanks for this though."

    l "I think I'd forgotten how important it is to get out and do things."

    "You both put on your coats and stack your mugs and plates."

    "You head out into the afternoon together."

    jump lyndagoodend4

## CONFESSION TIME

label lyndaconfession:

    $ lynda_confession = True

    show lynda neutral at char_center

    l "You know, we've been getting along since you moved in, and you've offered some kindness for my mid-life crisis, haha."

    l "I feel like I should be honest with you over this whole tenancy association thing."

    show lynda sad at char_center

    l "I might be moving…"

    m "Oh."

    show lynda unsure at char_center

    l "I know… I just know you've been working hard to get folks to sign up to the association, and I don't want you to waste your time with me if I'm not even going to be here."

    l "My partner and I are looking at properties and have been for a while. I just didn't have the heart to tell you."

    show lynda sad at char_center

    l "I'm sorry…"

    menu:
        "Press her":
            jump lyndaconfess_press

        "Nod understandably":
            jump lyndaconfess_understand

        "Express disappointment":
            jump lyndaconfess_disappoint

label lyndaconfess_press:

    m "How long have you be intending to leave?"

    show lynda unsure at char_center

    l "Uhh, a little bit."

    m "How long?"

    l "A little before you moved in…"

    m "You've known it the whole time and only now you're telling me?"

    show lynda sad at char_center

    l "[player_name] I-"

    m "Were you ever going to sign it?"

    show lynda annoyed at char_center

    l "Look, a lot of things have been up in the air and so I just don't know if it would be right for me to commit to something that I might not even be here for."

    m "But I need your help! I was relying on you to help me get folks interested!"

    show lynda sad at char_center

    l "I don't think I can."

    m "Why not? You work in marketing, you can sell any idea!"

    show lynda annoyed at char_center

    l "This is asking for more than peddling a product, [player_name], this is people's time and energy against a clearly disinterested entity."

    m "You won't even try?"

    show lynda sad at char_center

    l "What if I'm not enough to convince them? Then what?"

    m "Then why even do it for work?!"

    l "..."

    l "..."

    l "...I understand you're upset. But you know I've been struggling with things at work. So this-"

    show lynda annoyed at char_center

    "She gestures between the two of you."

    show lynda sad at char_center

    l "-was a low blow from someone I considered a friend."

    hide lynda sad with dissolve

    "Lynda leaves."

    "You sit for a moment with your thoughts rushing around your mind."

    "Why tell you now? Why does she have to leave? Why doesn't she think she could help? Who else can you convince to help you do this? Is this a waste of time?"

    "Lynda's 'what if I'm not good enough' echoes in your mind."

    menu:
        "Go after Lynda":
            jump lyndaconfess_chase

        "Go home":
            $ lynda_rating -= 2
            jump lyndabadend4

label lyndaconfess_chase:

    "You gather your things and head out after Lynda."

    m "She won't have gone too far."

    "You look down the street to see if you can spot her. A little ways down, you see Lynda leaning against a wall, staring out."

    "Slowly, you approach."

    show lynda annoyed at char_center

    m "So, uh, that sucked."

    "Lynda nods, not looking at you."

    m "I didn't mean to… I shouldn't have…"

    m "I'm sorry."

    show lynda sad at char_center

    l "I have enough pressure on myself [player_name]. I didn't expect more to come from you."

    l "I have this thing where, if I can't do something perfectly, I just don't *want* to do it."

    l "I've had it all my life."

    show lynda unsure at char_center

    l "So, I prepare. I study. I read everything I can, I practice, I slap on the lipstick and eyeshadow war mask and just-"

    "She gestures forward."

    l "Give it 150/%."

    show lynda sad at char_center

    l "Deep down, I still feel like I've lucked my way into everything."

    l "When a new challenge comes along, honestly, I'm paralysed. And this tenancy committee is so outside of what I know and I feel like I'm barely keeping up at work as it is."

    m "Lynda…"

    "You see tears form in her eyes."

    show lynda annoyed at char_center

    l "Ugh, I told myself I needed to stop crying in front of you."

    show lynda sad at char_center

    "You rest a hand on her arm."

    m "I didn't mean to add pressure on you. Let's just forget about the association for now, okay?"

    m "Let's just take a walk back home?"

    "Lynda sniffs and wipes her tears."

    m "I know there's a good ice cream place along the way!"

    show lynda neutral at char_center

    l "That sounds nice."

    "You link arms."

    l "You're a good one [player_name]."

    show lynda laugh at char_center

    l "And ice cream is on me for being an emotional wreck again, hahaha."

    m "Sounds like a plan."

    "You head off as the streetlights begin to flick on."

    hide lynda laugh with dissolve

    jump lyndagoodend4

label lyndaconfess_understand:

    "You nod slowly, taking in the information."

    show lynda sad at char_center

    l "Oh god, you're mad at me."

    m "No, I can understand. I mean, it isn't ideal, but I can't tell you that you can't leave."

    show lynda neutral at char_center

    "Lynda's whole physique relaxes."

    show lynda sad at char_center

    l "Ugh, I've felt awful not telling you."

    m "How long have you been planning to move?"

    l "..."

    show lynda unsure at char_center

    l "Not long after you'd moved in. The sink explosion was not the first issue I'd encountered in the building. The laundry machines have destroyed some of my favourite sweaters, the bin room is just disgusting, and the fan for the oven has the suction power of a geriatric mouse."

    l "This was always meant to be temporary while I got settled into my new role."

    l "And now my partner is thinking of moving out here to join me. We're in a position to sell our old place to purchase something here. So, yeah…"

    show lynda neutral at char_center

    m "And you're really not interested in joining the association?"

    l "It feels unfair to you to say I'm in, when in fact, I might not still be here in a couple months, you know?"

    m "Yeah… I hear you."

    l "And other folks in the building will still join your cause!"

    l "You can be very persuasive."

    show lynda wink at char_center

    m "Hah, thanks."

    show lynda neutral at char_center

    "Lynda pats your arm."

    l "I am sorry I didn't tell you."

    m "S'okay."

    l "Wanna swing by an ice cream place and get a cone? My treat for being a bad friend."

    m "Now who's being persuasive?"

    "You both chuckle as you pack up and head out to a dairy delight together."

    hide lynda neutral with dissolve

    jump lyndagoodend4

label lyndaconfess_disappoint:

    m "You're leaving?"

    show lynda unsure at char_center

    l "Well, nothing specific is confirmed yet, but there's definitely momentum towards it. And it doesn't mean we can't hang out! This has been really lovely and it's only really the first time we've hung out outside of the laundry room haha."

    m "Hey, I like our laundry room hangs. Don't knock them."

    show lynda neutral at char_center

    l "My point is, I know a lot of the time you've spent with me has been to convince me to join the association. But, it is kinda nice that a friendship has come from it."

    m "You make it sound like I was only nice to you to get you to join!"

    show lynda sad at char_center

    l "No! Not at all!!"

    l "I'm flubbing this majorly."

    l "I know you're disappointed. I'm sorry."

    "You let out a hefty sigh."

    show lynda neutral at char_center

    m "I just don't know where I stand with the others joining the association right now, and I felt you were a sure thing at this point."

    l "Again, I'm sorry."

    m "No, it's fiiiine."

    l "Wanna swing by an ice cream place and get a cone? My treat to ease my guilt and your disappointment?"

    m "I want sprinkles on my disappointment ice cream."
    
    show lynda laugh at char_center

    l "Ahaha, done!"

    show lynda neutral at char_center

    "You both chuckle as you pack up and head out to a dairy delight together."

    hide lynda neutral with dissolve

    jump lyndagoodend4

label lyndagoodend4:
scene bg pc apartment at bg_fit

    "You close your apartment door behind you and kick off your shoes. With a solid leap, you plant yourself on the couch."

    "It seems getting Lynda to join the association is going well. Hopefully, she'll jump on board officially soon. You want to get this association up and running sooner rather than later."

    "It's been lovely getting to know Lynda."

    "Even if there's a sadness behind her eyes at times."

    menu:
        "I think she just needs to trust her instincts.":
            $ lynda_reflection = "instincts"

            m "Lynda really has so much more figured out than she realises. I wonder why she just can't see that…"

        "I think she should be kinder to herself.":
            $ lynda_reflection = "kinder"

            m "We're all our own worst enemies. Lynda seems particularly hard on herself at times. Like nothing she does meets her own expectations. I wonder what her co-workers think of her? She seemed to think she lucked into her job, but she does so much for it."

        "I think she could benefit from more time away from work.":
            $ lynda_reflection = "work"

            m "Lynda seems to work 9-5 and then 5-9 on things. I get she's in some kind of senior role, but the amount of time she puts into prepping for things seems a little unhealthy… I'm surprised she said yes to spending time together."

    "You fiddle with a tassel on one of the couch throws."

    "..."

    "Are you like Lynda sometimes?"

    menu:
        "Yes":
            $ imposter = True

        "No":
            $ imposter = False

    jump lyndaevent3

label lyndabadend4:
scene bg pc apartment at bg_fit
    "You close your apartment door behind you and kick off your shoes. With a solid leap, you plant yourself on the couch."

    "It might be time to call it quits on trying to persuade Lynda to join the association. Nothing you've done has swayed her, regardless of exploding sinks and cat escapades."

    "Lynda has a lot going on underneath the surface, it seems."

    menu:
        "I think she just needs to trust her instincts.":
            $ lynda_reflection = "instincts"

            m "Lynda really has so much more figured out than she realises. I wonder why she just can't see that…"

        "I think she should be kinder to herself.":
            $ lynda_reflection = "kinder"

            m "We're all our own worst enemies. Lynda seems particularly hard on herself at times. Like nothing she does meets her own expectations. I wonder what her co-workers think of her? She seemed to think she lucked into her job, but she does so much for it."

        "I think she could benefit from more time away from work.":
            $ lynda_reflection = "work"

            m "Lynda seems to work 9-5 and then 5-9 on things. I get she's in some kind of senior role, but the amount of time she puts into prepping for things seems a little unhealthy… I'm surprised she said yes to spending time together."

    "You fiddle with a tassel on one of the couch throws."

    "..."

    "Are you like Lynda sometimes?"

    menu:
        "Yes":
            $ imposter = True

        "No":
            $ imposter = False
    
    "This is the end of the current game demo build. More on the way!"
    jump lyndaevent3

    