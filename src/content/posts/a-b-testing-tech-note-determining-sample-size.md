---
title: "A/B Testing Tech Note: determining sample size"
date: 2022-04-14T11:27:49Z
category: reading
description: "There’s no simple answer or generic “rule of thumb” that you can use, but you can very easily determine the right sample size to use for your test."
source: "https://signalvnoise.com/posts/3004-ab-testing-tech-note-determining-sample-size"
---

There’s no simple answer or generic “rule of thumb” that you can use, but you can very easily determine the right sample size to use for your test.
### What drives our needed sample size?
There are a few concerns that drive the sample size required for a meaningful A/B test:
- 1) We want to be reasonably sure that we don’t have a false positive—that there is no real difference, but we detect one anyway. Statisticians call this Type I error.
- We want to be reasonably sure that we don’t miss a positive outcome (or get a false negative). This is called Type II error.
- We want to know whether a variation is better, worse or the same as the original. Why do we want to know the difference between worse vs same? I probably won’t switch from the original if the variation performs worse, but I might still switch even if it’s the same—for a design or aesthetic preference, for example.
### What not to do
There are a few “gotchas” that are worth watching out for when you start thinking about the statistical significance of A/B tests:
1. Don’t look at your A/B testing tool’s generic advice that “about 100 conversions are usually required for significance”. Your conversion rate and desired sensitivity will determine this, and A/B testing tools are always biased to want you to think you have significant results as quickly as possible.
2. Don’t continuously test for significance as your sample grows, or blindly keep the test running until you reach statistical significance. Evan Miller wrote a great explanation of why you shouldn’t do this, but briefly:
   If you stop your test as soon as you see “significant” differences, you might not have actually achieved the outcome you think you have.
   If you keep running your test forever, you’ll eventually reach a large enough sample size that a 0.00001% difference tests as significant. This isn’t particularly meaningful, however.
3. Don’t rely on a rule of thumb like “16 times your standard deviation squared divided by your sensitivity squared”. Same thing with the charts you see on some websites that don’t make their assumptions clear.
### How to calculate your needed sample size
1. Specify the outcome you’re trying to measure. We typically measure conversion to signup as the primary measure, but depending on what you’re testing, it might be button clicks, newsletter signups, etc.
2. Decide how substantial of a difference you’d like to detect – this is the sensitivity of the test. I generally target an A/B test that will have a statistically meaningful sample size that detects a 10% difference in conversion rate (e.g., to detect 11% vs. 10% conversion rate).
3. Calculate the required sample size based on your baseline conversion rate and your desired sensitivity.
   - power analysis – is a statistical tool to determine the minimum sample size required so that you can be reasonably confident that you are detecting meaningful differences between two values.
   - two independent – since we fully separate visitors (they see only the A or only the B variant), our test is nominally independent; the results for variation A aren’t based on the results for variation B.
   - proportions – we’re comparing conversion rates, which are a proportion.
