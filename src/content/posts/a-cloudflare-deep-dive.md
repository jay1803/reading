---
title: "A Cloudflare deep dive"
date: 2023-12-28T16:03:01Z
category: reading
author: "muji"
description: "They are a leading cloud platform for managing the security and performance of resources on the Internet, and have become a top Content Delivery Network (CDN..."
source: "https://hhhypergrowth.com/a-cloudflare-deep-dive/"
---

They are a leading cloud platform for managing the security and performance of resources on the Internet, and have become a top Content Delivery Network (CDN). They have built a vast global network to help deliver your content to your users as quickly, securely and reliably as possible. Their edge network spans 200 cities worldwide, making 99% of the world's internet users within immediate reach of their data centers (within 100ms). They also have built up security capabilities to stop large-scale DDoS attacks and, like Crowdstrike (CRWD), have created their own threat intelligence system to monitor all the traffic in and out of their massive global network.

Cloudflare for Teams creates a dual-sided Secure Web Gateway (SWG) + Zero Trust combination to secure both outgoing and incoming enterprise traffic. This assures an enterprise's global user base can securely access external SaaS services as well as internal enterprise ones.

Sound familiar? It turns out Cloudflare is now a direct competitor to Zscaler. Given Zscaler's rapid deceleration while Cloudflare accelerates, Cloudflare has more revenue growth just from their existing cloud network platform (CDN and security), while their new product line -- directly entering Zscaler's turf!

I think there is room for both NET and ZS to succeed in this space, but NET will be supplanting ZS in my portfolio. Primarily because they are way more multi-faceted of a company, not beholden JUST to the Zero Trust paradigm that traditionalists are slow to adopt. But also because their platform is easier to integrate, as they have 90% direct sales; Zscaler has a more difficult integration, requiring integration partners.
### Cloudflare Platform
#### Core Platform
Global Anycast Network:
Cloudflare’s network spans 200 in over 90 countries, with 8,000+ networks globally.

Global Cloud Platform:
- Cloudflare provides a scalable, easy-to-use, unified control plane to deliver security, performance, and reliability for on-premises, hybrid, cloud, and SaaS applications.
- Security: Cloud-based security platform to secure infrastructure, whether public or private cloud, on-premise, SaaS apps, or IoT. They learn from all free and paid users to improve security. They block 72B cyber-threats/day.
- Performance & Reliability: Improve app performance & reliability, to enhance visitor experience, raise conversions, and reduce churn.

Platform Ecosystem:
Cloudflare has an integrated app store full of nearly 200 additional plugins you can enable in your Cloudflare account with a point-and-click.
#### Platform capabilities
- Security: Web application firewall (WAF), DDoS protection, bot mgmt, IoT security, SSL, rate limiting, Zero Trust access, Web gateway (SWG)
- Performance: Content Delivery (CDN), content optimization, mobile optimization, image optimization
- Reliability: local edge routing ("Anycast"), virtual private backbone (private global network), smart routing ("Argo", aka "Waze for the internet"), load balancing, managed DNS, caching
- Developer tools: serverless workers, KV store, mobile SDK
- Consumer tools: open DNS, VPN ("Warp")
#### Pricing tiers
- Free = simple sites
- Pro $20/mo = pro sites needing basic security & performance
- Business $200/mo = adv security & performance, priority support
- Enterprise $?/mo = enterprise grade security & performance, emergency support
### Finances
- 2M custs, 75k paying
- 20M internet properties
- 1069 empl
### Competitors
- CDN: Akamai, Fastly, AWS, Azure, GCP, Rackspace
- DDoS: Akamai, Fastly, Imperva, Oracle (Dyn), F5
- WAF: Imperva, Akamai, Fastly, Forinet, F5, AWS, Azure, GCP
- Security: Cisco, FireEye, Palo Alto, Juniper
- Zero Trust: Zscaler, Okta, Cisco, Akamai, Palo Alto, Symantec (Luminate)
- SWG: Zscaler, Cisco, McAfee, Symantec, Barracuda
#### Driving Trends
- App Economy
- Cloud computing
- Edge computing
- Serverless
- Zero Trust
- IoT
- 5G
#### Head to Head vs Fastly (FSLY)
Fastly is a direct competitor in the edge cloud space (CDN + DDoS protection).

It's interesting how different the storyline is of these two direct competitors. Cloudflare has a massive pool of free users with a fraction that pay, but it gives them a huge sales funnel. Fastly seems to focus on having a customer base of fewer, larger enterprises, then keeps their annual spend rising (high $NER).
#### My Stance
I like NET overall more than FSLY -- larger revenue that is growing faster, way better gross margins, improving op & FCF margins.

Cloudflare has a massive pool of free users with a fraction that pay, but it gives them a huge sales funnel. Fastly seems to focus on having a customer base of fewer, larger enterprises, then keeps their annual spend rising (high $NER).
#### New Pivots
#### New product: Argo Tunnel
Allows enterprises to hook their applications into Cloudflare edge network.
#### New product: Cloudflare Access
Zero-trust access to replace VPNs. Directly competes against Zscaler ZPA, Okta Access Gateway, and Google BeyondCorp.
- Extends Cloudflare's existing security platform.
- Access a private network via Cloudflare's edge network of 150+ (now 200+) data centers. Very akin to Zscaler's network layout.
- Basic tier at $3/user/mo, integrated with social identity providers like Facebook, Google and Github.
- Premium tier at $5/user/mo for enterprise identity providers like Okta, OneLogin or GSuite.
#### New product: Magic Transit
Protect entire enterprise network via software defined networking (SDN), with load balancing, advanced packet filtering, DDoS protection, next-gen firewall, traffic acceleration. Traffic originates on Cloudflare's edge network, is inspected & then routed into on-prem network.
#### New product: WARP & WARP+ consumer VPNs
WARP+ then extended it into a faster & more secure version, by leveraging Argo (virtual private backbone) to optimize routing and provide encryption edge-to-edge. It is a paid app w/ monthly subscription.
#### Acquisition: S2 System (Jan'20)
Remote browser isolation technology that went into Cloudflare Gateway (SWG side of Teams). [Zscaler acquired Appsulate for this in May '19.] 9 employees. CEO said in Q419 CC Q&A that they are normally averse to bolt-on acquisitions; they were going to partner with them but became great fit.
#### New product: Cloudflare for Teams (Jan'20, now in beta)
Cloudflare platform has been about securing network traffic to your resources (apps, websites, content). Now they are pivoting their platform to be able to secure ALL OF YOUR ENTERPRISE'S TRAFFIC.

Cloudflare Access is Zero Trust (protect incoming traffic) [akin to Zscaler ZPA or Okta Access] .
Cloudflare Gateway is an SWG next-gen firewall (to protect outgoing traffic), with SSL introspection and remote browser isolation [akin to Zscaler ZIA].
> “We started Cloudflare to solve one-half of every IT organization's fundamental challenge. How do you ensure the resources and infrastructure you expose to the Internet are fast, reliable and safe from attack? That's what our performance, firewall, bot management, rate limiting, load balancing and many other infrastructure protection products are for.

But Teams has to massively expand TAM (by a Zscaler amount), so I fully expect growth rates to rise as the "two halves" become whole.
### Conclusion
