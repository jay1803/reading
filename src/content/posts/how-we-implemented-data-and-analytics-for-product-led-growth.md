---
title: "How we implemented data and analytics for product-led growth"
date: 2022-03-15T21:37:56Z
category: reading
description: "Mixpanel’s PLG approach to new business looks like this:"
source: "https://mixpanel.com/blog/data-analytics-product-led-growth/"
---

Mixpanel’s PLG approach to new business looks like this:

From the data and analytics perspective, we needed to do two things to make this
process work:
- We needed to track potential customers along all the paths they may take in the diagram above and route them to sales when appropriate with the right contextual information.
- We needed to make data and analysis on how accounts are progressing through the entire diagram above available self-serve to everyone at Mixpanel.
The big challenge with implementing a PLG strategy is that you need to make use
of product data, marketing data, and sales data all together.
### Data infrastructure for PLG
With that in mind, below is how we set up our data infrastructure.

### Problem 1: Identity resolution
#### Product data
##### Transactional data
##### Clickstream data
#### Sales data
#### Marketing data
#### Tying them all together
- Transactional ≤≥ Clickstream ⇒ On signup, identify/alias your anonymous UUID to your user ID from the transactional database
- Product ≤≥ Sales ⇒ Create/update a lead on signup and make sure to tag the user ID on the lead/contact
- Sales ≤≥ Marketing ⇒ Most marketing tools already track marketing users to Salesforce leads and accounts
### Problem 2: Focus
#### Ideal customer profile (ICP)
##### Domain is key
#### Getting to value
### Conclusion
