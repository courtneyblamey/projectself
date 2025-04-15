**label lyndainteraction3**

"After scrolling social media for the morning, you roll over to spot your mountain of clothes bursting out of your laundry basket."

M "I should probably deal with that."

"You get up and make a coffee to sip."


## **CHOICE**



1. Sort the laundry into delicates, whites, and normal.
2. INTO THE BASKET YOU GO.


### Sort the laundry

**set $DiligentLaundry = True **

**+1 to $TidySkill **

"You dutifully separate out your laundry into piles."

M "No bleeding colours or shrinking sweaters on my watch!"

"You pile some of it into the basket and drop it by the front door."

**jump changesearch**


### INTO THE BASKET

**set $ChaosLaundry = True**

**-1 to $TidySkill**

"You wrap your arms around the laundry mountain, and like a claw machine, decant it into your laundry basket."

M "Y e e t"

**jump changesearch**

**label changesearch**

"You search around the apartment for some change."

M "I know I saw a pile of quarters somewhere…"


## **CHOICE**



1. Check the bowl by the door.
2. Check your coat pockets.

(set up menu here to allow player to check both)


### Bowl

"You shuffle around some mail and loyalty cards to find a smattering of coins."

**+5 to $Money**


### Coat

"You fish around in some coat pockets and find a stash of coins."

**+5 to $Money**

**label laundryquest**

"You grab the basket and head downstairs to the laundry room."

(change background)

"As you reach the door you notice someone filling the dryer."

L "Oh, hey &lt;playername>, sorry I'm just finishing this load and then I'm out of here."

"Lynda subtly dabs her eye with a sock and throws it into the drum. She slots her change in as you dump your laundry into the machine."

**if $ChaosLaundry = True**

L "Wow, you just throw it all together."

"You shrug."

M "I think separating laundry is a conspiracy made up by detergent companies to make us run more loads."

"You watch Lynda think for a moment."

L "Huh."

**jump lyndaokay**

**Else**

**+1 to $lynda_rating**

L "Ah, you're a laundry sorter are you?"

M "I want my stuff to stay soft!"

L "Not judging! Admiring, really."

**Jump lyndaokay**

**label lyndaokay**

"You notice Lynda's eyes are tinged pink."

M "Hey, are you okay?"

L "What? Me?"

"She takes a deep breath."

L "I was hoping to have my silly feelings contained by this age."

"Lynda looks at you and tears brim in her eyes."

L "Long distance is just really tough sometimes."

L "Don't get me wrong, it was worth it, the money is relatively good, and she'll probably move out here once I know how good a fit this role is, but…"

"She trails off, picking at a loose corner of a 'INSERT COINS HERE' sticker on the machine."

M "You miss her."

L "Yeah. And sometimes, I'm not sure I should even be trying to make this job work, I had a good one back home, but this one seemed so good for developing my skillset and-"

**if $TechSkill = 0**

L "Anyway, I am going to go back upstairs while this dries and have a nice glass of wine."

**jump invitelynda**

**else **

L "Sorry, I've already blabbed to you about all this before."


## **CHOICE**



1. You can blab more, it's okay.
2. I get it, it's tough.


### Blab more

**+2 to $lynda_rating**

M "You can blab more, I don't mind."

L "You're sweet, but I won't subject you to all of-"

"She gestures to her wet eyes."

L "-this."

M "Really, sometimes it's good to vent."

"Lynda sighs again and wipes away some smudged eyeliner."

L "I am one of the very lucky people on this planet who has found their person."

L "And I *never* subscribed to that idea until I met her."

L "Cliche, I know."

L "She has wholeheartedly supported my ambitions, and I've supported hers, don't get me wrong. Just, this last endeavour has me wondering if I made the right choice."


## 
    **CHOICE**



1. Why's that?
2. Maybe I've pried enough

### 
    Why's that?


    M "What has you wondering?"


    If $lynda_rating is x


    L "I just don't think I fit in at the office at all. Like we talked about the other day, I hear all these acronyms and everyone nodding in the room like it is something I should know, but I really don't."


    M "Do you mean with the people or like, the work itself?"


    "Lynda stares at the rumbling dryer."


    L "That is a good question…"


    "She looks lost in thought."


    **jump invitelynda**


    **Else**


    "Lynda picks at some loose skin on her lip, lost in thought."


    **jump invitelynda**


### 
    Pried enough


    "Maybe that's enough questions for this evening."


    **jump invitelynda**



### It's tough

**+1 to $lynda_rating**

M "I get it. It's tough."

L "Yeah, yeah it is."

"She wipes away a slight smear of eyeliner."

**jump invitelynda**

**label invitelynda**

"Maybe I should invite her out to do something?"

**(if $lynda_rating above X)**


## **CHOICE**



1. Offer a coffee hang
2. Offer a picnic in the park
3. **Offer drinks at a local bar (this is Lynda's favoured spot)**


### Coffee hang

**+1 to $lynda_rating**

M "Do you wanna grab a coffee sometime?"

"Lynda smiles at you."

L "You know what? That would be nice."

L "And Antony owes me one anyway for saving his dried laundry from being thrown onto the floor."

M "Okay! Then let's plan a time and we'll grab some."

**jump endlyndainteraction2**


### Park picnic

**-1 to $lynda_rating**

M "Are you a fan of picnics?"

L "Uhhh…"

L "Sure!"

M "Okay! I make a mean spinach dip. We can find a time and go to the park nearby?"

L "That sounds lovely."

**jump endlyndainteraction2**


### Local bar

**+2 to $lynda_rating**

M "Do you want to grab a casual drink sometime?"

"Lynda's eyes light up."

L "Oh, I'd love that."

L "I haven't had a drink outside of my place in a hot minute."

L "I've forgotten what it is like to be overcharged for an ounce of liquor."

M "Then we shall correct this and refresh your memory so that you remember why you drink at home instead!"

L "Perfect!"

L "I'll let you know when works for me and vice versa, 'kay?"

M "Sure!"

**jump endlyndainteraction2**

**label endlyndainteraction2**

"Lynda wiggles her fingers goodbye to you as she heads out of the laundry room. You don't see her again when you go to move over your own laundry.


    if $lynda_rating > X


    "You realise that the dryer is already running with your clothes in it. Lynda must have moved them over when she collected hers."


    if $ChaosLaundry = True


    "You decide to scroll on your phone for the last five minutes of the cycle and collect them, heading back upstairs for the night."


    Else


    "You load your next batch of clothes and head back upstairs. Eventually completing your laundry just in time for a reasonable bedtime."


    if $lynda_rating &lt; X and $ChaosLaundry = True


    "You throw the load into the dryer and return upstairs while it finishes the dry cycle. You grab it once it is done and watch some TV while folding it before heading off to bed."


    If lynda_rating &lt; X and $DiligentLaundry = True


    "You move over the current load and prep the next one, which you do one more time for the delicates, before bringing the last load upstairs. You lay out your delicates to dry, realising you should have done them first, and fold the remaining laundry while watching TV. Eventually, you sort it all away and flomp into bed for the night."

**jump lyndainteraction4**
