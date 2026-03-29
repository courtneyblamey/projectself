**label lyndainteraction1**

"You re-enter the building after an evening walk, making most of the remaining daylight at dusk and prepare to climb the stairs. There's a notice board in the entrance littered with 'for sale' furniture posters, business cards, and a couple hand-scrawled notes."

MENU:



1. Read 'laundry room'
2. Read 'disposal of goods'
3. Read 'pipe issues'
4. Read 'noise notice''

LAUNDRY ROOM

"*Dear tenants, as of the new rent cycle please be advised that the cost of laundry will increase by 1$. We have installed a new change machine to assist in this adjustment.* scrawled beneath it reads: *don't bother, none of the machines work anyway!!!!*"

m "Uh oh."

DISPOSAL

"*Can we get some more garbage bins?! We're having to pile laundry in the garage and the raccoons are having a field day with all the bags.*"

m "Raccoons are criminals, but cute and hungry tiny criminals."

PIPE ISSUES

"*Has anyone else noticed weird groaning sounds when running their sink? Come knock at apartment 7 - Lynda*"

NOISE

"*Dear tenants, we have been made aware that there is a beeping noise coming from inside the electrical room of the building. This is nothing to be concerned about and nothing can be done to silence it. With that in mind please do not email us about the beeping.*"

"A slight concern rises in your stomach."

"A woman emerges from the stairwell holding a laundry basket, startling you."

m "OH!"

l "Oh no, sorry!"

m "No, I'm sorry, I was just checking out this board and got lost reading."

"She looks to be in her late 40s, with some hints of grey in her hair wrapped up into a messy bun, though it looks so done with intention that it looks tidy."

"A set of well-manicured nails peek overtop the laundry basket handle and a gentle smell of laundry detergent waftslavender lingers in the air."

l "I thought I heard some chatter this morning outside my window - are you the one I heard telling someone 'no one will steal my stuff from the sidewalk it's 10am'?"

"You recall a joking exchange between yourself and your friend over ferrying things indoors when they had to leave. They looked guilty, but you didn't want them to worry. Plus, stealing is a night crime, everyone knows that."

m "Hah, yes that was me."

"The woman extends her hand out."

l "Lynda."

m "&lt;playername>."

l "Well, welcome to the building, &lt;playername>. I'm glad no one stole your things."

l "How are you liking it so far?"


## **MENU**



1. I'm adjusting
2. Better than my last place!


### I'm adjusting

m "I'm getting used to it. Once I've spent a few nights here, it'll feel a bit more like home, right?"

l "Of course! It takes some time."

**set $ BuildingPastGood = True**

**jump lyndabye1**


### Better than my last place!

m "Well, it's already better than my last place!"

"A flash of concern flits across Lynda's expression."

l "Oh, really? What was wrong with your place before?"

**set $ BuildingPastGood = False**


## **MENU**



1. Noisy neighbours
2. General disrepair
3. Frequent fire alarms
4. All of the above


### Noisy neighbours

m "It was a classic thin-walls-EDM-loving-party-neighbours situation. Didn't get much sleep."

l "Oh dear… luckily everyone in this building tends to be respectful of volume. Unless there's some kind of sports on. Antony is very into his sports."

m "What kind of sports?"

l "No idea."

"She laughs."

l "All I know is if the referee could hear him, they would be blushing."

m "Oh… oh dear."

m "Well, I moved to avoid it all, so let's hope it'll work out here!"

**jump lyndabye1**


### General disrepair

m "I think the building was held together with duct tape and dreams by the time I left…"

"Another look of concern from Lynda."

m "What?"

l "Hm? No, nothing, I just- this building has its quirks."

m "As in, sometimes the doors get stuck in the summer, or more, we've had multiple gas leaks? Because my old place existed across that spectrum of experiences."

l "...then you'll be fine!"

m "Well, I moved to avoid it all, so let's hope so!"

**jump lyndabye1**


### Frequent fire alarms

m "I think I've stood in rain, snow, and shine multiple times due to people setting off the fire alarm with toast or cigarettes or one time a birthday cake candle situation"

l "You won't have to worry about that here, the last time it was set off was months ago with a very real fire, but they contained it quickly. Someone left something on the stove and it was a warning and reminder enough to us all to be vigilant."

m "Yikes."

m "Well, I moved to avoid that kind of thing, so I'm looking forward to not waking up to beeping!"

**jump lyndabye1**


### All of the above

m "I mean, the building may as well have been Grey Sloan Memorial Hospital with the amount of tragedies that hit it."

l "Oh dear… well then I think you'll be just fine here!"

m "Well, I moved to avoid it all, so let's hope so!"

**jump lyndabye1**

**label lyndabye1**

**if $ BuildingPastGood = True**

l "Well, nice to meet you, and see you around the building!"

m "Nice to meet you, Lynda!"

Lynda starts to walk away, but pivots back to you.

l "Hey, uh, if you have any issues in the building, I just want to warn you that building management isn't great at dealing with things."

m "Oh, really? We had a tenant's association in my last building, which helped with that."

l "Like a union?"

m "Sort of! Collective action and power to deal with an absentee landlord."

l "Huh. Honestly, that might not be a bad thing for here."

m "Hmm… Well, hopefully it isn't necessary!"

"There's a pause."

l "Okay, well, see you round! Laundry still not folding itself."

m "See ya!"

"You both head off to your apartments for the night."

"You close your new apartment door behind you and take in your new space again. Some of your boxes still need unpacking but the bed is made and you're feeling ready to sleep."

m "Shower first. Fresh sheets, new apartment, clean pyjamas. The perfect rest trifecta."

"You undress and crank the shower on."

"The water dribbles out."

m "Maybe it needs a second."

"The pressure remains the same."

m "Ooookay then."

"You get into the shower and lather up. Upon rinsing some soap from your eyes, you look up and clock a patch of mould across the ceiling."

m "Not ideal."

"Finally, as you exit the shower, you reach for your towel and the rail falls out of the wall fixture."

m "...COOL."

"You dry off and open up your laptop, typing in the search 'how to start a tenants association' with gusto."

m "Okay, how many signatures do I need?"

"*It is recommended to get 50% of tenants signed up to have bargaining power, however, you can start an association with as little as two tenants.*"

m "Okay… so I just need one person to start?"

m "Lynda suggested this, maybe she'd be interested… I'll bring it up when I next see her."

"You spend the rest of the evening checking out how to run the association and details on tenants' rights in general. There's a sense of excitement, even if it means trying to persuade some total strangers to join you on the journey."

**jump lyndainteraction2**

**else**

l "It's been nice chatting, &lt;playername> but this laundry isn't going to fold itself, unfortunately."

m "No worries at all."

l "See you around the building!"

"Lynda starts to walk away, but pivots back to you."

l "Hey, uh, if you have any issues in the building, I just want to warn you that building management isn't great at dealing with things."

m "Oh, really? We had a tenant's association in my last building, which helped with that."

l "Like a union?"

m "Sort of! Collective action and power to deal with an absentee landlord."

l "Huh. Honestly, that might not be a bad thing for here."

m "Hmm… Well, hopefully it isn't necessary!"

"There's a pause."

l "Okay, well, see you round! Laundry still not folding itself."

m "See ya!"

"You both head off to your apartments for the night."

"You close your new apartment door behind you and take in your new space again. Some of your boxes still need unpacking but the bed is made and you're feeling ready to sleep."

m "Shower first. Fresh sheets, new apartment, clean pyjamas. The perfect rest trifecta."

"You undress and crank the shower on."

"The water dribbles out."

m "Maybe it needs a second."

"The pressure remains the same."

m "Ooookay then."

"You get into the shower and lather up. Upon rinsing some soap from your eyes, you look up and clock a patch of mould across the ceiling."

m "Not ideal."

"Finally, as you exit the shower, you reach for your towel and the rail falls out of the wall fixture."

m "...COOL."

"You dry off and open up your laptop, typing in the search 'how to start a tenants association' with gusto."

m "Okay, how many signatures do I need?"

"*It is recommended to get 50% of tenants signed up to have bargaining power, however, you can start an association with as little as two tenants.*"

m "Okay… so I just need one person to start?"

m "Lynda suggested this, maybe she'd be interested… I'll bring it up when I next see her."

"You spend the rest of the evening checking out how to run the association and details on tenants' rights in general. There's a sense of excitement, even if it means trying to persuade some total strangers to join you on the journey."

**jump lyndainteraction2**
