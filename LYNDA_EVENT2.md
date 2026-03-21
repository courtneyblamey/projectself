lyndaevent2

BEAN ESCAPES



* What is the player up to right now?
    * Baking
    * TV/Film
    * Gaming
* Knock on door
* Very stressed Lynda at the door - Bean somehow managed to get out
* Go searching (split the party)

Randomise location?

AROUND THE BUILDING



* Outside in bushes
    * If here: scared and hiding 

IN THE BUILDING



* Laundry room
    * If here: curled up in abandoned laundry belly up 
* Lobby/Entry
    * If here: curled up in plant pot snoozing next to chomped delivery box

IN YOUR APARTMENT



* Check balcony
    * If here: scared and meowing once you open the door
* Check inside
    * If here: happily snoozing in your bed next to some destroyed cardboard.
* Once found, bring back to Lynda's apartment
* $ AttentionSkill allows player to clock a popped window mesh 
* Otherwise Lynda is just happy to have Bean back



### label lyndaevent2

BEAN ESCAPES

"It's a quiet and grey afternoon, you decide to:"


## MENU


## 
    Bake some cookies



    1. "You put on some tunes and get to baking!"
    2. m "Hmm… what kind of cookies do I make…"
    3. > pick apple pie, pumpkin pecan, or double chocolate
    4. Set $ CookieType = "x"
    5. "The scent of baked goods slowly fills the air as you pull the tray of cookies out of the oven."
    6. "A sudden knock at the door startles you."
    7. **jump lyndabean1**

## 
    Put on a comfort series

* "You launch yourself onto the couch and bundle up in blankets."
* m "Ehehehehe."
* "You kick your feet excitedly as your streaming app boots up."
* "As the opening title rolls, there's a sudden knock at the door."
* **jump lyndabean1**

## 
    Curl up and play a game

* "You grab your controller and cocoon into some blankets."
* m "Yes. E x c e l l e n t."
* "As the console powers on, there's a sudden knock at the door."
* **jump lyndabean1**
* ~~What is the player up to right now?~~
    * ~~Baking~~
    * ~~TV/Film~~
    * ~~Gaming~~
* ~~Knock on door~~


### label lyndabean1

"You open your door to a very stressed out Lynda."

**if $ lynda_rating >2**

l "Oh, thank god you're home!"

m "Lynda, you okay?"

l "No, no not really. Bean is missing."

m "What?!"

"Lynda walks into your apartment, pacing frantically."

**	if $ Baking = True**

	l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- Oh my god it smells amazing in here."

	m "Want one?"

	"You offer a cookie to Lynda."

	l "I won't say no."

	"She shoves the cookie in her mouth and continues to pace."

	l "I domphn't know howmph Bean eshcaped."

	l "Sorry *ahem*, I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

	l "Can you help me look?"

	m "Of course!"

	l "Thank you thank you thank you. I'm going to check the apartment one last time and then look around the upstairs area."

	"She dusts the crumbs off of herself and pats you on the arm and spots the next batch of cookies waiting to go in the oven."

	l "Wait, no, I'm sorry, I feel like I'm intruding on your afternoon."

**	jump findbeanchoice**

	**elseif $ TVOn = True**

**	**l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- 

	l "Oh I'm catching up on that season too."

	l "Sorry, distracted - I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

	l "Can you help me look?"

	m "Of course!"

	l "Thank you thank you thank you. I'm going to check the apartment one last time and then look around the upstairs area."

	"Some characters begin to argue on the TV."

	l "Oh! I'm sorry, I realise I'm intruding on your afternoon."

**	jump findbeanchoice**

**	elseif $ GamingOn = True**

**	**l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- 

	"The start menu is blaring music in the background."

	m "Lemme just…"

	"You turn it down."

	m "Sorry, new game in a series I love, you were saying?"

	l "No I'm sorry! I feel like I'm intruding on your afternoon."

**	jump findbeanchoice**

**Else (negative/neutral rating)**

**	if $ Baking = True**

	l "I was doing something for work tomorrow and I went to feed him and- wow something smells good."

	m "Want one?"

	"You offer a cookie to Lynda."

	l "Umm… no it's okay, but thanks."

	L "I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

	l "I'm sorry to ask butm could you help me look?"

	m "Of course!"

	l "I really appreciate it. I'm going to check the apartment one last time and then look around the upstairs area."

	"She spots the next batch of cookies waiting to go in the oven."

	l "Wait, no, I'm sorry, I feel like I'm intruding on your afternoon."

**	jump findbeanchoice**

	**elseif $ TVOn = True**

**	**l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- 

	l "Oh I'm catching up on that season too."

	l "Sorry, distracted - I don't know how Bean escaped… I've checked everywhere in the apartment in case he's just hiding or zonked out somewhere sleeping, but he's nowhere."

	l "Can you help me look?"

	m "Of course!"

	l "Thank you thank you thank you. I'm going to check the apartment one last time and then look around the upstairs area."

"Some characters begin to argue on the TV."

	l "Oh! I'm sorry, I realise I'm intruding on your afternoon."

**	jump findbeanchoice**

**	elseif $ GamingOn = True**

**	**l "I was trying to study up on some tech before an all hands in meeting tomorrow and I went to feed him and- 

	"The start menu is blaring music in the background."

	m "Lemme just…"

	"You turn it down."

	m "Sorry, new game in a series I love, you were saying?"

	l "No I'm sorry! I feel like I'm intruding on your afternoon."

**	jump findbeanchoice**



* ~~Very stressed Lynda at the door - Bean somehow managed to get out~~
* ~~Go searching (split the party)~~

**label findbeanchoice**


## MENU



1. Yeah, a little, but it's okay!
2. No, it's okay.
3. Gaze longingly at your afternoon plans.

		


### 	label yeahbutbean

m "A little, but it's okay! Bean is missing. That takes priority."

**jump lyndabean2**


### 	label noitsbean

m "No, it's okay. Bean got out?"

**jump lyndabean2**


### 	label gameoverbean

**$ HelpLynda -= 2**

m "I mean…."

	**if $ GamingOn = True**


    "You look over at the bouncing title screen. You don't get a lot of free time, and you were *really* looking forward to being a couch gremlin."


    **elseif $ Baking = True**


    	"You think about whether the cookie dough would be fine in the fridge for a bit."


    **elseif $ TVOn = True**


    	"This season has had so much hype around it, and right now two of your favourite characters are getting into a heated argume- OH THEY'RE KISSING."


    **Else (NOTHING?)**

m "You're sure Bean isn't just hiding in the apartment?"

"Lynda chews her lip."

l "I'll go look again… if you see or hear him, would you look?"

m "Sure, yeah."

"Lynda walks out of the apartment and shuts the door behind her with a little bit more force than you expected."

**jump gameoverbeanend**


### label lyndabean2

	l "I just don't know how he got out!"

	l "He's normally so lazy that at any time I'll find him passed out in blankets or my bed, but today when I finished prepping he was nowhere."

	m "A sudden burst of adventure, maybe?"

	l "Maybe… but he's still my dopey boy and I want him home."

	m "Of course! I can look around if you want to check your place again?"

	l "Sure."

	"Time to split the party and find this furry escape artist."

**	jump beansearch**


### label beansearch

Randomise location?

bean_location = X

> Pick where you want to check.

> Inside the building

> Outside the building

> Check your apartment


### label beanoutbuilding

AROUND THE BUILDING

**if bean_location = "outside"**

	m "Oh I really hope he didn't get outside…"

"You head outside of the building, bundling up against the crisp breeze."

	m "Beaaaaan!"

	"The wind picks up a bit as you wander around the outside of the building."


## 	menu:



1. check bushes

            m "Maybe the bushes?"


            "You approach the group of bushes at the side of the building and begin to peer through the branches."


            m "Bean~?"


            b "mrow"


            m "Beaaaan~?"


            b "m r o w w w"


            m "Bean!"


            "A pair of eyes peer back at you through the branches. Bean is curled up tight and trembling."


            m "Oh, buddy!"


            "You take off your scarf and bundle him up in it. He's not game initially, but soon succumbs to the woollen burrito."


            **jump foundbean**

2. check garbage bins

			m "He does love cardboard, maybe near the bins?"

			"You head around the back of the building to the bins."

			m "Beaaan?"

			m "Beaaaaaaan!"

			"After some kissy sounds and searching, there's no sign of Bean."

			m "Darn."

			**jump beansearch**



3. check under cars

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


        **jump beansearch**


**Else**


## menu:



4. check bushes

            m "Maybe the bushes?"


            "You approach the group of bushes at the side of the building and begin to peer through the branches."


            m "Bean~?"


            "A bunch of litter is stuck amongst the branches."


            m "Mm, nice."


            "You climb slightly into the bushes to check Bean isn't hiding in one of them."


            m "Bean??"


            "There's no sign of Bean here."


            m "Where are you?"


        **jump beansearch**

5. check garbage bins

			m "He does love cardboard, maybe near the bins?"

			"You head around the back of the building to the bins."

			m "Beaaan?"

			m "Beaaaaaaan!"

			"After some kissy sounds and searching, there's no sign of Bean."

			m "Darn."

			**jump beansearch**



6. check under cars

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


        **jump beansearch**


            	

* ~~Outside in bushes~~
    * ~~If here: scared and hiding ~~


### label beaninbuilding

"Maybe 


## Menu:

	Check the lobby

	Check the laundry room


### label beanlobby

**if bean_location = "lobby"**


## 	Menu:



1. Check the mailbox area

            "You investigate the mailbox area."


            "...it's not likely that Bean climbed into one of the mailboxes."


            m "Why give me the option then?!"


        **jump beansearch**

2. Check planters

            "There's a few planters in the lobby. Some are easily large enough to hide a furry escapee."


            "You check them out one by one when - a wild Bean appears!"


            "Curled up and content, Bean is snoozing in one of the plant pots, with some shreds of cardboard from someone's delivery parcel."


            m "Ohhh, you little stinker."


            m "Your mum is worried sick about you."


            "You scoop him up, despite his complaining, and carry him back to Lynda's apartment."


            **jump foundbean**

3. Check stairwells

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


        **jump beansearch**


**Else**


## Menu:



4. Check the mailbox area

            "You investigate the mailbox area."


            "...it's not likely that Bean climbed into one of the mailboxes."


            m "Why give me the option then?!"


        **jump beansearch**

5. Check planters

            "There's a few planters in the lobby. Some are easily large enough to hide a furry escapee."


            "You check them out one by one."


            m "Achoo!"


            "Ironically, most of these are plastic plants."


            m "Must be the dust."


            "No napping cat in any of them."


            m "Where did you sneak off too you little stinker?"


        **jump beansearch**

6. Check stairwells

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


			**jump beansearch**


### label beanlaundry

**if bean_location = "laundry"**

"You wander into the laundry room. The lingering smell of floral laundry detergent and dryer sheets wafts in the air."

m "Well, this is a cosy spot for a mischievous cat."

"A couple of the machines rumble as you search around for Bean."

m "Beaaaan~?"

m "Are you hiding in here?"

b "Prrp."

m "Bean?"

"You spot a pile of orange fur snuggled up in someone's laundry basket."

"Bean is belly up snoring away in some freshly laundered bedsheets. Truly a cat that got the cream… sheets."

m "Excuse me, sir."

b "Prrrp?"

m "Sorry to disturb your slumber but *someone* is very worried about you."

"Bean sighs and stretches and begins to snore again."

m "Right."

"You scoop Bean up in your arms. He's too lazy to fight back and flops around instead of resisting. Truly orange cat behaviour."

**jump foundbean**

**Else**

"You wander into the laundry room. The lingering smell of floral laundry detergent and dryer sheets wafts in the air."

m "Well, this is a cosy spot for a mischievous cat."

m "Beaaaan~?"

m "Are you hiding in here?"

"A couple of the machines rumble as you search around for Bean."

"No sneaky cat napping in any baskets or piles of laundry."

m "Not here, it seems…"

**jump beansearch**



* ~~Laundry room~~
    * ~~If here: curled up in abandoned laundry belly up ~~


### label beaninapartment

m "There's no way he managed to sneak in here right? I only popped out a couple times to do some laundry."


## Menu:

	Check balcony

**		jump beanbalcony**

	Check bedroom

		**jump beanbedroom**


### label beanbalcony



* ~~Check balcony~~
    * ~~If here: scared and meowing once you open the door~~

**if bean_location = "balcony"**

**set $ bean_escape to "window"**

m "I will eat my shoe if he's on the balcony."

"You open the balcony door and a flash of orange streaks across your apartment."

b "MROWWW!!!"

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

**jump foundbean**

**Else**

m "I will eat my shoe if he's on the balcony."

"You open the balcony door and peer out and around."

m "No sign of him here… and I *don't* have to eat a shoe. Double win?"

**jump beansearch**


### label beanbedroom

**if bean_location = "bedroom"**

**set $ bean_escape to "door"**

"You flick on your bedroom light to see if Bean has somehow made his way into your apartment."

"Right in the middle is a very content, but now rudely awakened, orange blob of fur."

b "Mrow?"

"Bean folds his face into his paws trying to block out the light and grunts."

m "Ohhh you little stinker."

"You then spot a shredded box next to him on the bed."

m "You really do have a penchant for cardboard eh, Bean?"

m "C'mon, let's get you back home."

"Luckily, as an orange cat Bean offers little resistance to being scooped up by a relative stranger."

**jump foundbean**



* ~~Check inside~~
    * ~~If here: happily snoozing in your bed next to some destroyed cardboard.~~

**else** 

"You flick on your bedroom light to see if Bean has somehow made his way into your apartment."

"Looking around the room you see nothing out of place beyond your usual clutter."

m "Phew… if he'd have been in here the whole time I would have been a *little* surprised."

**jump beansearch**


### label foundbean

"You make your way up to Lynda's apartment with Bean in your arms and knock on her door."

m "Guess who~?"

"Lynda opens the door - she's clearly been crying."

l "BEAN!!!!"

"She grabs him from you and showers him in kisses."

l "You stupid, sweet, dumb, silly, beautiful cat!!!"

"She holds him out at arms length and scolds him. Bean blinks out of sync."

l "How did you get *out*?!"

l "Ugh who cares, I'm just glad you're back home."

**jump beanhome**



* ~~Once found, bring back to Lynda's apartment~~
* ~~$  AttentionSkill allows player to clock a popped window mesh or door latch issue~~
* ~~Otherwise Lynda is just happy to have Bean back~~


### label gameoverbeanend

SOMETIME LATER

**if $GameOn = True or $TVOn = True**

"You blink and your eyes feel as dry as the Sahara."

m "Oof. Maybe I should take a break."

"You stand up and stretch - a few things pop - and you realise it's dark out."

**elif $Baking = True**

	"You put away the last batch of cookies into a container."

	m "Ahh, procrasti-baking… My favourite pastime."

	m "Now I just need to figure out what to do with all these cookies… I hadn't thought that bit through.

	"You stretch - a few things pop - and you realise it's dark out."

m "I wonder if Lynda's found Bean…"

"You decide to go upstairs and check in on Lynda."

"You knock on her door, and there's a brief pause before she opens it." \
l "Oh, hey &lt;playername>."

m "Hey, I just wanted to check if you found Bean?"

"Lynda sighs with a light chuckle."

l "Yeah, I did in the end. It took a good couple hours of searching. He decided he'd curl up in Jasper's laundry basket in the laundry room. Little shit. He looked at me like I was disturbing him with my snotty tears."

m "That's good! Well, not the snotty tears but, finding Bean."

l "Yeah - still don't know how he got out though."

**jump beanhome**


### label beanhome


## MENU



1. You can always leave out food and something that smells like you.

    m "I've read before that leaving out food and something that smells like home helps guide them back."


    l "Oh, that's good to know. Hopefully he won't be breaking out again anytime soon."


    b "Meow."


    l "Yeah, you."


    "You both chuckle and bid each other good night."

2. Maybe a collar would be good in case he does it again?

    **$ HelpLynda -= 1**


    m "I mean, he doesn't have a collar, that's something you should probably look into getting for him."


    l "Yeah, do you have a cat?"


    m "No…"


    l "Then you don't know the struggle of putting anything on them. It is like wrestling a coat onto a toddler."


    m "Ah, gotcha." \
b "Mrowww."


    "Bean flomps near the doorway."


    l "You and I are *not* friends right now, mister."


    b "Purrrmeow."


    "You both chuckle while Beans rolls around."


    l "I gotta be up early so, night &lt;playername>."


    m "Night!"

3. Want me to look around and see if I can spot anything?

    **$ HelpLynda = +1**


    m "I could check and see where he maybe got out?"


    l "Honestly, sure, I cannot for the life of me figure out how."


    "You head into Lynda's apartment"


    "Bean and Treacle stalk you as you move around, looking for any signs of escape."


    **if $ AttentionSkill =1/2>?**


    **	if bean_escape = "door"**


    "After a scan of the apartment, you can't see any evidence of cat mischievousness. You turn to let Lynda know when you spot the door is ajar."


    m "Uh, Lynda?"


    l "Yeah?"


    m "Did you mean to leave the door open?"


    l "What?!"


    "She strolls over and goes to shut and latch it."


    "It pops open."


    l "Oh, you're kidding me."


    "She tries again."


    "It pops open."


    "Frustration builds on her face."


    **jump lyndabeanconvince1**


    **else if bean_escape = "window"**


    "After a scan of the apartment, you can't see any evidence of cat mischievousness. You turn to let Lynda know when you spot a missing chunk of window screen in one of the windows."


    m "Uh, Lynda?"


    l "Yeah?"


    m "Has that always had a, uh, Bean sized hole in it?"


    l "You're *kidding*."


    "Lynda moves over to investigate."


    l "Urgh! This was the loose panel I messaged the damn management about weeks ago!!"


    l "Great, now I have a HOLE in my WINDOW MESH."


    **jump lyndabeanconvince2**


    **else **


    **if bean_escape = "door"**


    "After peering around the apartment, you're unable to find where Bean got out."


    l "Any luck?"


    m "No… sorry, I thought I could help with that at least."


    l "Ah, it's okay."


    m "Hope your presentation goes okay tomorrow."


    l "Thanks &lt;playername>."


    "You roll out and Lynda shuts the door behind you."


    "It pops back open."


    m "Yeah?"


    l "Hmm? I didn't say anythi- why is this open?"


    "She goes to shut it again. *click* it creaks ajar."


    l "Oh, you're kidding me."


    "She tries again."


    "And again."


    "It won't shut."


    "Frustration builds on her face."


    **jump lyndaconvincebean1**


    **elseif bean_escape = "window"**


    "After peering around the apartment, you're unable to find where Bean got out."


    l "Any luck?"


    m "No… sorry, I thought I could help with that at least."


    l "Ah, it's okay."


    m "Hope your presentation goes okay tomorrow."


    l "Thanks &lt;playername>."


    "As you turn to leave a gust of wind blows through Lynda's apartment."


    l "Oh my, I must have left a window open!"


    "She saunters over and stops."


    l "Oh for- I know how Bean got out…"


    "Lynda points to a missing mesh panel in the window pane."


    l "Urgh! This was the loose panel I messaged the damn management about weeks ago!!"


    l "Great, now I have a HOLE in my WINDOW MESH."


    **jump lyndabeanconvince2**



### label lyndabeanconvince1

"A door that won't lock is a pretty convincing argument for Lynda to join the board…"

> CONVINCE

	m "That's not good."

	m "This is why I think we really should start a tenancy board. There are clearly issues around the whole building."

**	if $ lynda_rating >X (positive reaction)**

**		if $ lynda_convince = 2**

		"Lynda faffs with the door latch."

		l "Y'know, the argument is kinda making itself at this point."

		"The latch pops out properly."

		l "Ah-HA. Fixed it."

		l "But seriously, I am still considering it. I am just not sure what I could contribute to it, honestly. "

		m "It's more about numbers than anything. To show enough of us care and will fight."

		l "I hear you."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**		elseif lynda_convince = 1**

		"Lynda faffs with the door latch."

		l "I know, I know, I'm just so busy. I don't think I have time right now."

		m "It doesn't have to be right now. It'll take a little time to be official anyway."

		l "Oh, fair point."

		l "Let me think some more on it."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**		Else**

		"Lynda faffs with the door latch."

		l "Last time you brought this up it annoyed the hell out of me… but I am starting to see your point."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**	elseif $ lynda_rating = X (neutral reaction)**

**		if $ lynda_convince =2**

		l "I hear you, I hear you. I just need things to settle at work and then we can talk, 'kay?"


    l "Anyway, I gotta crack on with some more work now that Bean's secured."

		m "Yeah, of course. Night, Lynda!"

		**$ lynda_convince += 1**


    **jump beanconvinceneut**

		**if $ lynda_convince =1**

		l "Yeah, I just don't know about timing right now, but we can talk about it another time, 'kay?"


    l "Anyway, I gotta crack on with some more work now that Bean's secured."

		m "Yeah, of course. Night, Lynda!"

		**$ lynda_convince += 1**


    **jump beanconvinceneut**

		**Else**

		"Lynda sighs."

		l "I can understand where you're coming from."


    l "More than last time."


    m "Eheh… sorry."


    l "We can talk about it some other time. For now, I gotta figure out how to sort this out and then get back to prepping for tomorrow."


    m "Yeah, of course. Night Lynda!"


    **$ lynda_convince += 1**


    **jump beanconvinceneut**


    **Else**


    **	if $ lynda_convince = 2**


    **	**l "You know, I got where you were coming from before, but this really isn't going to make a difference. Respectfully, I love that you have the free time to deal with this, I just don't. I have too much on to be thinking about this right now."


    	l "Speaking of which, I need to get on with my prep work for tomorrow. So…"


    	m "Yeah, no, I'll head out."


    	l "I'll see you 'round, &lt;playername>."


    **	jump beanconvincebad**


    **	if $ lynda_convince = 1**


    	l "While I understand your ambition, between the sink and now Bean escaping, I'm starting to get very over this apartment complex in general."


    "Lynda sighs deeply."


    l "I gotta get on with some things."


    	m "Yeah, no, I'll head out."


    	l "I'll see you 'round, &lt;playername>."


    	**jump beanconvincebad**


    **	else **


    	l "Oh my GOD &lt;playername>, will you let it be? Can't you see, once again, this is n o t the time?"


    l "I am up to my eyeballs in work things, trying to learn everything I can in prep for every meeting, joining a tenancy board is the LOWEST thing on my priority list."


    l "So, no, thank you."


    	m "Yeah, no, I'll head out."


    	m "Sorry."


    	l "I'll see you 'round, &lt;playername>."


    **	jump beanconvincebad**

> DON'T CONVINCE


### label lyndabeanconvince2

"A loose mesh and now window… hole? is a pretty convincing argument for Lynda to join the board…"

> CONVINCE

	m "That's not good."

	m "This is why I think we really should start a tenancy board. There are clearly issues around the whole building."

**	if $ lynda_rating >X (positive reaction)**

**		if $ lynda_convince = 2**

		"Lynda faffs with the window."

		l "Y'know, the argument is kinda making itself at this point."

		l "But seriously, I am still considering it. I am just not sure what I could contribute to it, honestly. "

		m "It's more about numbers than anything. To show enough of us care and will fight."

		l "I hear you."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**		elseif lynda_convince = 1**

		"Lynda faffs with the window."

		l "I know, I know, I'm just so busy. I don't think I have time right now."

		m "It doesn't have to be right now. It'll take a little time to be official anyway."

		l "Oh, fair point."

		l "Let me think some more on it."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**		Else**

		"Lynda faffs with the window."

		l "Last time you brought this up it annoyed the hell out of me… but I am starting to see your point."

		l "For now, I gotta get back to researching for my meeting tomorrow. I think I'm getting a handle on some of the jargon and acronyms."

		l "I think…"

		l "I've got pages of notes so…"

		l "Anyway, good night!"

		m "Night, Lynda!"

		**$ lynda_convince += 2**

**		jump beanconvincegood**

**	elseif $ lynda_rating = X (neutral reaction)**

**		if $ lynda_convince =2**

		l "I hear you, I hear you. I just need things to settle at work and then we can talk, 'kay?"


    l "Anyway, I gotta crack on with some more work now that Bean's secured."

		m "Yeah, of course. Night, Lynda!"

		**$ lynda_convince += 1**


    **jump beanconvinceneut**

		**if $ lynda_convince =1**

		l "Yeah, I just don't know about timing right now, but we can talk about it another time, 'kay?"


    l "Anyway, I gotta crack on with some more work now that Bean's secured."

		m "Yeah, of course. Night, Lynda!"

		**$ lynda_convince += 1**


    **jump beanconvinceneut**

		**Else**

		"Lynda sighs."

		l "I can understand where you're coming from."


    l "More than last time."


    m "Eheh… sorry."


    l "We can talk about it some other time. For now, I gotta figure out how to sort this out and then get back to prepping for tomorrow."


    m "Yeah, of course. Night Lynda!"


    **$ lynda_convince += 1**


    **jump beanconvinceneut**


    **Else**


    **	if $ lynda_convince = 2**


    **	**l "You know, I got where you were coming from before, but this really isn't going to make a difference. Respectfully, I love that you have the free time to deal with this, I just don't. I have too much on to be thinking about this right now."


    	l "Speaking of which, I need to get on with my prep work for tomorrow. So…"


    	m "Yeah, no, I'll head out."


    	l "I'll see you 'round, &lt;playername>."


    **	jump beanconvincebad**


    **	if $ lynda_convince = 1**


    	l "While I understand your ambition, between the sink and now Bean escaping, I'm starting to get very over this apartment complex in general."


    "Lynda sighs deeply."


    l "I gotta get on with some things."


    l "..."


    	m "Yeah, no, I'll head out."


    	l "I'll see you 'round, &lt;playername>."


    	**jump beanconvincebad**


    **	else **


    	l "Oh my GOD &lt;playername>, will you let it be? Can't you see, once again, this is n o t the time?"


    l "I am up to my eyeballs in work things, trying to learn everything I can in prep for every meeting, joining a tenancy board is the LOWEST thing on my priority list."


    l "So, no, thank you."


    	m "Yeah, no, I'll head out."


    	m "Sorry."


    	l "I'll see you 'round, &lt;playername>."


    **	jump beanconvincebad**


### label beanconvincegood

"You head back downstairs. You're making progress with Lynda, you can feel it." 

m "Though hopefully less cat and sink issues for now…"

"Time to settle in for the night."

**jump beanconvinceend**


### label beanconvinceneut

"You head back downstairs. Maybe you can still convince Lynda. She didn't seem *un*interested."

"Time to settle in for the night."

**jump beanconvinceend**


### label beanconvincebad

"You head back downstairs."

m "...well, that was rough. Lynda seemed particularly annoyed at me."

m "I hope she still wants to go out like we planned."

"Time to settle in for the night."

**jump beanconvinceend**


### label beanconvinceend

**jump lyndainteraction4check**

