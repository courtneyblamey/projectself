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


### A Design and Writing Sprint - and some retroactive thoughts

#### 25-01-2026

Hello again. Turns out running a non-profit, writing a dissertation, and making a game might be a *bit* much on the old to-do list. I have an immovable deadline to complete my PhD by August, so we traced back the steps and that means this game project needs to be done early March to get playtesting and writing done. So, I'm dedicating chunks of my weekend (don't worry I am resting) to do sprints on this game. 

I've answered one of the questions from the last journal - I'm going to focus on Lynda for the vertical slice. I'm sad to lose some of the mechanics I wanted (dividing time between characters, managing the relationships, and inter-NPC interactions), but this way I can instead provide a deeper connection with one NPC and their struggle, while having the other NPCs maybe guest star for now.

Next I need to ruminate on who the PC is. This is partly scope, to reduce all the options one can make or rather that I feel should be available to a blank slate, but also to help shape their responses. There's a world where I do the writerly thing: write from my experience. There's still variety in responses, but I'm keeping it closer to home. While it is stereotypical for a female/femme character to be a source of empathy or emotional labour, I'm still trying to subvert this in the form of being overly helpful to an NPC wigs them out a bit (a proper documentation of that forthcoming from an archive reflection that I didn't digitise yet.)

Ending wise, I have them for Lynda (in the MEET_THE_TEAM.md), as I continue writing there's a chance they might shift, or have more nuance.

All in all, I've geared up for this sprint, with a game plan in action. Today is story-beating out the events to give myself a framework to write within. Something with a low commitment bar to get the creative ball rolling. I've found doing this effective for the performance anxiety I'm facing when staring at the Mountain of Things To Do. 

### Turns Out its a Marathon

#### 03-03-2026

My lesson of 2026 is that life will continue to happen even when you have Things To Do.

With that in mind, I'm dedicating myself to getting the game fully finished in the next couple of weeks, to then be able to write up my chapter and submit a version of it to FDG's late breaking work (alongside my game demo). I think one of the things MDM has made uncomfortable for me is that the traceability means I am constantly confronting how far behind I am and what Past Courtney thought I should have done by now. Not tracking it means I could generate a facade of getting certain things done, when in reality I could be doing the sprint under the guise of "yeah I have xyz done it should be fine". Instead, you can LITERALLY SEE WHAT MATERIALS I HAVE. I also want to be mindful that this isn't a journal of "woe is me" either. And on that note, allow me to shift to some interim reflective thoughts I've had on the project:

For managing the relationship tracker between the PC and Lynda, I've been grappling with whether I gate off certain interactions (these are in comments in the document that Markdown struggles to transpose). In the spirit of a deeper connection with Lynda, I am going to experiment writing more terse/unfriendly exchanges between Lynda and the PC, which may be shorter, but allows for a realisitic portrayal of the character interactions. I'm curious if there's a way to embed her impostor syndrome into that version of the relationship? Additionally, with the "overly helpful" storyline, there's an opportunity for a variance in what a "low" relationship can manifest as! Lynda might become avoidant of the PC because she feels they're a little overbearing, or avoidant because she doesn't like the PC. We've seen in BG3 some of the "fun" that can be derived from annoying or trying out what negative relationships with NPCs can look like (such as how they interact with you or respond to you when beginning a conversation, or just their general demeanour around you). Since this vertical slice is only with Lynda, I really don't want it to feel binary, like there's a good and bad outcome/choice every time. I'm keeping this all in mind as I set to fleshing out these Event scripts today. The upside of doing this in Ren'Py is that the coding is *relatively* straightforward, so I am not too stressed about getting it into engine. (Don't worry I just knocked on wood).

Finally, I've been playing around in QualCoder for MaDe RA work, and I think it is pretty good! A little janky in places (what software isn't) but I think it will be a suitable format to conduct my QDA for my repo!

### Make Do Push! - Visual Map

#### 05-03-2026

Thanks to the Make Do Meeting this week, I've set up deliverables to have by next week. One of those is a visual map of the game to help myself write what remains.

I've begun to map out the Interaction and Event Scenes to account for the Lynda relationship tracker, the skill variables, and weaving in now a Help/Hinder mechanic where players can be overly helpful and put Lynda off, or help the "right" way and increase their relationship with her. Doing this has made me realise: I, at no point, have introduced the concept of a tenancy board. THE ROOT OF THE PC'S PURPOSE. So! Mapping this out has been *extremely* useful. I've included the images and progress thus far below.

<img width="1024" height="768" alt="Whiteboard Mapping 1_PS" src="https://github.com/user-attachments/assets/8c8ee9d0-a3c1-405f-b8f5-b74f7564d62c" />
WHITEBOARD IMAGE 1
<img width="1024" height="768" alt="Whiteboard Mapping 2_PS" src="https://github.com/user-attachments/assets/fa723815-621b-4f03-88e4-8786ee401be2" />
WHITEBOARD IMAGE 2
<img width="1024" height="768" alt="Whiteboard Mapping 3_PS" src="https://github.com/user-attachments/assets/22c66eeb-82cf-4187-a18f-52f57b2f14e5" />
WHITEBOARD IMAGE 3
<img width="1024" height="768" alt="Whiteboard Mapping 4_PS" src="https://github.com/user-attachments/assets/cb68fa62-7cfa-471d-9980-2170785e1133" />
WHITEBOARD IMAGE 4
<img width="1024" height="768" alt="Whiteboard Mapping 5_PS" src="https://github.com/user-attachments/assets/dc2fe837-7a70-4ac9-99f1-423e60ace34f" />
WHITEBOARD IMAGE 5

I'll continue working on this tomorrow. More to come.

### Visual Map Complete!

#### 06-03-2026

The visual map is complete and I had a couple breakthroughs:

1. Having two separate variables to track the type of help the PC gave was going to get too complicated to code (see Discord image #1) because they could be simultaneous (i.e. +2 in each). So I've altered it to be one variable that is +ve or -ve instead, and once a certain -ve threshold is reached, it permanently impacts the relationship between the NPC and PC.
2. In getting into designing the -ve choice outcomes, I realised that self-doubt is a large component of Imposter Syndrome (thank you to National Library of Medicine for reminding me of this). So as a player, if you keep making comments or doing things that reaffirm this, I thought it would be interesting to have it result in Lynda realising her own capability (in seeing it be seen) helping offset the self-doubt and instead replaced by a level of self-assurance (e.g. "actually, I do have a handle on things!"). This has helped me weave back in her characteristic of IS without having to bash the player over the head with it.

Now that the visual map is completed, I can move into writing the remaining scenes over the weekend with a MUCH clearer sense of how I want to approach each scene and the variables that exist to make use of during the dialogue to keep it feeling dynamic to how the player defines themselves. I don't plan to have this visualised for the demo - but it could be something to design when I port this outside of Ren'Py post-PhD (Ren'Py is good for the time allowance I had to do this and keeping it simple, but it is not a user-friendly interface to use longer term imho).

Onwards!

<img width="1024" height="768" alt="Whiteboard Mapping 6_PS" src="https://github.com/user-attachments/assets/32af244c-541b-4723-88ca-9b1b9ca27c89" />
WHITEBOARD IMAGE 6
<img width="1024" height="768" alt="Whiteboard Mapping 7_PS" src="https://github.com/user-attachments/assets/4ea6b989-8087-4b1d-b34a-32ce2e796da4" />
WHITEBOARD IMAGE 7
<img width="1024" height="768" alt="Whiteboard Mapping 8_PS" src="https://github.com/user-attachments/assets/df4cb804-7851-4106-9fe9-4081fbc2c033" />
WHITEBOARD IMAGE 8
<img width="1024" height="768" alt="Whiteboard Mapping 9_PS" src="https://github.com/user-attachments/assets/d326c0eb-673c-4ed2-baac-6458e6e301f6" />
WHITEBOARD IMAGE 9

<img width="1168" height="116" alt="Screenshot 2026-03-06 at 5 14 55 PM" src="https://github.com/user-attachments/assets/6c6f63a5-e154-4b15-a11b-e49455c80fd1" />
DISCORD IMAGE 1


### Demo Build + Design Conversations Feedback

#### 02-04-2026

#### Demo Build
I put the pedal to the metal over the last two weeks to produce a demo build for FDG 2026. I've had a few scattered scratch pad thoughts, so here's my larger synthesis of them.

One of the things that struck me as I turned the raw script into code was the reminder that I am, in fact, making a *visual* novel. This meant when translating the dialogue into Ren'Py I was more conscientious about overdescribing Lynda's physicality at times. Additionally, I can now see why visual novels need such a variety of emotions on their character assets. Having to use a laughing asset for all "joyful" moments makes me wish I had more assets with nuanced emotions (but since the artist very kindly did this for free in their spare time, I would not ask for more!) 

In debugging, I've been reminded of the importance of variable naming conventions and keeping them consistent across coding (e.g. drinkchoice vs. drink_choice crashed the game) - something I need to revisit and make uniform as I go further anyway. I also kept finding variables without defaults, so I combed my code for all variables and organised them by category and scene title to create a clearer architecture for myself. 

Finally, ahead of the design meeting, I had to remind myself that since I've "lived" with this story and game for so long, it has lost its impact for me entirely. I'm whipping through scenes to test interactions and outputs, skipping certain moments just to jump ahead, but that won't be the case for players and playtesters - it will be their first time interacting with it. Might be a bit obvious to say, but it was something that struck me in the moments when I felt bored by the game content or self-doubting the game.

There's certain finicky polishing I want to do before this goes to the committee:
- add sound
- add splash page
- cleaner transitions between scenes
- nicer itch.io landing page
- checking .md style and replacing with Ren'Py style (for italics)

Because, as much as this is a vertical slice and not a complete game, I want it to have a level of polish to show a certain professionalism to the committee, and also to external folks if this *does* end up on a portfolio in the future.

I feel like this section is missing the "so what" to a certain degree... but anyway.

Importantly, this build is lacking an ending. That is because I don't like what I have currently. So, I brought it to discuss with the design conversations group!

#### Design Conversations Feedback
There were key themes that appeared out of this conversation:
1. Visual Novel genre
2. Player expectations
3. Fourth wall moments
4. Thoughts for the ending

I'll attach images of my note scribbles here also at the end.

For context: one of my biggest design issues is that I d o n o t l i k e t h e e n d i n g. Since the ending is where the "aha" moment resides right now, where the player is confronted with their (potential) kindness towards Lynda and queried if they offer themselves the same level of kindness, it needs to *work*. This is what I presented as the design problematic to the crew.

**Visual Novel Genre**
I was asked, in essence, why a visual novel? For me, it was down to ease of coding, pre-existing examples of subverted expectations in other VN games, and access to an engine *made* for exactly that genre with lots of documentation and tutorials. As someone newly returning to coding, it offered a low skill ceiling to re-enter and make something. I listed games like Hatoful Boyfriend and Doki-Doki Lit Club as games that did something funky with the VN format. The follow up was, how am I subverting it? One of the main ways is that many VNs are dating simulators. The dating sim was initially something I was going to engage with more closely through mechanics of a "love meter", "gifting", and so on. But the realisation of trying to "date" you inner child? That was a no no to try and translate. So, instead I pivoted away from dating, and instead into the idea of this tenant union. Something metaphorical for the mending of self-esteem and taking care of the building together with all your struggles working alongside you. Not letting players date the characters feels like a subversion. Equally, this fourth wall break of "oh you've been really nice to this fictional character, but can you return yourself the favour?" is a moment of subversion too. Where the player is not simply a player-character with the goal of a tenant union, but has in fact been tracked this whole time for the decisions they made and *confronted* with them. It's not "did I get the good ending?" but rather "was I kinder to an NPC than I am to myself?" Going to pause here because I want to ruminate on the next couple of points on the bus ride home.

- ending isn't satisfactory to me yet (feels flippant due to abruptness - thanks Cameron!, doesn't weave through enough of the player reflection opportunities, tenant association feels like a by-product or "oh right" goal)
- Lynda is described as clingy but also still feels like pseudo-dating to others.
- 
