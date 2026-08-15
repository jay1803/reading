---
title: "#19 - Muji (Founder of Hhhypergrowth) - Data Infrastructure Trends, Operational vs Analytical Databases, Benefits of Edge Network Architectures, Emergence of SASE Security, Zero Trust Security"
date: 2023-10-11T17:24:19Z
category: reading
description: "AWS and red shift, which is basically a glorified Postgres database."
source: "https://shomik.substack.com/p/19-muji-founder-of-hhhypergrowth#details"
---

## Muji (Founder of Hhhypergrowth) - Data Infrastructure Trends, Operational vs Analytical Databases, Benefits of Edge Network Architectures, Emergence of SASE Security, Zero Trust Security
### (01:15) - Overview of Cloud Data Infra - Trends and Architectures (including differences between Snowflake, Redshift, BigQuery, Databricks)
#### 00:01:40 Muji
AWS and red shift, which is basically a glorified Postgres database.
Snowflake emerged out of that train of thought where they wanted to go serverless in that you didn't have to worry about the underlying infrastructure set up specific cluster sizes and and that sort of thing.

hey really focused on the separation of storage and compute.

I'd say that those hyperscalers are catching up to some of the.
#### 00:04:08 Muji
Regions across clouds they can span across clouds across regions.
So that I can have one department using Azure in Europe and another using a WS in The United States and that data can seamlessly migrate between the two to keep them both In Sync.

So they've again have really kind of dumbed down the infrastructure that's actually quite complicated in the world of databases, distributed data and how you distribute data and keep things In Sync.
#### 00:05:22 Muji
But Google Azure all moving in that same direction towards Data Lake houses.
#### 00:07:07 Muji
Just today, Databricks announced Lake House apps, so it's following them that native embedded application paradigm as well. So Snowflake is leading in a lot of directions. All the competition tends to catch up pretty quickly.
#### 00:07:32 Shomik Ghosh
obviously there's a latency benefit to having the app be so near the data, right?
#### 00:07:52 Muji
the bigger benefits are to the customer themselves and that the data never has to leave their hands.
#### 00:08:17 Muji
That you have to completely upload your data into, you know, so it's completely outside of your control at that point. That's been shifting to what Snowflake likes to call connected apps, which is you provide them credentials and they can log into your database and be making queries directly in your database. But they still have some external service that has to be hosted somewhere.
#### 00:09:10 Muji
In that not compute about the applications running so far, that's going to be free. Actually it's the queries that those applications generate.
That is a value to snowflake.

the developer doesn't have to maintain their own infrastructure that is appealing. You can have apps that embed directly into the customer's Database.
### (11:12) - Operational vs Analytical Databases
#### 00:11:22 Muji
I like to consider them as the operational databases or the transactional ones.
And the analytical databases are the ones that are collecting data out of those operational databases.

The data warehouse is a transforming in purpose. It's not just for data warehousing. Now in the operational view, it can be used for data operations themselves, engineering, use cases, the transformation and collection of data.
even unstructured data such as video files and audio files, images that sort of thing.
#### 00:12:42 Muji
the modern data stack is being built with the data warehouse. the Data Lake House as a big pool of data that a lot of different tools and departments and use cases.
#### 00:13:40 Muji
Your business needs to be data-driven. You need to know your inventory levels, your supply chain demand, and how it's shifting on a real time basis. And you can't rely on ohh I gotta collect all these data.

From 50 different platforms we use take the time to move all that data somewhere else and organize it. You really need to streamline that process to be as real time as possible.

I see the value of Bigquery and Snowflake and Databricks is Data Lake house.
#### 00:14:19 Shomik Ghosh
Snowflake has released their Python workflows
they're trying to move deeper like you said, into the data scientists workflows.

Meanwhile, Databricks, Inc. has lived and breathed that from day zero.
### (15:13) - Databricks & Snowflake Differentiation (especially as it relates to AI)
#### 00:15:25 Muji
Hadoop that remains today is Spark, which is in memory data processing over vast quantities of data via programmable notebooks, and so it's fantastic for data exploration data manipulation.
And analysis and ultimately data science and driving machine learning jobs. That is what databricks lives and breathes. And so they're of course highly ideal tool for this moment in time.
you're creating your own models. It's a great platform for that.
#### 00:16:07 Muji
That is what Snowflake has been trying to move towards.
Snowpark, which is their answer for spark embedded within the snowflake platform.
they've been moving towards that same long term goal to collide absolutely.
#### 00:17:45 Muji
But it's do you have the resources to run all that yourself, or do you want a turnkey platform to do it for you in Snowflake? So that for me is the big difference between those platforms. Of course, this is also where Azure is moving with its new data Lake house called Fabric.
Google has been moving with its BigLake and bigquery and how well it's integrating spark deeply into its own platform.
### (19:35) - Overview of Edge Networks - Trends & Architectures (Cloudflare, Fastly, AWS)
#### 00:19:25 Shomik Ghosh
Can you describe what edge networks are and how they literally have these point of presences?
#### 00:19:36 Muji
I like to equate it to a giant mesh network across the globe.
you've got a giant programmable net.
#### 00:24:34 Shomik Ghosh
So why is it that AWS, GCP, Azure, anybody they already have these regions set up all over the world, right? And then it's not like Cloudflare using Equinix.
### (25:04) - Edge Network Providers vs Big 3 Cloud Providers
#### 00:25:24 Muji
I didn't really get into the history of how edge networks emerged, but it was out of the CDN and DDoS protection markets, but especially CDN.
Now why AWS hasn't moved this way yet? I'm not quite sure. They have cloud front which is their CDN product, their content delivery network.
#### 00:26:47 Muji
else edge networks come in handy so.
There's this explosion of interest in AI and ML that requires intense amounts of compute, massive amounts of data. That may not be ideal to run on an edge Network.
Great to run on an edge network is data collection platform.
#### 00:27:07 Muji
Forms globally distributed applications data messaging where you've got to send data constantly between different parts of the globe, IoT platforms. And so I see it as a modern set of tools for today's developers for a particular direction of applications.
#### 00:28:53 Shomik Ghosh
what data looks like in sort of an edge Network.
#### 00:29:42 Muji
absolutely the edge network is most primed for you to not be doing the most heavy compute at the edge.
For all the data globally and you're gonna be training AI over it Or doing analytical processes over the entirety of the data in one place, but you can absolutely have the data stored at the individual pops and be doing analytics on them. say for fleet tracking or IoT analysis directly in that pop. And so all of the above really it's ideal for both of those.
Where they're starting to develop products around both of those use cases. Cloudflare in particular.
#### 00:30:33 Muji
And I see both of them being highly valuable, much less stream processing, and where Confluent been trying to go lately with Apache Flink, there's value in real time data and data in motion. And I think edge networks are primed for that as.
### (31:48) - Overview of Security & Networking Convergence (SASE Security, Zero Trust Networking, SSE, CNAPP, etc)
#### 00:31:48 Muji
安全性一直对投资犹豫不决，因为它在不断发展。对手通常领先一步
I think zero trust was pretty easily identifiable.
#### 00:33:07 Muji
With Zscaler and then with Cloudflare with that Edge network again because they're the interconnection point between a lot of distributed users and a lot of distributed applications.
So that someone doesn't have to VPN into your network.
And then Secure Web Gateway is a layer where all your web usage for enterprise tools goes through a secure web gateway, typically done in the past with an appliance that you would install into your network and you'd route all your traffic through a data center, then to the public Internet. So it's been around a long time that the concept of a secure web gateway.
#### 00:34:25 Muji
Microsoft Office with Zoom with Workday, the tools that they use in a very secure and governed way.
#### 00:35:14 Muji
Across all those things, plus zero trust + a secure web gateway + CASB
They decided to split it in half and say,there's the SD-WAN port, And then there's the SASE part.
#### 00:36:24 Muji
why Edge networks are so ideally suited in that your users can be anywhere your apps can be anywhere, your cloud environments, your retail locations, your factories, whatnot. Sassy platform serves as the interconnection of all those points globally.
### (37:15) - Public Company SASE Security Landscape (Cloudflare, Z-Scaler, Palo Alto Networks)
#### 00:36:38 Shomik Ghosh
But I want to dive deeper into cloud first, specifically because why did you think they were so well positioned?
obviously, yeah, I think actually you were at one point and maybe still are long Zscaler and you've studied Netskope and Cato and all the other players out there, right. But from the beginning.
#### 00:39:45 Muji
going up against huge names like Zscaler that defined this category for the most part, at least with zero trust and secure web gateway.
And now Palo Alto obviously has been hugely risen into this direction, and it is the primary focus for them, which is interesting in that it eats their other market. But they found a way to navigate it where it's not so much eating their market that they leverage their existing pool of firewalls that they sell out into the world, that you're installing not only on premise but also in the cloud.
The fact that they can still lead with firewalls is just remarkable to me.
#### 00:42:46 Shomik Ghosh
They made some very impressive acquisitions.
I still don't think they're fully tied together in the way that you would expect or or want them to be.
#### 00:43:20 Muji
 if I was an investor in Palo Alto, it's entirely about their next Gen, which they call NGS, which is Prisma SASE.
 They bought a couple of companies that allowed them to move into cloud security very quickly,
#### 00:44:24 Muji
Then Cortex, which is their XDR or EDR endpoint protection platform that's moving into XDR as well as automation capabilities and external attack surface management side of things.
Which is the world of CrowdStrike and Sentinel One.
But they're really helping customers make that transition from older traditional network security to new, and that's where they're excelling.
### (46:03) - XDR/EDR & Zero Trust Converging (Crowdstrike, SentinelOne, Microsoft, Palo Alto Networks)
#### 00:46:12 Muji
Microsoft had actually throw in the same in that they're actually Microsoft is less SASE.
Zscaler is coming from zero trust, but moving into cloud security.
CrowdStrike started at endpoint is moving into cloud security.
SentinelOne the same and have a partnership with Wiz to kind of fill out their missing gaps.
#### 00:47:46 Shomik Ghosh
And we'll link to the Snowflake piece. That's still probably the best piece that anybody has put out.
### (48:06) - How Muji Conducts In-Depth Technical and Qualitative Research
#### 00:49:04 Muji
I have my own tool I use called Obsidian, which is a lot like Rome. If you're familiar. A lot of people use notion, you know, you've got these personalized wikis that you can have. I love this modern wave of research tools to capture in all these things collect a bunch of links. I keep running notes of everything and it's really for me writing it down that really drives it in for me versus just reading. And so I like to think of my service as a collector of all this data and then honing it down into something.
#### 00:52:16 Muji
So I can understand the difference between say what Zscaler is calling SASE, what Palo Alto is calling SASE, and what Cloudflare calling SASE or absolutely three different architectures.
### (55:23) - Audience Question: Big Cloud Providers vs Nvidia in ASICs and GPUs
### (58:39) - Audience Question: Outside of AI, What Area of Software Infra Still Has the Most Innovation and Growth Ahead?
