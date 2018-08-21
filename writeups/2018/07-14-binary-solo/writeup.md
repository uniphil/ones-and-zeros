## Ones and Zeros: first run writeup

On July 14<sup>th</sup> 2018, seven people crowded into my living room for the first Ones and Zeros workshop.
This project has been in development since I attended the NYC [School for Poetic Computation](http://sfpc.io) sprint 2018 session, and based on the success of this first run, I hope to keep developing it further.
This documentation is intended to record what happened at the workshop, summarize the feedback, and lay some groundwork for transparency and accountability into the Ones and Zeros project.

Feedback was collected twice: once as a group (over watermelon!) immediately following the workshop, and again individually through [a survey](https://airtable.com/shr6xgtVOrodeTksj).
(linked here to show the questions, wording, and format. Please don't submit responses unless you were there :) ).

The follow-up individual feedback survey proved to be valuable, especially for criticism.
This comment, for example, highlights some room for improvment in my teachng style, which was not brought up in group feeback:
A
> Splitting people into groups was a good idea, but sometimes it felt like one group (esp. folks sitting at the larger table) would get more instruction / attention while others waited / craned their necks to see what was going on

This document is mostly a first-person account (hi! I'm [Phil Schleihauf](https://uniphil.github.io)), and all commentary here is my own opinion.
The TA for this workshop was [Riley Shaw](https://rileyjshaw.com).
Quoted text in this document comes from the individual feedback surveys.


### Timeline

- May 23: went from rough sketches to developing the workshop in earnest
- July 1: practiced the first half of the slide deck with one volunteer, initial feedback
- July 14: first run: six attendees, myself, and one TA.


### Introductions

We did a quick name/pronouns/ice cream flavour round for everyone.
It did the job, especially since many people already knew several other attendees.
In the future I'd like to have name-tags, and maybe a more creative activity.

The code of conduct and social rules were received positively and enthusiastically!
In the group feedback, Riley brought up that the social rules at RC are introduced with short skits, which seems like a fantastic idea to try copying.

All participants except Riley and I had little to no prior programming experience.


### The workshop

I used two themes for the presentation: light for core content, dark for technical digressions.
This was inspired by a teaching tech unconference session at a !!con, and worked very well.

![The light and dark slide themes used](./slide-formats.png)

> I thought the slide format worked well and I like the switch between purple/white.

Two suggestions for improvement were broughg up in group feedback:

1. Temporarily switch the presentation to the dark theme for unplanned digressions (with slid.es it can be entirely blacked-out with one keypress, hopefully sufficient)
2. Take it further, maybe I can put on a purple hat or something for digressions.

The room was set up in a "landscape" layout, with the presentation screen in the middle of one of the longer walls.
This made the space feel collaborative (everyone was facing in, no table was behind another), but was not optimal for the presentation.

> Obviously this is not possible in the current space, but at times it was hard to see/read the screen from the side table where I was sitting.

It might still work in this layout with a projector that can create a larger image.


#### Base 10 to base 2

Explaining how counting in binary works went smoothly.
I showed the [animated base system counter thing](https://codepen.io/uniphil/full/QQBEzx/) that I made at SFPC as part of the explanation, and received enthusiastic feedback about it in group feedback.
People actually asked for it to go faster ("once you see how base 9 works, it's a small jump to base 2"), which is great!

> Learning about how binary works blew my mind.

> The base number system conversation was a bit too long.

The digressions about binary->decimal conversion and hexadecimal kept peoples's interest.
The feedback from the July 1<sup>st</sup> practice to avoid slowing down at that part helped.

> explanation! (response to "things that went well")


#### Brainstorming sending messages with 1s and 0s

People suggested new, really creative ways to encode messages with 1s and 0s.
I love seeing what people come up with.

> group brainstorms (response to "things that went well")


#### Setting up the hardware

I didn't actually have enough power adapters capabale of powering the printers, and was hoping a few people would bring some we could use.
That didn't happen.
The printers need a high-current, 6-9V supply, which is a little unusual.
I might make some 8V power regulator boards so that we can use the 12V and 20V supplies people bring in.

> Having more reliable and/or consistent hardware.

We had an unplannded discussion about reading the backs of power adapters, which was interesting, but too much to include before the first break.
Bringing and reading adapters is still fun (for me at least), but maybe maybe it can be part of the intro/greeting time instead.

The printers themselves were finicky.
The nano and guts versions were not happy with the large 5v supply I had, though the mini at least partially worked.
We'll stick to the mini version in the future.

I was worried about having different types of arduino around, but in the group feedback, Riley suggested that this is a good place to show some variety.
Selecting the right board in the IDE isn't hard, and it's a useful exercise.
And it's cool to see the different ones!

People bringing their own laptops worked out fine.
One person had a chromebook, and successfully used the arduino web IDE with it.
(though, reading Serial had some start-up delay).


#### Snack break (bits and bites)

I don't know if anyone likes the bits and bites/bits and bytes joke, but they're delicious enough to keep doing :)

> Bits and bytes were tasty af!


#### Decoding the binary solo

This section felt fun.
One participant (who usually avoids tech altogether) got *really* into it.
Another enjoyed it even though they didn't know the flight of the conchords reference.

The ascii table on screen was too small.
In the group feedback, Riley suggested making a table with *only* decimal and ascii chars.

> Text on TV was still a bit small for ASCII chart etc. Hand out booklets earlier?

I made little booklets with ASCII charts.

- The binary numbers were off by one, which was a fun mistake to have a discussion about, but made them pretty annoying to use&hellip;
- They should have come out earlier.
- People didn't take them home &ndash; In the future I'll emphasize that people can take home whatever paper stuff they want to keep.

In group feedback we talked about the opportunity to do more with the chart booklet: it could be a little zine that summarizes the concepts covered in the workshop.
In future workshops I'll pre-load the zine as a sketch on all arduinos, which we'll print out at the "powering things up" step before the first break!


#### Sending messages over serial to the computer

After hooking everything up, we loaded a tiny sketch onto the arduinos that simply opened a serial connection and sent a message, 'HELLO', defined as a series of bytes (in `0b01001011` literal style) over serial.
Then, we used the ASCII charts to customize and create new messages to send to the computer.

> using arduino (response under "things that went well")

This was fun!
Being in pairs especially worked well here.

One participant created a message that was many thousands of bytes long (an expert at copy/paste) which crashed the compiler and generally caused trouble that, unfortunately, we never got working.
It would have been a great moment to talk about loops in programming, but other things that were going on distracted me.


#### Playing with the thermal printers

Everyone wanted more time:

> I wish I had more time with it.

> more time for creative activity at the end

> More hands on time would have been really handy, the idea for a sandbox period at the end of the workshop would be really nice.

> Having more time to play around at the end.

And, fortunately, we will normally ahve more time!

- We started about 30 mins behind schedule. I think this can be solved through communication.
- I let the breaks go long.
- A few slides and discussions are going to be cut based on feedback.
- We went right into a long group feedback session at the end.

In terms of actual activities, I had only prepared two arduino sketches to start from: a binary message (expanding on the serial exercise) and a 16x16 bitmap image.
I've already created a few more, and hopefully we'll collect more and improve them as more workshops go.

> The printing pictures idea was really cool but also it seemed like we touched on it and then never really engaged in depth/engaged with it. It would have been cool if we were to try and code in a really simple emoji like a smiley face, or a letter.

This workshop doesn't teach programming, but just asks attendees to jump in and start hacking on pre-written code.
This was a little bit of a gamble, but it worked very well!
Working in pairs was effective for simple debugging, even though everything was so new.


### Critical views of tech

We got into it a little bit, but I'd like to add more.
We talked a little about how ASCII can only encode the latin alphabet, and Riley added some insights about how unicode still encodes certain biased defaults that can have real impacts on things people use, like the twitter tweet-length limit.


### Handling questions

I think I did pretty well at keeping the flow going by answering questions either immediately when they came up, or deferring and promising that they would be answered soon (and doing so) &ndash; another strategy from the !!con session.

> I think you are a great teacher! You did a good job anticipating the questions we would have.

We got into a little discussion about the jacquard loom, from a question about "why base 2".
From group feedback, having pictures of the loom and punch cards (esp. the card reading machine) would have been an improvement.
Since it's not part of the slides (though I'll add it if it keeps coming up), a google images search to illustrate probably would have helped.
My whiteboard illustrating skills are not amazing.

> After the workshop ended I liked being able to follow up on some more technical questions (like ground, etc.) so in your future workshops I like the idea of not only office hours but time immediately after the workshop ends to ask those kinds of questions and mess around more with the printers.


### Lunch

> Breaks were well timed and delicious.

I'm not going to be modest: the food was really good, and I think it helped keep everyone in a good mood, important for the workshop.
I don't plan to cut corners here.


### Location

I had imagined that running this out of my living room would just be a scrappy way to get some experience with the workshop before finding more professional locations to work out of, but the feedback about it was positive.

> Home-y environment (response to "things that went well")

On the other hand, it was a very hot day and my home has no AC.

> Temperature was a bit warm


### The future

In response to "How likely is it that you would recommend this workshop to a friend?", three people chose 10/10 stars and two chose 8/10.
From an 8/10 response:

> I (and anyone else at the first workshop) want to support this so am happy to actually recommend this to real folx

I think word of mouth will be the most important way that Ones and Zeros can grow, so this is encouraging.
Positive responses to the "Why or why not?" follow-up focused mainly on learning:

> it's a easy intro to something you have always been curious about but never had the time or opportunity to learn on your own

> Great intro to topics that seem scary, might trigger a chain reaction of learning

Hesitations touched on accessibility:

> It's a time and money commitment that not everyone can make


### Money

> Since this will be a pretty big commitment for folx to attend, it's worth thinking about what the "value prop" is. I would LOVE for it to remain "this stuff is cool and more accessible than folx think, and I'm a good teacher, so curious learners can come do workshops". For something like that, that's less skills/employment based, it could really be worth partnering with a library or government grant so that a) you stay paid and b) more folx can attend.

Grant applications are in the works, and seem like a good fit for keeping costs down.

The disposable costs for this workshop are very reasonable on a per-person basis, so it doesn't need to charge high rates.

#### Materials already owned

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
Most of the big tickets were for reusable equimpent &ndash; the per-student disposable costs are fairly low.

I hope to pa the TA for all future workshops, which will be the biggest new expense.
Graduate-level teaching assistant rates are [around $44/hr](http://www.2626.ca/your-rights/salary-rates/).


### Outcomes

The goals of the workshop were met!

> I had fun!

> Everyone seemed to leave with a really positive experience / mood

> Friendly, good pace, fun way to spend a day

> Considerable breadth covered for just a couple of hours

> [another attendee] feels SO accomplished and proud!!!

> it was so approachable and accessible!


![Panorama of the classroom](./jul18-pano.jpg)
