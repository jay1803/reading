---
title: "An Okta technical review"
date: 2023-12-28T16:15:09Z
category: reading
description: "EVERY COMPANY MUST be a tech-driven company."
source: "https://hhhypergrowth.com/an-okta-technical-review/"
---

EVERY COMPANY MUST be a tech-driven company.
- EVERY COMPANY MUST rely on applications to run the day-to-day operations of their business.
- EVERY COMPANY MUST maintain security and monitoring over those systems.
- And EVERY COMPANY MUST ultimately take advantage of analytics over those systems, to better drive their strategy and stay ahead of the competition.
### Security Basics
You need to understand these terms, as I believe it helps you more clearly see the potential in Okta as an investment.
- Authentication (authN) = proving to a system that you (the user) are who you say you are. Can be as basic as username & password, a PIN code, or as advanced as biometric scans on your phone with TouchID (fingerprint) and FaceID (facial recognition). End result is being a trusted user.
- Authorization (authZ) = once you are authenticated, now what can you do? What level of access do you have? This is normally tracked via some combination of RBAC (role-based access control) or ACLs (access control lists that track the rights each individual user has for every action in the system). Roles are fairly self-explanatory. For example: In a sales tracking app, are you a salesperson tracking their assigned leads, or a manager needing dashboards to oversee metrics? In an HR app, are you the employee entering time sheets and viewing their own paystubs, or a manager that is managing the users and approving payroll?
- Authentication factor = categories of info that is user is presenting during authentication. Either something you know (a password or PIN), something you have (a token or device), or something you are (biometric data). Most common form is username and password.
- One-Time Password or PIN (OTP) = security mechanism where a single use temporary validation password or PIN is generated for authentication, provided to the user via a trusted method. Stronger than static passwords, as it is not subject to common attack vectors like man-in-the-middle or replay attacks.
- Security token = security mechanism where a temporary code must be used that is associated with a given user's identity for a set time frame. Common in authentication systems where trusted hardware devices (like RSA SecurID) or software apps can generate a token to use for login attempts, each valid for a short time window (say, 30 seconds) before it then refreshes with a new one.
- Multi-Factor Authentication (MFA) or Two-Factor Authentication (2FA) = having a system require more than a single authentication factor (user credentials) to log into it. First called 2FA until security folks realized they should leave it a bit more open-ended. If you use online banking, you likely have been using some type of MFA to complete your login. Forms of MFA may include receiving an OTP via SMS or email, using an OTP from a software app, using a software- or hardware-based token generator, or providing biometric information like a fingerprint, retinal scan or facial recognition.
- Lightweight Directory Access Protocol (LDAP) = an open protocol and data store (a "directory") for tracking user authentication (credentials) and authorization (access rights) on a organization's trusted private network. A common one is Active Directory (AD), Microsoft's LDAP service for Windows networks.
- Identity and Access Management (IAM) = a application to track and manage users' authentication and authorization details across an organization's systems.
- Provisioning = process in IAM that relates to automating authorization changes (access rights) when users are created, modified, disabled or deleted. An example is when a new employee on-boards, HR would need to coordinate with IT to get accounts and rights set up in multiple systems (such as systems for payroll, benefits, travel expensing, email account, server or software access, etc). This step has becoming increasingly complex with the proliferation of SaaS tooling!
- Delegate = handing your access rights over to another trusted system or user.
- Federation = common standards and protocols to enable identity sharing across trusted disparate systems. This is the key to enabling inter-dependencies between SaaS apps!
- Security Assertion Mark-up Lang (SAML) = open standard to pass authentication and authorization data between federated parties (the user, an identity manager, and the service the user is accessing). Typically used in enterprise systems.
- Open Authorization (OAuth) = an open standard for token-based authentication to authorize across systems (enabling "delegated authorization"). For example, this enables how you can allow LinkedIn to access your GMail contacts, or let Yelp post on Twitter on your behalf. OAuth 2.0 is the current standard. After authentication, OAuth will generate a token that subsequent requests can use for a limited time (say, an hour), instead of requiring re-authentication each request. Internally the system will track what tokens are associated with what identity, and will expire or invalidate those tokens as needed.
- OpenID Connect (OIDC) = an identity layer over OAuth 2.0, allowing OAuth authorization across cooperating systems over a common identity (enabling "federated authorization"). For example, this allows how you can use a Google or Facebook account to log into Yelp or LinkedIn, where it then creates a new local account within that app, linking back to that Google or Facebook identity for needed details like name or email. Typically used in web and mobile apps.
- Single Sign On (SSO) = the ability to use same credentials to authenticate into multiple disparate systems. SSO is enabled by SAML or OIDC. (NOTE: SAML or OIDC are competing standards for identity intercommunication, with different process flows and message formats. OIDC is newer, and IMHO, more streamlined for using with web & mobile apps and APIs.)
- Federated Identity Management (FIM) = an IAM system linking your users' identities across multiple disparate systems. SSO is one of the important features federation enables.
- Identity-as-a-Service (IDaaS) = FIM SaaS provider.
- Zero Trust Security = newly emerging business strategy for keeping systems secure, by no longer trusting a network perimeter (such as a firewall blocking the public internet from accessing a company's private network) to isolate trusted users from untrusted. Zero Trust = Always Verify -- all users must be verified on every system at all times.
### Okta Overview
Okta is all about identity management. Identity is about knowing who a user is, what systems they can access, and what they can do in that system once in. Okta is helping companies mitigate the huge overhead needed to manage and track their users across all their systems -- whether those users are their workforce (employees, contractors and partners) or their customers.

Okta is Identity-as-a-Service (IDaaS), which provides identity management capabilities for businesses (Okta's customer). Companies sign up and pay Okta, on a monthly basis per user, to manage their workforce users (controlling what systems and data they can access) and/or their customers (controlling access to the company's software), allowing companies to embrace a Zero Trust security paradigm.

Companies today are spread out more and more (remote employees, global locations), and are utilizing a wide variety of 3rd party applications as deeply integrated pieces of their day-to-day operations. For example, they need to use SaaS applications for sales & marketing (Salesforce, Marketo), HR and payroll (Workday, Paycom), communications (Slack, Gmail), and document mgmt (Google Suite, Office365), and on and on. Beyond business operations, companies who develop their own software on on-premise, IaaS (cloud compute) and PaaS (cloud platforms) systems need to manage developer and sysadmin access, developer tooling (Atlassian, Github) and infrastructure monitoring (Splunk, New Relic).

Rather than manage individual user credentials and rights across all these applications separately, companies use a FIM provider to do it for them, so users can log into the provider, and via SSO, be able to access all the internal and external systems needed. Think of it as getting a wristband at an amusement park, which you use to ride every ride within (auth once, access many), instead of having to buy separate tickets per ride (auth each time).

Once a business starts using a IDaaS provider to manage their users across all their internal and 3rd party systems, I don't see them EVER GOING BACK to a self-managed solution. This means Land and Expand is the name of the game for Okta
### Product Lines
Okta Identity Cloud is the primary platform or ecosystem that Okta has built, and all its SaaS products are within. This platform is built around identity - interconnecting all the employees, contractors, and partners a business might have, as well as their customers.

At its core, Okta depends on integration. Okta Integration Network (OIN) is their platform's collection of pre-built integrations with that vast pool of 3rd party SaaS systems.
### Segments
#### Workforce Identity
This segment is comprised of products for tracking workforce access to a company's internal or 3rd party (SaaS providers & APIs) systems.
#### Single Sign On (SSO)
#### Universal Directory
Cloud-based IAM, providing a single location to manage all users, groups and devices. Can authenticate against existing LDAP or AD service. Meta-directory can combine identity metadata from multiple sources. Integrates with all OIN apps over LDAP or API.
#### MFA (Multi-Factor Auth)
#### API Access Managment
#### Lifecycle Managment
Automate any business process involving users. Manage identity access and automate triggered processes after workforce events via customizable policy engine. For example, auto-provision OIN app access after employee onboarding or dismissal.
#### Customer Identity
Outside of those workforce-focused products is the Customer Identity segment (originally known as API Products). These products are for tracking customer access by companies developing their own SaaS solutions, who want to manage their customer accounts while integrating better security and federation capabilities to be able to work with other systems.

Adobe did a major pivot to cloud, both in product (such as Creative Cloud, which took their softwares for creatives from licensed to SaaS) and in tooling (they shifted from on-prem hosted apps to the cloud). They left their legacy SSO solution behind and migrated their 20.5k employees to use Okta SSO to access 300+ cloud apps in only 3 months!

think Adobe is going to back Okta out of every product of theirs? They have a set annual fee for unlimited number of customer identities across unlimited products.
### New Pivots
#### Okta Hooks
Customers can use code to customize Okta policies and behaviors. Increases extensibility of platform, as it enables new custom integrations and downstream workflows.
#### Okta Identity Engine (OIE)
#### Risk-based Authentication
#### Advanced Server Access
#### Access Gateway
#### Okta Ventures
### Acquired Products
#### ScaleFT (Jul 2018)
The Advanced Server Access product just released is all from last summer's ScaleFT acquisition. The ephemeral client certifications that enable "Continuous Authentication" methods are directly from their Server Access product.
#### Azuqua (Mar 2019)
Allowed for quickly creating complex workflows between SaaS tools, in a no-code visual designer.
### Final Takeaways
Before now, I would have placed Okta in the IT/Security category (in a way that oversaw biz-ops use of SaaS apps), but after this exercise, I now realize that Okta seems unique in that it spans ALL these categories.

Okta is clearly intent on embedding itself deeper and deeper into the workflows of its customers. I will be keeping Okta in the "top tier" of my holdings until another company can prove itself more invaluable to businesses.
