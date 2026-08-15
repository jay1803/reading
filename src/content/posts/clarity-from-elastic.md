---
title: "Clarity from Elastic"
date: 2023-12-28T16:00:28Z
category: reading
description: "I really really like how they have boiled down what they do into very clear paths. It always seems like Elastic is moving in a lot of directions, but this bo..."
source: "https://hhhypergrowth.com/clarity-from-elastic/"
---

### Platform Core
I really really like how they have boiled down what they do into very clear paths. It always seems like Elastic is moving in a lot of directions, but this boils into the 3 distinct markets.

The core is in the middle, which I've covered before. The Elastic Stack (nee ELK stack) consists of Elasticsearch (search database), Kibana (visualization, dashboard and ML interface), Beats (open-ended ingestion interface), and Logstash (file conversion). This is available as the open source or enterprise supported release, in order to run self-managed instances on whatever infrastructure desired.

At the bottom is their managed hosting methods for the stack beyond self-managed:
- Elastic Cloud (cloud SaaS provider, billed on usage)
- Elastic Cloud Enterprise (managed SaaS deployed on-prem)
- Elastic Cloud on Kubernetes (container cluster manager)
### Product Lines
#### Elastic Enterprise Search
This direction came about through their acquisition of SwiftType, a SaaS private that built these services over Elasticsearch open-source.

Competition: MongoDB Atlas Search, Algolia, Coveo
##### Products:
- Workplace Search = Search engine & interface over a internal content and SaaS tools (email, Slack, Github, Google Drive, Office 365).
- App Search = Search engine & interface over provided content, via their API (for e-commerce, or inline search within SaaS or mobile apps).
- Site Search = Search engine & interface over web content (for publishing, blogs, static written content).
#### Elastic Observability
Allows a centralized search capabilities & interface over all your infrastructure & services (SaaS services, APIs, web apps, or mobile apps).

Competition: Datadog, Dynatrace, NewRelic

Search over these types of internal data:
- Metrics
- Log files
- App performance monitoring (APM)
- Uptime
#### Elastic Security
It started as as Observability, but their stack pivots easily into security concerns over that same data, providing monitoring of a different kind.
- SIEM = Cybersecurity search engine and visual dashboard over that Observability data, but geared for a different audience and purpose -- the detection & tracking of intrusions and cyber attacks. Elastic provides SIEM-specific dashboards in Kibana, to provide a security-centric view into same observability data that IT uses. The initial GA of SIEM has released, for observability & monitoring of a company's network -- but Elastic is still iterating. They have an expanding list of pre-build collectors for a wide variety of security equipment & data sources. New partnership & integrations announced with Palo Alto for their SOAR capabilities (orchestration of incident response).
  Competition: Splunk, LogRhythm

- Endpoint = EPP from their acquisition of Endgame, an installed app to protect a user's devices from malware and intrusion. Has been directly integrated into Elastic SIEM.
  Competition: CrowdStrike, Microsoft, Blackberry/Cylance, VMWare/Carbon Black
### Hosted Services
### Security
Palo Alto has new partnership w/ Elastic, and is co-sponsor of the conference. They announced a new product, Cortex XSOAR.
- Next evolution of product line coming out of their Demisto acquisition and its SOAR product, now rebranded as "XSOAR" (next-gen security automation & response).
- Does orchestration, automation & case mgmt for security ops & incident response.
- Has workflow automation engine (flow chart UI) over 100s of security products and 1000s of actions.
- Security ticketing system & collaboration platform.
- Ties directly into Elastic SIEM.
### And now ... the even MORE interesting stuff
#### Elastic Security
- So is EPP a unified solution thru the UI or separate from the Endgame solution?
  We have an aggressive road-map to collapse the Endgame console into the stack and fully integrate its capability creating a unified UI.
- Is there a tentative date for the Elastic/Endgame integration?
  I believe this will be a way better product in the next 6-12 mo; they iterate fast.
- Will Endgame in ELK be in open source or enterprise package?
  We are still looking into it, which part will be free and which parts will be in subscription lanes, more to come once the integration matures.
- How often do you guys put out new rules?
  New rules are added for each release. The last release included the first 92 Detection Rules, the release prior added 30+ ML rules. We are on a DevOps release cycle and historically version updates occur every 6-10 weeks.
  But compare this model to CrowdStrike, who can react in an instant globally across their entire customer base. I continue to insist that cloud-based EPP providers like CRWD will ALWAYS be more nimble, and hence BETTER, than Elastic Endpoint because of this massive difference in reaction speed (weeks vs seconds) and scope (global view over all customers vs a single customer's island).
#### FedRAMP Certification
[This is important as it opens the floodgates for Federal use of Elastic SaaS services. Elastic is widely in use now across Fed govt. This opens up a massive market for the managed cloud service.]
#### Enterprise Search
#### Miscellaneous
