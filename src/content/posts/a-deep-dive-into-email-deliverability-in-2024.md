---
title: "A Deep Dive into Email Deliverability in 2024"
date: 2024-04-08T17:31:40Z
category: reading
description: "in October 1971, Ray Tomlinson, a graduate of MIT, sent the first email over a network.. Last year, [~121 trillion emails](https://www.statista.com/statistic..."
source: "https://www.xomedia.io/blog/a-deep-dive-into-email-deliverability/"
---

in October 1971, Ray Tomlinson, a graduate of MIT, sent the first email over a network.. Last year, [~121 trillion emails](https://www.statista.com/statistics/456500/daily-number-of-e-mails-worldwide/) were sent between [~4.3 billion people](https://www.statista.com/statistics/255080/number-of-e-mail-users-worldwide/).
### Overview
On October 3, 2023, Google and Yahoo announced upcoming email security standards to prevent spam, phishing and malware attempts. Outlook.com (formerly Hotmail) also encourages senders to abide by these standards.

The biggest change involves implementing email authentication standards like SPF, DKIM, and DMARC.
Here’s the complete listing of [Gmail SMTP errors codes](https://support.google.com/a/answer/3726730).
### Who’s Affected?
Enforcement primarily pertains to Bulk Senders:
> “A bulk sender is any email sender that sends close to 5,000 messages or more to personal Gmail accounts within a 24-hour period. Messages sent from the same primary domain count toward the 5,000 limit.”
These guidelines require bulk senders to enable SPF, DMARC and DKIM for their domains.
### The Guidelines
Google:
- [Email sender guidelines](https://support.google.com/a/answer/81126)
- [Email sender guidelines FAQ](https://support.google.com/a/answer/14229414)

Yahoo:
- [Sender Requirements & Recommendations](https://senders.yahooinc.com/best-practices/)

Outlook:
- [Set up DMARC to validate the From address domain for senders in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide)

Here’s a quick summary of the guidelines:
1. Sender Authentication: Senders should implement email authentication protocols like SPF, DKIM, and DMARC to prevent email spoofing and phishing attempts.
2. Bulk Senders Requirements: Sending unsolicited bulk emails can lead to deliverability issues (spam filtering) and reputation damage.
3. Easy Unsubscribe: Implement easy unsubscribe options (One-click Unsubscribe).
4. Engagement: Avoid misleading subject lines, excessive personalization, or promotional content that triggers spam filters.

Special Considerations:
1. Keep your email spam rate is less than 0.3%.
2. Don’t impersonate email ‘From:’ headers.
3. Ensure that sending domains or IPs have valid forward and reverse DNS records, also referred to as PTR records.
4. Use a TLS connection for transmitting email.
5. Make sure your forward and reverse DNS records are valid.
6. Ensure receivers can easily unsubscribe from your marketing messages.
7. Format messages according to the ‘Internet Message Format standard’ RFC3522
8. If you regularly forward email, including using mailing lists or inbound gateways – add ARC headers to outgoing messages.
9. For direct mail, the domain in the sender’s From: header must be aligned with either the SPF domain or the DKIM domain. This is required to pass DMARC alignment.
10. Marketing messages and subscribed messages must support one-click unsubscribe, include a clearly visible unsubscribe link in the message body and process recipient unsubscribe requests within 2 days.
11. Reference [this](https://support.google.com/a/answer/81126) for the full list.
### Sender Authentication
There are 3 authentication standards to help protect an organization’s email:
- SPF (Sender Policy Framework) specifies the servers and domains allowed to send email for your business. This protects against spoofing and helps prevent your emails from being flagged as spam. This is added as a record on public DNS server that is used to check the source IP of the email and compares it with a DNS TXT record.
- DKIM (DomainKeys Identified Mail), used to digitally sign every outgoing message sent from your organization. The receiving server uses this to verify that it came from your business. It is a unique key for domain that allows mail servers to verify email authenticity and resist tampering. It is a generated key that is configured on a public DNS server.
- DMARC (Domain-based Message Authentication, Reporting and Conformance) is an email authentication protocol designed to give domain owners the ability to protect against spoofing, phishing, email scams and other cyber threats. It instructs receiving servers on how to handle outgoing messages from your organization that don’t pass SPF or DKIM.

DMARC:
1. Reduces email Spoofing & Phishing: Prevents bad actors from impersonating an organization’s domain by verifying which domain the email originated from.
2. Improves Email Deliverability: Sets policies for how the receiving email server should deal with failures.
3. Provides Reporting & Feedback: DMARC provides a reporting mechanism for policy actions performed by the above policy.

BIMI (Brand Indicators for Message Identification), not part of the new Gmail or Yahoo guidelines – is an emerging standard that enables organizations to showcase their validated brand logo in authenticated emails.
1. Verified Brand Logo: Organizations implement a BIMI record containing a verified brand logo.
2. Reduces Phishing Attacks: The visual verification helps users distinguish legitimate emails from potential phishing attempts (e.g., bank0famerica.com vs bankofamerica.com, paypalsupport.com vs support.paypal.com, etc).
3. Brand Recognition: By displaying a familiar logo, BIMI can enhance brand recognition and build trust with recipients.

Here’s a simple diagram to help explain the entire email journey:

1. Sender composes and sends an email.
2. Sender’s MTA (Mail Transfer Agent on mail server) adds a DKIM signature to the email header as a special field..
3. Recipient’s MTA checks SPF and DKIM records.
4. DMARC alignment is verified, and the policy is applied:
   1. If a message passes authentication by the receiving server – Deliver to user’s inbox.
   2. If a message fails authentication by the receiving server:
      1. Quarantine (send them to recipients’ spam folder).
      2. Reject messages are never deliver to the recipient. The receiving server usually sends a bounce message to the sender
### Impact
[Google’s AI Spam filtering algorithms](https://workspace.google.com/blog/identity-and-security/an-overview-of-gmails-spam-filters) block 99.9% of spam

The following email statistics reveal the impact these new security guidelines will have on deliverability and engagement (especially for email marketing campaigns and newsletters):
- In 2025, the number of email users is expected to reach 4.6 billion ([Techjury](https://techjury.net/blog/email-marketing-stats/))
- In 2023, we expect to see an average of over 347 billion emails sent per day ([Oberlo](https://www.oberlo.com/statistics/how-many-emails-are-sent-per-day))
- There are projected to be an estimated 4.37 billion email users in 2023 ([Statistics](https://www.statista.com/statistics/255080/number-of-e-mail-users-worldwide/))
- Millennials and Gen Xers rely on their email more than any other generation at 98% ([Statista](https://www.statista.com/statistics/1332384/us-users-depending-on-emails-by-age/))
- In 2021, an average of just over 2 hours a day are spent on email ([Statista](https://www.statista.com/statistics/1332517/time-spent-checking-emails-us-users-daily/))
- 63% of people who open up an email try and find a discount ([LXA](https://www.lxahub.com/stories/email-marketing-stats-and-trends-for-2023))
- 99% of email users check their inbox every day, with some checking 20 times a day ([HubSpot](https://blog.hubspot.com/marketing/email-marketing-stats))
- The image above tells us that email marketing revenue is estimated to reach almost 12.5 billion by the end of 2024 ([Statista](https://www.statista.com/statistics/812060/email-marketing-revenue-worldwide/))
- 58% of consumers check their email first thing in the morning ([Optinmonster](https://optinmonster.com/is-email-marketing-dead-heres-what-the-statistics-show/))
- 84.3% of consumers say they check their emails at least once a day ([Mailjet](https://www.mailjet.com/resources/research/email-engagement-2021/))
