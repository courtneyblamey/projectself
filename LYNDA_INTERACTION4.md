### label lyndainteraction4check

**if $ lynda_rating =&lt;0**

	**jump lyndanoshow**

**else **

	**jump lyndainteraction4**


### label lyndanoshow

	"Another day rolls by. It is a crisp fall morning, and the sunlight cascades upon your windowsi-"

	"Oh, that's kinda dusty."

	"You run your finger over the windowsill."

	m "Oh, ew."

	m "I should probably clean today."

	m "Good way to kill time before hanging with Lynda later."

	"You set out to make breakfast and your source of caffeine for the morning. Then, the Cleaning Game Plan."

**	if $ TidySkill = 1**

		m "Okay, first dusting, then vacuum and mop. Next, wash the bedding, and clean the bathroom while the laundry is on."


    "Your phone pings."


    m "Oh, it's Lynda."


    l "Hi &lt;playername>. Sorry… something's come up and I can't hang out like we planned.. Lynda."


    "You stare at the text, deciding what to respond."


## 
    MENU



1. Be disappointed
    1. m "Awh. That's a bummer. I was looking forward to it… Guess it's a cleaning and couch day today."

                **jump lyndanoshowend**

2. Be understanding
    2. m "All good, it happens! Hope all is okay."

				**jump lyndanoshowend**



3. Be annoyed 

                $ lynda_rating -= 1


                m "Oh. Okay. I wish you'd have let me know a little sooner?"


                **jump lyndanoshowend**


**	Else**

		m "Hmm…"

		"You gaze around the apartment."

		m "I have no idea where to start."


    "Your phone pings."


    m "Oh, it's Lynda."


    l "Hi &lt;playername>. Sorry… something's come up and I can't hang out like we planned.."


    "You stare at the text, deciding what to respond."


## 
    MENU



4. Be disappointed
    3. m "Awh. That's a bummer. I was looking forward to it… Guess it's a couch day today."

                **jump lyndanoshowend**

5. Be understanding
    4. m "All good, it happens! Hope all is okay?"

				**jump lyndanoshowend**



6. Be annoyed 

                $ lynda_rating -= 1


                m "Oh. Okay. I wish you'd have let me know a little sooner?"


                **jump lyndanoshowend**


**label lyndanoshowend**

"You meander around the apartment cleaning for the next couple of hours."

"Another ping from your phone. It's an email with a coupon. You check out your text to Lynda."

m "She left me on read?"

m "...rude."

m "Or is this an older person thing?"

m "..."

m "It's still rude."

"You put your phone away and focus back on cleaning, wondering what caused such a last-minute cancellation from Lynda."

**jump lyndaevent3**


### label lyndainteraction4

**if hangout_location = "bar"**

**	jump lyndabartime**

**if hangout_location = "park"**

**	jump lyndaparktime**

**if hangout_location = "cafe"**

**	jump lyndacafetime**


# BAR


### label lyndabartime

"You arrive at the bar where you agreed to meet Lynda for a drink."

"She is already sitting at the bar with a glass of wine." 

l "&lt;playername>! Over here!"

"She waves at you."

l "Come, come, grab a seat."

"She pats the barstool next to her and you sit down."

if drink_choice = "wine"

l "I hope its alright, I ordered you a glass too."

"Lynda points to the freshly poured glass of wine."

m "Oh, thanks!"

"You take a sip. Lynda has good taste in wines, clearly, as it goes down *smooth*."

else 

	l "I wasn't sure what you'd like so I'll let you order for yourself."

	m "All good!"

	"The bartender saunters over to take your order."


## MENU:



1. A beer.
2. A glass of wine.
3. A mocktail.
4. A glass of water.


## Beer

m "I'll take a beer, please."

m "Something light."

"The bartender nods and pours you an amber coloured beer from the tap and places it in front of you."

**Set $Alcohol to True**

**jump lyndabar1**


## Wine

m "Same as hers, thanks."

"The bartender nods and produces the bottle from behind the bar and pours you a glass."

"They signal to Lynda for a top-up and she nods."

**Set $Alcohol to True**

**jump lyndabar1**


## Mocktail

m "Oh, I'll take a mocktail, please. Maybe something with pear and ginger?"

"The bartender nods and whips up a delicious-looking mocktail, complete with garnish and fizz."

**set $ Alcohol to False**

**jump lyndabar1**


## Water

m "Just a water, thanks."

l "Really?"

m "Yeah."

"The bartender shrugs and pours you a glass of water and leaves to serve someone else."

**set $ Alcohol to False**

**jump lyndabar1**


### label lyndabar1

"Lynda sighs wistfully after taking a sip of her wine."

l "I appreciate this invite out. I don't think I realised how much I've missed doing things that aren't just *work*."

l "Or rotting on my couch."

l "While thinking about work."

"Lynda raises her glass."

l "Cheers!"

m "Cheers!"


## MENU:



1. Slam the drink
2. Drink it normally


## Slam the drink

"You grasp the glass, throw your head back and open your throat, sending it back."

**if $ Alcohol = True**

	"It burns ever so slightly, and you signal the bartender for another."

	l "So it's that kinda drinking session?"

	"Lynda smiles at the bartender and taps her wine glass lightly."

	l "Hi - I'll take a bottle of this then, please."

**	jump lyndadrank1**

**Else**

**	**"How hydrating."

	"You signal the bartender for another."

	l "Thirsty, huh?"

**	jump lyndabar2**


## Drink it normally

"You take a healthy sip and place the drink back down."

**jump lyndabar2**



* ~~Option to get more and more drunk w/Lynda~~
* ~~(She won't get drunk without you!)~~


### label lyndadrank1

**$ drunk_level +=1**

l "I didn't take you for a chugger."

m "Nah, I just like to do that with my first drink, means I spend less for the rest of the night, hahaha."

"Lynda raises an eyebrow."

l "It's certainly a choice."

l "I'm not one to shy away from a good night of drinks, but be warned, I have a strong constitution and a work from home day tomorrow so…"

"The bartender places your next drink in front of you."


## MENU:



1. Slam this one too
2. Maybe don't?


## Slam too

**$ drunk_level +=1**

"You grab the glass once more and neck it."

l "Alright, now I gotta catch up!"

"Lynda slams her glass of wine and grimaces."

l "bleugh… I wouldn't have got the nicer wine if this was how we were going to drink."

**jump lyndadrank2**


## Maybe don't?

"You decide to take this one slower. Lynda looks like she's willing to compete with you. Maybe it is best not to encourage that."

**jump lyndadrank2**


### label lyndadrank 2

**if drunk_level ==2**

**	**(insert python text modifier here)

	l "Oooh, shall we get some shots?"

	MENU:

	> Yes

	> Yes and LOTS

	> NOOO

	m "Abso-LUTELY!"

	"Lynda flags down the bartender and orders a couple shots for each of you."

	"You both slam them down with a clink of your glasses."

**	$ drunk_level +=2 (if LOTS +2 more)**

**	jump lyndabar2**

**else**

**jump lyndabar2	**


### label lyndabar2

m "How are things going?"

l "Well, you know, work is busy as usual."

l "I'm prepping for my partner Anna to come visit also!"

m "That's fun! Has she been to visit yet?"

l "No, not yet, she's been busy with her own work with an art collective. I'm excited to show her around town and have her finally see the place and not just virtually."

m "Wait, how long have you been apart and not seen each other?"

l "Oh! I still travel back to our home every month or so. I think Bean and Treacle would lose it if they didn't see her for long periods of time."

l "Though wrangling them into the car and giving them their "chill out" pill leaves something to be desired."

l "But they love their other mama, so who am I to deny them?"

m "Especially when they're so cute."

l "Even when one of them escapes like an ungrateful asshole."

m "I just know he's snoring on your couch right now as we speak."

l "Oh, absolutely, look-"

"Lynda pulls out her phone and opens a pet camera."

l "Bean, Treacle~"

"Two very curious faces appear close up to the camera."

b "mrow?"

t "mewww~"

"You both burst into giggles."

l "I'll just shoot them some treats and they'll be happy."


## MENU:



1. You seem to be getting the hang of tech things!
2. Those cameras can be hacked, you know.
3. Look at those faces, I can't.


## Tech things!

m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

"Lynda flaps her hand at you."

l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

m "Look at you, having opinions on *technology*."

l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought. 'You've gone to the dark side, darling.' She's ridiculous."

**jump lyndabar3**


## Hacking cameras

**$ HelpLynda -=1**

m "You know, those cameras are easily hacked these days."

l "What?!"

m "Yeah, I've seen videos of them being hacked."

l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

l "And me fighting with an exploding sink."

l "Hmm, I could charge for that level of entertainment."

**jump lyndabar3**


## Look at those faces

"The two cats scatter and chase down the dispensed treats."

m "I can't even with them, they're so cute."

l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

"Lynda elbows you playfully."

l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Treacle gained 2lbs because I didn't realise the setting was giving her double portions."

m "But I bet she was happy."

l "Very."

**jump lyndabar3**


### label lyndabar3

**if $ lynda_rating =>4**

	**jump lyndaconfession**

**Else**

**	**"You both continue to share anecdotes and small talk over the next couple of hours."

l "Well, this has been fun, &lt;playername>, but I should probably get going. I'm not used to being out on a school night as it were, and I'm an early bedtime kinda person."

"Lynda flags down the bartender and produces her card."

l "This is on me, don't try and fight me on it."

m "But-"

l "Nope."

"She taps her card."

l "This was really lovely, let's do it again sometime?"

m "Sure!"

"You both grab your coats and head out into the evening."

**jump lyndagoodend4**


# PARK


### label lyndaparktime

"You arrive at the park, picnic basket in hand (well, a tote bag with a pithy catchphrase on it - the contemporary picnic basket), and look out for a good spot."

"Luckily, even though there's a chill in the air, the sun is beaming across the park."

m "Okayyy, where to set up?"


## MENU:



1. A spot near the pond.
2. A spot near some trees.
3. A spot in the gazebo.


## POND

"You make your way over to the pond. Now that summer has passed, you don't have to worry too much about mosquitoes or that funky pond smell. Some ducks wade across the water. It's quite tranquil."

m "Perfect!"

"You lay out a tartan blanket and set up the food on it."

l "Hey!"

m "Oh, hey!"

"Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses too."

l "Oh god, are we sitting on the ground? I'm going to have to do my physio later."

m "Sorry, I thought being by the pond was nice."

l "It's cute!"

l "The ducks will feast well off of any crumbs left behind."

**jump lyndapark1**



* Lynda clearly hates this
* Chance to regain some small ground with her if at +1 (bringing a canopy/tarp and actual chairs, NO A GAZEBO CHOSEN AS THE SPOT).


## TREES

"There's a picturesque spot near some trees. Some leaves are floating off of them, but their vibrant colours make for a lovely canopy over a picnic."

"You wander over and set up next to one of the trees. You lay out a tartan blanket and start to set food up on it."

m "Oh, hey!"

"Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses, too."

l "Oh god, are we sitting on the ground? I'm going to have to do my physio later."

m "My bad! I just love being around the trees this time of year."

l "No bother, it's pretty."

**jump lyndapark1**


## GAZEBO

**$ lynda_rating +=1**

**$ Gazebo = True**

m "Ooh, the gazebo is empty. And there are no events on, it seems."

"You stroll over to the gazebo and climb its brief steps. From here, there's a wonderful view of the park, and *chairs*."

"There's even a folded table left behind from a previous event."

"You throw your tartan picnic blanket over the table and set up the picnic."

l "Hey!"

m "Oh, hey!"

"Lynda strolls over in what looks like a cashmere coat and heeled boots. She's rocking a pair of large sunglasses, too."

l "Oh, see now *this* is my kind of picnic. It's dining al fresco!"

l "I don't have to worry about bugs in my food."

m "I'm glad you like it."

**jump lyndapark1**


### label lyndapark1

"You both take in the fresh air while you graze on fruits, cheese, crackers, and crudites."

**if $ Gazebo = True**

**	**l "You know, I was not super enthralled by the idea of a park picnic, but now… now I see the appeal."

**else **

l "Okay, yeah, this is a good spinach dip."

m "You wouldn't believe how much it cost to make."

l "What?! It's spinach and artichoke, no?"

m "If I showed you the receipt, you'd have an aneurysm."

"There's a brief pause."

m "How are things going?"

l "Well, you know, work is busy as usual."

l "I'm prepping for my partner Anna to come visit also!"

m "That's fun! Has she been to visit yet?"

l "No, not yet, she's been busy with her own work with an art collective. I'm excited to show her around town and have her finally see the place and not just virtually."

m "Wait, how long have you been apart and not seen each other?"

l "Oh! I still travel back to our home every month or so. I think Bean and Treacle would lose it if they didn't see her for long periods of time."

l "Though wrangling them into the car and giving them their "chill out" pill leaves something to be desired."

l "But they love their other mama, so who am I to deny them?"

m "Especially when they're so cute."

l "Even when one of them escapes like an ungrateful asshole."

m "I just know he's snoring on your couch right now as we speak."

l "Oh, absolutely, look-"

"Lynda pulls out her phone and opens a pet camera."

l "Bean, Treacle~"

"Two very curious faces appear close up to the camera."

b "mrow?"

t "mewww~"

"You both burst into giggles."

l "I'll just shoot them some treats and they'll be happy."


## MENU:



4. You seem to be getting the hang of tech things!
5. Those cameras can be hacked, you know.
6. Look at those faces, I can't.


## Tech things!

m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

"Lynda flaps her hand at you."

l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

m "Look at you, having opinions on *technology*."

l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought. 'You've gone to the dark side, darling.' She's ridiculous."

**jump lyndapark2**


## Hacking cameras

**$ HelpLynda -=1**

m "You know, those cameras are easily hacked these days."

l "What?!"

m "Yeah, I've seen videos of them being hacked."

l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

l "And me fighting with an exploding sink."

l "Hmm, I could charge for that level of entertainment."

**jump lyndapark2**


## Look at those faces

"The two cats scatter and chase down the dispensed treats."

m "I can't even with them, they're so cute."

l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

"Lynda elbows you playfully."

l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Treacle gained 2lbs because I didn't realise the setting was giving her double portions."

**jump lyndapark2**


### label lyndapark2

**if $ lynda_rating =>4**

	**jump lyndaconfession**

**Else**

**	**"You both continue to share anecdotes and small talk over the next couple of hours."

l "Well, this has been fun, &lt;playername>, but I should probably get going."

l "Thank you for making such a lovely spread. I am *not* going to need dinner tonight, that's for sure."

l "Next time, I'll take you to a place I like."

m "A park?"

l "Noooo, haha - it's a place with a nice dining patio. Best of both worlds."

"Lynda helps you pack up the picnic debris, you walk back to the building together, taking in the fall sunshine."

l "See you around, &lt;playername>."

m "Likewise!"

**jump lyndagoodend4**


# CAFE


### label lyndacafetime

"You arrive at the neighbourhood cafe."

"The walls are littered with event posters, business cards, and some local artist prints to purchase."

"The smell of freshly ground coffee beans wafts by the counter. There is a large selection of sweet and savoury pastries stored in a display section. It all looks good."



* $  DrinkChoice comes into play here


### label lyndacafe1

m "How are things going?"

l "Well, you know, work is busy as usual."

l "I'm prepping for my partner Anna to come visit also!"

m "That's fun! Has she been to visit yet?"

l "No, not yet, she's been busy with her own work with an art collective. I'm excited to show her around town and have her finally see the place and not just virtually."

m "Wait, how long have you been apart and not seen each other?"

l "Oh! I still travel back to our home every month or so. I think Bean and Treacle would lose it if they didn't see her for long periods of time."

l "Though wrangling them into the car and giving them their "chill out" pill leaves something to be desired."

l "But they love their other mama, so who am I to deny them?"

m "Especially when they're so cute."

l "Even when one of them escapes like an ungrateful asshole."

m "I just know he's snoring on your couch right now as we speak."

l "Oh, absolutely, look-"

"Lynda pulls out her phone and opens a pet camera."

l "Bean, Treacle~"

"Two very curious faces appear close up to the camera."

b "mrow?"

t "mewww~"

"You both burst into giggles."

l "I'll just shoot them some treats and they'll be happy."


## MENU:



7. You seem to be getting the hang of tech things!
8. Those cameras can be hacked, you know.
9. Look at those faces, I can't.


## Tech things!

m "So, compared to the Lynda who was fighting with cables and wires a couple weeks ago, you now have a pet camera hooked up *and* connected to your phone?"

"Lynda flaps her hand at you."

l "Ohh, someone at work helped explain to me how to set it up. I have not become an aficionado overnight."

l "But I did research the cameras to find the best one, and I'm pretty sure the team I work with could make a better one."

m "Look at you, having opinions on *technology*."

l "Honestly, Anna was already teasing me for this when I showed her the electronic wine opener I bought. 'You've gone to the dark side, darling.' She's ridiculous."

**jump lyndacafe2**


## Hacking cameras

**$ HelpLynda -=1**

m "You know, those cameras are easily hacked these days."

l "What?!"

m "Yeah, I've seen videos of them being hacked."

l "Oh great. Well, at least the only thing they'd really be seeing is these two dumb-dumbs."

l "And me fighting with an exploding sink."

l "Hmm, I could charge for that level of entertainment."

**jump lyndacafe2**


## Look at those faces

"The two cats scatter and chase down the dispensed treats."

m "I can't even with them, they're so cute."

l "They're less cute at 5AM when they want breakfast even though they have an *automated dispenser* and I have never got up to feed them in their *lives*."

m "An automated dispenser? And you're really trying to sell me on the fact you're not tech savvy?"

"Lynda elbows you playfully."

l "Yeah, yeah, you should have seen me trying to set it up when I moved here. Treacle gained 2lbs because I didn't realise the setting was giving her double portions."

**jump lyndacafe2**


### label lyndacafe2

**if $ lynda_rating =>4**

	**jump lyndaconfession**

**Else**

**	**"You both continue to share anecdotes and small talk over the next couple of hours."

l "Well, this has been fun, &lt;playername>, but I should probably get going."

m "So soon?"

l "Yeah, I have to do some more prep for a client meeting next week. I've bought a stack of books and I plan to get through them!"

m "Of course, of course. I understand."

l "Thanks for this though. I think I'd forgotten how important it is to get out and do things."

"You both put on your coats and stack your mugs and plates, before heading out into the afternoon."

**jump lyndagoodend4**


# OUTRO


### label lyndaconfession

**(for when lynda_rating = 4>)**

**set $lynda_confession to "True"**

l "You know, we've been getting along since you moved in, and you've offered some kindness for my mid-life crisis, haha."

l "I feel like I should be honest with you over this whole tenancy association thing."

l "I might be moving…"

m "Oh."

l "I know… I just know you've been working hard to get folks to sign up, and I don't want you to waste your time with me if I'm not even going to be here."

l "My partner and I are looking at properties and have been for a while. I just didn't have the heart to tell you."

l "I'm sorry…"


## MENU:



1. MAKE A SCENE
2. Nod understandably
3. Express disappointment


## Make a scene

"Your blood starts to boil. She has been hiding this from you for how long? You thought you'd become good friends over the last few weeks, and she knew this was something you were working towards. Something you cared about."

m "Are you serious???"

"Folks around take notice of you both."

l "&lt;playername> I-"

m "No, seriously?! The building is basically falling down around our ears and you're just gonna move??"

l "I just don't think I'm the person to help with this. I think you need someone who can coordinate and communicate with the other tenants and-"

m "Isn't that what you do for work?!"

l "..."

m "You're literally in selling things to people! You could help me 'sell' the idea of a functional building!"

l "And what if I can't?!"

"..."

l "...what if I'm not good enough at convincing them?"

"..."

l "I think it's time for me to go."

"Lynda picks up her things, puts on her coat, and begins to leave."

"..."

l "...I understand you're upset. You know I've been struggling with things at work. So this-"

"She gestures between the two of you."

l "-was a low blow from someone I considered a friend."

"Lynda leaves."

"You look around to see folks try to look like they were not obviously listening in on the conversation."

"Lynda's words 'what if I'm not good enough', echo in your mind."

m "Ah, hell."


## MENU:



1. Go after Lynda
2. Go home


## 	Go after Lynda

	"You gather your things and head out after Lynda."

	m "She won't have gone too far."

	"You look down the street to see if you can spot her. A little ways down, you see Lynda leaning against a wall, staring out."

	"Slowly, you approach."

	m "So, uh, that sucked."

	"Lynda nods, not looking at you."

	m "I didn't mean to… I shouldn't have…"

	m "I'm sorry."

	l "I have enough pressure on myself &lt;playername>. I didn't expect more to come from you."

	l "I have this thing where, if I can't do something perfectly, I just don't *want* to do it."

	l "I've had it all my life."

	l "So, I prepare. I study. I read everything I can, I practice, I slap on the lipstick and eyeshadow war mask and just-"

	"She gestures forward."

	l "Give it 150%."

	l "Deep down, I still feel like I've lucked my way into everything."

	l "When a new challenge comes along, honestly, I'm paralysed. And this tenancy committee is so outside of what I know and I feel like I'm barely keeping up at work as it is."

	m "Lynda…"

	"You see tears form in her eyes."

	l "Ugh, I told myself I needed to stop crying in front of you."

	"You rest a hand on her arm."

	m "I didn't mean to add pressure on you. Let's just forget about the association for now, okay?"

	m "Let's just take a walk back home?"

	"Lynda sniffs and wipes her tears."

	m "I know there's a good ice cream place along the way!"

	l "That sounds nice."

	"You link arms."

	l "You're a good one &lt;playername>."

	l "And ice cream is on me for being an emotional wreck again, hahaha."

	m "Sounds like a plan."

	"You head off as the streetlights begin to flick on."

**	jump lyndagoodend4**


## Go home

**$ lynda_rating -=2**

"With a huff, you pack up to leave as well."

m "Whatever. I'll find others to join the association."

**jump lyndabadend4**


## Nod understandably

"You nod slowly, taking in the information."

l "Oh god, you're mad at me."

m "No, I can understand. I mean, it isn't ideal, but I can't tell you that you can't leave."

"Lynda's whole physique relaxes."

l "Ugh, I've felt awful not telling you."

m "How long have you been planning to move?"

l "..."

l "Not long after you'd moved in. The sink explosion was not the first issue I'd encountered in the building. The laundry machines have destroyed some of my favourite sweaters, the bin room is just disgusting, and the fan for the oven has the suction power of a geriatric mouse."

l "This was always meant to be temporary while I got settled into my new role."

l "And now my partner is thinking of moving out here to join me. We're in a position to sell our old place to purchase something here. So, yeah…"

m "And you're really not interested in joining the association?"

l "It feels unfair to you to say I'm in, when in fact, I might not still be here in a couple months, you know?"

m "Yeah… I hear you."

l "And other folks in the building will still join your cause!"

l "You can be very persuasive."

m "Hah, thanks."

"Lynda pats your arm."

l "I am sorry I didn't tell you."

m "S'okay."

l "Wanna swing by an ice cream place and get a cone? My treat for being a bad friend."

m "Now who's being persuasive?"

"You both chuckle as you pack up and head out to a dairy delight together."

**jump lyndagoodend4**


## Express disappointment

m "You're leaving?"

l "Well, nothing specific is confirmed yet, but there's definitely momentum towards it. And it doesn't mean we can't hang out! This has been really lovely and it's only really the first time we've hung out outside of the laundry room haha."

m "Hey, I like our laundry room hangs. Don't knock them."

l "My point is, I know a lot of the time you've spent with me has been to convince me to join the association. But, it is kinda nice that a friendship has come from it."

m "You make it sound like I was only nice to you to get you to join!"

l "No! Not at all!!"

l "I'm flubbing this majorly."

l "I know you're disappointed. I'm sorry."

"You let out a hefty sigh."

m "I just don't know where I stand with the others joining the association right now, and I felt you were a sure thing at this point."

l "Again, I'm sorry."

m "No, it's fiiiine."

l "Wanna swing by an ice cream place and get a cone? My treat to ease my guilt and your disappointment?"

m "I want sprinkles on my disappointment ice cream."

l "Ahaha, done!"

"You both chuckle as you pack up and head out to a dairy delight together."

**jump lyndagoodend4**


### label lyndagoodend4

"You close your apartment door behind you and kick off your shoes. With a solid leap, you plant yourself on the couch."

"It seems getting Lynda to join the association is going well. Hopefully, she'll jump on board officially soon. The paperwork is due shortly."

"It's been lovely getting to know Lynda."

"Even if there's a sadness behind her eyes at times."


## MENU:



1. I think she just needs to trust her instincts.
2. I think she should be kinder to herself.
3. I think she could benefit from more time away from work.


## INSTINCTS

**$ lynda_reflection = "instincts"**

m "Lynda really has so much more figured out than she realises. I wonder why she just can't see that…"


## KINDER

**$ lynda_reflection = "kinder"**

m "We're all our own worst enemies. Lynda seems particularly hard on herself at times. Like nothing she does meets her own expectations. I wonder what her co-workers think of her? She seemed to think she lucked into her job, but she does so much for it."


## AWAY FROM WORK

**$ lynda_reflection = "work"**

m "Lynda seems to work 9-5 and then 5-9 on things. I get she's in some kind of senior role, but the amount of time she puts into prepping for things seems a little unhealthy… I'm surprised she said yes to spending time together."

"You fiddle with a tassel on one of the couch throws."

"..."

"Are you like Lynda sometimes?"

> Yes

**$ imposter = True**

> No

**$ imposter = False**

**jump lyndaevent3**


### label lyndabadend4

"You close your apartment door behind you and kick off your shoes. With a solid leap, you plant yourself on the couch."

"It might be time to call it quits on trying to persuade Lynda to join the association. Nothing you've done has swayed her, regardless of exploding sinks and cat escapades."

"Lynda has a lot going on underneath the surface, it seems."


## MENU:



4. I think she just needs to trust her instincts.
5. I think she should be kinder to herself.
6. I think she could benefit from more time away from work.


## INSTINCTS

**$ lynda_reflection = "instincts"**

m "Lynda really has so much more figured out than she realises. I wonder why she just can't see that…"


## KINDER

**$ lynda_reflection = "kinder"**

m "We're all our own worst enemies. Lynda seems particularly hard on herself at times. Like nothing she does meets her own expectations. I wonder what her co-workers think of her? She seemed to think she lucked into her job, but she does so much for it."


## AWAY FROM WORK

**$ lynda_reflection = "work"**

m "Lynda seems to work 9-5 and then 5-9 on things. I get she's in some kind of senior role, but the amount of time she puts into prepping for things seems a little unhealthy… I'm surprised she said yes to spending time together."

"You fiddle with a tassel on one of the couch throws."

"..."

"Are you like Lynda sometimes?"

> Yes

**$ imposter = True**

> No

**$ imposter = False**

**jump lyndaevent3**
