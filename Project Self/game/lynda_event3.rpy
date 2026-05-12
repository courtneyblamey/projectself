label lyndaevent3:
if lynda_rating <= 2:
    jump lyndaevent3bad
elif lynda_rating >= 5:
    jump lyndaevent3neut
elif lynda_rating >= 8:
    jump lyndaevent3good


# LOW RELATIONSHIP ENDING
label lyndaevent3bad:
    scene bg lobby at bg_fit
    with Dissolve(2.0)
    "A COUPLE WEEKS LATER"
    "On your way back in from a walk you spot a letter jutting out of your mailbox."
    m "Huh."
    "Upon unlocking it and large brown envelope falls out. It was crammed in poorly."
    "The envelope is not addressed to you, but to Lynda."
    m "Hmm. I'm not sure she wants to see me."
    m "I can just drop it off real quick and be gone."
    "You realise the envelope has the building company's logo on the top left-hand corner."
    m "Oh. Weird."
    "You head upstairs to deliver the letter."
    "As you approach, you hear another voice in Lynda's apartment and the smell of something good cooking."
    "{i}Knock knock knock.{/i}"
    "After a brief pause, someone you don't recognise opens the door."

    scene bg lynda apartment at bg_fit
    with dissolve

    show anna neutral at char_center
    a "Hello?"
    m "Oh, uh, hi! I have something for Lynda? It was put in my mailbox for some reason."
    show anna concern at char_center
    a "Lynda? One of your neighbours are here with some mail?"
    hide anna concern
    show anna neutral at char_left
    show lynda neutral at char_right
    l "Ah. Hey."
    l "Thank you for bringing it up, you could have just left it on the table downstairs."
    m "Oh, its no bother. Figured you might not want someone taking mail from the building company?"
    l "From the… oh!"
    "She takes the envelope from your hand."
    show lynda laugh at char_right
    l "This was what I was telling you about, love! They've got some options we can look through in their new buildings."
    show anna happy at char_left
    a "Ohhh, okay perfect, I'll wrap up dinner and we can check it out. Nice to meet you…?"
    show anna neutral at char_left
    m "[player_name]."
    a "Gotcha. Anna, by the way."
    "With a curt wave she heads back inside."
    hide anna neutral
    show lynda neutral at char_center
    "Lynda stands in the doorway tracing the edges of the envelope."
    l "Anything else?"

    menu:
        "Try to invite yourself in":
            jump invitein
        "Excuse yourself for the evening":
            jump excuseyourself

label invitein:
    "You subtly peer behind her to see an amazing spread of food."
    m "Oh, wow. Dinner looks good."
    show lynda wink at char_center
    l  "Haha, yeah, Anna is the chef of our duo. My aptitude lies in selecting from a food delivery app."
    show lynda neutral at char_center
    "..."
    show lynda unsure at char_center
    l  "Listen, [player_name], I'm just gonna come out and say it. I'm not going to be in the building much longer. Anna and I are making plans to buy somewhere and the building company offered a deal to buy one of their new condos."
    show lynda neutral at char_center
    l "So, I won't be joining your association."
    show lynda unsure at char_center
    l "Sorry."
    jump lyndabadendmenu

label excuseyourself:
    m "No, no. Just the mail."
    show lynda unsure at char_center
    l "Cool, well, thanks, [player_name]."
    m "I'll see you around?"
    show lynda neutral at char_center
    l "Ah, probably not. I'm gonna be moving at some point soon."
    m "Oh."
    show lynda annoyed at char_center
    l "Yeah, I complained enough to the company that they offered a deal to rent one of their newer places while Anna and I condo shop from their catalogue, so…"
    m "I see…"
    show lynda unsure at char_center
    l "Less Bean escapes! Yaaay"
    "She gives a half-hearted jazz hands."
    show lynda neutral at char_center
    jump lyndabadendmenu

label lyndabadendmenu:
    menu:
        "Be disappointed":
            "You stare down at the floor for a second, tempering yourself."
            m "I really thought you might come around eventually."
            show lynda annoyed at char_center
            l "Oh, [player_name], don't be like that. There are others in the building! I'm just a lost cause for this. I'd been planning this for a while and saying yes to the association meetings felt wrong."
            show lynda neutral at char_center
            m "I just thought with your management savvy you could have helped me manage the others."
            l "Oh, you're putting too much stock in my skills for that."
            a "Lynda?"
            show lynda annoyed at char_center
            l "Yep! Coming!"
            show lynda neutral at char_center
            l "I have to go, but… yeah, keep at it?"
            "She gives you a small wave and closes the door with a firm click."
            hide lynda neutral
            "You stand there for a moment absorbing the failure."
            m "fuck."
            jump gameendingbad

        "Be angry":
            m "Really?!"
            show lynda sad at char_center
            m "I helped you with your sink and figuring out how Bean got out!! You can't just join in the meantime until you move?"
            show  lynda annoyed at char_center
            l "Okay. First of all, I don't *owe* you anything, let me be very clear."
            show lynda unsure at char_center
            l "Second, you have overstepped in other ways with me that I have not loved."
            show lynda annoyed at char_center
            l "I might not always know what I'm doing, but I'm not totally incompetent you know."
            l "I was trying to be polite about it, but quite frankly, this is a lost cause. If you really hate it here so much, just move."
            show lynda annyed at char_left
            show anna concern at char_right
            a "Lynda?"
            "Anna appears behind her."
            l "They're just leaving, don't worry."
            l "Goodnight, [player_name]."
            "The door shuts firmly in your face."
            hide lynda annoyed
            hide anna concern
            scene bg black at bg_fit
            with dissolve
            menu:
                "Fuck this":
                    m "I'm over this. I can't convince anyone to sign up, its like no one cares or maybe {i}maybe{/i} they just aren't willing to spend the energy to care."
                    m "Screw all of this."
                    jump gameendingbad
                "Fuck her":
                    "You glower at the shut door and storm back downstairs."
                    m "Well, if she's gonna move out and leave the rest of us to deal with the stupid company…"
                    "You get into your apartment and crank the TV volume to max."
                    m "She can deal with this."
                    m "Hope it doesn't distract you from the APARTMENT SHOPPING."
                    "You flomp onto your bed, put on some headphones, and curl up under the blankets."
                    "A couple hours later, someone starts banging on your wall telling you to shut it off. You switch off the TV and curl back up in your pit of grump."
                    jump gameendingbad

        "Try to appeal":
            m "There's no way you might just join us in the interim?"
            show lynda annoyed at char_center
            l "[player_name], I am going to say this very clearly and only once."
            l "No."
            m "Nothing could persuade you?"
            show lynda unsure at char_center
            l "I am just not interested at this point. I have to do what is best for me, and it is not joining what I think is a lost cause - sorry."
            l "Maybe you'll get some others? But I really need you to drop this with me."
            show lynda neutral at char_center
            a "Lynda?"
            l "Yep, coming!"
            l "Good night, and good luck."
            hide lynda neutral
            "Lynda shuts the door."
            m "..."
            m "Well, shit."
            jump gameendingbad


label lyndaevent3neut:
    scene bg lobby at bg_fit
    with Dissolve(2.0)
    "A COUPLE WEEKS LATER"
    "On your way back in from a walk you spot a letter jutting out of your mailbox."
    m "Huh."
    "Upon unlocking it and large brown envelope falls out. It was crammed in poorly."
    "The envelope is not addressed to you, but to Lynda."
    "On the top left-hand corner is the building company's logo and slogan: for loving city living."
    m "Yeah, {i}sure{/i}."
    m "I should probably take this up to Lynda."
    "You arrive at her door and knock. There's sounds of cooking and laughter coming from inside."
    scene bg lynda apartment at bg_fit
    a "One second!"
    "An unfamiliar voice."
    show anna neutral at char_center
    a "Hi! Can I help you?"
    "A woman with a gentle smile and bubbly presence stands in the doorway."
    m "Sorry, I just have some mail for Lynda? It got put in my mailbox by accident."
    show anna happy at char_left
    a "Oh, how kind of you - Lynda!"
    show lynda neutral at char_center
    l "Hey, [player_name], what's up?"
    a "This is [player_name]! Nice to meet you."
    show anna neutral at char_left
    m "Likewise, you must be Anna?"
    show anna happy at char_left
    a "That I am!"
    l "Oh, is that for me?"
    show anna neutral at char_left
    "You reach out with the envelope and she takes it."
    show lynda laugh at char_right
    l "Ah… Thanks for bringing it up!"
    l "Would you like to come in for a drink or something?"
    m "Sure!"
    show lynda neutral at char_right
    "You head into her apartment, following her and Anna."
    if LyndaDrink:
        l "I remember from our tech escapades, [drinkchoice] right?"
        m "Yeah! Thanks."
        jump lyndaevent3drink
    else:
        l "What can I get you? I got wine, tea, water…"
    menu:
        "Wine":
            jump lyndaevent3drink
        "Tea":
            jump lyndaevent3drink
        "Water":
            jump lyndaevent3drink
    label lyndaevent3drink:
        "Lynda preps your drink and sets it on the table in front of you."
        if lynda_confession:
            show anna happy at char_left
            a "Ooh, the condo brochure?"
            "Anna looks to you."
            show anna neutral at char_left
            a "We still love print media in this house."
            show lynda wink at char_right
            l "That's the one."
            show lynda netural at char_right
            l "I told [player_name] about the move."
            show anna concern at char_left
            a "Sorry about the tenant association hit from Lynda leaving."
            m "No, I understand."
            show anna neutral at char_left
            l "Well, I wanted to tell you after going through the brochure with Anna, but, it doesn't feel right to leave you in a lurch. Especially since I am kindaaa the one who warned you about the building in the first place."
            l "So, while I am still planning to move, I will sign on for now, and help you corral some of the others onto the team."
            show lynda laugh at char_right
            m "You will?!"
            l "Yeah! Anna and I are both in agreement that I can probably encourage folks since I've been here a while, where you're new to the building, and so on."
            show anna happy at char_left
            a "Plus, we don't necessarily know how long it'll take to find a place and set it up."
            show lynda neutral at char_right
            show anna neutral at char_left
            l "Exactly. So, we've got some time!"
            m "This means a lot to me, thank you, Lynda."
            jump lyndasaysyes
        else:
            show anna concern at char_left
            a "So, what's this mysterious piece of mail?"
            l "Ohh, it's nothing, we can talk about it later."
            a "What did you get another parking ticket?"
            show lynda laugh at char_right
            l "That was one time!"
            show anna happy at char_left
            a "In my car!"
            "They both laugh and Lynda playfully taps Anna on the head with the envelope."
            a "Oh! Is it the condo listings?"
            show lynda annoyed at char_right
            l "ANNA."
            show anna annoyed at char_left
            a "What?!"
            "Lynda glances over at you sheepishly."
            m "Condo listings?"
            show anna concern at char_left
            a "Why do I feel like I've mistepped here?"
            l "Because you {i}have{/i} my love."
            show lynda neutral at char_right
            l "[player_name] has been trying to set up a tenants association to deal with the building issues."
            show anna happy at char_left
            a "Oh, that's so good of you!"
            l "I was one of those who signed up."
            show anna concern at char_left
            a "...Ah."
            show lynda sad at char_right
            l "And then didn't go to the first meeting."
            show anna annoyed at char_left
            a "Ahhh...."
            show lynda neutral at char_right
            show anna neutral at char_left
            m "You weren't the only one to be fair..."
            m "Wait, so you're leaving?"
            show lynda sad at char_right
            l "I'm sorry, [player_name], you've been so into getting it set up and I know I'm the first one you spoke to about it and I encouraged you and the whole time I've-"
            l "I am sorry."
            show anna concern at char_left
            a "Nothing is finalised, mind, we're just looking through some options."
            l "I do think it is a noble cause."
            show lynda neutral at char_right
            show anna neutral at char_left
            m "{i}Maybe I can make one final attempt to convince her even to help me until she leaves?{/i}"
            menu:
                "Appeal to her skills as a manager":
                    jump lyndamanager
                "Appeal to her being inconvenienced in the building":
                    jump lyndainconvenient
                "Appeal to your friendship":
                    jump lyndafriendship

label lyndamanger:
    m "I could really use your skills, even if it's just before you move, you don't even have to sign up. Just help me get some of the other folks on board."
    if lynda_convince >= 2: 
        m "You know you have that managerial magic that could really make a difference here."
        show lynda laugh at char_right
        "Lynda chuckles."
        l "Managerial magic??? I wouldn't go that far!"
        show anna happy at char_left
        a "They're right! I keep telling you that you're better than you admit!"
        l "The pair of you!"
        l "Okay, fine, I will help with some of the others, but I make no promises *and* I'm not joining the association. Hopefully, I can magic you some support."
        m "This means a lot to me, thank you, Lynda."
        show lynda neutral at char_right
        show anna neutral at char_left
        jump lyndasaysyes
    else:
        show lynda unsure at char_right
        l "I think you overestimate my skills in this regard [player_name]."
        l "I genuinely wish you the best of luck, but I'm just very done with this building in general. It's time to leave."
        jump lyndasaysno


label lyndainconvenient:
    m "You can't just join on for a short while? This building is such a nightmare, as you well know. Any help can make a difference. Who knows when someone else's sink will explode?"
    show lynda unsure at char_right
    l "Respectfully [player_name], that's why I'm leaving. I don't mean to sound blunt or uncaring, but I can't stay here in solidarity just to face more issues. I've already been here for over a year - I'm ready to be out of here."
    show lynda neutral at char_right
    jump lyndasaysno

label lyndafriendship:
    m "Could you join to help a friend in need? Before you go? Or at least help me corral the others into action?"
    if lynda_rating >= 6:
        show lynda sad at char_right
        l "We have become fast friends, haven't we?"
        show lynda unsure at char_right
        l "Okay, here's what we'll do. Before I leave, I'll help you with a couple of the folks in the building. I can't promise anything, but I will use my powers for good."
        m "Thank you!!"
        m "This means a lot, truly, thank you."
        show lynda neutral at char_right
        show anna neutral at char_left
        jump lyndasaysyes
    else: 
        show lynda unsure at char_right
        l "I'm sorry [player_name], I wish I could do more, but I think you're better off just chatting with the other folks in the building."
        show lynda neutral at char_right
        show anna neutral at char_left
        jump lyndasaysno


label lyndaevent3good:
    scene bg lobby at bg_fit
    with Dissolve(2.0)
    "A COUPLE WEEKS LATER"
    "On your way back in from a walk, you spot a letter jutting out of your mailbox."
    m "Huh."
    "Upon unlocking it and large brown envelope falls out. It was crammed in poorly."
    "The envelope is not addressed to you, but to Lynda."
    "On the top left-hand corner is the building company's logo and slogan: for loving city living."
    m "Yeah, sure."
    m "I should probably take this up to Lynda."
    "You arrive at her door and knock. There's sounds of cooking and laughter coming from inside."
    scene bg lynda apartment at bg_fit 
    with dissolve
    a "One second!"
    "An unfamiliar voice."
    show anna neutral at char_center
    a "Hi! Can I help you?"
    show anna happy at char_center
    a "Oh! You must be [player_name]!"
    m "Uh, yes! You must be Anna?"
    a "In the flesh! Come on in, come on in."
    "Anna ushers you inside."
    show anna happy at char_left
    a "Lynda! [player_name] is here!"
    show lynda laugh at char_right
    "Lynda emerges from her office."
    l "Hey! Didn't expect to see you today!"
    m "Yeah, sorry, I don't mean to interrupt, I just got mail for you in my mailbox, so I figured I'd bring it up."
    show lynda neutral at char_right
    show anna neutral at char_left
    "Lynda clocks the envelope and takes it from you."
    l "Ah! I know what this is."
    if lynda_confession:
        show anna happy at char_left
        a "Ooh, the condo brochure?"
        "Anna looks to you."
        show anna neutral at char_left
        a "We still love print media in this house."
        show lynda wink at char_right
        l "That's the one."
        show lynda netural at char_right
        l "I told [player_name] about the move."
        show anna concern at char_left
        a "Sorry about the tenant association hit from Lynda leaving."
        m "No, I understand."
        show anna neutral at char_left
        l "Well, I wanted to tell you after going through the brochure with Anna, but, it doesn't feel right to leave you in a lurch. Especially since I am kindaaa the one who warned you about the building in the first place."
        l "So, while I am still planning to move, I will sign on for now, and help you corral some of the others onto the team."
        show lynda laugh at char_right
        m "You will?!"
        l "Yeah! Anna and I are both in agreement that I can probably encourage folks since I've been here a while, where you're new to the building, and so on."
        show anna happy at char_left
        a "Plus, we don't necessarily know how long it'll take to find a place and set it up."
        show lynda neutral at char_right
        show anna neutral at char_left
        l "Exactly. So, we've got some time!"
        m "This means a lot to me, thank you, Lynda."
        jump lyndasaysyes
    else:
        show anna happy at char_left
        a "Ooh, the condo brochure!"
        m "{i} Condo brochure?{/i}"
        show anna concern at char_left
        show lynda annoyed at char_right
        l "Anna."
        "Anna side eyes Lynda."
        a "I... I'm gonna just..."
        hide anna concern with dissolve
        "Anna disappears back into the apartment."
        show lynda unsure at char_center
        l "Well, I {i}wanted{/i} to tell you {i}after{/i} going through the brochure with Anna, but, it doesn't feel right to leave you in a lurch. Especially since I am kindaaa the one who warned you about the building in the first place."
        l "Yes, this is a brochure for a new place. Yes, I'll be moving {i}but{/i}-"
        show lynda wink at char_center
        l "Not without attending the meetings before I leave."
        m "Really?!"
        show lynda laugh at char_center
        l "Yeah! Anna and I are both in agreement that I can probably encourage folks since I've been here a while, where you're new to the building, and so on."
        show anna happy at char_left
        show lynda neutral at char_right
        a "Plus, we don't necessarily know how long it'll take to find a place and set it up."
        show lynda annoyed at char_right
        "Lynda glares back playfully at Anna."
        show anna concern at char_left
        a "Eheh."
        show lynda neutral at char_right
        show anna neutral at char_left
        l "Exactly. So, we've got some time!"
        m "This means a lot to me, thank you, Lynda."
        jump lyndasaysyes

#######
# LYNDA SAYS NO
#######

label lyndasaysno:
    show lynda sad at char_right
    l "Again, I'm sorry [player_name]."
    m "No, no, it's okay, I do understand. It just…"
    show lynda neutral at char_right
    l "I know."
    l "I really do think other folks will join you. I just don't have the time or capacity to help you with it at this point."
    l "It really isn't personal."
    show anna concern at char_left
    a "Why don't you stay for dinner? It's the least we can do."
    menu:
        "Stay for dinner":
            jump staydinner
        "Politely decline":
            jump politeno

label staydinner:
show lynda neutral at char_right
show anna neutral at char_left
m "I won't turn down a free meal, and it already smells good!"
l "You don't even know. There's a reason I live off of takeout when she's not around."
"While Anna preps dinner, you all hang out in the kitchen, chatting about everything from favourite foods to funniest stories involving a suitcase."
"Anna serves an amazing pasta dish with accompanying salads and then homemade cookies and ice cream."
"At the point you think you're going to burst, Anna hands you a tupperware filled with leftovers to take home."
hide lynda neutral at char_right
hide anna neutral at char_left
scene bg pc apartment at bg_fit 
with dissolve
"You wish them a good night and head downstairs. A pang of sadness hits knowing you're down one point of support."
m "I'll just have to convince the others."
m "But for now, I digest all this food in a blanket pile."
hide bg pc apartment
with dissolve
jump gameendingneut

label politeno:
show lynda neutral at char_right
show anna neutral at char_left
m "Oh, I appreciate it, but I think I'm going to head home and finish some leftovers or they're going to spoil."
a "Sure, no worries!"
l "At least take one of the cookies Anna made earlier."
a "That I do insist on."
"Lynda bags you a couple cookies and walks you to the hallway."
m "See ya, Anna, nice to meet you!"
show anna happy at char_left
a "Likewise!"
hide anna happy with dissolve
"You step out of Lynda's apartment."
show lynda neutral at char_center
l "Hey."
show lynda sad at char_center
l "I do appreciate the kindness you've shown me over the last couple months. This isn't a reflection on that."
show lynda neutral at char_center
m "I know. But thank you."
"Lynda pats you on the shoulder and heads back into her apartment."
hide lynda neutral with dissolve
"You head downstairs with a pang of sadness."
scene bg pc apartment at bg_fit
with dissolve
m "Guess I'll need to convince some of the others."
"You get into your apartment, reheat your leftovers, and lock in on binge watching something."
hide bg pc apartment
with dissolve
jump gameendingneut


######
# LYNDA SAYS YES
######

label lyndasaysyes:
    show lynda unsure at char_right
    l "Anyway, enough shop talk, you wanna join us for dinner?"
    show anna happy at char_left
    show lynda neutral at char_right
    a "Oh, I insist you do."
    m "Guess I have no choice then!"
    "You all chatter over drinks while Anna makes dinner."
    "Anna serves an amazing pasta dish with accompanying salads and then homemade cookies and ice cream."
    "At the point you think you're going to burst, Anna hands you a tupperware filled with leftovers to take home."
    "You wish them a good night and head downstairs, feeling full of optimism - and food."
    hide bg lynda apartment
    with dissolve
    jump gameendinggood

