---
title: "Choose Boring Technology"
date: 2021-02-02T00:30:05Z
category: reading
description: "“Boring” should not be conflated with “bad.”"
source: "https://boringtechnology.club/"
---

“Boring” should not be conflated with “bad.”
But there are many choices of technology that are boring and good, or at least
good enough. MySQL is boring. Postgres is boring. PHP is boring. Python is
boring. Memcached is boring. Squid is boring. Cron is boring.

The nice thing about boringness (so constrained) is that the capabilities of
these things are well understood. But more importantly, their failure modes are
well understood.

When choosing technology, you have both known unknowns and unknown unknowns.
- A known unknown is something like: we don’t know what happens when this
  database hits 100% CPU.
- An unknown unknown is something like: geez it didn’t even occur to us that
  writing stats would cause GC pauses.

The problem with “best tool for the job” thinking is that it takes a myopic view
of the words “best” and “job.” Your job is keeping the company in business, god
damn it. And the “best” tool is the one that occupies the “least worst” position
for as many of your problems as possible.

One of the most worthwhile exercises I recommend here is to consider how you
would solve your immediate problem without adding anything new. First, posing
this question should detect the situation where the “problem” is that someone
really wants to use the technology. If that is the case, you should immediately
abort.

It’s helpful to write down exactly what it is about the current stack that makes
solving the problem prohibitively expensive and difficult.

http://boringtechnology.club
