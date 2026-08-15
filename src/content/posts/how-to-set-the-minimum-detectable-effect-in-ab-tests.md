---
title: "How to set the Minimum Detectable Effect in AB-Tests"
date: 2022-05-29T20:42:18Z
category: reading
description: "The MDE is necessary to calculate the minimum required sample size, which is the number of observations that have to be collected. An AB-Test’s results must..."
source: "https://towardsdatascience.com/how-to-set-the-minimum-detectable-effect-in-ab-tests-fe07f8002d6d"
---

### What does the Minimum Detectable Effect mean?
The MDE is necessary to calculate the minimum required sample size, which is the number of observations that have to be collected. An AB-Test’s results must not be analyzed before this threshold has been reached.

The MDE is the minimum effect size that should be detected with a certain probability.
### Why the MDE matters
If you wanted to prove that the quality of 50% of the screws being produced was below standards, how many screws would you examine before drawing a conclusion? Probably less than if you wanted to prove that 2% of the screws are low quality.

The smaller the effect we’re interested in, the more samples we need to collect before drawing any conclusions.
### Controlling Risk and Costs with the MDE
In some cases, having a very low MDE can thus be a waste of money and time. Imagine a product team is testing a very promising MVP on a marketplace website. Implementing the change is risky and would cost months of development work but could lead to a massive increase in user conversion. In this case, the team would need an uplift in the conversion rate of at least 5% to justify the costs. Setting a significantly lower MDE would thus not be necessary for the underlying cause and prolong the test unnecessarily (the test would be overpowered).

At the same time, we need to ensure that the AB-Test has the right statistical set up to detect an effect if there exists one. Let’s assume we conduct an experiment where we change the copy on our website’s Buy Now-button to increase the conversion rate. We only power our test to detect an increase in conversion rate by at least 50% with a certain probability. In this case, the test would be very likely not to deliver any significant results even if the change had a positive effect. We might wrongly conclude that the change doesn’t make a difference and decide to continue using the old copy (in this case, one speaks of underpowered tests).
### Setting an appropriate MDE
MDE highly depends on the use case.

Your minimum MDE should be the smallest effect that would justify implementing the change that is being tested.

come up with an exact number? It comes down to a simple ROI calculation. Consider the following (very simplified) situation:
- A team is validating an MVP to make users add travel insurance to their purchase on a travel website’s checkout.
- The website registers 2000 bookings per day (730.000 per year).
- The estimated net profit for insurance is 3$ per user.
- Implementing the full feature would cost the team ca. 150 developer hours with, let’s say 500$ per hour, totaling up to 75.000$ (not considering any opportunity costs).

On a yearly basis, the website would have to sell 25.000 insurances to break even, equalling 3.42% of bookings adding insurance.

With the insurance conversion rate being the primary metric for the experiment, 3.42% would be a reasonable MDE. Any value lower than this would not be of interest to the team and would unnecessarily prolong the test’s duration.
