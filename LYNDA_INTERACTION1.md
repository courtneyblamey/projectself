**label lyndainteraction1**

"You re-enter the building after an evening walk, making most of the remaining daylight at dusk and prepare to climb the stairs. A woman emerges from the stairwell holding a laundry basket."

"She looks to be in her late 40s, with some hints of grey in her hair wrapped up into a messy bun, though it looks so done with intention that it looks tidy."

"A set of well-manicured nails peek overtop the laundry basket handle and a gentle smell of lavender lingers in the air."

L "I thought I heard some chatter this morning outside my window - are you the one I heard telling someone 'no one will steal my stuff from the sidewalk it's 10am'?"

"You recall a joking exchange between yourself and your friend over ferrying things indoors when they had to leave. They looked guilty, but you didn't want them to worry. Plus, stealing is a night crime, everyone knows that."

M "Hah, yes that was me."

"The woman extends her hand out."

L "Lynda."

M "&lt;playername>."

L "Well, welcome to the building, &lt;playername>. I'm glad no one stole your things."

L "How are you liking it so far?"


## **CHOICE**



1. I'm adjusting
2. Better than my last place!


### I'm adjusting

M "I'm getting used to it. Once I've spent a few nights here, it'll feel a bit more like home, right?"

L "Of course! It takes some time."

**set $BuildingPastGood = True**

**jump lyndabye1**


### Better than my last place!

M "Well, it's already better than my last place!"

"A flash of concern flits across Lynda's expression."

L "Oh, really? What was wrong with your place before?"

**set $BuildingPastGood = False**


## **CHOICE**



1. Noisy neighbours
2. General disrepair
3. Frequent fire alarms
4. All of the above


### Noisy neighbours

M "It was a classic thin-walls-EDM-loving-party-neighbours situation. Didn't get much sleep."

L "Oh dear… luckily everyone in this building tends to be respectful of volume. Unless there's some kind of sports on. Antony is very into his sports."

M "What kind of sports?"

L "No idea."

"She laughs."

L "All I know is if the referee could hear him, they would be blushing."

M "Oh… oh dear."

M "Well, I moved to avoid it all, so let's hope it'll work out here!"

**jump lyndabye1**


### General disrepair

M "I think the building was held together with duct tape and dreams by the time I left…"

"Another look of concern from Lynda."

M "What?"

L "Hm? No, nothing, I just- this building has its quirks."

M "As in, sometimes the doors get stuck in the summer, or more, we've had multiple gas leaks? Because my old place existed across that spectrum of experiences."

L "...then you'll be fine!"

M "Well, I moved to avoid it all, so let's hope so!"

**jump lyndabye1**


### Frequent fire alarms

M "I think I've stood in rain, snow, and shine multiple times due to people setting off the fire alarm with toast or cigarettes or one time a birthday cake candle situation"

L "You won't have to worry about that here, the last time it was set off was months ago with a very real fire, but they contained it quickly. Someone left something on the stove and it was a warning and reminder enough to us all to be vigilant."

M "Yikes."

M "Well, I moved to avoid that kind of thing, so I'm looking forward to not waking up to beeping!"

**jump lyndabye1**


### All of the above

M "I mean, the building may as well have been Grey Sloan Memorial Hospital with the amount of tragedies that hit it."

L "Oh dear… well then I think you'll be just fine here!"

M "Well, I moved to avoid it all, so let's hope so!"

**jump lyndabye1**

**label lyndabye1**

**if $BuildingPastGood = True**

L "Well, nice to meet you, and see you around the building!"

M "Nice to meet you, Lynda!"

"You both head off to your apartments for the night."

**jump lyndainteraction2**

**else**

L "It's been nice chatting, &lt;playername> but this laundry isn't going to fold itself, unfortunately."

M "No worries at all."

L "See you around the building!"

"You both head off to your apartments for the night."

**jump lyndainteraction2**
