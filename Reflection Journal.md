## Reflective Journal

### From the Top, and a little late...

#### 04-11-2024

This is probably a little late to be writing the first reflective journal entry, but better late than never! Also, I'll never judge anyone with inconsistent updates 
on projects ever again - remembering to do this requires an alarm clock or something.

After successfully pitching Project: Self to the Behaviour Grant Committee, I'm getting to make my dissertation game with supplementary pay and support from an 
amazing group of makers. This is particularly special because it is the first time I've won a grant! Yay me! So between now and Sept 2025 I'll be working on 
this game, though I'll likely be using an earlier version of the game for the actual dissertation chapter I plan to write about the game, so that I can wrap this
PhD swiftly. 

#### What is the game?

Project: Self (working title) is a "dating" sim, interactive fiction game about nurturing your relationships with the parts of you that need reconciling and impact 
your self-esteem and persona. Procrastination, your inner child, rage, defence (defense?) mechanisms, and impostor syndrome. This all takes place in a building 
that wants to form a tenancy group to hold the landlord responsible for not fixing the various issues in the building. The player's goal is to get each of the NPCs 
to sign up to be a part of this group, but they each have a reason to want to avoid doing so. You build a non-romantic relationship with each of these personified traits to 
gain insights as to why and encourage them to sign up. 

#### What are my goals?

1. A game that conveys emotionally mature material through a light-hearted experience.
2. Players to walk away from the experience being able to identify each of the characters' themes - or closely identify them.
3. A closer examination as to how a game shifts from start to finish, especially when built around emotional game design.

I might add to these as I go, but for now these are my foundational ones. 

Also, I don't have a specific plan as to when I'll update these reflective journals (something we've discussed at length in the GaR project), but I'll try to at least once a month! It depends on how much momentum there is at a time.

### She's committiiiiing

#### 09-12-2024

I've officially added the game file to the main (?) branch. There was a lot of Googling to make sure this didn't break anything, because "fetch" and "staging" are completely new words to me. But it is there! And now in theory, when I update the script (which I will now check) it will push here. There's a weird fumbling vulnerability with all of this, where I know folks are very aware and familiar with how to do this and I truly feel like I am taking my first Bambi-style steps into it all. In the same vein, I'm not converting this from a docs file, I'm typing it right into the code editor. Maybe that'll do something funky with the commits, idk. I'm definitely going to get things wrong, and need some guidance in keeping this all relatively sensical (in terms of where commits are coming from and pushes etc.) but I'm happy it didn't take me too long to set this up! I am going to edit the test script I have to see if it does anything, and I also have more reflections/updates that I'll need to do retroactively this week (I have two demo-weeks worth of feedback I'd like to document). With many plates spinning it definitely feels like a routine is necessary to avoid these reflections being somewhat scattered, but equally just in developing the game, it is a little haphazard and "when I have time" like the dissertation. I think this is just the plight of the contemporary grad student though. As I wrap this up, I will note that I did suggest a monthly update, so I'm SORT OF on track in that light. yay. Okay, off to see if edits, commits, and pushes are doing what they should.

### Feedback before the holidays

#### 13-12-2024

So the first prototype/build hit itch.io this week! I had a bunch of folks at the Behaviour meeting give their feedback (I'm writing it after the session so that it is fresh and forcing good reflective practice). I presented the prototype with a couple of questions:

1. Without knowing what the character Lynda represents in terms of restraints towards self-esteem, what do you think she is thematically?
Responses I got included: hypervigilant, insecure, gives up easily, and writes herself off quickly. Which is supremely interesting as Lynda is embodying impostor syndrome. Perhaps I can build to this being more obvious, or allow this more open-ended non-specific take on the character!
**Maybe it is more about what does this character facilitates in terms of thoughts and reflections around her persona?**

2. How do we feel about the dialogue options not telling you what the outcome of your choice is (i.e. "help/not help Lynda")?
I didn't actually get any specific feedback on this! Will need to continue not including it to see how folks feel.

The remaining feedback can be ordered like so:

**General Responses**
Mostly the feedback was positive! Folks felt the story was relatable, cosy, and some of them want to be allowed to date the characters (a frequent tension I'm noticing - I might do a bigger write-up on this in the future). The comedic pacing worked well for folks also, which makes me happy. The facial reactions even of the placeholder twinned with the writing (her face drops) compounded the complexity of emotions going through Lynda's mind, which is what I wanted!!! Yay payoff!!

**Character Customisation (Skills and Proficiency)**
Folks liked shaping their character through dialogue choices rather than through a potential skill selection menu. We discussed how flags would make even the writing easier, so I don't have to account for all the different kinds of skills, and rather have them appear in the narrative as I see fit or make sense contextually.

**Natural Conversational Flow**
I floated the idea of looping menus, so that the player can select all the dialogue options to get insights into more things (in this case, information about the other NPCs) - however - the feedback was folks preferred having a more natural flow of conversation. Not just "click all options". Instead, you have to be thoughtful about the conversation choices you make. Like a dialogue economy of sorts.

We chatted about how Ren'Py doesn't have a visualisation plug-in, which SUCKS, so coding hygiene and best practices are going to REALLY matter for this game project.

So, the game is (as a prototype of one scene) definitely affective. There's an investment in the character, and that is GREAT this early. The identification of themes is pretty loose right now, but it is also extremely early days into the prototype. Next steps is making another scene, perhaps with a different character, or setting up the full introduction before the inciting incident. 

### Feedback 2.0 - Scoping is hard

#### 04-02-2025

I've been writing the "meet the gang" opening to the game script, and started to very quickly realise:

I am one human.
I only write so fast.
I have a dissertation.
My current script would need 50 scenes written and coded into Ren'Py.

...

See the concern?

So, I wrote as much as I could for the opening, and came to the table asking for feedback on the writing's tone (i.e. is it consistent) and then asked for help scaling all of it down into a good vertical slice with the following conditions:

1. I can get it done for end of August.
2. It offers a strong portfolio piece to potential studios.
3. It works towards my goals for the game.

The feedback on the writing itself was great! Folks really enjoy the tone of the narrative, and that (most of - sorry Jasper, I'm working on you) the characters are compelling to interact with. Each of them offered a memorable moment during the interaction. Also, apparently my attention to detail in the writing is "insane" (the cardboard box of jumpers being safe to drop and sit on was cited). We also got into questions about the player character: who are they? Are they a distinct person, or a shell to be filled? One person noted that even Harry in Disco Elysium, despite his gripes, is a white, heteronormative, cop. We can play him differently, but who he is fundamentally still shapes his responses. By having a more defined player character, I can cut down a lot of extra work in trying to make them an open, empty shell for players to decide everything for. In the same vein, player choices can be limited too - building up to a more impactful option A or B can have a great payoff if done well. (I also got kudos on making one of the dialogue choices simple and the other being a hyperexaggerated version in "share" and "overshare" with Jasper, as a way to break from the binary yes/no options).

I think a lot of my character and narrative design is based around having some similarities and familiarities to what has come before in visual novels, while also subverting expectations a bit to challenge myself as a designer and to offer (maybe) more impactful gameplay experience. Not selecting all the dialogue options and then moving on, or taking the good/bad choice route, I think I'm trying to create a more dynamic and natural feel to the conversations with these characters - partly because I know they stem from certain themes and I don't want them to be one-note. Also because so many games now present dialogue choices with three tones: anger/abrasive, funny/lighthearted, and compassionate/kind (looking at Horizon and DA:Veilguard as recent examples). Not sure why it bothers me, maybe it is a flattening of a character response, maybe it just doesn't feel impactful if I keep picking a certain one it doesn't seem to change anything other than how I want to personify the player character.

I've flicked away and back to this a couple of times in the last 20 mins, so I think this is all I have for this reflection entry. Oh, actually - one last thing about *scope*. Once I've hashed out what a vertical slice could look like, I'll spend time coding it into Ren'Py, and MDM that experience (over a week was the suggestion), to give some insight into how it will actually go for more than one scene. Then I can kill my relative darlings and adjust from there.

**Next steps...**
- Who is the player character?
- Who should I focus on for the vertical slice?
- What is the ending, and write it.
