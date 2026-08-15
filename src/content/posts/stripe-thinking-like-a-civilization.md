---
title: "Stripe: Thinking Like a Civilization"
date: 2023-08-11T18:32:00Z
category: reading
description: "In Patrick and John Collison, Stripe has two framers thinking at a civilization-level. This is rare, even among tech’s boldest executives. With the exception..."
source: "https://www.generalist.com/briefing/stripe"
---

In Patrick and John Collison, Stripe has two framers thinking at a civilization-level. This is rare, even among tech’s boldest executives. With the exception of Musk, Bezos, and Buterin, no founder is constructing an empire with quite the same thousand-year stare or detailed, architectural love as the Siblings Stripe.

More than anything else it is this horizonal focus that defines Stripe, guiding its remarkable recruitment, celebrated culture, and sophisticated product strategy.
Stripe’s mission to “increase the GDP of the Internet” is impelled by powerful global tailwinds
### Origins: Permissionless Entrepreneurship
#### Early days
In April of this year, Patrick tweeted his discovery that one of the authors of a computer science book entitled Electronic Payments Systems for E-Commerce once lived in the brother’s childhood home.

In 2006, using an SAT score from a test he’d taken at the age of 13 (an infuriating anecdote), Patrick matriculated to Lisp’s birthplace: the Massachusetts Institute of Technology. He’d sped through the final two years of his high school curriculum in just twenty days.
#### Shuppa and Auctomactic
In 2007, the brothers founded “Shuppa,” a play on the Irish word “siopa” for shop.

At the incubator, the Collisons were encouraged to join forces with another precocious duo, united by family bonds.

In the end, Live Current Media, an owner of premium domain names like Communicate.com and Brazil.com, won out paying $5 million for the business. Patrick and John became young millionaires

Even great founders take years to internalize the fact that entrepreneurship is permissionless, an open door that anyone, no matter how junior, can walk through, and that no shame will (or should) cling or mark those that venture and fail. The ease with which the Collisons intuited this indicates a precocity of wisdom even more impressive than their prodigious intellect.
#### /dev/payments
John having now matriculated to Harvard — by building mobile apps. It was in earning money through this relatively seamless method that the brothers realized what a mess processing payments was elsewhere on the internet.

Almost a decade after PayPal had entered the space in 1998 and ostensibly “solved” the problem, the state of play remained byzantine and punitive, requiring considerable administrative work and holding funds for weeks at a time.

In realizing the brokenness, the Collisons overcame what Paul Graham once described as “[Schlep Blindness](http://www.paulgraham.com/schlep.html)”:
> There are great startup ideas lying around unexploited right under our noses. One reason we don't see them is a phenomenon I call schlep blindness. Schlep was originally a Yiddish word but has passed into general use in the US. It means a tedious, unpleasant task…
>
> The most striking example I know of schlep blindness is Stripe, or rather Stripe's idea. For over a decade, every hacker who'd ever had to process payments online knew how painful the experience was. Thousands of people must have known about this problem. And yet when they started startups, they decided to build recipe sites, or aggregators for local events. Why? Why work on problems few care much about and no one will pay for, when you could fix one of the most important components of the world's infrastructure? Because schlep blindness prevented people from even considering the idea of fixing payments.

As [Patrick would note in conversation with John Lilly](https://www.youtube.com/watch?v=qrDZhAxpKrQ), the Collisons initial goal was to create “Slicehost for payments,” emulating the ease of spinning up new servers with service.
beginning in 2009. They even had a “super awesome, cool” name for it: /dev/payments.

it emphasize one of the Collisons’ keenest insights — that developers, not businesspeople
Patrick and John raised a $20,000+ round from previous backer, Y Combinator.

The YC network proved a particularly useful way to find first customers. Two weeks after the Collisons released an MVP, /dev/payments processed its first transaction, with Ross Boucher of 280 North the first to use the system. As Boucher remembers, the first transaction was for $40.00. Apparently, 280 North was using PayPal, but Patrick offered to write the code to switch the company over to/dev/payments.

the company had roughly 30 customers from the incubator, growing further through word of mouth. As Patrick would later tell, product/market fit on /dev/payment’s first product proved almost “instant.”

in name, /dev/payments did not last. Though the Collisons had, characteristically, done their research to ensure corporations were allowed to use a slash in their name
That name proved particularly off-putting to the stuffier bankers at Wells Fargo that Patrick and John attempted to woo.

To fulfill transactions, Patrick and John had to fill out forms manually with the transacting customer’s information, then send them onto the financial platform.

In the end, the team made a decision through default. Brockman declared that if a better alternative couldn’t be agreed upon within a week, /dev/payments would become Stripe. In its simplicity, allusion to a credit card’s strip, nod to lines of code, and inference of frictionless speed, it proved the perfect appellation for the company to come.
#### Stripe
Before scaling, Stripe would first need to solve its banking issue. Once again, a Y Combinator connection proved the ace in the hole.

So developer-centric was Stripe’s culture that the Collisons found it troubling to hire someone non-technical. “But he doesn’t code,” Patrick recounted saying.

What followed is too eventful to be adequately summarized. Since its inception in 2009
the Collisons have guided the company to a $95 billion valuation, raising over $2 billion
### Product: Type 0 to 1
Carlin Vieri, another MIT matriculant, coined the term “yak shaving” to refer to problems that arise in the course of trying to solve a problem. As described by fellow researcher, Jeremy Brown:
> You see, yak shaving is what you are doing when you're doing some stupid, fiddly little task that bears no obvious relationship to what you're supposed to be working on, but yet a chain of twelve causal relations links what you're doing to the original meta-task.

According to Patrick, company engineer Avi Bryant refers to Stripe as the “greatest yak shave of all time.” In seeking to solve one problem (processing payments) dozens of others emerged; by trying to facilitate seamless online payments, Stripe revealed the need for fraud detection, card issuing, financing, and more.

It’s intriguing to look at these projects along a timeline:

Maintaining existing products at increased scale while onboarding, culturally inculcating, and training new members takes up considerable bandwidth, making new launches difficult.
#### GPTN
Starting in 2018, Stripe began describing its suite as a Global Payments Treasury Network, or GPTN.

Though less memorable than Stripe’s guiding imperative to “increase the GDP of the internet,” GPTN gets at the same point — providing universal infrastructure for a diverse range of financial interactions.

The current product suite fits well, though not completely, within this framework:

In that respect, Stripe feels almost like a fork of the Kardashev Scale. Soviet astrophysicist Nikolai Kardashev proposed a tiered model for civilization, related to energy usage. Type 1 civilizations could use and store all available energy on their planet, Type 2 civilizations could do the same across their solar system, and Type 3 could manage across their galaxy. According to Kardashev, Earth was a Type 0 civilization, yet to unlock the power of its comely blue dot.
Other thinkers forked Kardashev’s framework, with Robert Zubrin suggesting the scale could apply to “mastery” of planets and beyond, while Carl Sagan framed it in the context of the information.

Not every product fits within GPTN, of course. Atlas, Capital, Issuing, and other business lines sit outside this central engine but play critical roles in the company’s expansion and counter-positioning.
#### Offense and defense
Stripe Atlas, launched in 2016.

Marqeta, one of Stripe’s competitors, has used its impressive card issuing business to bolster a payments play with companies like Brex and Ramp impinging via corporate cards. By providing alternative solutions, Stripe protects its core payments business, while adding new sources of revenue and even expanding margin.
#### Margin expansion as mille-feuille
Payments are a low-margin business. By adding a constellation of other products, Stripe is able to extract more basis points (BPS) from the same customer. As explained by one former employee:
> There can be a case, if you are successful with these software products... you could easily see that it brings you quite a decent margin. If all of your customers use Stripe Radar, it's like another two BPS.

Many of Stripe’s products can be seen as another layer of cream on top of the payments pastry. Here are the charges different business lines levy:
- Payments: 2.9% + 30c per transaction
- Connect: $2 per user / 0.25% + 25¢ per payout
- Atlas: $500
- Radar: 5c per transaction
- Sigma: 1.4c - 2c per charge / $0-$100+ per month
- Billing: 0.5 - 0.8% on recurring charges
- Issuing: 10c virtual card/ $3 per physical card/ 0.2% + $0.20 per transaction
- Terminal: 2.7% + 5¢ per transaction
- Tax: 0.4 - 0.5% per transaction
#### Detail and delight
As Byrne Hobart noted in his rather [wonderful analysis of the company](https://diff.substack.com/p/stripe), “Stripe is part of an interesting category of value-creating companies whose offering is to make some process work the way you'd imagine it worked if you had never actually tried to do it yourself.”

From design to functionality, every aspect of Stripe’s suite seems to have been worried over, honed, polished. Indeed, [one of Stripe’s values](https://newsletter.bringthedonuts.com/p/building-products-at-stripe) is to “really, really care.”

For goddess sake’s, Stripe’s landing page is not only achingly gorgeous — inspiration for a wave of gradient chasers — but even thoughtful enough to offer an Easter Egg.

If you go to Stripe.com and enter the old “Konami code” (↑ ↑ ↓ ↓ ← → ← → B A) here’s what you’ll see:

Visit Stripe Terminal and enter the code “4242” and here’s what happens:
### Leadership: An Unusual Morality
If Silicon Valley’s ethics can be distilled into a coherent ethics, this is it: do what is necessary to change the world, no matter how many toes are trampled, privacy rights violated, or human norms deranged.
This is the ethos of Kalanick and Zuckerberg, and many tribute acts. It could not be further from the morality of the Collisons.

Patrick and John seem to adhere to a deontological ethics. This school, best articulated by glorious weirdo Immanuel Kant, suggests that the morality of an action is determined independently of its outcome.

Just as Patrick notes that the “no jerks policy” companies sometimes apply to restrain themselves from hiring brilliant assholes is “too low a bar,” Stripe’s leadership seems to understand that success alone is not enough. You have to win with grace.
#### Patrick
As one former GM noted, Patrick obsessively studied what created generational companies:
> [He’d research] things like, what was Amazon doing in 1999? And what things were they doing back then that are very big now, and how many years did it take them to get there? So how should we think about our software and services?...And when, along the way, did [Amazon] feel like, "Okay, we're onto something, this makes sense or should we actually kill it?"

According to the same GM, a rumor circled Stripe that during a meeting with Elon Musk, Patrick disagreed with the SpaceX founder about rockets. Though the former employee wasn’t sure whether the anecdote was true or not, it almost didn’t matter — it was plausible to everyone that Patrick would not only know about rocket engines but know enough to intelligibly debate Elon Musk.

One of Patrick’s particular academic interests is “Progress Studies,” a field he hopes to advance in coordination with George Mason’s Tyler Cowen. As outlined [in an Atlantic op-ed](https://www.theatlantic.com/science/archive/2019/07/we-need-new-science-progress/594946/), Progress Studies seeks to “get better at knowing how to get better.”

Patrick’s mission. Stripe is not just a capitalist enterprise, but an endeavor to drive humanity forward.
Patrick’s intellect is matched by a humility rarely seen among elite entrepreneurs...he deflects attention from himself and reinforces the notion that Stripe is defined by its many employees, rather than its fraternal heads.

Patrick also does rotations with different teams to better understand frontline work:
> [O]ne of the cool things he did, too, was he would do a quarterly rotation with a random part of the organization and work as a team member on that part of the org as a grunt. So he did a sales rotation, he did an engineering rotation, marketing, where he was just the grunt on those teams doing a small project.
>
> And then he would take that feedback back to the execs and the Board and just have a good eagle eye on what was happening, which I thought was really cool.

Patrick proximity to the nuts and bolts of the business, information that he seems to store encyclopedically.
> [A]t any given time, especially when we were smaller, [Patrick] could ask about a particular deal you were working on, and he knew about that company and how they should be using Stripe…[H]e took the time to actually be plugged into the technology and the products and the business. I think you felt like when he made a comment about how a product should work or the user experience should work, you actually knew that he had spent the time...some other executives I've interacted with are just kind of a talking head.

The final point to make about Patrick is perhaps the least visible: he is extremely ambitious.
That’s perhaps because he doesn’t appear driven by either money or power — employees note he is not someone with a flash car or boat — but simply by the challenge.
> Patrick always wanted Stripe to be compared to Amazon or Google, he didn't want to be compared to...API-based companies…[H]is aspiration was for Stripe to be a global behemoth…[Not] a company that he sold to another business or a company that just went IPO and kind of flat line.
#### John
the younger Collison is more easygoing and effusive.

There’s a reason that John tends to be the more visible of the pair, jumping onto podcasts, or agreeing to interviews. From a former GM:
> [A]ll the PR and all the interviews are mostly done by John, because John is actually more funny, more social, more nimble, more jokey. And when you ask Patrick a difficult question in an interview, he'll just keep still for 15 seconds and think about a really smart response, and then you'll get a response of one sentence of three minutes with five words you never thought you heard before.

He seems to be particularly fascinated by the corporate world, with a particular interest in conglomerates, including two Generalist favorites [LVMH](https://www.readthegeneralist.com/briefing/lvmh-the-civil-savage) and [Constellation Software](https://www.readthegeneralist.com/briefing/constellation), and their ability to grow via acquisition.
#### Claire
Claire joining the company in 2014 and taking on the mantle of COO.
After beginning her career in politics, serving as the Deputy Campaign Manager for Massachusetts gubernatorial candidate Scott Harshbarger, Claire pivoted into the business world. Joining Google in 2004, she rose through the ranks to become VP of Global Online Sales, then VP of Google Offers, and finally VP of Google[X] and the company’s self-driving cars division.

she appears to exhibit much of the Collisons ecumenical intelligence (she was an English major at Brown before her peripatetic path to tech), high EQ, and pursuit of ideologically meaningful work.
> I really love reading about sports...there’s a binary win or lose. And so I love reading about amazing players and amazing coaches and team environments. How did they create that amazing will to win?

Claire highlights a particular profile of American Football coach Bill Parcells:
> The thing that this coach is looking for is when the center will hold. I think that when you think about great companies, it’s like, all of these things happen that you didn’t predict. Maybe the rules change while you’re playing the game. But mostly, you don’t know what’s going to happen on the other side, on the external team piece. But at a really great company, the center holds.
### Culture: Taking the Long View
#### Multi-decade vision
Stripe doesn’t have explicit plans for the next several millennia, but the company has succeeded in shifting employee mindset to think further ahead. In [an interview with Ken Norton](https://www.bringthedonuts.com/essays/building-products-at-stripe/), Business Lead Michael Siliski articulated this trait:
> We talk a lot about building multi-decade abstractions. I personally like to think 10 to 30 years to get out of the three- to five-year mode, but generally here people do say “multi-decade” a lot. Patrick and John and the entire leadership team are clear that this is a long-term bet and that we’re still very early. That long time horizon comes from the top, and it’s in the culture. And my sense is it’s been like that at Stripe since day one.

Others make the same note. From Patio11:
> [M]y career success metric is making a large improvement in the lives of a large number of software people. I encourage anyone who isn’t already planning on a 45 year time scale to try taking a stab at this and reviewing the plan every year; the weeks are long but the years fly by sometimes.
>
> At present I’m at Stripe because I think it is probably the best option available in working against those long-term goals. 15 years down; 30+ to go; still early innings.
#### User-driven
As product manager [Jeff Weinstein noted in a tweet](https://twitter.com/jeff_weinstein/status/1141154179274219520):
> One of the few sins you can commit at Stripe is not talking to users. Thankfully it’s nearly a panacea for all tricky situations. I mean you need to be texting with them. What's the founder's pet's name? Get all up in their lives style [sic] user first.

Though nearly every company suggests a “customer-first” approach, few seem to embrace it as thoroughly as Stripe. ([One exception, of course, is Coupang](https://www.readthegeneralist.com/briefing/coupang), who are true psychopaths. That is a compliment.)
#### Writing-first
Jeff Bezos famously banned Amazon employees from relying on PowerPoint presentations. His rationale was that written memos forced clearer, deeper thinking. Presentations could be pettifogged with animations, visuals, and a sparkling delivery; doing so with the stern monochromatism of a dossier was much trickier.
Stripe has adopted the same approach.
#### Painful transparency
In Stripe’s early days, every employee was blind copied on every single email. That meant that if a customer service rep could read what Patrick had just emailed John about. And, of course, Patrick could see what you’d just sent to a customer.

As Patrick described it, this kept standards high across the organization and encouraged a culture of constant, multi-directional feedback. Employees would correct each other’s delivery, spelling, grammar — anything was up for discussion.

This is an audaciously blunt (brutal?) approach. Every action can be critiqued by every other person, workplace privacy evaporates, and employees are required to triage an insane stream of information. One intern noted that she received “about 2,000 emails” in her first week.

And yet, it seems to work (or did for a time). Though it may have required more employees, it ensured information spread across the organization, discouraging the creation of silos and helping ideas bloom from the bottom up.
#### Exacting standards
Working nights and weekends seems to be a common expectation and the most frequent complaint on [the company’s Glassdoor page](https://www.glassdoor.com/Reviews/Stripe-Reviews-E671932_P4.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng) is the lack of work/life balance. One poster remarked:
> Stripe prides itself on being understaffed, to the point that it is a core principle: "efficiency as leverage.” There is an unsustainable workload and the work pressure on individuals and teams is unreasonable. There is a common feeling of burnout in the company, with workload only increasing since Covid.

Pragmatically, there’s likely another benefit of this intensity — it attracts a certain type of high-performer that enjoys the challenge of thriving in difficult circumstances and enjoys being surrounded by others of a similar disposition.
#### Artifex Rex
there’s still the sense that this is an organization where engineers and builders rule; artifex rex.
### Management: Edge Administration
In its decentralization, broad dispersion of information, and pushing of strategic thinking downwards, Stripe operates with something like “edge administration.”

The best example of this came from a friend of mine, David Phelps. In discussing Stripe, he shared his takeaways from a recent encounter he’d had with a member of the customer support team.
> [O]ne thing that’s always impressed me about Stripe is that their CS people always operate as though they’re CEOs. They talk a bit about their lives, talk about the vision of the company, offer to run projections, and offer to negotiate deals to support. I’d like to think that that means we’re a big deal to them, but I’m pretty confident that’s not the case. My support referred to herself as a “payments nerd” and talked about “Patrick” and how he always writes long and thoughtful emails the exact same way he gives interviews.

Everyone within Stripe is encouraged to think deeply, strategically, and bring their best, most ambitious ideas to the fore, no matter where in the company they come from.

titles are “used to keep score.” Maintaining a degree of fluidity and vagueness is useful in thwarting internal empire-building, and emboldening employees to speak up.
### Brand: Masters of Soft Power
As adroitly pointed out by Packy McCormick [in his lovely breakdown of the company](https://www.notboring.co/p/stripe-the-internets-most-undervalued-ec3), Stripe is a brand with near-universal appeal, wooing developers, designers, and the rest. No other company in the space gets close. (Square’s Cash App, though only tangentially related, might be an exception, though in a minor key.)
This comes down to two core reasons. First, Stripe prides itself on its “taste.” Second, the company is a master of soft power.
#### Taste
From the start, Stripe had a sense of style. Even its 2011 website is admirably clean and rather appealing.
#### Soft power
There’s a cynical tint to the phrase “soft power.” In Stripe’s case, that Machiavellian element seems largely absent.
Stripe Press is arguably the most intriguing.
Increment is a similar endeavor. A print and digital magazine about “how teams build and operate software systems at scale,” Increment serves to populate ideas Stripe considers important, and reinforce the company’s thought leadership.
In spring of 2017, Stripe purchased Indie Hackers, a community for builders taking a non-venture track.

Stripe Climate is the most altruistic. Via Climate, customers can easily redirect a portion of revenue to environmental initiatives chosen by Stripe. What’s so impressive about the endeavor is the thought that’s gone into it. While many other businesses might have passed on the selection responsibility to another organization, Stripe has assembled a coterie of experts and researchers to allocate funds to achieve maximum impact.
### Investing & M&A: Outposts and Emissaries
That’s because of Fast, a company that purports to be building the fastest checkout experience. The business has built up a large following on social media (and a plenty of detractors) through endless blitz-posting, aggressive meme’ing, and explicit growth hacking.
They’re also one of Stripe’s investments.
This is perhaps the most remarkable part of Stripe’s venture investing: they transparently back companies they will almost certainly compete with. In some cases, Stripe invests and then outright acquires the business a few years later.
#### Venture investing
In an [interview with Ben Thompson](https://stratechery.com/2020/an-interview-with-stripe-president-john-collison/), John highlighted the activity of some of China’s tech conglomerates as a source of inspiration.

Stripe’s two rules for investing:
1. Focus. They have to be part of Stripe’s focus and expertise. That usually means increasing the GDP of the internet, particularly with reference to payments.
2. Genuine return opportunity. They have the potential to make money.

an exception to Rule 1, which is that Stripe will also invest in businesses founded by former employees.
Stripe has announced investments in 21 companies, across geographies.

According to those with knowledge, Stripe takes an entirely straightforward approach in these conversations, noting that while it’s possible they might move into the company’s space, the internet is usually a big enough place to allow for multiple winners, and that Stripe cannot dominate all of it.
This is a refrain [Patrick has repeated](https://twitter.com/patrickc/status/1375612742258683910?lang=en):
As Stripe grows, we want to avoid the “we must win everything” mindset that can easily set in. We’d rather help enable a successful ecosystem… it’s a big, abundant world out there.
Ben Thompson describes [Stripe as the “platform of platforms,”](https://stratechery.com/2020/stripe-platform-of-platforms/)
#### M&A
Stripe has made 11 acquisitions to date. As you would expect, many of these purchases seem to have been rolled into internal product development.

#### Next moves
I expect Stripe to invest in the near-term.
- Insurance. This is one of the most lucrative parts of the financial world and one that Stripe has yet to touch.
- Brazil. Stripe is currently in “Preview” in the country, meaning they are operating on a trial basis.
- Indonesia. As it stands, Stripe does not operate in Indonesia.
### Risks: Yes, There is a Bear Case
This is a relatively young company, operating in a highly competitive space, valued at nearly $100 billion (more in secondary transactions).
in comparison to its closest rival, Adyen, Stripe looks cheap.

it is growing revenue at ~2x Adyen’s speed and commanding a lower multiple.

If Stripe is to struggle, it may come from its ambition. The company has a lot of products and is trying to win both the top and bottom of the market.
#### Doing all the things
Stripe’s range is impressive. The product suite is expansive and the company is able to serve tiny companies (like The Generalist) to major corporations like Amazon. As [Packy notes](https://www.notboring.co/p/stripe-the-internets-most-undervalued-ec3), that’s a conscious choice by the company, and something Patrick hammered during his Sessions 2019 edition.
#### Payment margins
Because payment processing is (mostly) a commodity, there is [significant pricing pressure](https://www.theglobaltreasurer.com/2019/09/18/slow-payment-transformation-risks-shrinking-margins-further/) on companies in the space. If Stripe offers you a 1% processing fee, but Adyen proposes 0.5%, is there enough product differentiation to pay twice as much?
#### Maturing out
A downside in serving enterprise companies is that there’s always an alternative to the solution you offer: building in-house.
Airbnb, for example, took the steps to build out a bespoke payment system for its marketplace.
According to a former Airbnb employee with knowledge of the project, Stripe was considered as a provider, but the team decided building a platform themselves would give them greater control, customization, and, of course, reduce fees in the long-run.
#### Competition
In 20 years, all of the companies mentioned below may be an order of magnitude larger than they are today.

#### Major characters
Adyen is Stripe’s most direct competition. Founded a few years before the Collison’s creation, the Dutch company has a robust offering, particularly for enterprise. On three critical dimensions, Adyen appears to have an advantage over Stripe.
- Country coverage. Stripe has 44 countries live.
- Payment methods coverage. The same individual noted Stripe offered support for ~40 payment methods, with only ~15 shipped in the last three years. Meanwhile, Adyen supports ~200.
- POS. Though Stripe offers Terminal, it is said to be an inferior product to Adyen’s POS solution.

 the ex-GM noted that Adyen had been thinking about an omnichannel approach for a much longer time than Stripe:
> The difference is with omnichannel, and that's where I think Adyen has a big gateway. Just like Stripe has way more experience and a proven product on Stripe Connect and marketplaces, Adyen has a way more proven product on point of sale terminals. If I recall correctly, already 6 years ago, people were saying "everybody at Adyen is talking about the bricks and clicks. Yeah, we need to invest in a seamless integration of unified commerce between online and offline." That shows you how important already omnichannel was for Adyen and how many years of building they put into POS.
That has helped Adyen seal deals with companies like McDonald’s and Starbucks.

In the POS space, Stripe also competes with Square. It remains to be seen how seriously Stripe takes offline commerce  — it may decide to allow others to dominate that space while it pulls away in online transactions.

PayPal represents a multi-dimensional competitor. In particular, its Braintree division directly competes with Stripe. But PayPal has not shown much of an ability to drive forward the product suites of its acquisitions. Venmo has been a desperate disappointment, effectively unchanged since being picked up (via Braintree), and Braintree itself is a static product, despite being a financial success. Stripe will believe they can continue out-operating the subsidiary.

Marqeta is a formidable adversary on the card issuing front. After IPO’ing this week, the company jumped to a $16 billion market cap. That’s a fair way beneath Stripe’s size, but the Oakland firm is said to have a better issuing system.

Plaid. One would imagine that the Collison brothers were almost as happy about the mooted Visa deal as Plaid’s investors. The breakdown of the acquisition puts them back in the game, and accumulating growth capital. As I proposed in our piece “Plaid’s Quiet End Run,” the company has the chance to fundamentally alter the traditional payment process, providing “pay by bank” services. That reconfiguration would give Plaid enormous leverage and might disturb Stripe’s operations.

The payments industry is an expensive one in which to operate with a trend of declining margins, and while Stripe’s product suite may provide some differentiation, it may also prove a distraction.
### Growth: The Road to $1 Trillion
what would it take for Stripe to join the likes of Amazon, Apple, and Microsoft to become a trillion dollar company? How could Stripe feasibly 10x?
#### Macro
1. The internet’s kind of a big deal.
2. There are still a lot of people who are not online.
3. Those that are online still buy most stuff offline.
4. Those that are online still buy most stuff offline.
5. As more people come online, Stripe will power more transactions.
6. As people buy a bigger proportion of things online, Stripe will power even more transactions.

Stripe’s team suggests that the digital economy is currently 5-6% of the total economy (the [US is pegged at around ~7%](https://apps.bea.gov/scb/2019/05-may/0519-digital-economy.htm#:~:text=For%20example%2C%20in%202017%2C%20the,percent%20growth%20in%20real%20GDP.) per the Bureau of Economic Analysis). If the majority of commerce is eventually conducted online, Stripe has the potential to power 10x the number of transactions.

Simultaneously, only [60% of the world’s population](https://wearesocial.com/blog/2021/04/60-percent-of-the-worlds-population-is-now-online) has access to the internet.

There are major national markets the company has yet to crack:
Of the world’s 25 largest countries by GDP, Stripe is essentially non-operational in ten of them.
#### Micro
Though the company offers payments processing in 44 countries, much of the rest of the suite is restricted.
In this respect, Stripe’s growth can be visualized in waves. As products take off in one market, the company can subsequently roll them out across its remaining geographies.
