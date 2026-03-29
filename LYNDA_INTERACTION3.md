**label lyndainteraction3**

"After scrolling social media for the morning, you roll over to spot your mountain of clothes bursting out of your laundry basket."

m "I should probably deal with that."

"You get up and make a coffee to sip."

"You open your laptop to check your emails while you sip and realise you left the design software open with an example tenant association poster."

m "Right, gotta make one at some point."

"Something falls off of your laundry basket."

m "Okay, you first."


## **MENU**



1. Sort the laundry into delicates, whites, and normal.
2. INTO THE BASKET YOU GO.


### Sort the laundry

**set $ DiligentLaundry = True **

**$ TidySkill +=  1**

"You dutifully separate out your laundry into piles."

m "No bleeding colours or shrinking sweaters on my watch!"

"You pile some of it into the basket and drop it by the front door."

**jump changesearch**


### INTO THE BASKET

**set $ ChaosLaundry = True**

**-1 to $ TidySkill**

"You wrap your arms around the laundry mountain, and like a claw machine, decant it into your laundry basket."

m "Y e e t"

**jump changesearch**

**label changesearch**

"You search around the apartment for some change."

m "I know I saw a pile of quarters somewhere…"


## **MENU**



1. Check the bowl by the door.
2. Check your coat pockets.

(set up menu here to allow player to check both)


### Bowl

"You shuffle around some mail and loyalty cards to find a smattering of coins."

**+5 to $ Money**


### Coat

"You fish around in some coat pockets and find a stash of coins."

**+5 to $ Money**

**label laundryquest**

"You grab the basket and head downstairs to the laundry room."

(change background)

"As you reach the door you notice someone filling the dryer."

l "Oh, hey &lt;playername>, sorry I'm just finishing this load and then I'm out of here."

"Lynda subtly dabs her eye with a sock and throws it into the drum. She slots her change in as you dump your laundry into the machine."

**if $ ChaosLaundry = True**

l "Wow, you just throw it all together."

"You shrug."

m "I think separating laundry is a conspiracy made up by detergent companies to make us run more loads."

"You watch Lynda think for a moment."

l "Huh."

**jump lyndaokay**

**Else**

**+1 to $ lynda_rating**

**Jump lyndaokay**

**label lyndaokay**

"You notice Lynda's eyes are tinged pink."

m "Hey, are you okay?"

l "What? Me?"

"She takes a deep breath."

l "I was hoping to have my silly feelings contained by this age."

"Lynda looks at you and tears brim in her eyes."

l "Long distance is just really tough sometimes."

l "Don't get me wrong, it was worth it, the money is relatively good, and she'll probably move out here once I know how good a fit this role is, but…"

"She trails off, picking at a loose corner of a 'INSERT COINS HERE' sticker on the machine."

m "You miss her."

l "Yeah. And sometimes, I'm not sure I should even be trying to make this job work. I had a good one back home, but this one seemed so good for developing my skillset and-"

**if $ TechSkill = 0**

l  "Anyway, I am going to go back upstairs while this dries and have a nice glass of wine."

"*beep boop*"

"The electrical room beeps."

l "I really wish they could do something about that damn sound."

l "Sorry for the word vomit. Anna keeps saying I need to get out more to take my mind off of work but then I'm so busy with work stuff that I don't know when to take that time, y'know?"

**jump invitelynda**

**else **

l "Sorry, I've already blabbed to you about all this before."


## **MENU**



1. You can blab more, it's okay.
2. I get it, it's tough.


### Blab more

**+2 to $ lynda_rating**

**$ lynda_blab = "True"**

m "You can blab more, I don't mind."

l "You're sweet, but I won't subject you to all of-"

"She gestures to her wet eyes."

l "-this."

m "Really, sometimes it's good to vent."

"Lynda sighs again and wipes away some smudged eyeliner."

l "I am one of the very lucky people on this planet who has found their person."

l "And I *never* subscribed to that idea until I met her."

l "Cliche, I know."

l "She has wholeheartedly supported my ambitions, and I've supported hers, don't get me wrong. Just, this last endeavour has me wondering if I made the right choice."


## 
    **MENU**



1. Why's that?
2. Maybe I've pried enough

### 
    Why's that?


    m "What has you wondering?"


    If $ lynda_rating is x


    l "I just don't think I fit in at the office at all. Like we talked about the other day, I hear all these acronyms and everyone nodding in the room like it is something I should know, but I really don't."


    m "Do you mean with the people or like, the work itself?"


    "Lynda stares at the rumbling dryer."


    l "That is a good question…"


    "She looks lost in thought."


"Anna keeps saying I need to get out more, so that I'm not so cooped up and feeling like this."


    **jump invitelynda**


    **Else**


    "Lynda picks at some loose skin on her lip, lost in thought."

"Anna keeps saying I need to get out more, but I'm so busy with work stuff at the moment."


    **jump invitelynda**


### 
    Pried enough


    "Maybe that's enough questions for this evening."

"Anna keeps saying I need to get out more, but I'm so busy with work stuff at the moment."


    **jump invitelynda**


### It's tough

**+1 to $ lynda_rating**

**$ lynda_validate = "True"**

m "I get it. It's tough."

l "Yeah, yeah it is."

"She wipes away a slight smear of eyeliner."

"Anna keeps saying I need to get out more, but I'm so busy with work stuff at the moment."

**jump invitelynda**

**label invitelynda**

"Maybe I could suggest a hangout to help her feel less trapped at home?"

**(if $ lynda_rating above X)**


## **MENU**



1. Offer a coffee hang
2. Offer a picnic in the park
3. **Offer drinks at a local bar (this is Lynda's favoured spot)**


### Coffee hang

**+1 to $ lynda_rating**

m "Do you wanna grab a coffee sometime?"

"Lynda smiles at you."

l "You know what? That would be nice."

l "And Antony owes me one anyway for saving his dried laundry from being thrown onto the floor."

m "Okay! Then let's plan a time and we'll grab some."

**$ hangout_location = "cafe"**

**jump endlyndainteraction3**


### Park picnic

**-1 to $ lynda_rating**

m "Are you a fan of picnics?"

l "Uhhh…"

l "Sure!"

m "Okay! I make a mean spinach dip. We can find a time and go to the park nearby?"

l "That sounds… lovely."

**$ hangout_location = "picnic"**

**jump endlyndainteraction3**


### Local bar

**+2 to $ lynda_rating**

m "Do you want to grab a casual drink sometime?"

"Lynda's eyes light up."

l "Oh, I'd love that."

l "I haven't had a drink outside of my place in a hot minute."

l "I've forgotten what it is like to be overcharged for an ounce of liquor."

m "Then we shall correct this and refresh your memory so that you remember why you drink at home instead!"

l "Perfect!"

l "I'll let you know when works for me and vice versa, 'kay?"

m "Sure!"

**$ hangout_location = "bar"**

**jump endlyndainteraction3**

**label endlyndainteraction3**

"Lynda wiggles her fingers goodbye to you as she heads out of the laundry room."

"You head back upstairs yourself while your load runs and get to work making an info poster."

"When your alarm rings to move over your laundry you head back downstairs."


    if $ lynda_rating > X


    "You realise that the dryer is already running with your clothes in it. Lynda must have moved them over when she collected hers."


    if $ ChaosLaundry = True


    "You decide to scroll on your phone for the last five minutes of the cycle and collect them, heading back upstairs for the night."


    Else


    "You load your next batch of clothes and head back upstairs. Eventually completing your laundry just in time for a reasonable bedtime."


    if $ lynda_rating &lt; X and $ ChaosLaundry = True


    "You throw the load into the dryer and return upstairs while it finishes the dry cycle. You grab it once it is done and watch some TV while folding it before heading off to bed."


    If lynda_rating &lt; X and $ DiligentLaundry = True


    "You move over the current load and prep the next one, which you do one more time for the delicates, before bringing the last load upstairs. You lay out your delicates to dry, realising you should have done them first, and fold the remaining laundry while watching TV. Eventually, you sort it all away and flomp into bed for the night."

**jump lyndainteraction4**
