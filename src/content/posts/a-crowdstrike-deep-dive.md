---
title: "A CrowdStrike deep dive"
date: 2023-12-28T16:11:03Z
category: reading
description: "The S-1 in-depth report from Meritech and the latest growth numbers sure got me interested in the upcoming CrowdStrike IPO."
source: "https://hhhypergrowth.com/a-crowdstrike-deep-dive/"
---

The S-1 in-depth report from Meritech and the latest growth numbers sure got me interested in the upcoming CrowdStrike IPO.

They are pretty akin to Zscaler as a cloud-based security company using crowdsourced data and AI for threat detection, but a different technical setup and focus (that I dive into in more detail below).
- ZS and CRWD have similar revenue (~250M TTM).
- ZS has better margins (80% vs 66%) and much lower net losses (almost profitable). CRWD has been improving margins, but Pro Svcs is weighing it down. (Counterpoint: Pro Svcs is a huge sales entry point for Falcon Platform.)
- CRWD has way higher rev growth (124% vs 66%), nearly double!
- CRWD has huge cust growth (+103%) that are spending more ($NER 147%). Muted $NER of 118% has been my one disappointment with ZS that I've griped about before; CRWD is showing way better expansion rates with its modular/tiered pricing, plus having a completely managed service at the top tier.
### CrowdStrike Overview
CrowdStrike is a SECaaS providing cloud-native endpoint protection, that leverages crowdsourced data and cloud analytics to stop threats.
- Cloud-based architecture - customers can immediately implement & scale. Modular products can be used depending on need, or their managed service.
- AI over threat detection. Replaces existing anti-virus & malware detection.
- Internal teams of experts analyzing threat database, and providing services like assessment, proactive checks, incident response.
- Marketplace to integrate products from partners that extend Falcon platform. Ties directly into to other SECaaS & analytics providers.
#### Product Lines
1. Enterprise endpoint protection
2. Threat intelligence
3. Security and vulnerability mgmt
4. IT Service mgmt
5. Managed security services
Competitors: Symantec, Cylance (Blackberry), Cybereason, Carbon Black, Palo Alto, FireEye
Customers: ADP, Shutterstock, Pokemon Co, Rackspace, Tribune Media, State of Wyoming, Hubspot, City of San Diego, Hyatt
#### At a Glance
- processes data from endpoints across all customer base (crowdsourced security)
- use AI and behavior pattern-matching to stop breaches
- started w/ focus on large enterprises, now sells to SMBs
- in 44% of Fortune 100
- 2/3 of custs <1k empl
- 23% int'l (+700bps YoY)
- recent cust onboarded in 1d to protect >100k endpoints
- internal data showed 40% of detects were exploits in OS (not malware)
- global TAM expected to be $29.2B by 2021 (ZS said $17.7B TAM at IPO a year ago)
- last reported private valuation $3.15B
### Platform Overview
#### Falcon Platform
2 software components
- light-weight endpoint agent: installed on Windows, Mac, Linux systems
- Threat Graph cloud database: analyzes 1T real-time events/wk
- 10 cloud modules, all subscription-based
- 47% of sub custs on >4 modules (+1700bps YoY) !!

Crowdstrike discusses 2 different approaches to protection.
- Indicators of Compromise (IOCs) = The unique characteristics of a breach. Reactive approach. Examples: malware, exploits, attack signatures.
- Indicators of Attack (IOAs) = A focus on detecting the intent of what an attacker is trying to accomplish. Represents series of actions adversary would take. Proactive approach. Examples: Code execution, persistence, stealth, lateral movements w/in network.
#### Product Modules
##### Endpoint Security:
Falcon Prevent (Next-Gen Antivirus): comprehensive protection against both malware and fileless attacks; replaces legacy antivirus/malware detection products

Falcon Insight EDR (Endpoint Detection and Response): notify customers about endpoint activity in real time

Falcon Device Control: gives admins visibility and granular control of USB peripheral devices
##### Security and IT Ops:
Falcon Overwatch (Threat Hunting): elite team of security experts who utilize the Threat Graph to augment customer's in-house security

Falcon Discover (IT Hygiene): network security monitoring & introspection

Falcon Complete (Turnkey Security): managed service for monitoring, mgmt, response, and remediation

Falcon Spotlight (Vulnerability Mgmt): detect vulnerabilities in real time across customer endpoints
##### Threat Intelligence:
Falcon X (Threat Intel): AI over endpoint protection

Falcon Search Engine (Malware Search): search over 300Tb of 400M malwares collected across Falcon, overlaid with Threat Intel data

Falcon Sandbox (Malware Analysis): analyze files for malicious behavior in isolated VMs, can integrate into workflows & SIEMs
##### Services:
- Cybersecurity assessment
- Proactive checks
- Pre/Post incident response
- Compromise assessment
##### Other:
- CrowdStrike Falcon for Mobile: (coming soon) EDR for mobile devices
- Falcon on GovCloud: FedRAMP approved gov't endpoint security, delivered on AWS GovCloud; includes Prevent, Insight and Discover products, plus IR & Proactive services
- Falcon for Data Centers: secure physical, virtual or cloud/hybrid infrastructure

CrowdStrike Store: PaaS store for cybersecurity tools, to sell products from CrowdStrike partners that enhance Falcon Platform and/or utilize same agent … example apps/partners:

Falcon Connect: collection of APIs to interface with Falcon Platform
#### Pricing
Multiple tiers for 5-250 endpoints. Any tier can:
- ... add optional services
- ... add optional product Spotlight
- ... operate in specialized environs (GovCloud, Data Centers)
- ... add standalone products: Search Engine, Sandbox
##### Tiers:
- Falcon Pro - endpoint protection & threat intelligence
- Falcon Enterprise - prevents and detects attacks beyond malware, stop breaches, complete visibility
- Falcon Premium - next level breach protection, real-time rogue detection and user monitoring, health checks and quarterly briefings w/ recommendations.
##### Managed Service:
Falcon Complete - fully managed endpoint protection, delivered as a service by a CrowdStrike team of experts. Backed by $1M coverage to address breaches that occur within protected environ.
### IPO Details
### Competitive Landscape
There have been many threat-prevention SECaaS (Security-as-a-service) IPOs over past year: Tufin (TUFN), Zscaler (ZS), Carbon Black (CBLK) and Tenable (TENB), some of which are direct competitors. Another competitor is Cylance, bought by BlackBerry in Feb '19 for $1.4B. Then there are the traditional/big players in Symantec, Cisco, McAfee, Sophos, Palo Alto, FireEye and TrendMicro.

As for TAM, the cloud cybersecurity market is $138B this year, and estimated to be $232B by 2022 (CAGR 19% over 3y).

Quick look at last Q of each of those recent SECaaS IPOs:
- CBLK Q119: Revenue 56.8M +21%, Cloud Rev +80%, GM 78%
- TUFN LastQ: Revenue 29M +31%, GM 84% (just IPOd)
- TENB Q119: Revenue 80.3M +36%, GM 85%
- ZS Q219: Revenue 74.3M +65%^^, GM 80%, NER 118%
- CRWD: LastQ Revenue 72.8M +124%^^, GM 66%, NER 147%, custs +103% (about to IPO)

Fighting antivirus & malware, like the traditional competitors (anti-virus and anti-malware), is a small part of the problem - in today’s environment, endpoint protection providers focus on THREAT DETECTION as well as BREACH PROTECTION, INVESTIGATION, and MITIGATION. It is better to equate CrowdStrike's product lines with Zscaler, Tenable and Carbon Black, not traditional AV apps like Norton, Symantec and McAfee.
#### Crowdstrike vs Zscaler
They both focus on stopping breaches from malicious actors (hack attempts, viruses, malware). But know that they are protecting two separate pieces of the puzzle. CrowdStrike is focused on protecting the device or system (the endpoint), while Zscaler is focused on protecting the outgoing/incoming traffic (the network).

Zscaler's focus is on being a cloud firewall and Secure Web Gateway (SWG) with a Zero Trust focus. They are in the Gartner "Secure Web Gateway" quadrant, where they are a top Leader.

Gartner defines a Secure Web Gateway (SWG) as:
> “Secure Web gateway solutions protect Web-surfing PCs from infection and enforce company policies. A secure Web gateway is a solution that filters unwanted software/malware from user-initiated Web/Internet traffic and enforces corporate and regulatory policy compliance. These gateways must, at a minimum, include URL filtering, malicious-code detection and filtering, and application controls for popular Web-based applications, such as instant messaging (IM) and Skype. Native or integrated data leak prevention is also increasingly included.”

CrowdStrike, and its AI & expert driven threat detection and endpoint protection platform, is clearly doing something right with those revenue & customer growth numbers. They claim 91M blocked events a minute (meaning ~130B/day). They are in the Gartner "Endpoint Protection Platform" quadrant, where they are top Visionary (nearly Leader).

Gartner defines an Endpoint Protection Platform (EPP) as:
> An endpoint protection platform (EPP) is a solution deployed on endpoint devices to prevent file-based malware attacks, detect malicious activity, and provide the investigation and remediation capabilities needed to respond to dynamic security incidents and alerts. Detection capabilities will vary, but advanced solutions will use multiple detection techniques, ranging from static IOCs to behavioral analysis. The inclusion of artificial intelligence (AI) and human-driven managed services such as managed threat hunting — lowering the barrier to entry for more advanced capabilities — will increase over the next 18 months. Deception capabilities, intended to trick adversaries into revealing their presence by accessing fake services or planted files, or by using planted credentials, are emerging.
>
> Desirable EPP solutions are primarily cloud-managed, allowing the continuous monitoring and collection of activity data, along with the ability to take remote remediation actions, whether the endpoint is on the corporate network or outside of the office. In addition, these solutions are cloud-data-assisted, meaning the endpoint agent does not have to maintain a local database of all known IOCs, but can check a cloud resource to find the latest verdicts on objects that it is unable to classify. Integration with security orchestration, automation and response (SOAR) tools will become increasingly desirable.
