---
title: "All you need is Wide Events, not “Metrics, Logs and Traces”"
date: 2024-02-29T13:44:47Z
category: reading
description: "This quote from Charity Majors is probably the best summary of the current state of observability in the tech industry - a total, mass confusion."
---

This quote from Charity Majors is probably the best summary of the current state of observability in the tech industry - a total, mass confusion.

OpenTelemetry is and what it does makes the observability look tricky and complex.

First, Open Telemetry from the very beginning makes a clear distinctions between traces, metrics and logs:
Then it goes deeper in explaining each of these 3.

when it comes to the distributed systems at scale what’s more important is an ability to “dig” into data - “slice and dice” it, build and analyse various views, correlate, search for anomalies… And systems that offer all of this do exist.

Wide Event is just a collection of fields with names and values, pretty much like a json document. If you need to record some information - whether it’s the current state of the system, or an event caused by an API call, background job or whatever - you can just write some Wide Event to Scuba.
