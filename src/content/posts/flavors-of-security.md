---
title: "Flavors of Security"
date: 2023-12-28T16:04:17Z
category: reading
author: "muji"
description: "Every company in today's world MUST have the technical skills to setup, secure, and monitor their day-to-day business operations and company secrets (aka pro..."
source: "https://hhhypergrowth.com/flavors-of-security/"
---

### Intro
Every company in today's world MUST have the technical skills to setup, secure, and monitor their day-to-day business operations and company secrets (aka proprietary data: payroll, contracts, intellectual property, payroll, supply chain, customer lists). This is why I like to say [repeatedly] that "EVERY company is a tech company" under this connected global economy.

A company typically has digital assets & connected hardware (file storage, data systems, POS systems, printers, IoT sensors, "smart" equipment, cameras) within physical locations (offices, factories, mobile fleet, store fronts) containing a workforce that utilizes computing devices (workstations, laptops, tablets, phones) to track business operations (sales, marketing, finances, HR, payroll, operations, accounting, IT, R&D).

And then there is a company's operational infrastructure. A company could be maintaining their own email, HR, payroll, accounting and identity mgmt systems, or, increasingly, they could be using outside SaaS providers. A company may have on-site or remote data-centers that they maintain, or they may use one or more IaaS (Infrastructure-as-a-Service) cloud providers, or some hybrid mixture of the two. And if a company is itself a SaaS company, infrastructure is all the more important as it is also customer facing (hosting web servers and APIs).

And on top of all that networking complexity above, a company needs to SECURE that nest of systems, users, and the processes between them. For that, SaaS services have emerged, providing cybersecurity services to protect your company's assets, systems and/or employees.

- Cybersecurity = Protection of internet-connected systems from cyberattacks.
- Security-as-a-Service (SECaaS) = A SaaS company providing some type of cybersecurity service to enterprises.

I feel cybersecurity-related services have the HIGHEST LEVEL of stickiness due to the nature of security

Several popular hyper-growth stocks are in the SECaaS space -- OKTA, ZS, CRWD, ESTC.
and there is room in your portfolio for all of them. (Well, at least in mine.) Other SaaS companies followed here that are not directly related to security are benefiting as well -- IT services like managed databases (MongoDB Atlas & Stitch, Elastic Cloud), infrastructure monitoring (Elastic Stack, Datadog), endpoint communications (Twilio) and incident response (PagerDuty) are also thriving, in part due to this never-ending need to manage and watch your systems.
### Network Basics
Conventional network security has always been built on the assumption that that your internal network is a trusted zone, requiring a perimeter be built and maintained to keep the untrusted clients out of it. It's called castle-and-moat security
#### Network Layers
a conventional company's network layout is typically comprised of, as it helps us understand where attacks are hitting.
your house being a trusted network (castle), the outside walls of your house the periphery (moat), and the outside world as untrusted (public internet).
- Core = A company's data center(s), comprised of on-premise or cloud infrastructure. Typically where the centralized database storage, file repository, and the compute tasks live (aggregation, search, analytics, monitoring).
- Edge = Edge of the company's network that control and manage the network entry into the trusted network. Edge is the gateway used to corral communications from endpoints and allow them access to core.
- Endpoint = Hardware devices that connect into a company's network -- all the individual computers, laptops, phones, tablets, printers, IoT sensors, cameras, smart meters, POS terminals, etc.
#### Network Devices
There are many common basic network devices:
- Network router = Device that moves packets between 2 points in an optimum way.
- Network gateway = Device that joins two networks together, serving as a boundary to both.
- Proxy server = A gateway device that acts as an intermediary, to prevent direct access from untrusted networks to trusted.
- Firewall = A gateway device acting as a barrier that utilizes pre-set security rules to control & monitor incoming and outgoing network traffic based on pre-determined security rules, typically between a trusted internal network and untrusted external network
- DMZ (De-Militarized Zone) or Screened Subnet = A specialized subnet (separated subdivision of a network) used to isolate external traffic to a different network space than the internal trusted one.
- Edge devices = A network gateway that controls access to the trusted network, controlling requests and data flows between endpoints and core.
  So edge devices are gateways that deal with network interconnections, and endpoints are typically remote devices that are connecting to the edge device as a client. Cloud computing and IoT have started making the role of edge devices more important, increasing the need for more intelligence (compute) at the network edge.
- Edge computing = Refers to how edge devices that are gathering remote data from endpoints could be doing compute or analysis BEFORE passing the data to core, as opposed to the core doing it.
  Downside would be that edge devices typically don't have a complete picture that the core would, so is only capable of handling & analyzing its own data subset.

#### Ever-Growing Perimeter
Network security is comprised of products designed to monitor and secure network traffic moving in and out of your perimeter, to stop threats before they materialize.

Enterprises have to be ever-vigilant to maintain their perimeter, with a lot of monitoring and implementing of new security approaches.

It's easy to hit the limits of this perimeter strategy -- companies hope to grow, and often need to expand their trusted networks beyond a simple structure (for example, interconnect multiple locations, or add acquired companies into their network, or allow access to a remote or mobile workforce). This leads to a lot of complexity in maintaining security, as the perimeter becomes much larger than a single location and what one set of devices can handle.

Enterprise networks are designed to be "outside-in" -- users are moving from the outside (untrusted network) to inside (within the trusted).
- VPN (Virtual Private Network) = Extends a private network across a public network (the internet), so that remote users can securely access a trusted network from outside the perimeter. Creates an encrypted tunnel between the end user and the trusted network. This is commonly used to allow remote employees access to an trusted network, in order to access enterprise applications.
- WAN (Wide Area Network) = Separate networks joined together as one, regardless of distance. Useful to interconnect various physical locations together (offices, factories). Can use a VPN or set up dedicated connections with a telco/ISP.
- Hub-and-spoke topology = WAN layout having one main hub (primary office) and the rest integrated as spokes (all the other locations) off the hub. All traffic is routed through the hub as spokes intercommunicate. Simplest to set up but has a single point of failure.
- Mesh topology = WAN layout having all the networks interconnect with each other directly. More redundant than hub-and-spoke, but harder to build & maintain. Could be utilized over a hub-and-spoke ("Partial Mesh") to have most important locations meshed and secondary ones spoked.
#### Endless Cloud
All of these topologies still try to maintain a perimeter around a trusted network. When you have multiple locations, security gets complicated fast, as your perimeter has to extend around the entirety of it.
The explosion of cloud infrastructure and SaaS services (driving today's and tomorrow's hypergrowth) hinder a company in maintaining a meaningful perimeter.

Companies are starting to leverage cloud infrastructure due to cost, ease of use, and that it's scalable and can grow with them and their needs.
- On-premise = Company that has a enterprise network across one or more locations, and maintains their own servers for application and data hosting, hosted on-premise or in a remote data center.
- Cloud-native = Company whose entire business operations are maintained on cloud infrastructure or from using cloud SaaS services.
- Cloud-hybrid = Common combination of the two. Many companies are have been on-premise so long - the only choice until IaaS services took off - that they are slow to migrate. Companies have a lot of existing infrastructure, so are likely adopting cloud initiatives to start testing the waters.
- Cloud-first = Hybrid company that has come to a tipping point, where they will choose SaaS and IaaS solutions over building it themselves or maintaining internal infrastructure. They are not interested in buying any more infrastructure beyond that which they already have in place.

Now that systems are be being moved out to the cloud IaaS platforms, and services are being used from SaaS enterprise services, all those network connections passing data back and forth must be protected.

Capital One was just breached by a former AWS employee, and AWS said "it wasn't us, it was a mis-configured WAF". The complexity of maintaining security doesn't go away when you adopt IaaS for infrastructure.

Incoming network connections (to your apps) must be protected! Outgoing network connections (your employees conducting business) must be protected! Intercommunication to and from SaaS services must be protected! ALL TRAFFIC must be protected!
### ATTACK!
Per IndustryWeek, 2018 saw a massive increase in cyberattacks, so 75% of companies are increasing cybersecurity spend.

One enormous setback with the conventional network security model is that "every company is its own island", meaning every company only sees its own network logs and breach attempts. There are plenty of ways for IT staff to distribute information about attacks and try to keep up to date on security concerns and best practices (newsgroups, blogs, industry groups) - but companies are NOT going to share their security logs and cannot compare notes with others in real-time. It makes for a lopsided battle, where attacks can be coordinated, but the response never is.
#### What you can lose?
- Personally Identifiable Information (PII) = Term for any data that could potentially identify a specific individual (name, addr, SSN, DOB) or reveal private info a user may have.
- Personal Health Information (PHI) = PII pertaining to medical data, such as your charts, diagnoses, or genetic makeup.
- Payment Card Info (PCI) = PII pertaining to financial payment, typically credit card payment details (CC number, expry date, security code).
- Company secrets = Not PII, but every company has valuable & proprietary data they want kept internal -- intelletual property, software code, competitive plans, supply chains, etc.
- Data Breach = Incident in which sensitive or confidential data was illegally accessed and downloaded. Typically involves theft of data with PII, PHI, PCI, or company secrets (like financial data or intellectual property).
- Incident Response (IR) = An organized approach to addressing and managing the aftermath of a security breach or cyberattack, in order to handle the situation in a way that contains the attack and limits damage.
#### Who is attacking?
There are different types of hackers, based around the intent of the hack:
- Black Hat hacker = An unethical hacker (malicious actor) that wants violate systems to steal or to cause harm.
- White Hat hacker = An ethical hacker attempting to discover exploits and patch vulnerabilities. Typically has advance authorization to do penetration testing.
- Gray Hat hacker = A mix of the two that lives in the middle. Generally means someone who is breaking laws (hacking w/o authorization or notice to the company) but the intent is not malicious. Some companies are offering bounties for any details on how to breach their systems, so it has become lucrative work.
#### How are you attacked?
- Attack vector = The path a malicious actor takes into your system, in order to plant malware, steal data, or burrow deeper into your network systems.
- Exploits = Known vulnerabilities in software or hardware systems that become easy entries into your computer if left unpatched.
- Zero Day Exploit = An exploit that is newly discovered and has not yet been patched. Big trouble
- Shadow IT = Software exposed to internet that IT doesn't know about, or the use of unauthorized cloud apps. Hard to patch things when IT is unaware of it being there.
- Social engineering = Use of deception to fool employees into divulging information or system access that they should not be (aka the human element).
- Advanced Persistent Threat (APT) = A prolonged and targeted attack that gains access to your trusted network, and potentially remains undetected for a long period of time. A ghost in the machine (as mentioned in my haiku), that is covering its own tracks.
- Distributed attack = A coordinated attack from multiple nodes across one or more compromised networks.
- Distributed Denial of Service (DDoS) attack = A coordinated, distributed attack against your web services or servers, in order to disrupt normal traffic
- Botnet = A collection of connected devices that have been compromised, in order to be under a hacker's control for DDoS or other distributed attacks.
- Brute Force Attack = An attack that attempts to force its way into an account by guessing as many possible combinations of credentials as possible.
- SQL Injection = Web server attack against database query services that allow for running additional embedded commands against the database.
- Cross Site Scripting (XSS) = Web server attack that allows a hacker to submit or embed a custom script that other users of the web site may be exposed to.
- Phishing = A form of social engineering involving widely broadcast emails disguised as legitimate messages (ie a Paypal email that asks you to log in to your account) that attempt to lure you onto a fake website in order to capture your user credentials.
- Spear Phishing = A highly targeted phishing attack against a specific group or individual, instead of being widely broadcast out. "Whaling" is a spear phishing attack against a high-value target, like a CEO or politician.
- Business Compromised Email or Man-in-the-Email attack = Attack gaining access to a corporate email account, to pose as a higher up in order to entice or threaten employees into performing an action - typically to commit fraud by getting staff to pay bogus invoices or wire money.
- Malware (malicious software) = Hidden software planted on your system to capture keystrokes, gather sensitive data or gain access. Common types include viruses (manipulates files), worms (self-replicating), trojan horses (masquerades as legitimate), spyware, ransomware and fileless malware.
- Spyware = Malware that allows a user to spy on the user, such as a keyboard logger (captures what you type) or camera or mic capture.
- Ransomware = Malware that encrypts your files, in order to extort you into paying a ransom to regain access.
- Fileless malware = Malware that resides entirely in memory (RAM), never writing to disk as a file, in order to evade detection.
- Drive-By-Download = Malware downloaded from a compromised website, where a user inadvertently installs it onto their own system.
- Malvertising = Online ads that lead to malware installation.
- Cryptojacking = Malware to take over your system for its compute power, in order to build a network of systems to mine cryptocurrency on your dime
- Polymorphic malware = A type of malware that constantly changes its identifiable features in order to evade detection.
- Wifi spoofing or "evil twin" = Creating a fake wifi network (e.g. "Starbucks-Guest-Wifi") to fool users into connecting to it, in order to eavesdrop on their network traffic.
- Man-in-the-middle attack = Eavesdropping on network traffic in order to sit between two sides of a valid request, acting as the destination while capturing the steps of entry. Websites typically use HTTPS protocol now in order to help thwart this, which makes network traffic encrypted.
- Replay attack = Eavesdropping on network traffic to capture the steps of entry into systems, in order to replay them to gain entry.
- Account hijacking = When an attacker uses stolen account credentials.
- Session hijacking = Compromising your account by using an existing login token taken in a man-in-the-middle attack.
### Why SECaaS?
the bottom line is... it is extremely difficult to fully secure your network!

The Cloud Security Alliance (CSA) is an industry coalition that is trying to define cybersecurity norms...I don't agree with it completely
#### Pros
- Added insulation - SECaaS can stop the attacks before it hits your system, if they are acting as a gateway or proxy.
- Companies are flocking to SECaaS because it reduces cost AND reduces risk.
- Outsource to experts
- Shared security strategies & research...This is a massive advantage over conventional network security.
- Flexible - Monthly or annual charge
- Regulatory adherence - Makes it easier to maintain regulations around GDPR, HIPAA and others. SECaaS can build those features directly into their system so you are assured to be in adherence.
#### Cons
- Lack of visibility - No idea how truly strong the security is, as you have to trust the service.
- Potential for data leakage - If one customer can see another's data, that is a huge no-no in SaaS.
- Difficult to change - Can have vendor lock-in.
- Difficult to migrate into - Companies can have difficulties in changing their network security over to a new service.
- Never ending - You can never stop protecting your equipment. Potential for breach will always remain!the costs never stop regardless if its SaaS or traditional hardware.
### Flavors of Security
There is a general maxim in cybersecurity of "defense in depth" -- which means overlaying multiple security efforts and having redundancy.
#### Identity Tracking
Services for tracking users and their access rights. SECaaS varieties are typically called IDaaS (Identity-as-a-service).
- Identity and Access Management (IAM) = Tracking & verifying who your users are (workforce and/or customers) and managing their access and policies around it. These days it typically includes Federated Identity Mgmt (FIM), which enables Single Sign On (SSO). [Revisit "Security Basics" in my [Okta Deep Dive](https://hhhypergrowth.substack.com/p/an-okta-okta-technical-review) post if you need a refresher on tech terms around identity.]
- Identity Governance and Admin (IGA) = New category split off from IAM by Gartner. The "admin" of managing identity helps control identity lifecycle, manage passwords, and automate provisioning capabilities. For governance, it involves policy enforcement, role mgmt and segregation of duties, for risk reduction in workflows.
- Privileged Access Management (PAM) = Centralized tracking for sysadmin credentials and system access. Monitors and logs all privileged admin access to systems.
#### Monitoring & Detection
Services for monitoring systems, or detecting abnormal or threatening behaviors on your network.
- Intrusion Detection System (IDS) = Monitors and analyzes network behavior patterns to detect unusual events or intrusion attempts, and help prevent vulnerability exploits. Passive system to scan network traffic, compared to Intrusion Prevention (IPS).
- Data Loss (or Leak) Prevention (DLP) = Monitor, protect and verify security of data at rest, in motion and in use. Makes sure end users don't send private info outside the trusted network. Helps maintain compliance and mitigate insider threats.
- Security Assessment (or Vulnerability Scanning) = Services that perform scans and audits of infrastructure or applications for vulnerabilities.
- Continuous Monitoring = Automates security monitoring across various sources of security info (mostly device logs). Provides real-time visibility into a company's security posture, providing threat monitoring and performing vulnerability assessments.
- Deep Packet Inspection (DPI) = An advanced packet filtering process for inspecting and monitoring network traffic for malware or other unwanted instructions or behavior. Looks deeper at traffic packets than traditional firewalls. Ineffective against encrypted traffic.
- SSL Inspection = More advanced DPI for intercepting encrypted network traffic (such as HTTPS) via a proxy acting as a man-in-the-middle between the requester and destination, maintaining encryption separately to both ends. It can decrypt and monitor encrypted traffic for malware or other unwanted intrusions.
- Network Traffic Analysis (NTA) = Utilizes ML algorithms and rule-based detection over raw network traffic and flow data, in order to isolate suspicious activities on an enterprise network. Alerts on abnormal traffic patterns.
- User and Entity Behavior Analytics (UEBA) = Utilizes ML algorithms to track normal behavior of users, in order to detect anomalous behaviors or deviations. Focuses on user behavior (as opposed to network traffic), to help mitigate against insider threats, compromised accounts, brute-force attacks, intrusions and APT threats.
- Endpoint Detection & Response (EDR) = Continuous monitoring of endpoint usage to analyze, investigate and respond to advanced threats and broader attacks across many endpoints. Likely integrated with Endpoint Protection (EPP) features. Likely utilizes NTA and UEBA ML/AI algorithms.
- Security Information & Event Management (SIEM) = A forensics-type system for tracking and correlating disparate events from network, system and device logs to generate real-time monitoring & alerts. May include IDS/IPS, NTA, UEBA and SOAR features, or integrate with those services.
#### Protection
- Intrusion Prevention System (IPS) = Monitors and analyzes network behavior patterns to detect unusual events, in order to prevent intrusion attempts. Similar to Intrusion Detection (IDS) but with add'l alerting & response features.
- Web Application Firewalls (WAF) = Redirects incoming web requests to a service that analyzes and filters traffic before passing it through to the web server. Helps prevent web-based attacks like DDoS, SQL injection, and XSS.
- Next-gen Firewall (NGFW) = Combining of a traditional firewall with other features for smarter packet inspection, typically with features like DPI, IPS, SSL inspection, and WAF.
- Firewall-as-a-Service (FWaaS) = Cloud-based NGFW service.
- API Gateway = System utilized to manage service API endpoints and set policy for access. Serves as a proxy and firewall over APIs or microservices -- being more focused specifically on those than a WAF.
- Secure Web Gateways (SWG) or Web Security Gateways (WSG) = Real-time protection of outgoing web requests. Can include employee compliance checking, policy enforcement, and malware detection.
- Email Security = Inbound & outbound email protection, access control and spam filtering. Helps mitigate against email attacks like phishing, or attached viruses & malware.
- Sandbox = Quarantined process to test files in a managed space (such as an isolated ephemeral VM). Isolates and tests new files for malware and zero-day exploits (the unknowns) away from production servers.
- Network Access Controller (NAC) = Service that allows implementing policies to control access to infrastructure from endpoints. This has gotten more popular as number of endpoints has exploded from BYOD (bring your own device) policies and IoT.
- Next-Gen Anti-Virus (NGAV) = Behavior-based tools to help discover and isolate malware and viruses. Unlike traditional AV, which is signature-based, it tries to determine intent in order to identify malicious behavior.
- Endpoint Protection Platform (EPP) = Service deployed on all endpoints for the monitoring and detection of malicious activity. EPP is about protecting the device itself, not the traffic to and from it. That includes NGAV, to help prevent malware and virus attacks, and may include device mgmt and endpoint detection (EDR) capabilities. Remember, endpoint includes any system on a company's network -- each and every server, storage device, workstation, desktop, printer, laptop, mobile device, IoT device, camera, POS systems, etc.
- Advanced Endpoint Protection (AEP) or Advanced Threat Protection (ATP) = Combination of EPP, EDR, and DLP capabilities under a fancier name.
- Cloud Access and Security Brokers (CASB) = Platform to monitor and provide security policy enforcement points between a company and cloud-hosted services, extending security to outside of your firewall. Most commonly used to manage the SaaS services a company utilizes, and block usage of unsanctioned ones. Services could include DLP, SSO, WAF, SWG, threat detection, predictive analytics, and incident response.
- Unified Threat Mgmt (UTM) = The complete package in one hardware appliance, as a souped up next-gen firewall which provides many security features in one. Much simpler for companies to manage instead of piecing together a solution from the desired flavors above, but, as a large downside, provides a potential single point of failure. Made obsolete by cloud-forward solutions like FWaaS.
- Managed Security Services Provider (MSSP) = Outsourced service that uses log aggregation to discover threats and provide response. Customers ship logs to an automated IDS service that provides user alerts via portal.
- Managed Detection and Response Services (MDR) = Outsourced service that uses continuous monitoring to discover threats and provide response. Provides deeper inspection than MSSP, that typically involves human monitoring as well as ML/AI over IDS and EDR (network and endpoint behavior tracking), plus DF/IR services.
#### Response
Systems to automate response handling or help react to an incident.
- Security Orchestration and Automated Response (SOAR) = Service to collect data and automatically respond to low-level security events w/o intervention. Typically interfaces with other security services like IDS/IPS and EPP, to help automate workflows and incident response handling.
- Distributed Denial of Service (DDoS) Mitigation = Tools to help protect against DDoS attacks. Identifies normal conditions & patterns of network traffic for threat detection, alerting, and traffic filtering.
- Breach Containment = Tools to help analyze and contain breaches, and help isolate attackers. Includes systems for hacker deception (decoys) and capture via baited traps (honeypots).
- Digital Forensics and Incident Response (DF/IR) = Advisory services that help clients deal with a security breach, investigating a security incident to determine scope and time-line of breach, and provide response.
- Internet Security Awareness Training (ISAT) = Training services for your workforce to be educated on cybersecurity, and for admins to learn how to identify threats and utilize security layers.
- Business Continuity and Disaster Recovery (BCDR) = Services that back up data instead of relying on local systems. Helps provide operational resiliency in event of service disruptions. Somewhat ancillary to cybersecurity but vital none-the-less.
### A New Dawn
 new trend has started of doing away with purpose-specific appliances, and to instead run these various pieces of your networking as software on a VM stack. This move from appliances to software has really opened up the possibilities of what is possible, as it allows companies to modularize and scale their networking needs easily instead of being locked into using proprietary hardware-based solutions.
#### Software/Virtualization
- Software Defined Networking (SDN) = Software-based networking controllers to replace device appliances. They allow for the networking flows be controlled programmatically, which allow for more flexibility and customization than hardware would typically allow. Splits the controller (control plane, aka the brains) from the data (data plane, aka traffic flows) for maximum flexibility, as you can adjust or scale up one or the other as needed.
- Software Defined WAN (SD-WAN) = Software-based WAN controllers, which provide more flexibility and customization than hardware WAN devices. Can typically mix and match various connection types and topology layouts as needed.
- Network Virtualization = Just as infrastructure servers are getting virtualized [see VMWare and Nutanix], so too is network equipment. Instead of using dedicated, specific-to-purpose networking appliances, companies can utilize VM servers and run network devices as software virtually. Any networking component can be easily scaled as needed, and combining this trend with SDN (splitting control and data planes) gives a huge amount of flexibility in controlling the network's security and data flows, allowing for more adaptive responses.
- Virtual Network Functions (VNFs) or Network Virtual Functions (NVFs) = Specific VMs in your network virtualization stack that take the place of a particular network device: a firewall, proxy, gateway, load balancer, storage node, or telecommunication hookup. [Industry can't decide which way to call it, apparently.]
- Network Orchestration = Automation of SDN networking devices, by using intercommunication via APIs to cross-coordinate between themselves. This allows networks to scale and adjust themselves based on policy settings, without manual intervention.
- Management and Network Orchestration (MANO) = Architectural framework to run and manage VNFs and to control cross-coordination policies between them.
- Software Defined Access (SD-Access) = SDN at the edge of perimeter, having identity mgmt and policy driven rules to control access into the trusted network. Replaces edge firewall/gateway hardware appliances with orchestrated VNFs.
- Intent-Based Networking (IBN) = Network strategy using ML/AI and MANO to automate VNFs and appliances, in order to make "smart" rule policies that are more intent-based vs device-based (yay/nay) rules. Cisco has been a big proponent, as is it attempting to continue to make network appliances relevant.
#### Zero Trust
The rise of software-based networking has brought upon us new possibilities. Maintaining a trusted zone within a network perimeter always had a large downside -- once a threat gets inside the perimeter, it can typically move laterally from the breach point into any other systems within the trusted network, and companies typically have few resources to track intruders down and contain them.
- Micro-segmentation = Creating smaller secure zones in infrastructure, instead of relying on a trusted network or other network segmentation like DMZs. Security becomes more granular and local to each service (per-application), instead of being centralized within perimeter firewalls. However it adds complexity
- Software-Defined Perimeter (SDP) or Black Cloud = Security framework designed to dynamically create direct micro-segmented network connections between the user and the services they can access, once identity is established (trust). Users are never put on the trusted network - it instead creates an ephemeral point-to-point access tunnel from the requester to the services they are allowed to access as determined by policy rules. This prevents lateral movement within the enterprise network, and leaves non-trusted users unable to see any of the internal services available. Also known as "Black Cloud" due to this obscuring of the services within it. CSA states that SDP can stop a variety of network attacks, including DDoS, Exploits, Man-in-the-Middle, and Advanced Persistent Threats.
- Zero Trust Network Access (ZTNA) = Access system based on using software-defined perimeters to create secure network connectivity between entities, but with no implicit trust (regardless of whether they are inside or outside of any perimeter) until an identity is established. Within trusted perimeters, the default access level was "allow", but under Zero Trust, it is now "deny". Zero Trust = Always Verify, as all users must be verified on every system accessed, at all times. And when establishing identity, it can adaptively factor in other attributes and context (time of access, geo-location, and device used) while determining trust. Gartner calls this "Client-Initiated ZTNA" as it requires a client agent to be installed on the endpoint device. Zscaler is adopting this variety.
- Identity Aware Proxy (IAP) = A flavor of Zero Trust that utilizes a cloud service that verifies identity, and, once trust is established, acts as proxy to the services that that user can access. This adds centralized identity checking (IAM) to a Zero Trust stack instead of it being handled per-service, and as such can be used to more-easily "SaaS-ify" legacy on-premise services without having to modify them for Zero Trust. It avoids using SDP micro-segments however, instead it serves as a centralized cloud proxy. Gartner calls this "Service-Initiated ZTNA", as no client agent is needed, but as a downside, it only works with HTTP-based web applications. Google ("BeyondCorp") and Akamai are adopting this variety, as is Okta.
- Zero Trust Privilege = A flavor of Zero Trust for managing and securing Privileged Access (PAM). Instead of securing applications, it controls access to server infrastructure via a Zero Trust method.
#### Added Complexity
However, going Zero Trust requires a huge mentality shift by IT staff maintaining these enterprise networks.

1. Zero Trust is designing the security from the "inside out" instead of the "outside in". You must map out and understand all valid paths a user can take to every server resource. You need to track what systems or users have to talk to what servers or services. For example, what exact systems need to be able to talk directly to your database server, and over what network paths?
2. You must adopt the "principle of least privilege" across your systems. Default access is "deny" under Zero Trust, as opposed to "allow" in traditional trusted networks. Every request to a service must prove identity. You must utilize a role-based access (RBAC) system to limit who can access each system, always keeping users at the lowest level needed.
3. Since security is per-system, every system must verify users & monitor its traffic at all times. Tying Zero Trust services into a common identity tracking system is a must. Every resource should be keeping its own logs, which need to be continuously analyzed. Monitoring and analysis becomes more complex, as expected, since security must be tracked so so granularly.
4. Zero Trust means NO PERIMETER, and hence, no EDGE gateways needed. Your server resources no longer need to be centralized, and can be scattered across any environment. What was edge compute becomes just another server or service. Every server becomes just another endpoint - so your network essentially becomes endpoint-to-endpoint. This layout dovetails nicely with using external SaaS services and cloud infrastructure, as those are just more endpoints. User devices will now talk directly to biz op services and database systems, regardless of where those live. Endpoint security becomes critical, and it must be layered directly with network security.

By combining the benefits of SECaaS services PLUS the endpoint-focused strategy of Zero Trust, and it seems to be a new dawn for cybersecurity. You can now hire the experts in security (SECaaS), instead of having to build and maintain it yourself, while doing away with trusted perimeters by securing everything individually (Zero Trust).

For cloud-first or cloud-native companies, adopting Zero Trust is a much easier choice. For those companies with a lot of existing traditional networking infrastructure around securing a perimeter, they likely want to move slow. The SECasS must help them adopt these new strategies while safely migrating their existing infrastructure towards a Zero Trust driven one.
#### A Proactive Mindset
One maxim in security is that you can never have enough.
So every company needs all these services:
- A component to manage user identities and be utilized to establish trust (IAM, IGA, PAM).
- A component to manage and protect the endpoint devices (EPP/NGAV, EDR).
- A component to secure incoming traffic (ZTNA, IAP, WAF, API Gateway) to a company's services.
- A component to secure outgoing traffic from endpoints and communications with SaaS providers (SWG, CASB, DLP).
- A component to watch and monitor everything (SIEM) and orchestrate the user/policy changes (SOAR).
- And finally, a component to apply ML/AI over it all to analyze the entire stack - network, devices, & users - and to adapt the security rules & responses as necessary (SIEM, NTA, UEBA, EDR, MDR, SOAR).

Beyond Zero Trust, Gartner ultimately recommends a Continuous Adaptive Risk and Trust Assessment (CARTA) mindset, which uses the above layers just mentioned, but recognizes that security decisions and responses must continuously adapt to new threats.
To achieve this, they state several security layers must be present:
1. Identity mgmt system
2. Zero Trust networking (incoming traffic)
3. Endpoint protection (device and traffic)
4. Continual monitoring with ML/AI

A big part of becoming proactive is to factor in context and behavior of users and their network traffic.
- Indicators of Compromise (IOCs) = Reactive approach that tries to detect the unique characteristics of a breach. Examples: detecting malware, exploits, or attack signatures.
- Indicators of Attack (IOAs) = Proactive approach focusing on detecting the intent of what an attacker is trying to accomplish, by looking a user behavior and network traffic. Determines the series of actions an adversary would take. Examples: detecting code execution, persistence, stealth, or lateral movements within the network.

Given the vast number of unknown vectors, using ML/AI over an adaptive CARTA strategy appears to be a much better approach than the traditional reactive "fingers crossed" methods. Security components will still have a reactive side (analyzing logs), but it can now react better and adapt in real-time.
#### Putting it all together
Gartner released another research paper to define a new recommended path forward for overall enterprise networking & its security, that basically agrees with and combines all the above.

In today's reality, so many external users are trying to get into a company's systems...A network must remain agile, and not be locked into an inflexible security posture.
- Secure Access Service Edge (SASE) = Combination of software-defined network capabilities (eg SD-WAN, SD-Access), with comprehensive network security at its edge for incoming and outgoing traffic (eg SWG, CASB, FWaaS and ZTNA), utilizing CARTA methods (eg NTA, UEBA) to learn and adapt.

SASE combines:
- Software-defined networking, to network your enterprise and IaaS and end users together.
- At its edge must be a complete cloud-based, identity-centric Zero Trust and CARTA solution to secure all endpoint traffic.

These two sides must go hand-in-hand now, and converge as an orchestrated whole - either from a complete all-in-one vendor, or one vendor for networking and another for cloud-based cybersecurity over it. While Gartner posits that uber-services will arise that provide it all, I think our specialized SECaaS providers will continue to be successful
### Hypergrowth
Now let's talk about the pillars of Zero Trust & CARTA, and what is driving hypergrowth within it. Then I will break down the technological landscape of each of these hypergrowth companies in this space: Okta, Zscaler, CrowdStrike and Elastic.

while SECaaS is just getting started. There are a lot of old-school players in this field (McAfee, Symantec, Cisco, Juniper, Ciena, Palo Alto) that have a lot of disruption coming from all angles.
#### Silos cannot compete
#### Drivers of hypergrowth
I feel that SECaaS services, in particular, can have a very strong defensive position of being EXTREMELY sticky due to these aspects:
- They must be a SECaaS service that is disrupting the status quo of traditional network security (castle-and-moat and hub-and-spoke, with its reliance on having a puzzle of task-specific hardware appliances to maintain a trusted perimeter). That means they are adopting the new paradigms of Zero Trust & CARTA, and have continual monitoring and ML/AI analytics to analyze their own and their customer base's security, and have the ability to adapt as necessary.
- They must be cloud native, so they can scale when needed, and more easily reach all systems and endpoint devices (whether on-prem or cloud-based or mobile).
- They must have a core competency within the pillars of Zero Trust and CARTA that customers trust, as seen in the proof of high revenue growth combined with high customer and $NER growth. That shows that customers are flocking to the service as new customers, and then expanding use from there. Don't guess at what technologies MAY be up-and-coming or disruptive -- the proof is in execution resulting in hypergrowth.
- They must have a platform developed around their core, that enables interoperability and orchestration, to allow customers to tie their security efforts together, and more easily integrate with other services the company may rely on. That platform also gives the provider the ability to then easily enhance their offerings in order to expand into new markets and increase TAM.
- Proof that the company is expanding into adjacent product lines and markets that the platform enables and that the customers want. You must see adjacent products appearing (or being bolted on as tuck-in acquisitions) that leverage the existing platform while expanding it into new directions. This allows new product lines to continue the hypergrowth after growth of the initial core product levels off. I think it is very helpful to map out where our companies ARE NOW but also watch the signals as to WHERE THEY ARE GOING from here.
#### Competition
As you can imagine, there is a LOT of competition in the network security space. From just perusing Gartner Magic Quadrants and reviews, I found:
- Network Firewalls - Palo Alto, Fortinet, Cisco, CheckPoint, Sophos, Juniper, Barracuda
- UTM (SMB Firewalls) - Fortinet, Check Point, Sophos, Cisco, Juniper, Barracuda
- WAF - Imperva, Akamai, Cloudflare, F5, Fortinet, Barracuda, Oracle, Rapid7, AWS, Citrix
- SWG - Zscaler, Broadcom/Symantec, Cisco, McAfee, Sophos, Barracuda, Trend Micro, SonicWall
- EPP - Broadcom/Symantec, CrowdStrike, Trend Micro, Sophos, McAfee, Dell/RSA, VMWare/Carbon Black, Elastic/Endgame, Blackberry/Cylance, Microsoft, Palo Alto, Cisco, FireEye, Fortinet
- EDR - Broadcom/Symantec, McAfee, Dell/RSA, CrowdStrike, VMWare/Carbon Black, Elastic/Endgame, Blackberry/Cylance, Microsoft, Palo Alto, Cisco, FireEye, Fortinet
- IDM - Okta, Microsoft, Oracle, IBM, PingID, Centrify, ForgeRock, Broadcom/CA Tech, Sailpoint, Auth0
- IGA - Sailpoint, Okta, IBM, Oracle, Broadcom/CA Tech, Dell/RSA, SAP, Microsoft
- PAM - CyberArk, Okta, BeyondTrust, Centrify, Broadcom/CA Tech, OneID
- SIEM - Splunk, IBM, LogRhythm, Dell/RSA, McAfee, Rapid7, Fortinet... or Elastic for DIY

I believe the focused cloud-based disruptors have little to fear from these all-in-one providers rolling up new features via acquisition, especially from those whose core competency is outside of cybersecurity.
### A Look at Some Hypergrowth Companies
As mentioned before, companies adopt "defense in depth" by layering security solutions together. To build a multi-layered fortress, CARTA highlights needing Identity, Incoming Protection (Zero Trust), Outgoing Protection (SWG/CASB), Endpoint Protection (Devices), and Monitoring/Orchestration, with ML/AI over it all. Here are 4 companies that hit one or more of these complementary layers: Okta, Crowdstrike, Zscaler and Elastic. I guess I should consider them a "basket of Zero Trust" even though that was not the intent at the time -- I selected them first and foremost for their hypergrowth.
- Identity mgmt = Okta
- Incoming protection (Zero Trust) = Zscaler, Okta
- Outgoing protection (SWG/CASB) = Zscaler
- Endpoint protection (Devices) = Crowdstrike, Elastic
- Monitoring = Elastic ... plus all the others being very monitoring friendly w/ integrations to 3rd party SIEM and SOAR
- ML/AI = all the above
