### label lyndaevent3 

**if $ lynda_rating =&lt;2**

**	jump lyndaevent3bad**

**elif $ lynda_rating =>5**

**	jump lyndaevent3neut**

**elif $ lynda_rating =>8**

**	jump lyndaevent3good**

~~If relationship low enough you don't get this scene? Or you're not privy to the whole conversation.~~



* ~~Got some mail of Lynda's by accident - notice that it is from the building management company.~~
* ~~Head up to deliver it to her that evening.~~

Low relationship


### label lyndaevent3bad

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

"Knock knock knock."

"After a brief pause, someone you don't recognise opens the door."

a "Hello?"

m "Oh, uh, hi! I have something for Lynda? It was put in my mailbox for some reason."

a "Lynda? One of your neighbours are here with some mail?"

l "Ah. Hey."

l "Thank you for bringing it up, you could have just left it on the table downstairs."

m "Oh, its no bother. Figured you might not want someone taking mail from the building company?"

l "From the… oh!"

"She takes the envelope from your hand."

l "This was what I was telling you about, love! They've got some options we can look through in their new buildings."

a "Ohhh, okay perfect, I'll wrap up dinner and we can check it out. Nice to meet you…?"

m "&lt;playername>."

a "Gotcha. Anna, by the way." \
"With a curt wave she heads back inside."

"Lynda stands in the doorway tracing the edges of the envelope."

l "Anything else?"


## MENU



1. Try to invite yourself in
2. Excuse yourself for the evening


## INVITE IN

"You subtly peer behind her to see an amazing spread of food."

m "Oh, wow. Dinner looks good."

l  "Haha, yeah, Anna is the chef of our duo. My aptitude lies in selecting from a food delivery app."

"..."

l  "Listen, &lt;playername>, I'm just gonna come out and say it. I'm not going to be in the building much longer. Anna and I are making plans to buy somewhere and the building company offered a deal to buy one of their new condos."

l "So, I won't be joining your association."

l "Sorry."

**jump lyndabadendmenu**


## EXCUSE YOURSELF

m "No, no. Just the mail."

l "Cool, well, thanks, &lt;playername>."

m "I'll see you around?"

l "Ah, probably not. I'm gonna be moving at some point soon."

m "Oh."

l "Yeah, I complained enough to the company that they offered a deal to rent one of their newer places while Anna and I condo shop from their catalogue, so…"

m "I see…"

l "Less Bean escapes! Yaaay"

"She gives a half-hearted jazz hands."

**jump lyndabadendmenu**


### label lyndabadendmenu


## MENU:


## Be disappointed

"You stare down at the floor for a second, tempering yourself."

m "I really thought you might come around eventually."

l "Oh, &lt;playername>, don't be like that. There are others in the building! I'm just a lost cause for this. I'd been planning this for a while and saying yes to the association felt wrong."

m "I just thought with your management savvy you could have helped me manage the others."

l "Oh, you're putting too much stock in my skills for that."

a "Lynda?"

l "Yep! Coming!"

l "I have to go, but… yeah, keep at it?"

"She gives you a small wave and closes the door with a firm click."

"You stand there for a moment absorbing the failure."

m "fuck."

**jump gameendingbad**


## Be angry

m "Really?!"

m "I helped you with your sink and figuring out how Bean got out!! You can't just join in the meantime until you move?"

l "Okay. First of all, I don't *owe* you anything, let me be very clear."

l "Second, you have overstepped in other ways with me that I have not loved."

l "I might not always know what I'm doing, but I'm not totally incompetent you know."

l "I was trying to be polite about it, but quite frankly, this is a lost cause. If you really hate it here so much, just move."

a "Lynda?"

"Anna appears behind her."

l "They're just leaving, don't worry."

l "Goodnight, &lt;playername>."

"The door shuts firmly in your face."

	Menu:



1. Fuck this

    m "I'm over this. I can't convince anyone to sign up, its like no one cares or maybe *maybe* they just aren't willing to spend the energy to care."


    m "Screw all of this."

2. Fuck her

    "You glower at the shut door and storm back downstairs."


    m "Well, if she's gonna move out and leave the rest of us to deal with the stupid company…"


    "You get into your apartment and crank the TV volume to max."


    m "She can deal with this."


    m "Hope it doesn't distract you from the APARTMENT SHOPPING."


    "You flomp onto your bed, put on some headphones, and curl up under the blankets."


    "A couple hours later, someone starts banging on your wall telling you to shut it off. You switch off the TV and curl back up in your pit of despair."


**jump gameendingbad**


## Try to appeal

m "There's no way you might just join us in the interim?"

l "&lt;playername>, I am going to say this very clearly and only once."

l "No."

m "Nothing could persuade you?"

l "I am just not interested at this point. I have to do what is best for me, and it is not joining what I think is a lost cause - sorry."

l "Maybe you'll get some others? But I really need you to drop this with me."

a "Lynda?"

l "Yep, coming!"

l "Good night, and good luck."

"Lynda shuts the door."

m "..."

m "Well, shit."

**jump gameendingbad**



* ~~Lynda's SO answers the door. "One of your neighbours is here with some mail?"~~
* ~~Lynda appears and takes the mail~~
* ~~Attention allows you to clock that she looks a little guilty.~~
* ~~Awkward pause, where you can excuse yourself or invite yourself in lol~~
    * ~~Excusing yourself ends the conversation and event.~~
    * ~~Inviting yourself in via seeing Bean? Or just biding time?~~
* ~~Come in for tea and ask about project and work~~
* ~~Small talk learning about SO~~
* ~~SO lets slip that Lynda is looking at buying a place from the management to offset breaking the lease.~~
    * ~~So many issues~~
    * ~~They have some new properties that are standout~~
* ~~You can take a disappointed, frustrated, or an appeal route with her.~~
* ~~Disappoint~~
    * ~~Going to leave without helping us? Could use your management savvy to corral the other tenants.~~
* ~~Frustrated~~
    * ~~I really need help! I helped with the sink and finding your cat, this is the least you could do!~~
* ~~Appeal~~
    * ~~Could you at least help us in the meantime?~~


### label lyndaevent3neut

"On your way back in from a walk you spot a letter jutting out of your mailbox."

m "Huh."

"Upon unlocking it and large brown envelope falls out. It was crammed in poorly."

"The envelope is not addressed to you, but to Lynda."

"On the top left-hand corner is the building company's logo and slogan: *for loving city living*."

m "Yeah, sure."

m "I should probably take this up to Lynda."

"You arrive at her door and knock. There's sounds of cooking and laughter coming from inside."

a "One second!"

"An unfamiliar voice."

a "Hi! Can I help you?"

"A woman with a gentle smile and bubbly presence stands in the doorway."

m "Sorry, I just have some mail for Lynda? It got put in my mailbox by accident."

a "Oh, how kind of you - Lynda!"

l "Hey, &lt;playername>, what's up?"

a "This is &lt;playername>! Nice to meet you."

m "Likewise, you must be Anna?"

a "That I am!"

l "Oh, is that for me?"

"You reach out with the envelope and she takes it."

l "Ah… Thanks for bringing it up!"

l "Would you like to come in for a drink or something?"

m "Sure!"

**if $LyndaDrink = "true"**

l "I remember from our tech escapades, **[drink_choice]** right?"

m "Yeah! Thanks."

**Else**

	l "What can I get you? I got wine, tea, water…"


## 	MENU:



1. Wine
2. Tea
3. Water

"Lynda preps your drink and sets it on the table in front of you."

a "So, what's this mysterious piece of mail?"

l "Ohh, it's nothing, we can talk about it later."

a "What did you get another parking ticket?"

l "That was one time!"

a "In my car!"

"They both laugh and Lynda playfully taps Anna on the head with the envelope."

a "Oh! Is it the condo listings?"

l "ANNA."

a "What?!"

"Lynda glances over at you sheepishly."

m "Condo listings?"

a "Why do I feel like I've mistepped here?"

l "Because you *have* my love."

l "&lt;playername> has been trying to set up a tenants association to deal with the building issues."

a "Oh, that's so good of you!"

l "I was one of those asked to join."

a "...Ah."

m "You're leaving?"

l "I'm sorry, &lt;playername>, you've been so into getting it set up and I know I'm the first one you spoke to about it and I encouraged you and the whole time I've-"

l "I am sorry."

a "Nothing is finalised, mind, we're just looking through some options."

l "I do think it is a noble cause."

"Maybe I can make one final attempt to convince her even to help me until she leaves?"


## MENU:



1. Appeal to her skills as a manager
2. Appeal to her being inconvenienced in the building
3. Appeal to your friendship


## MANAGER

m "I could really use your skills, even if it's just before you move, you don't even have to sign up. Just help me get some of the other folks on board."

**if $ encourage?? **

m "You know you have that managerial magic that could really make a difference here."

"Lynda chuckles."

l "Managerial magic??? I wouldn't go that far!"

a "They're right! I keep telling you that you're better than you admit!"

l "The pair of you!"

l "Okay, fine, I will help with some of the others, but I make no promises *and* I'm not joining the association. Hopefully, I can magic you some support."

m "This means a lot to me, thank you, Lynda."

**jump lyndasaysyes**

**else**

l "I think you overestimate my skills in this regard &lt;playername>."

l "I genuinely wish you the best of luck, but I'm just very done with this building in general. It's time to leave."

**jump lyndasaysno**


## INCONVENIENCE

m "You can't just join on for a short while? This building is such a nightmare, as you well know. Any help can make a difference. Who knows when someone else's sink will explode?"

l "Respectfully &lt;playername>, that's why I'm leaving. I don't mean to sound blunt or uncaring, but I can't stay here in solidarity just to face more issues. I've already been here for over a year - I'm ready to be out of here."

**jump lyndasaysno**


## FRIENDSHIP

m "Could you join to help a friend in need? Before you go? Or at least help me corral the others into action?"

**if $ lynda_rating = >6**

l "We have become fast friends, haven't we?"

l "Okay, here's what we'll do. Before I leave, I'll help you with a couple of the folks in the building. I can't promise anything, but I will use my powers for good."

m "Thank you!!"

m "This means a lot, truly, thank you."

**jump lyndasaysyes**

**else **

l "I'm sorry &lt;playername>, I wish I could do more, but I think you're better off just chatting with the other folks in the building."

**jump lyndasaysno**


### label lyndaevent3good

**if $lynda_confession = "True":**

"On your way back in from a walk, you spot a letter jutting out of your mailbox."

m "Huh."

"Upon unlocking it and large brown envelope falls out. It was crammed in poorly."

"The envelope is not addressed to you, but to Lynda."

"On the top left-hand corner is the building company's logo and slogan: *for loving city living*."

m "Yeah, sure."

m "I should probably take this up to Lynda."

"You arrive at her door and knock. There's sounds of cooking and laughter coming from inside."

a "One second!"

"An unfamiliar voice."

a "Hi! Can I help you?"

a "Oh! You must be &lt;playername>!"

m "Uh, yes! You must be Anna?"

a "In the flesh! Come on in, come on in."

"Anna ushers you inside."

a "Lynda! &lt;playername> is here!"

"Lynda emerges from her office."

l "Hey! Didn't expect to see you today!"

m "Yeah, sorry, I don't mean to interrupt, I just got mail for you in my mailbox, so I figured I'd bring it up."

"Lynda clocks the envelope and takes it from you."

l "Ah! I know what this is."

a "Ooh, the condo brochure?"

"Anna looks to you."

a "We still love print media in this house."

l "That's the one."

l "I told &lt;playername> about the move."

a "Sorry about the tenant association hit from Lynda leaving."

m "No, I understand."

l "Well, I wanted to tell you after going through the brochure with Anna, but, it doesn't feel right to leave you in a lurch. Especially since I am kindaaa the one who warned you about the building in the first place."

l "So, while I am still planning to move, I will sign on for now, and help you corral some of the others onto the team."

m "You will?!"

l "Yeah! Anna and I are both in agreement that I can probably encourage folks since I've been here a while, where you're new to the building, and so on."

a "Plus, we don't necessarily know how long it'll take to find a place and set it up."

l "Exactly. So, we've got some time!"

m "This means a lot to me, thank you, Lynda."

**jump lyndasaysyes**

**Else**

**"Lynda did not confess"**

~~High relationship~~



* ~~Lynda's SO answers the door. "Oh hey! You must be playername!"~~
* ~~You head in as they offer tea or wine.~~
* ~~Hand over the letter (attention catches some guilt).~~
* ~~Get to chatting with SO and learning about them.~~
* ~~Lynda opens letter while talking - (it is a brochure of apartments) eventually admits to you that she was looking at buying somewhere newer to be able to WFH more and have a better space for their SO to visit. (The shower had issues and the fire alarm was hyper sensitive in the last two days). And the agency offered a favourable rate to break the lease.~~
* ~~Can choose to say nothing or the above options of disappointment, frustration, appeal.~~
* ~~Say nothing~~
    * ~~Lynda tells you she hasn't made any kind of permanent decision but she has to think about more than the association.~~
    * ~~SO vouches that she's been torn knowing how kind you've been.~~
* ~~Continue to say nothing or empathy~~
    * ~~Say nothing: Lynda continues to explain herself~~
    * ~~Empathy: you understand~~


### label lyndasaysno

l "Again, I'm sorry &lt;playername>."

m "No, no, it's okay, I do understand. It just…"

l "I know."

l "I really do think other folks will join you. I just don't have the time or capacity to help you with it at this point."

l "It really isn't personal."

a "Why don't you stay for dinner? It's the least we can do."


## MENU:



1. Stay for dinner
2. Politely decline


## STAY FOR DINNER

m "I won't turn down a free meal, and it already smells good!"

l "You don't even know. There's a reason I live off of takeout when she's not around."

"While Anna preps dinner, you all hang out in the kitchen, chatting about everything from favourite foods to funniest stories involving a suitcase."

"Anna serves an amazing pasta dish with accompanying salads and then homemade cookies and ice cream."

"At the point you think you're going to burst, Anna hands you a tupperware filled with leftovers to take home."

"You wish them a good night and head downstairs. A pang of sadness hits knowing you're down one tenant signature."

m "I'll just have to convince the others."

m "But for now, I digest all this food in a blanket pile."

**jump gameendingneut**


## POLITELY DECLINE

m "Oh, I appreciate it, but I think I'm going to head home and finish some leftovers or they're going to spoil."

a "Sure, no worries!"

l "At least take one of the cookies Anna made earlier."

a "That I do insist on."

"Lynda bags you a couple cookies and walks you to the hallway."

m "See ya, Anna, nice to meet you!"

a "Likewise!"

"You step out of Lynda's apartment."

l "Hey."

l "I do appreciate the kindness you've shown me over the last couple months. This isn't a reflection on that."

m "I know. But thank you."

"Lynda pats you on the shoulder and heads back into her apartment."

"You head downstairs with a pang of sadness."

m "Guess I'll need to convince some of the others."

"You get into your apartment, reheat your leftovers, and lock in on binge watching something."

**jump gameendingneut**

~~- kinder conclusion to the exchange - you understand~~


### label lyndasaysyes

l "Anyway, enough shop talk, you wanna join us for dinner?"

a "Oh, I insist you do."

m "Guess I have no choice then!"

"You all chatter over drinks while Anna makes dinner."

"Anna serves an amazing pasta dish with accompanying salads and then homemade cookies and ice cream."

"At the point you think you're going to burst, Anna hands you a tupperware filled with leftovers to take home."

"You wish them a good night and head downstairs, feeling full of optimism - and food."

**jump gameendinggood**


# GAME OUTRO


### label gameendingbad

"A FEW WEEKS LATER."

"As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."

"Today must be the day Lynda moves out."

"A flicker of irritation courses through you."

"While she might not have joined your cause, now's the time to start thinking about the others."

m "Guess it's time to chat with the other tenants."

**jump lyndareflectiontime**



* ~~Moving truck appears and Lynda leaves, sit and reflect.~~


### label gameendingneut

"A FEW WEEKS LATER."

"As you enjoy your morning coffee you hear some commotion outside. You peer out the window to see a moving truck slowly filling up with furniture. A cat tower, wine rack, and antique box sit waiting to be added."

"Today must be the day Lynda moves out."

"A wave of sadness hits."

"While Lynda's departure makes sense, you can't help but be sad to see her go. Partly because of the rapport you both built over the last couple months, but equally because you'd hoped she would be your first signature for the association."

m "Guess it's time to chat with the other tenants."

**jump lyndareflectiontime**



* She is leaving but you're less bitter loll


### label gameendinggood

"A FEW WEEKS LATER."

l "Yeah, just stack them here for now!"

"You lug some moving boxes over to the lobby doorway."

m "My god, what do you have in this one?"

l "Fashion magazines from the 90s."

m "Bricks would be lighter."

"You plonk it down and grab another box with an open top."

m "Oh, this one needs taping shut!"

l "Oh! Actually!"

"Lynda trots over."

l "That's for you!"

m "Me?"

"You peer into the box."

"There's another box in there labelled 'The Story Cube'"

l "It's the actual product I was trying to figure out way back! This is one of the first ones manufactured that we're showcasing soon."

l "I thought it might be a silly gift. I know it's bedtime stories, but-"

m "No, that's very wholesome, thank you."

"You place the box to the side and hug Lynda."

l "I chatted with Antony and Sasha about the association, so hopefully they'll have a little more intrigue than before."

m "Thank you."

a "Lynda, my love, the movers said they'd grab the rest and we should drive ahead to the new place."

a "Also, I think Bean and Maple might lose it if we leave them outside the car in their carriers much longer."

a "The kitty Xanax hasn't kicked in yet it seems."

l "Alright."

"Lynda squeezes your arm." \
l "Best of luck with it all &lt;playername>."

"You wave bye to Lynda and Anna as they head out."

"As you get back into your apartment, you see the freshly signed association document with Lynda's name on it."

"Her lease isn't up for a little bit longer, so she's technically still a tenant until next month."

"You put the document back down and sit on the couch."

m "Guess it's time to chat with the other tenants."

**jump lyndareflectiontime**



* Get her signature on the association document, sit and reflect. Still leaving, but you're actually helping load up the truck.


### label lyndareflectiontime

"Do I ever doubt my skills?"

**If $ lynda_knowledge = "True"**

When Lynda doubted her skills you told her "I think you know more than you realise."

"Do I talk with people when I'm struggling?"

When Lynda was struggling with the long-distance nature of her relationship meaning she lacked support in her feelings you 

**if $ lynda_blab = "True"**



1. Let her talk it out. You offered an ear to her problems.

**if $ lynda_validate = "True"**



2. Validated how she felt. Sometimes just hearing someone echo back to you that you're facing a tough situation helps.

"Am I harder on myself than I should be?"

When Bean escaped, Lynda felt wholly responsible for his escapade. 

**if $ lynda_blame = "True"**



1. You reminded her to not blame herself. Some things are beyond our control, and beating yourself up over a misstep is not kind to yourself.

**if $ lynda_overwork = "True"**



2. You pointed out she worked too much. Not as a critique, but as a concern. Lynda spends a lot of time overpreparing for work meetings and presentations, and you helped her realise she could ease off a little bit.

"Sometimes, it is easier to give advice than take it."

"But I hope, for a moment, that you can see your kindness towards Lynda, someone who isn't real, as things you can say to yourself. To grant yourself the same level of kindness."

"If you didn't pick these options, that doesn't mean you're a bad person or unempathetic! Perhaps you were curious what certain options might bring you, or maybe you just didn't vibe with Lynda."

"Thank you for playing this vertical slice of Project Self. There's more on the horizon!"
