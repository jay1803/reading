---
title: "The Easiest Way to Mess-up Email Deliverability (MX, SPF, DKIM, DMARC)"
date: 2024-03-28T16:04:48Z
category: reading
description: "The single most important way to improve email deliverability is properly configuring your email domain."
source: "https://www.spiralytics.com/blog/email-deliverability-domain-configuration/"
---

### Email Domain Check: The Secret to Improving Email Deliverability
The single most important way to improve email deliverability is properly configuring your email domain.
### What is Domain Reputation?
Domain reputation is a metric that checks your website’s credibility and trustworthiness across search engines. Email service providers evaluate your domain reputation on a scale of 0 to 100, much like a credit score. Your score is based on the number and quality of links pointing to your domain.
### Are Your Email Domains Properly Configured? (How to Check Email Domain)
#### Google’s Check MX Tool Results of Over 100 Clients

How can you properly configure your email domain? Well, there are two key methods:
1. Email Domain Validation
2. Email Domain Authentication
### What is Email Domain Validation?
It delves into checking a domain’s mail exchange (MX) record.
### Email Domain Validation Test with Google’s Check MX Tool
The Check MX Google Admin Toolbox can help you check for problems with the configuration of your domain. Some points the tool checks are:
- Domain should have at least 2 NS servers
- Naked domain must be an A record (not CNAME)
- SPF must allow Google servers to send mail on behalf of your domain
- MX lookup must fit in one UDP response packet
### What is Email Authentication?
Email authentication is a solution using multiple technical methods to verify that a message isn’t forged. With 70% of global emails classified as malicious, email authentication prevents spoofing, phishing scams, and other instances wherein an email appears legitimate but is actually from a malicious third party.
#### Email Domain Authentication Test with MX Toolbox’s SuperTool
If you’re using Google, it checks across the three email security controls, namely:
- SPF – Identifies the servers and domains authorized to send an email on behalf of your organization.
- DKIM – Adds a digital signature to outgoing messages, letting receiving servers verify that the email was from your organization.
- DMARC – Tells receiving servers what they want to do with outgoing messages from your organization if they aren’t SPF or DKIM.
