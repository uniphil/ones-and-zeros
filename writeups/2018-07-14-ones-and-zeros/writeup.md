## Ones and Zeros: first run writeup

On July 14<sup>th</sup> 2018, seven people crowded into my living with me for the first Ones and Zeros workshop.
This project has been in development since I attended the NYC [School for Poetic Computation](http://sfpc.io) sprint 2018 session, and based on the success of this first run, I hope to keep developing it further.

This documentation is intended to record what happened at the workshop, summarize the feedback, and lay some groundwork for transparency and accountability into the Ones and Zeros project.

Feedback was collected twice: once as a group (over watermelon!) immediately following the workshop, and again individually through [a survey](https://airtable.com/shr6xgtVOrodeTksj).
(linked here to show the questions, wording, and format. Please don't submit responses unless you were there :) ).

The follow-up individual feedback survey proved to be valuable, especially for criticism.
This comment highlights a teaching style problem that I didn't notice and want to fix, and was not brought up in the group feedback:
A
> Splitting people into groups was a good idea, but sometimes it felt like one group (esp. folks sitting at the larger table) would get more instruction / attention while others waited / craned their necks to see what was going on

This is mostly written in first-person. Hi! I'm [Phil Schleihauf](https://uniphil.github.io). The TA for this workshop was [Riley Shaw](https://rileyjshaw.com). All quoted text in the document comes from the individual feedback surveys.

### Timeline

- May 23: went from rough sketches to developing the workshop in earnest
- July 1: practiced the first half of the slide deck with one volunteer, initial feedback
- July 14: first run: six attendees, myself, and one TA.


### Attendance

My initial plan was for a test group of six for the first run. Nine people (plus Riley, TA) actually signed up for the workshop, but

- 1 extra person (who was crashing at my house) attended last-minute
- 1 person who had signed up dropped out three days before the workshop
- 2 more people dropped out the morning-of

Having people drop out last minute is not a good sign, and could make it hard to plan, especially with hardware constraints putting caps on how many people can be accommodated at a given workshop, however:

- All three who dropped out were under very specific, very extenuating circumstances.
- All expressed regret and a desire to attend at the next chance.
- Everyone who signed up was a close friend &ndash; the workshop was not framed in detail in advance.
- This workshop was run for free.

So, I don't think there's useful information from these numbers to predict how reliably people will show up for future workshops.


#### Showing up

The workshop started late, which was not surprising for the casual nature of the group. Everyone who came showed up by about 10:15.

It would probably be worth communicating the start time as a window for coffee and snacks instead of a hard start time.


### Introductions

Many attendees knew each other prior to the workshop. In the future, get name-tags and plan a better intro activity.
If people are asked to bring old power adapters again, reading them could be part of the causal introduction period.
Maybe something with the name-tags&hellip;

The code of conduct and social rules were received really positively and enthusiastically.
In the group feedback, Riley brought up that the social rules at RC are introduced with short skits.
This seems like a great idea to copy!
The skits can be figured out in prep with the TA before next time.


### The workshop

People generally liked the slides.
I used two themes for the presentation: a light-background one for core content, and a dark-background one for technical digressions.
This was informed by some discussion about teaching tech at a !!con unconference session I attended.

> I thought the slide format worked well and I like the switch between purple/white.

In group feedback, we talked about taking this even further: we could put on purple hats or something whenever we get into digressions.

Also, that it would be useful to make the screen purple for unplanned technical digressions.
Slid.es makes it easy to black-out the screen, which might be enough.
Especially if we do hats.

The room was set up in a "landscape" layout, with the presentation screen in the middle of one of the longer walls.
This made the space feel collaborative (everyone was facing in, no table was behind another), but was not optimal for the presentation.

> Obviously this is not possible in the current space, but at times it was hard to see/read the screen from the side table where I was sitting.

It might still work in this layout with a projector that can create a much larger image.


#### Base 10 to base 2

Explaining how counting in binary works went smoothly, everyone picked it up pretty quickly.
I showed the [animated base system counter thing](https://codepen.io/uniphil/full/QQBEzx/) that I made at SFPC as part of the explanation, and received enthusiastic feedback about it in group feedback.
Also, people asked for it to go faster (once you see how base 9 works, it's a small jump to base 2).

> Learning about how binary works blew my mind.

> The base number system conversation was a bit too long.

This is exciting: at SFPC, we spent a whole day introducing binary, and while more content was covered (converting to decimal in detail, addition, &hellip;), some of the basics were still confusing to some of my classmates at the end.

The digressions about binary->decimal conversion and hexadecimal went well.
I managed not to get into the weeds (thanks to feedback from the Jul 1 practice run), and they didn't seem to add to much of a burden for participants.


#### Brainstorming sending messages with 1s and 0s

People came up with new, really creative ways to encode messages with 1s and 0s.
We didn't talk much about this part in feedback, but I will definitely keep this part for at least selfish reasons, it's one of my favourite parts.
(and I think it probably was helpful&hellip;)

> group brainstorms (response to "things that went well")


#### Setting up the hardware

I didn't actually have enough power supplies up to spec for all the printers, and was hoping a few people would bring some we could use.
I did an unplanned discussion about reading the back of the adapters, which I would not do again.
Bringing in adapters is fun for me at least, so I think I'll keep doing that, but maybe build it into the greeting as people arrive. hehe.

> Having more reliable and/or consistent hardware.

The printers themselves were more finicky than expected.
The nano and guts versions were not at all happy with the 5v supply, but the mini ones at least worked.
Test page bugged out, but we could print.
In the future, I'll only use mini printers.
They work better, and having consistent hardware there means we can step through their hookup as a group.

I was worried about having a variety of types of arduino around, but in the group feedback we figured this is a good place to have variety.
Selecting the right board isn't hard, and it's a useful exercise.
And it's cool to see the different ones!

People bringing their own laptops worked out fine.
Since people are in pairs, it's ok if a few people don't bring one.
One person had a chromebook, and successfully used the arduino web IDE with it.
I didn't personally see this get set up (TA helped), so I'd still have to sit with it to try problems.
But it worked!
Serial communication had small problems with this one though, needed to add a delay at the start to catch short one-off messages.

I did a little "proof" thing with one of the arduinos once we got the "blink" sketch running on it, disconnecting it from the computer and running it off a USB power supply, to&hellip; prove that it was really running the code we just uploaded.
No one needed this proved to them haha.
They weren't impressed.
Don't need to do this.


#### Snack break (bits and bites)

I don't know if the bits and bites/bits and bytes joke is enough to make it worth all the effort of making a huge batch of bits and bytes for everyone, but they're delicious and whatever so I'm going to keep doing so.

> Bits and bytes were tasty af!


#### Decoding the binary solo

Ukulele solo feels weird and out of place but people liked it a lot and I guess weird and out of place can be unexpected and delightful...

Decoding the binary solo was fun.
One participant who I did not expect to be the most engaged got *really* into it.
Another enjoyed it even though they didn't know the flight of the conchords reference.

The ascii table on screen was horrible and not readable by anyone.
I knew it was bad but couldn't think of anything good.
I think we solved this in the group feedback though: make a table that is *just* decimal and ascii chars.
I was stuck on how to keep binary in without making it a mess.

> Text on TV was still a bit small for ASCII chart etc. Hand out booklets earlier?

I made little booklets with ASCII charts.

- The binary numbers were off-by-one, which was a wonderful mistake to talk about, but made them pretty annoying to use&hellip;
- They should have come out earlier (maybe have them be out right from the start).
- People didn't take them home (I forgot to say they could). In the future I'll emphasize that people can take home whatever paper stuff they want to keep, because I think some would have.

In group feedback we talked about the opportunity to do more with the chart booklet: it could be a little zine that summarizes all of the lessons.

I've since taken that awesome idea to its logical next step for this workshop, and sketched up some arduino code that prints a little zine and ascii chart on the thermal printers.
I think it fits in if it's pre-loaded on the arduinos, and is the first thing we do when we hook everything up after the first slides!
A few people from the workshop who have seen it loved it, and I'm unreasonably excited about this.

> explanation! (response to "things that went well")


#### Sending messages over serial to the computer

After hooking everything up, we loaded a tiny sketch onto the arduinos that simply opened a serial connection and sent a message, 'HELLO', defined as a series of bytes (in `0b01001011` literal style) over serial.
Then, we let people use the ASCII charts to customize the message that gets sent to the computer.

> using arduino (response under "things that went well")

This was fun!
Being in pairs especially worked well here.

One person had an issue that they believed they by changing whitespace in their code.
I could get better at my "well it's great that it works, but I'm not sure if that was the real problem" reaction.

Another very quickly copy/pasted until they had an absolutely massive sequence of bytes that crashed the compiler and generally caused trouble that, unfortunately, we never got working.
It would have been a great moment to talk about loops.
Kind of sad I missed that chance.


#### Playing with the thermal printers

Five for five on the feedback on this one:

> I wish I had more time with it.

> more time for creative activity at the end

> More hands on time would have been really handy, the idea for a sandbox period at the end of the workshop would be really nice.

> The printing pictures idea was really cool but also it seemed like we touched on it and then never really engaged in depth/engaged with it. It would have been cool if we were to try and code in a really simple emoji like a smiley face, or a letter.

> Having more time to play around at the end.

The workshop ran long.
For now, I'm not too worried about fixing this:

- We started about 30 mins behind schedule. As mentioned above, I'll specify the start time as a window for coffee and introductions, so we can start closer to the scheduled time.
- I didn't keep the breaks contained at all. I don't want to make them too short, but I think we could get probably another 30 mins back here.
- There were a few digressions and parts of the workshop that are being reduced or cut. At least 15 mins worth, maybe 30.
- We went right into a long group feedback session at the end. It can be a lot more flexible once all planned parts of the workshop are over.

In terms of actual activities, I had only prepared two arduino sketches to start from: a binary message one (like the serial exercise) and a 16x16 bitmap one.
I've already created a few more, and hopefully we'll collect more and improve them as more workshops go.

Oh yeah and, all of the participants (except the TA) had no or very little prior experience with programming.
This workshop doesn't teach programming, but just asks attendees to jump in and start hacking on pre-written code.
This was a little bit of a gamble, but it worked great!

At the same time, in group feedback, people didn't feel like they had "actually programmed" anything.
I think that's ok, but hope to give people more confidence that programming is really what they did!


### Critical views of tech

We got into it a little bit, but I'd like to add more.
We talked a little about how ASCII can only encode the latin alphabet, and Riley added some insights about how unicode still encodes certain biased defaults that can have real impacts on things people use, like the twitter tweet-length limit.
It would be great to have more discussion around this stuff.


### Handling questions

I think I did pretty well at keeping the flow going by answering questions either immediately when they came up, or deferring and promising that they would be answered soon (and doing so), another strategy suggested in the !!con session.

> I think you are a great teacher! You did a good job anticipating the questions we would have.

We got into a little discussion about the jacquard loom, from a question about "why base 2".
Is this question always going to come up?
Pictures of the loom and punch cards (esp. the card reading machine) would have been really good, from group feedback.
If this doesn't become part of the slides, google images would probably have been enough (and awesome).
My whiteboard illustrating skills are not amazing.

> After the workshop ended I liked being able to follow up on some more technical questions (like ground, etc.) so in your future workshops I like the idea of not only office hours but time immediately after the workshop ends to ask those kinds of questions and mess around more with the printers.


### Lunch

> Breaks were well timed and delicious.

I'm not going to be modest: the food was really good, and I think it helped keep everyone in a good mood, which was great for the workshop.
I don't plan to cut corners here.


### Location

I had imagined that running this out of my living room would just be a scrappy way to get some experience with the workshop before finding more professional locations to work out of, but I'm rethinking that.

> Home-y environment (response to "things that went well")

The unprofessional aspect of running it out of a house actually sort of fits the theme.
There are definitely other environments that would work really well, but at a minimum they should have a good kitchen.
Never underestimate the value of a good kitchen in creative spaces.

On the other hand, it was a very hot day and my home has no AC.

> Temperature was a bit warm


### Outcomes

People apparently had a good time

> I had fun!

> Everyone seemed to leave with a really positive experience / mood

> Friendly, good pace, fun way to spend a day

&hellip;and learned things :)

> Considerable breadth covered for just a couple of hours

> [another attendee] feels SO accomplished and proud!!!

> it was so approachable and accessible!


### The future

Running the best workshops and classes I can is my primary goal with Ones and Zeros, but I'm pretty sure the thing that will make or break it is communicating its value and attracting an audience.
Marketing, essentially.
Unfortunately.

In response to "How likely is it that you would recommend this workshop to a friend?", three people chose 10/10 stars and two chose 8/10.
One of the 8-star responders (considered "passive" in NPS) wrote,

> I (and anyone else at the first workshop) want to support this so am happy to actually recommend this to real folx

I think word of mouth will be the most important way that Ones and Zeros can grow, so this is encouraging.
Positive responses to the "Why or why not?" follow-up focused mainly on learning:

> it's a easy intro to something you have always been curious about but never had the time or opportunity to learn on your own

> Great intro to topics that seem scary, might trigger a chain reaction of learning

And included some hesitations:

> It's a local event, which is awesome, but also restricts to Kingston residents

> It's a time and money commitment that not everyone can make

I hope to run workshops in Kingston, Toronto, and Ottawa to start, and I believe there is an audience for this in each of those places.
At least I hope.


### Money

> Since this will be a pretty big commitment for folx to attend, it's worth thinking about what the "value prop" is. I would LOVE for it to remain "this stuff is cool and more accessible than folx think, and I'm a good teacher, so curious learners can come do workshops". For something like that, that's less skills/employment based, it could really be worth partnering with a library or government grant so that a) you stay paid and b) more folx can attend.

Grant applications are in the works.
This is new to me so I don't know what to expect, but it does seem like there is a money available for things like Ones and Zeros.

The disposable costs for this workshop are very reasonable on a per-person basis, but the up-front costs are steep: each thermal printer alone costs $50 USD, plus shipping and import charges.

#### Materials we had prior to the workshop

- One "mini" thermal printer
- One thermal printer "guts" (Riley)
- Many arduinos
- A couple breadboards
- A whiteboard
- Some food staples, spices, and condiments
- Lined paper
- Pens


#### Expenses

- $50 USD: One "mini" thermal printer
- $45 USD: One "nano" thermal printer
- $12 USD: 2 breadboards
- $3 USD: male-male strip headers
- $18 USD: digital multimeter

**tech total: $128 USD**

- $30: groceries for bits and bites
- $97: groceries for lunch

**food total: $127**

- $3.30: Printing (code of conduct, social rules, washroom sign, xkcd comic, tweet from Loren Schmidt, photo releases, ascii table booklets)
- $5: whiteboard markers
- $80: car rental to pick up some of the materials

**other supplies total: $88**

This workshop was free, so there was no revenue.

I've paid about $400 CAD out of pocket so far to run the first workshop, or almost $70 per student.
I expect some of these items to reduce significantly in future runs.

- the car rental fee was a one-off to pick up my whiteboard (it was a multi-purpose trip, so perhaps $25 would be a more fairer line-item in the expenses)
- all of the tech items can be reused over many workshop runs.
- I over-spent on the groceries: the bits and bites recipe makes at least 3&ndash;4x more than we needed, and there was probably 50-100% more lunch food than necessary.

However, there will be more large expenses:

- We're only going to use the "mini" thermal printers in the future, and I only have two. At two people/per printer, it's at least $25 USD per person to expand the size of workshops. (I have three more printers already ordered, so we're set for workshops up to 10 people for now).
- I want to pay any TAs for from now on. Graduate-level teaching assistant rates are [around $44/hr](http://www.2626.ca/your-rights/salary-rates/) (5 hours: $220).
- I'll need to start paying myself at some point to keep this going. SFPC shares [some information](https://github.com/SFPC/finance-and-administration/tree/master/2018#teacher-fee) about teacher pay.
- Running workshops in three cities will mean travel fees.

Finding out how much people will pay for workshops, how many will need financial assistance, and how much I can get in grants for this are all exciting things ahead to figure out!
