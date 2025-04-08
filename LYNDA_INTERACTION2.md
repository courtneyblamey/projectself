**label lyndainteraction2:**

“As you are headed back home you spot Lynda wrangling a pair of boxes through the building’s front door.”

“You quicken your approach to meet her at the door and go to hold it open.”

L “Oh thank you!”

“She fumbles with the boxes and shimmies through the doorway.”

“Partway through, the door jams.”

L “You’re kidding me.”


## **CHOICE**



1. Shove the door
2. Kick the door
3. Yell at the door


### **Shove the door**

**$ DoorShove = True**

**$ lynda_rating += 1**

“You give the door a hefty shove and it scrapes against the ground in protest before finally giving - swinging back on its hinges.”

L “Nicely done!”

“She readjusts the boxes in her arms and carries on through the doorway.”

jump postdoor


### **Kick the door**

**$ DoorKick = True**

“With some gumption, you give the door a swift boot. It pops back with force and slams against the doorway causing an echo down the corridor. BUT it is open. You see a shoe print on the (luckily) glazed glass.”


### **Yell at the door**

**$ DoorYell = True**

**$ lynda_rating += 1**

M “C’MON DOOR.”

“…”

“The door remains stuck.”

“Lynda leans into it and it scoots past its sticking point, finally swinging freely on its hinges once more.”

L “I like the enthusiasm?”

“She nearly drops the boxes she’s holding, but manages to adjust her grip and carries on through the doorway.”

(maybe something for the PC personality here?)

**label postdoor**

L “That door keeps getting stuck… I hope it doesn’t properly jam one of these days.”

“She shrugs and moves further into the lobby.”

M “What have you got there?”

L “Oh, some things from work I need to try out.”

“She sighs placing the boxes down to stretch out her back.”

L “It's a new product they want us to get to know.”

“Lynda looks down at them with a grimace.”


## **CHOICE**



1. Sounds… fun?
2. You want me to carry them up for you?
3. WHAT’S IN THE BOX.


### **Sounds fun?**

**$ BoxIntense = False**

M “Sounds… fun?”

L “Yeah.” She lets out a soft sound through her nose. “Super fun.”

“Lynda looks at you deadpan”

L “I know nothing about tech, &lt;playername>.”

L “Well, that’s not fair actually. I know how to run apps and find which HDMI my devices are hiding on, but this?”

“She indicates the boxes.”

L “Nothing.”

**jump boxdetails**


### **You want me to carry them up for you?**

**$Box Intense = False**

**$CarryBox = True**

**$ lynda_rating += 1**

“Lynda’s eyes widen.”

L “Are you sure? These things are heavy! Which is ironic.”

M “Yeah, I got this!”

“You lift up the boxes from the ground. They’re certainly heavy, but you know you can make it to Lynda’s apartment thanks to the elevator.”

“As you walk towards the elevator Lynda peels off a loose label on the top of the box with a sigh.”

(again, player stats? Maybe we do a DE thing here and have them pick a stereotype).

**jump boxdetails**


### **WHAT’S IN THE BOX.**

**$ BoxIntense = True**

**label boxdetails**

**if $ BoxIntense = True**

M “What’s in the booooox?”

“Lynda blinks at you.”

L “Great film.”

L “Specifically? Uh, some kind of holographic thing? There’s some kind of app with it… They’re pitching it for kid's bedtime stories.”

**(else) if $BoxIntense = False**

L “They want us to test and play with some kind of holographic thing. It has an app integration too. Apparently they think it will be the next big thing in ‘Kids Bedtime Tech Peripherals’”

“You both continue along to the elevator.”

“There’s a palpable silence before Lynda turns to you.”

L “Are you good at tech-y things?”

“You see a glimmer of anxiety in her eyes.”


## **CHOICE**



1. I’m not, but we can suffer together? (Help Lynda)
2. I’m pretty good with tech! (Help Lynda)
3. I will break whatever you hand me. (Do not help Lynda)


### **I’m not but we can suffer together?**

**$ TechSkill += 1**

M “I’m not amazing with it, but we can suffer together in it?”

“Lynda’s eyes light up.”

L “Really?”

L “Oh, I really appreciate it &lt;player name>! I’m feeling a little out of my depth here.”

&lt;UPDATE CHARACTER MENU>


### **I’m pretty good with tech!**

**$ TechSkill =+ 2**

M “Actually I do know a decent amount about tech.”

“Lynda’s shoulders relax as she smiles at you.”

L “Would you help me out in setting this thing up?”

M “Of course! Lead the way!”


### **I will break whatever you hand me**

**$ TechSkill = 0**

M “Candidly, I will break whatever this is in record time.”

“Lynda’s shoulders slump in defeat.”

L “Damn it. Okay.”

“Lynda looks at the boxes once more.”

L “Guess it’s you, me, tutorial videos, and a tall glass of wine.”

**jump lyndaboxfinal**

**label lyndaboxfinal**

**if $CarryBox = True and TechSkill == 0**

“You carry the boxes up to Lynda’s apartment and wish her a good evening with her tech adventure and head home for the night.”

**jump lyndaboxend**

**if $CarryBox and TechSkill != 0**

“You chat with Lynda on the way to her apartment, carrying the boxes along the way.”

**jump lyndaboxapartment**

**label lyndaboxapartment**

**$ lynda_rating += 1**

“You reach her door, decorated with a minimalistic doormat stating REAL FRIENDS BRING WINE, and a fall wreath of brightly coloured leaves and pinecones.”

“Lynda notices you scanning the doorway and nods to the wreath.”

L “Sasha made me this!”

“And points to the doormat.”

L “*That* was a dumb online purchase, but I stand by it.”

“She unlocks the door and flicks on the lights to the apartment.”

**if $CarryBox = True**

L “You can place the boxes right here on the counter.”

“You prop them up and onto the counter, trying very carefully to not drop them, noticing the VERY LARGE ‘FRAGILE THIS WAY UP’ label on the side.”

**if $CarryBox = false**

“Lynda grunts as she places the boxes on top of the countertop.”

L “Alright, can I get you something to drink before we get into this?”


## **CHOICE**



1. No, I’m good for now.
2. Yeah, some water would be great.
3. I’d love some tea.
4. Some wine, perchance?


### **No, I’m good for now.**

**$ LyndaDrink = false**

M “No, I think I’m okay for now, but thanks.”

**jump lyndaopenbox**


### **Yeah, some water would be great.**

**$ LyndaDrink = true**

M “Just some water for now, thanks.”

“Lynda smiles from behind a heavily painted white cabinet door.”

L “On it!”

**jump lyndaopenbox**


### **I’d love some tea.**

**$ LyndaDrink = true**

M “I’d love some tea, actually!”

L “Sure thing! Let me get it brewed for you and we’ll get into it.”

**jump lyndaopenbox**


### **Some wine, perchance?**

**$ lynda_rating += 1**

**$ LyndaDrink = true**

M “I know great friends bring wine, but maybe you have some already to share?”

“Lynda peers from behind a heavily painted white cabinet door, wine glasses in hand.”

L “Already on it!”

**jump lyndaopenbox**

**label lyndaopenbox**

**if $LyndaDrink = true**

“Lynda sets down the drinks and begins to open the box.”

else

“Lynda sets down her drink and begins to open the box.”

“You look into the boxes to see a short tangle of wires, an odd looking box with angled windows, and various cubes reading: Alice in Wonderland, The Gruffalo, Ferdinand the Bull, and more.”

“Lynda pulls out and sets everything down on the countertop, throwing the boxes into the front room.”

“Within moments, two cats appear and hop into each of them respectively. One a mottled grey, orange, and white, and the other a slim black cat.”

L “They’re cardboard box fiends. Give it a second and you’ll see Bean just start chomping it.”

“Sure enough, the black cat begins to move along the box, biting it. Leaving a trail of bite marks as it goes.”

L “We found him behind a restaurant with a bunch of empty bean tins and boxes. You can take cat out of the street but-”

“Bean continues his tirade against the box’s edges.”

L “…anyway. Where to start with this thing.”

“She looks with dismay at the tech in front of her.”

**If $TechSkill = 1**

“You also look down at the tech in front of you.”

M “Is there an instruction booklet?”

“Lynda fishes around in the box and produces a paper booklet with a flourish.”

L “Yes, there is!”

“You both read over the instructions, which are relatively well-written, if a bit over-written.”

L “Wow, these are kinda idiot-proof.”

L “Maybe I could have done this myself. Now I feel bad for asking for help.”


### **CHOICE**



1. You want me to leave you to get on with it? (jump lyndaleaveearly)
2. I can stay, I don’t mind. (jump lyndastayearly)

**label lyndaleaveearly**

**$ lynda_rating =+ 1**

“Lynda flicks through the instructions with neon painted nails.”

L “Yeah, actually, I think I got this!”

L “Thanks anyway. I’ll let you know how it goes.”

if **$ LyndaDrink = true**

“You finish up your drink as Lynda gets to work and head back home for the evening. You sense she’s feeling a little more confident in herself as she sets up the tech on your way out.”

L “See ya, &lt;playername>!”

**jump lyndaboxend**

**else**

“You wish Lynda luck in deciphering the device and head home for the evening. You sense a new level of confidence in her as she begins to set up the pieces of tech.”

L “See ya, &lt;playername>!”

**jump lyndaboxend**

**label lyndastayearly**

“Lynda flicks through the instructions with neon painted nails.”

L “You know, I wouldn’t hate the help…”

M “Sure! Let’s figure it out.”

“You each begin to take turns following the instructions, setting up the base, power source, and fetching the different story cubes.”

L “It’s so comforting to know I’m not the only one moderately afraid of technology like this.”

M “I mean, this is pretty high-tech. I think you’re allowed to be a little intimidated by it.”

L “I do feel a bit out of my depth. I moved to this job from the beauty industry, and it's just…”

“Lynda slots a piece of the device in place.”

L “It’s very different sometimes.”

L “I guess I didn’t think I’d feel like this still at this point in my career.”

“She chuckles softly to herself and flicks on the device.”

M “Feel like what?”

L “I don’t really know how to describe it other than out of my depth.”

“The images of Alice in Wonderland begin to faintly appear on the holographic part of the device.”

L “Oh look at that!”

“Over the next couple minutes, the images get brighter and words begin to appear, telling the story of a girl growing too fast after eating a cake.”

M “Not going to lie, that is pretty cool.”

“Lynda stares at the holograph with a slightly furrowed brow.”

L “This could be used for more than just storytime, right?”

M “Probably? The concept can do lots of things.”

“Lynda grabs a notebook off of her desk and begins to scribble down notes.”

“She looks up at you after a moment with a soft smile.”

L “&lt;player name> you have no idea how much this has helped me out.”


### **CHOICE**



1. I think you knew more about this than you realise. (jump lyndalearn)
2. I’m happy to help! (jump playertech)
3. I really enjoyed playing with this thing. It’s cool. (jump playertech)

**label lyndalearn**

**$ lynda_rating =+ 1**

M “You know, I think you actually know more than you're giving yourself credit, Lynda.”

“Lynda’s face drops for a moment.”

L “You think so? Huh.”

M “Considering we both went into this a little unsure- we made it, and it works!”

“She looks over the device, now clearly playing colourful sequences from Alice in Wonderland.”

L “I feel like the team is just so adept and knowledgeable about these things compared to me.”

“She looks at you with a smile and a wink.”

L “Maybe that’s just me getting older.”

L “Anyway, I’ve kept you long enough. I’m sure you’d like some of your evening to yourself!”

“You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her.”

**jump lyndaboxend**

**else If $TechSkill = 2**

“You pick up the cables and untangle them, plugging in the power source, and opening the instructions.”

M “Okay so, this is the base. You just have to make sure it is plugged into the outlet. And then…”

“You reach for one of the cubes.”

M “This goes into the base.”

L “Okay, this makes sense.”

“You then pick up the box of angled windows and place it overtop, slowly piecing together the device, as Lynda watches on chewing her rosy pink stained lip.”

“You talk her through each phase, ensuring she’s following along and answering her questions. She slowly becomes more and more inquisitive as you get ready to boot up the device.”

L “Okay and so this then refracts? the projection to make it look 3D?”

M “Exactly, yeah! And each of these cubes holds the data of the images and words that will play.”

M “Wanna boot it up?”

L “YES!”

“You flick on the device and it whirs to life.”

“After a couple minutes, you begin to faintly see the outlines of a girl growing too big for a doorway. Alice in Wonderland is playing on the holographic projector.”

M “Weird, there’s no sound…”

L “Oh! They told us they’re working on the audio component right now. But the words appear on the screen- well holograph, too.”

“You both continue to watch as the projector warms up and the colours become more vibrant and words clearly display alongside the pictures.”

L “So, this could actually be used for more than just storytime, right?”

M “Probably? The concept can do lots of things.”

“Lynda grabs a notebook off of her desk and begins to scribble down notes.”

“She looks up at you after a moment with a soft smile.”

L “&lt;player name> you have no idea how much this has helped me out.”


### **CHOICE**



1. I think you knew more about this than you realise. (jump lyndapride)
2. I’m happy to help! (jump playertech)
3. I really enjoyed playing with this thing. It’s cool. (jump playertech)

**label lyndapride**

**$ lynda_rating =+ 1**

M “You know, I think you actually know more than you're giving yourself credit, Lynda.”

“Lynda’s face drops for a moment.”

L “You think so? Huh.”

“She looks over the device, now clearly playing colourful sequences from Alice in Wonderland.”

L “I feel like the team is just so adept and knowledgeable about these things compared to me.”

“She looks at you with a smile and a wink.”

L “Maybe that’s just me getting older.”

L “Anyway, I’ve kept you long enough. I’m sure you’d like some of your evening to yourself!”

“You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her.”

**jump lyndaboxend**

**label playertech**

M “No problem! I enjoyed it.”

L “Me too. It was less daunting than I expected in the end.”

“Treacle comes to investigate the quietly whirring device. Lynda switches it off and shoos her away from the ever-tempting-to-cat-brain cubes.”

L “I’ve kept you for enough of your evening, you should head home - but thank you, again.”

“You finish up with the device and say bye to Lynda for the evening. She sends you off with a small haul of beauty goods that her old co-workers sent her.”

**jump lyndainteraction3**

**label lyndaboxend**

show lynda_rating

“Thanks for playing this sequence!”

return
