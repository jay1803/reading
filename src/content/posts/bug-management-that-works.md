---
title: "Bug management that works"
date: 2024-10-08T13:48:16Z
category: reading
author: "Gergely Orosz"
description: "Dogfood products. The term “dogfooding” is the name of the common practice of devs and employees using a product while they are building it, pre-release."
source: "https://newsletter.pragmaticengineer.com/p/bug-management-that-works-part-1"
---

### 1. Finding bugs
- Dogfood products. The term “dogfooding” is the name of the common practice of devs and employees using a product while they are building it, pre-release.
- At smaller companies, be close to users.
  These places tend to be closer to users and can use this to build a relationship with users who get invested in the product and the reporting of bugs.
- Consider alpha and beta testing at larger companies. Alpha and beta testing is about giving customers access to unfinished, less stable versions of a product. “Alpha” usually refers to a latest build that has had little to no QA testing. “Beta” versions have had some testing, but not as much as a full release.
- Automation: testing and code analysis. Unit tests, integration tests, end-to-end-tests, and other automated tests, are great ways to catch regressions, which is a software bug introduced into a feature after the feature was working correctly; the feature has ‘regressed’ into a faulty state.
- Code reviews. These serve multiple purposes, offering a second pair of eyes to double check code, spread knowledge, and follow not-yet-automated conventions, and more.
- Define what a bug is. Users often report “bugs” when they mean missing features, so it can be helpful for teams to agree what a bug is and how to categorize them.
### 2. Users reporting bugs
Great reports and data come from simple, suitable processes. Features of useful bug reports:
- Useful metadata (e.g. version, device, system metrics)
- Relevant context (e.g. on mobile while connected to bluetooth speaker and poor connectivity, on a server in this region during lunch hour, on a debug build with these feature flags active, etc)
- Straightforward to reproduce, or have reproduction steps
- Reported by users who trust a reported bug will be fixed

Make it easy to create quality bug reports. Walter de Bruijn, Head of Engineering Productivity at Miro suggests this is critical:
Make the reporting process accessible. If creating a bug report is too complicated, it discourages reporting. There are ways to make it accessible:
#### Scaling bug reporting processes
Smaller companies and startups: bug reports are usually simple, and the reporting process is lean because time is precious and knowledge is dense.

Mid-sized companies and scaleups: process matters more, and these places are big enough for it to be wasteful for everyone to keep tabs on reported bugs.

Large companies: investing in automated processes is worthwhile due to the size and nature of the business:
