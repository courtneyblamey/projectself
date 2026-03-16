Note: no matter the $character_rating, these events will occur in sequence, but the rating entering the Event (plus any choice made that can bump the rating) will impact the outcome.

SINK EXPLODES


#### label startlyndaevent1

"You're settled on your couch for the evening scrolling through a streaming service for SOMETHING good to watch."


## **CHOICE**



1. While you totally scroll on your phone at the same time.
2. Your attention can handle one screen.


### Totally scroll

**set $AttentionSkill to 1**

**set $SinkTimer to 3**

"You select something mindless that fades into the background as you scroll through social media, also mindlessly." \
"Sometimes brain overload feels good."


## SCROLL



1. Scroll 


### SCROLL

"A cute video of a dog. Aww, he's chasing something in his sleep."

>scroll again

"How to make girl dinner actually nutritious."

"Why is everyone so obsessed with protein?"

>scroll again

"Did you know, that when you know, you know things?"

"Do I smell burnt toast?"

>scroll again

"You hearing thumping upstairs from Lynda's apartment."

"Oh, she must be home."

>scroll again

"Come with me to check out this cute new spot in the city."

"More thumping from upstairs."

"Silence."


## **CHOICE**



1. Continue scrolling
2. Pause scrolling and listen


### Continue scrolling

**set $SinkTimer to 5**

"You continue to scroll your feed."

>scroll again

"10 signs that your cat loves you! Has your cat ever slow blinked at you? That could mean-"

"A crash from upstairs."


### Pause scrolling and listen

**Set $SinkTimer to 4**

"You stop the video and listen."

"Muffled shouts"

"Less muffled shouts"

"You head upstairs to investigate."

**jump goupstairs**


#### **label goupstairs**

"As you round the corridor, you hear banging. Lynda's door is ajar, and a handful of swears echo down the hallway."

**jump enteraptsink**


## **CHOICE**



3. Continue scrolling
4. Stop scrolling and investigate


### Continue scrolling

**set $SinkTimer to 6**

"You continue to scroll."

"Whatever was on in the background ends and pulls up some recommendations."

"You select the next thing to watch and notice some water drops on the coffee table.

"You notice that something is dripping into the water drops."

"Something is dripping a LOT into the water drops."

"You look up to see that the water is coming from the ceiling."

m "Oh shit"

"You rush upstairs."

**jump goupstairspanic**


#### label goupstairspanic

"You skid around the corner to see Lynda's door open and run to it."

l "Ohhhhh noooooo! Stop!!!"

"Lynda sits in front of her sink, slinging towels under it to prevent the jettison of water from going any further."


## **CHOICE**



1. PANIC AS WELL $HandsonSkill to 1
2. Grab more towels to help! $HandsonSkill to 3
3. Dive under the sink. $HandsonSkill 5


### **PANIC AS WELL**

**set $HandsonSkill to 1**

**( $lynda_rating =-1)**

m "UH OH."

"Bean and Treacle scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

M "What do i do?!"

l "I don't know!!!"

l "It won't stop!!!"

"You move towards the sink, trying not to slip on the floor."

"Both you and Lynda desperately try to block the flow of water."

l "Oh my godddd."

l "There has to be a way to turn this off!!!"

"Lynda reaches in and fumbles at the back of the pipes."

l "Ah HA!"

"You watch her twist something. With a *clunk*, the water flow ebbs from a jet to a trickle."

"You both wipe the water off your faces and adjust yourselves."

m "Well, that sucked."

**jump investigatefaucet**


### TOWELS

**set $HandsonSkill to 3**

**$ lynda_rating = +1**

"Bean and Treacle scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

m "Where are some other towels?!"

l "In the bathroom!"

"You rush to grab more towels and sprint back to the kitchen."

"Lynda grabs one of the towels out of your hand."

l "WAIT NOT THIS ONE."

"She clutches a red towel with a cat chasing leaves embroidered on it."

l "...its decorative."

"She throws it away from the flood of water and pulls the other towels off of you to jam under the sink."

"You create a barrier out of the remaining towels to prevent the water from spreading further."

l "There has to be a way to turn this off!!!"

"Lynda reaches in and fumbles at the back of the pipes."

l "Ah HA!"

"You watch her twist something. With a *clunk*, the water flow ebbs from a jet to a trickle."

"You both wipe the water off your faces and adjust yourselves."

**jump investigate faucet**


### DIVE UNDER SINK

**set $HandsonSkill to 5**

**$ lynda_rating = +1**

m "Move!"

"Bean and Maple scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

if TechSkill = 1

"You dive under the sink, moving Lynda out of the way, and reach for the stop valve."

"With a creak, the jet of water finally ebbs to a trickle."

Else

$SinkTimer = +1

$lynda_rating = -1

"You dive under the sink."

m "I got this! Just keep the water from getting everywhere!"

"Water sprays you in the face."

"You reach in to try and figure out what is causing the leak."

"Water continues to spray you in the face."

"You realise that maybe… you don't got this."

"Lynda clocks you fumbling around."

l "Oh hell, now *you* move."

"Lynda pushes you out of the way and gets under the sink once more."

"You hear a *thunk* and the water finally ceases flowing across the kitchen."

"She emerges, equally as soaked as you."

l "I appreciate your enthusiasm to help."

m "Sorry…"

**jump investigatefaucet**


### Attention strong

**set $AttentionSkill to 5**

**set $SinkTimer to 1**

"You flick through some videos."

m "I'm pretty sure I've hit the end of all the content that ever existed."


## CHOICE



1. Give up and just pick something at random
2. Maybe a nature documentary?
3. Ooh, latest episode of a dating show


### SOMETHING RANDOM

"You give up scrolling and select the 'surprise me' button."

"The opening credits to a 90s romcom roll across the screen, and you settle in to watch something that probably hasn't aged well."

**jump upstairsnoise**


### NATURE

"You pick a nature doc and settle in to the gentle voiceover of David Attenborough." 

**jump upstairsnoise**


### DATING SHOW

m "Ooh I forgot there's a new episode of Attraction Isle."

"You tune in to your guilty pleasure."

**jump upstairsnoise**


#### label upstairsnoise

"You feel your eyes starting to drift shut when you hear some stomping upstairs."


## CHOICE 



1. Shrug it off and make some tea
2. Listen to check


### SHRUG IT OFF

**$ SinkTimer = +1**

"Lynda does love a one-woman dance party. You swear you can hear music. She might not have rhythm, but the woman loves to groove."

"You get up to make an herbal tea. In filling the kettle you notice the flow of water is off."

m "Huh, the water pressure's weird."

"Eventually, the kettle fills and you set it to boil."

"You collect a mug and select your tea when-"

"C R A S H"

"A loud noise from upstairs."

m "Uh oh."

**jump goupstairspanic**


### LISTEN TO CHECK

"Lynda is typically quite light on her feet."

"You pause your show to listen in."

l "*muffled* motherfuc-"

"More crashing."

**jump goupstairs**



* ~~Feel like you've finished all the content on streaming services~~
* ~~Hear a kerfuffle upstairs in Lynda's apartment~~
    * ~~Decide to brush it off and make some tea~~
        * ~~Tap isn't working/super low pressure.~~
        * ~~Hear shouting and running above~~
        * ~~Go upstairs~~
    * ~~Go upstairs ~~
        * ~~See the door open and hear banging~~
* Lynda's kitchen tap is spraying water everywhere
* Determine physical skill! $HandsonSkill
    * Oh holy s#$&! - set to 1
    * Grab some towels - and tampons if you have them!!!! - set to 3
    * Ask to start pulling stuff from out under the sink - set to 5


#### label enteraptsink

"You step into Lynda's apartment to see her sink tap spraying water in the air and a small flood emerging under the sink."


## CHOICE


### Oh holy S***

**set $HandsonSkill to 1**

**( $lynda_rating =-1)**

m "UH OH."

"Bean and Treacle scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

M "What do i do?!"

l "I don't know!!!"

l "It won't stop!!!"

"You move towards the sink, trying not to slip on the floor, and reach for the tap."

"The tap won't budge."

m "C'monnnn"

**if $ StrengthSkill = 2 : break the tap**

**else : it really won't budge**

l "Oh my godddd."

l "There has to be a way to turn this off!!!"

"Lynda reaches in and fumbles at the back of the pipes."

l "Ah HA!"

"You watch her twist something. With a *clunk*, the water flow ebbs from a jet to a trickle."

"You both wipe the water off your faces and adjust yourselves."

m "Well, that sucked."

**jump investigatefaucet**



* ~~You both start panicking~~
* ~~Start trying to turn off the tap and hold the pressure (with no luck)~~
* ~~Lynda dives under the sink to turn off the water at the shut off valve~~
* ~~The water flow stops, you're both soaked.~~


### Grab towels

**set $HandsonSkill to 3**

**$ lynda_rating = +1**

"Bean and Treacle scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

m "Where are some other towels?!"

l "In the bathroom!"

"You rush to grab more towels."

**If $ ShareSkill is 2: ask about tampons, lynda is menopausal so no**

**else :and sprint back to the kitchen."**

"Lynda grabs one of the towels out of your hand."

l "WAIT NOT THAT ONE."

"She clutches a red towel with a cat chasing leaves embroidered on it."

l "...its decorative."

"She throws it away from the flood of water and pulls the other towels off of you to jam under the sink."

"You create a barrier out of the remaining towels to prevent the water from spreading further."

l "There has to be a way to turn this off!!!"

"You climb under the sink, shielding yourself from the spray of tap water. You spot a valve with a handle at the back."


## 
    CHOICE



1. Twist up (shut off)
    1. "You turn the handle upwards to a 90 degree angle."
    2. "With a *clunk*, the water flow ebbs from a jet to a trickle."
    3. "You emerge from under the sink - soaked."
    4. "You both wipe the water off your faces and adjust yourselves."
    5. **jump investigatefaucet**
2. Twist down (uh oh)
    6. **$ lynda_rating =-1**
    7. "You turn the handle down in line with the pipe."
    8. "The water pressure increases."
    9. m "Oh NO"
    10. "Lynda yanks you out of the way and fumbles at the back of the sink."

"With a *clunk*, the water flow ebbs from a jet to a trickle."

"You both wipe the water off your faces and adjust yourselves."

**jump investigatefaucet**



* ~~You shout to Lynda to grab towels and anything absorbent (high share skill asks for tampons or period towels).~~
* ~~You grab some too to slow the flooding~~
* ~~Crawl beneath the sink to find the shut off valve~~
* ~~Choice between two (one makes it worse the other shuts it off)~~


### Under Sink

**set $HandsonSkill to 5**

**$ lynda_rating = +1**

m "Move!"

"Bean and Treacle scatter across the floor as Lynda tries to block the water spray and catches them in the crossfire."

l "h e l p"

**if TechSkill = 1**

"You dive under the sink, moving Lynda out of the way, and reach for the stop valve."

"With a creak, the jet of water finally ebbs to a trickle."

Else

**$SinkTimer = +1**

**$lynda_rating = -1**

"You dive under the sink."

m "I got this! Just keep the water from getting everywhere!"

"Water sprays you in the face."

"You reach in to try and figure out what is causing the leak."

"Water continues to spray you in the face."

"You realise that maybe… you don't got this."

"Lynda clocks you fumbling around."

l "Oh hell, now *you* move."

"Lynda pushes you out of the way and gets under the sink once more."

"You hear a *thunk* and the water finally ceases flowing across the kitchen."

"She emerges, equally as soaked as you."

l "I appreciate your enthusiasm to help."

m "Sorry…"

**jump investigatefaucet**



* ~~You clatter everything out from under the sink~~
* ~~Reach for shut off valve (while getting soaked)~~
* ~~Manage to turn it off~~


#### label investigatefaucet1

**if $ lynda_rating = more +1**

	"The two of you take a moment to catch your breath and look at each other. Lynda's makeup is all over her face and your shirt is drenched."

	l "Pfft."

	"Lynda begins to laugh."

	l "Ahahaha!"

	l "Oh, I'm so sorry, but we're a STATE."

**Else**

**	**"You both stand in silence with only the quiet dripping of the remaining water in the background."

**jump investigatefaucet2**


#### label investigatefaucet2

m "What the hell caused the sink to explode like that?"

l "I don't know, I was just washing my dishes when the water pressure dipped and then-"

"She gestures at the flood around you both."

"You check out the sink."

TAPS - turn no problem, no issues.

FAUCET - turn the faucet - it breaks off. Very corroded. (when selected jump **investigatefaucet3**)

PIPE - all intact, no drippage.


#### label investigatefaucet3

m "Well, there's your problem."

"You turn holding the faucet."

m "This thing's corroded to hell."

l "Oh GOD. How long has it been like THAT?!"

"She takes the faucet head from you and looks it over."

l "This has to have been going on for ages."

l "Well… hell."

l "Sasha had a similar problem next door, not quite as bad, and it took nearly two or three weeks before someone came to fix it."

l "I need a faucet &lt;playername>! My partner is coming to visit soon!"

"Well, this is what a tenant's board is good for… shall I suggest it to Lynda?"


## CHOICE



1. Ask Lynda
    1. **jump lyndaboard1**
2. Leave it be
    2. **jump lyndatidyup**

Investigate Faucet



* ~~Depending on relationship she either laughs with you or you both stand in silence as the remaining water drips into the sink.~~
* ~~Realise that the faucet is horribly corroded~~
* ~~Its probably been like that for a while~~
* ~~Mentions another neighbour had a similar problem that wasn't sorted for a week. And her S.O. is coming to visit soon.~~
* Relationship determines options to talk to her about the board
    * High at this point = +2 to Convince
    * This is what a board can help with
    * Bargaining power for this and pressure to sort things
    * I know you're busy with your new job and it can take the pressure off
    * Neutral = +1 Convince
    * Bargaining power
    * Low = no convince
    * Lynda is frustrated and doesn't like you using this situation against her.


#### label lyndaboard1



* **if lynda_rating +1> and SinkTimer is >5**
    * m "You know… I mentioned that tenancy board before. This is the kind of thing that it could help with."
    * "Lynda sighs, looking around her now very damp kitchen."
    * l "I really do appreciate the sentiment &lt;playername>... let me think on it, okay?"
    * l "I do think it's a good idea."
    * **jump lyndatidyup**
* **Elseif lynda_rating +1> and SinkTimer is &lt;5**
    * m "You know… I mentioned that tenancy board before. This is the kind of thing that it could help with."
    * "Lynda looks at the corroded faucet in her hand and then to you."
    * l "Yeah, I know. You make a good point. Just… let me think about it, okay? I just have so much on right now."
    * m "I understand."
    * **jump lyndatidyup**
* **else**
    * m "You know… I mentioned that tenancy board before. This is the kind of thing that it could help with."
    * l "Right now is not the time &lt;playername>! We don't know that it'll speed things up and it takes time and paperwork to even set it up."
    * "Lynda plonks the corroded faucet down in the sink and sighs."
    * l "I need to deal with this."
    * "She starts tidying up around the sink. You get the sense you should let yourself out."
    * m "Can I-"
    * l "I'm good, &lt;playername>, really."
    * m "Okay, I'll uh… see you around?"
    * l "Yep."
    * "You leave and head back downstairs."


#### label lyndatidyup

"Lynda starts sorting out the area around the sink."

m "Can I help?"

l "No, no, its okay I can manage."

m "Yeah, but I'd like to help."

l "Okay then!"

"You both get to mopping up the kitchen, chatting and laughing, before you head home for the night."

END
