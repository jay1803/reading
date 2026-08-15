---
title: "Understanding Twitter's Algorithm"
date: 2023-04-10T15:12:06Z
category: reading
description: "Understanding how Twitter Ranking works, which will benefits for [[roam:Social Media Marketing]]."
source: "https://tanay.substack.com/p/understanding-twitters-algorithm"
---

## Related
Understanding how Twitter Ranking works, which will benefits for [[roam:Social Media Marketing]].
## Understanding Twitter's Algorithm
### The Algorithm Explained
1. Retrieval: Twitter’s algorithm fetches the ~1500 “best” tweets total for a given user in a given session across multiple sources.
2. Ranking: It then ranks those tweets using a machine-learning model
3. Filtering: It then applies a few heuristics and filters to remove things you’ve blocked/muted/seen
4. Mixing: Lastly, it mixes in a few promoted tweets and other Twitter units (that aren’t organic tweets).
### 1. Retrieval
It uses two sources: (1) in-network sources (the top tweets from people you follow) and (2) out-of-network sources to try to generate an initial list of ~1500 tweets.
1. <<<In-network sources>>>: The universe of in-network tweets is basically all the tweets from all the people you follow that you’ve not seen, which applies some light ranking (detailed later) to determine which are the top ones.
2. <<<Out-of-network sources>>>: To get the very best of Twitter from the people you don’t follow, which as one can imagine can be 100s of millions of tweets
   1. <<<Social graph>>>: Generate tweet recommendations based on Tweets popular in your social graph. About 30%.
   2. <<<Topic embeddings>>>: Generate tweet recommendations based on the topics you tend to enjoy, based on mapping all users and tweets into clusters/communities using embeddings.
### 2. Ranking
Basically, given a user whose timeline it is loading, and given a tweet X, Twitter tries to predict the likelihood that the user will take actions such as like, comment on, retweet, etc on the tweet.

It then assigns a weight to these actions and multiplies the prediction of the likelihood of the action with its weight across all actions to get an overall score for the tweet for the specific user, as below

### 3. Filtering
It involves a mix of things to exclude tweets as well as other things to downrank certain tweets, such as:
- Visibility Filtering: removing tweets from people you have blocked and muted
- Author diversity: Make sure you don’t have too many tweets from one user too close together in your list
- Content balance: Balancing in-network and out-of-network (they really shouldn’t be doing this in my opinion other than to increase in-network tweets)
### How to get your tweets to rank highly?
#### A. Tweet Factors
- Post Images and Videos: They receive a 2x boost
- Post in the same language as your followers: Tweets in a different language from them get penalized by 90%
- Post about something that’s trending: That receives a 1.1x boost
- Don’t post multiple hashtags: That gets penalized by 40%
- Don’t post misspellings/unknown words: That gets penalized by 95%

#### B. Tweet Engagement Factors
- Each like gets a boost of 30
- Each retweet gets a boost of 20
- Each reply gets a boost of 1

Similarly, avoiding negative engagement (mutes on the tweet/user, reports/blocks, unfollows) on your tweet since those lower the tweet level score.

Specifically: tweets have a half-life of 6 hours, meaning that every 6 hours, the base score decreases by 50%.

#### C. User Factors
1. Subscribe to Twitter Blue: Blue users get boosted by 4x for people who follow them and by 2x for people who don’t follow them
2. Don’t follow too many more people than follow you: You get penalized if your followers/following ratio is very low.
3. Be aware that all your actions are going into calculating a TweepCred: Twitter has something like Google’s PageRank for every user known as Tweepcred, which assigns a score of 0 to 100 for every user. If your score is high, its more likely more of your tweets are eligible to show.
