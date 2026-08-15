---
title: "Roneal Desai - CrowdStrike: Cyber SaaS"
date: 2024-07-25T13:39:44Z
category: reading
description: "CrowdStrike, a cybersecurity provider. Founded in 2011 by George Kurtz, the former CTO of McAfee, CrowdStrike differentiated from firewalls and anti malware..."
source: "https://www.joincolossus.com/episodes/79440285/desai-crowdstrike-the-security-cloud?tab=transcript"
---

### Introduction
CrowdStrike, a cybersecurity provider. Founded in 2011 by George Kurtz, the former CTO of McAfee, CrowdStrike differentiated from firewalls and anti malware by building a platform that actively predicts threats rather than blocking attacks that have happened before.
### Size and Scale of CrowdStrike
CrowdStrike is a cloud native cybersecurity vendor that specializes in the endpoint segment of the security market.

now where you need to protect every individual device or laptop as opposed to just protecting one IT estate.
Historically, that was very difficult to do. The development of the cloud allowed the creation of a new type of endpoint security construct where you could put an agent, an agent being a piece of software provided by CrowdStrike that you would download to your laptop or your desktop or your phone. That agent would collect data on not just the actions that you were taking on that device with the internet or with your network, meaning like the things you're downloading or the things you're sending out, but it would also collect data on what was happening on the phone. When you open your mail app on your iPhone, you click on a link that routes you to an application. That's your iPhone mail app talking to the Reddit app, giving you the popup saying, "Do you want to open this in Reddit as opposed to open it in Safari?" Those are apps talking to each other.

So the agent would monitor all of those interactions as well. It would feed all of that information from each endpoint into a single threat graph managed by CrowdStrike, and then they would use machine learning to in a live dynamic way, look out for anomalies in behavior. It could be as simple as, "Hey, this person lives in Southern California and they're getting a packet being sent to them from Russia. That seems weird. Don't accept the packet." But it could also be, "Hey, this app is asking for permissions to be authenticated to send information via an email attachment or something like that that the ESPN app has never asked for the safe password in the middle of the app session." It was a way to go beyond the historical endpoint security, which was basically the McAfee Firewall that we all saw when we got our computers in 1990. That was basically the best thing you had up until the 2015 year. Essentially, CrowdStrike and a handful of other people figured out how to make a much, much, much more intelligent endpoint as opposed to downloading a static application that was told at the very beginning that this is bad and this is good and then just going off of that into perpetuity.

They're currently growing 60% year over year when ServiceNow Workday and Salesforce were at $2 billion of ARR. The three of them were all growing somewhere in the range of high 30s or potentially even low 40s.

customer use cases of what they might have done before CrowdStrike came along and then what CrowdStrike now does for them.

In 2016, when the DNC thought that they might have gotten hacked during the Hillary Clinton, Donald Trump election, they brought in CrowdStrike to see, "Does anything look off to you?" CrowdStrike put an agent on all of the DNC laptops and phones. And then very quickly after observing where traffic was flowing between apps as well as onto the internet, they noticed that a number of apps were sending without the users knowing, information, data, identification codes to servers in Russia. CrowdStrike was then able to crosscheck those other ports or IP addresses along with some of the specific methods to move data around that they were able to identify and were able to then basically trace all of that back to a very specific group of Russian hackers that were known in the CrowdStrike world as Cozy Bear. Then by back tracing the strategies that they had known that group to use in the past, they were able to sort of retrace the steps and figure out what they had done before CrowdStrike had even shown up. We're then able to provide evidence that the FBI, helping the FBI confirm that they had taken information out of the DNC and use that to try and help Donald Trump win the election that year.

Before CrowdStrike got there, presumably the DNC had an endpoint protection software product on all of their phones or laptops, but it was probably something more like than the McAfee Firewall that people saw when they were growing up. The McAfee Firewall said, "Hey you're not sending a virus that we already know about so there's nothing we're going to stop."

### What the Market for Cybersecurity Solutions Looks Like
The old school or the McAfee is almost like TSA airport security. It's like once you've passed that security... You can't bring a drink in with you and you can't bring certain knives in with you, but once you're passed that, theoretically you could do whatever you want and no one's really watching you, versus CrowdStrike is almost like a casino. You may or may not come in, but they're watching the way that you're betting, they're watching what's going on with your winnings, your cards. They're watching all these other things that are happening in order to figure out if something nefarious is happening.

a McAfee Firewall is trying to do the same thing that a supercharged Palo Alto Firewall is, which is just be the gatekeeper of things coming in and out. The McAfee Firewall on our laptop is just 100 thousandth as powerful as the Palo Alto Firewall protecting our offices.

The second being a new module that CrowdStrike helped usher in which is called EDR, endpoint detection and response. And that's much more of what you described, which is actually looking at behavior and actions on the device and looking to see if once you've gotten past TSA, someone's still watching you to see if you're doing something strange. As soon as you walk past TSA, you leave all your bags on the ground and start running off for the bathroom in the opposite direction of the gate that you were just standing at, hopefully a machine learning algorithm could figure out that that's not standard behavior.

Palo Alto has 70,000 customers. They charge 20 to 25% premium above the next option in the market, which would be a Fortinet or a Cisco firewall than there are 70,000 enterprises out there that are willing to pay up for the best and the greatest and know that they have the absolute best of breed available to them from a security perspective.

The largest three of the old guard would be Symantec, McAfee, and a company called Trend Micro. A Symantec customer could be paying $1 per endpoint per month for just the very basic computer antivirus firewall, as opposed to CrowdStrike at list pricing $16 for the next-gen antivirus plus the endpoint detection and response that actually tracks your behavior and then an additional $6 to $22 per month if you want CrowdStrike to monitor that behavior for you.

The two most competitive vendors with CrowdStrike are Microsoft and a company called Sentinel One. Microsoft has a basic free endpoint that comes with their overall Office package. And then if you upgrade all the way to their E5 license, the most expensive one, with that comes their advanced endpoint product. It's called ATP, Advanced Threat Protection. If you're buying an Office E5 license for all the other reasons that you would buy an Office E5 license, and it comes with this free next gen endpoint protection

Like Microsoft could do that, whereas CrowdStrike is cross-checking the behavior of the LA airport with the Houston airport, with the New York airport and all their other 18,000 customers. So, it's a far deeper level of insight.
### CrowdStrike's Founding Story and Secret Sauce
The CEO is George Kurts. He started a cyber security company in the 1990s that ended up being acquired by McAfee. He then became the CTO of McAfee, sort of had a front row seat window into what the endpoint market was and what it was doing and what problems it was solving and where the flaws in it were. He leaves McAfee in 2011 to start CrowdStrike. He is joined by one of his colleagues who became the CTO of CrowdStrike. His name is Dmitri Alperovitch. Coincidentally, also started a security company that was acquired by McAfee. He actually was the father of the trusted source reputation system, which is a very widely used security protocol today. He was the VP of threat research at McAfee. Goes on to be a CrowdStrike CTO. They then name Sean Henry to be the head of their incident response team. Sean had spent 24 years at the FBI. Was the number two guy in charge of all criminal and cyber investigations, as well as all of their international threats and investigations and operations.

two companies that beat them, the first was called Cylance and the setting was called Carbon Black. Cylance had basically said they're just going to focus on the next gen antivirus firewall. 2019 is incredibly important because Cylance gets acquired by Blackberry. Carbon Black gets acquired by VMware, and Symantec, who's the market leader and revenue with about 15% of the market, gets acquired by Broadcom.

In 2014, Sony gets hacked and they decide to call CrowdStrike. CrowdStrike shows up, their endpoint gets downloaded in a day across 40,000 endpoints in multiple countries. They figure out the next day that North Korea was the one who hacked Sony.

two biggest next gen competitors acquired by legacy companies, and we all know that tends not to go well because everyone leaves and you can't acquire talent anymore. And they tend not to be run as efficiently in those types of companies. Then COVID hits right as the playing field had sort of been cleared out.

What about us not going into offices all of a sudden opened up this opportunity for CrowdStrike?

If your company was progressive enough to have an application or data in the cloud as opposed to going directly to AWS, you would VPN into your office, go from your office on the network to AWS, back to your office, and then back to home.

when all 50 people go home, because now all of that traffic is running back and forth, back and forth through the firewalls, and firewalls are capacity-constrained.
### A Special and Growing Product Range
I'm sure a bunch of your listeners read Ben Thompson, who loves to quote Clay Christensen theory of interdependence and modularity. It's one of my favorite investing principles, which is, in every value chain, the most value approves to the proprietary product that vertically integrates within the chain and everything else module arises around that point of integration and becomes commoditized.

Anytime one previously proprietary segment itself becomes a commodity, it opens the door for that proprietary value to shift to a new portion of the supply chain.

The obvious example of that is the three big CSPs, but I think you will see others, particularly ones that fill a void to customers who want multi-cloud or hybrid cloud architectures. And I think CrowdStrike has positioned themselves to be one of the two most likely new platforms within cybersecurity.

they bought a identity product. So, basically, when we talked about watching behavior on the endpoint earlier, originally, that was really watching behavior between apps. What are the apps talking to each other about? Whereas now you can incorporate a lens into what the actual user themselves does, not just what the apps do to interact with each other. And you can follow that user through a network, across different endpoints. They bought that company, it was really just a product, in September 2020. They paid $80 million for it. At the time, it had a little bit over $6 million of ARR. Today, it has $50 million of ARR, and it's growing 30% quarter over quarter.

previously, the thing that watched you on the endpoint was EDR, endpoint detection and response. Now, they have launched XDR, extended detection and response, and they basically said, "As opposed to just using all of the data that we have from our endpoint agents," which is a lot, they have application data, they have user data, they have information how the endpoints are talking to each other, "We're now going to sell a logging platform that you'd previously use Splunk or someone else like that. You can also dump into that data from any of our security partners," and those include CloudFlare, Zscaler or Okta, Proofpoint, ServiceNow. All of these other security companies are also giving their data into that same pool that CrowdStrike is running machine learning on.

As opposed to the Splunk initial vision, which was "If we noticed that malware has come in via email, we need to be able to go into your email client and figure out how to stop it there." CrowdStrike has said, "Hey, if we see in the Proofpoint data malware's coming in via email, we'll just turn off that laptop. We can just cut it off there because we have so many touch points throughout the entire estate." I think it's incredibly, incredibly powerful, and we're only starting to see the initial implications of that.

fourth bucket is a very hot market right now, is cloud workload protection.
drop a CrowdStrike agent on it, and it'll monitor that server for you. And it'll be able to turn it off the same way that we could turn off Jesse's computer in his home.
### Unit Economics Explained
on sales and marketing is you have to start with the go-to-market structure.
MSSPs, managed security software providers. System integrators like Accenture, and then Amazon is sort of their own animal.
The big distinction between a value-add reseller and a managed service provider, a value-add reseller, they are considered an expert on whatever is they do...those guys are buying from CrowdStrike at a discount. They're then selling it to the enterprise. They make some small margin on that wholesale spread, and then they get paid by the enterprise for installation and other services around maintaining that implementation.

Managed software providers on the other hand, they take over the entire management of the software. So you're paying them not just to source the product for you, but to own it. CrowdStrike uses both of those.

Let's say you were the Accenture account manager, and Accenture next year is like, "Wow, CrowdStrike is growing 100% year over year. We're going to double our practice and we're going to go from 50 people to a hundred people." CrowdStrike will definitely have to spend a little bit more in terms of they'll have to have more sales engineers to support them when they have big customers who want to see a demo, and maybe a couple more customer service reps. But CrowdStrike doesn't have to double their spend to support an Accenture team that's twice as large. That has real implications for how that spend is able to scale over time and how much fixed cost there is within it.

This is fairly rare. MongoDB or Snowflake, they don't have IT consultants running around, knocking on company's doors, being like, "Who do you use for your data warehouse? We recommend Snowflake."

Security is very unique...They tend not to carry more than two vendors for a single product. Part of that is because they get higher wholesale discounts the more volume that they do, so they're incentivized to not spread out over too many different vendors.

Once CrowdStrike has gotten to this best of breed status within the endpoint world and started to build out their platform offering, you start to see a flywheel develop where they are offering their channel partners about half the percentage wholesale margin relative to other companies.

CrowdStrike's ASPs are about 20% higher. You get 20% more plus maybe you get an extra one or two modules that are attached. Plus the implementation's easier because it's faster, and you have the opportunity to cross-sell more in the future.

Fundamentally those questions boil down to:
1. what is the true growth investment that the company is making and in this case needs to be pulled out of the P&L because it's all being recognized as OPEX.
2. The second being how much ARR does that growth investment lead to generating both now and over time?
3. The third is what is the incremental margin on those ARR dollars?
4. The fourth is how efficiently can that growth investment be scaled at this level of return?
So for Crowd, that math implies that CAC did improve, meaning it went down at the very beginning of COVID, reflecting like a shift in structural demand.

they're spending about 90 cents to acquire a dollar of ARR at 30% incremental margins, which at 2% churn spits out a 40% incremental ROIC
## Summary
1. **Introduction**: Jesse Pujji and Roneal Desai discuss CrowdStrike, its founding, and its differentiation in cybersecurity by predicting threats rather than just blocking attacks.

2. **Company Overview**: CrowdStrike is a cloud-native cybersecurity vendor founded in 2011, specializing in endpoint security by using an agent-based system that collects and analyzes data in real-time.

3. **Size and Scale**: CrowdStrike is valued at $45 billion, with ARR of $1.9 billion growing at 61% YoY, serving over 18,000 customers globally.

4. **Key Events**: CrowdStrike's notable contributions include identifying Russian hackers in the 2016 DNC breach and various high-profile cyber espionage cases.

5. **Cybersecurity Market Dynamics**: The discussion covers the comparison between old-school firewalls and CrowdStrike's advanced endpoint security, illustrating how traditional firewalls like McAfee differ from CrowdStrike’s dynamic and predictive approach.

6. **Market Potential**: Roneal highlights that the market for endpoint security is growing, with legacy vendors still holding significant market share but increasingly losing ground to modern solutions like CrowdStrike.

7. **Competitive Landscape**: Key competitors include Microsoft and SentinelOne, with Microsoft bundling basic endpoint protection in its Office packages, presenting a significant but not insurmountable challenge.

8. **Testing and Evaluation**: CrowdStrike’s capabilities are assessed through formal tests and real-world incident responses, showcasing its effectiveness compared to competitors.

9. **Founding Story and Evolution**: CrowdStrike was founded by George Kurtz and Dmitri Alperovitch, both ex-McAfee executives, with significant contributions from Sean Henry, a former FBI official. The company slowly developed its product to ensure a lightweight, upgradeable agent.

10. **Key Incidents and Growth**: CrowdStrike gained prominence through high-profile incident responses, such as the Sony hack by North Korea and various cyber espionage cases, leading to significant market trust and expansion.

11. **Impact of COVID-19**: The pandemic accelerated the demand for endpoint security as remote work became prevalent, highlighting the need for local device protection over traditional network-based security models.

12. **Business Model and P&L**: CrowdStrike’s business model includes various modules and managed services, contributing to its ARR. The company’s subscription gross margins are around 77%, with significant room for scalability and efficiency improvements.

13. **Sales and Marketing**: The go-to-market strategy involves channel partners and direct sales, with a strong emphasis on building relationships with managed security service providers and value-add resellers.

14. **Growth Drivers**: The company’s growth is driven by expanding its product range through R&D and strategic acquisitions, with a focus on endpoint security, identity protection, and cloud workload protection.

15. **Future Prospects**: CrowdStrike aims to continue expanding its product suite, leveraging its lightweight agent technology to secure a broad range of endpoints and cloud environments, positioning itself as a leader in the evolving cybersecurity landscape.
