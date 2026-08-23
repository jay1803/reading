---
title: "MongoDB goes Mobile"
date: 2023-12-28T16:12:08Z
category: reading
author: "muji"
description: "MDB just had an acquisition, their third. Their prior one, mLab in Oct 2018"
source: "https://hhhypergrowth.com/mongodb-goes-mobile/"
---

MDB just had an acquisition, their third. Their prior one, mLab in Oct 2018
### Overview
What has allowed companies like MDB and Elastic (and non-database dev tools like Twilio) to thrive is how embedded they become as tools a software company uses to solve problems.
### Mobile Databases
The primary methodology used to access SQL and NoSQL databases is the client-server model, where the web or mobile app is a client that makes requests to a database that is hosted on a remote server (either on-prem on cloud-hosted).

A different type of access method being used on mobile apps is having a synchronized copy of the database as a mobile database, in order to store the data locally on the phone or device itself, instead of being hosted elsewhere.

the database must be geared for synchronizing data between a centralized master server and the local database on each mobile device. In a mobile database, synchronization ultimately needs to support updates in BOTH directions:
- Master to Mobile = syncing updates from the master  database to the embedded database, updating the local data on the device with any inserts or changes they should get a copy of.
- Mobile to Master = syncing updates from the local mobile database back to the master database.

SQLite is the long-time standard for on-device databases. It's an open-source, light-weight relational "database in a file" that has been around forever, having been long used in embedded devices.

though AWS AppSync aims to provide some of the sync features.
### Cloud Atlas
#### All Eyes on the Cloud
### Stitching Together a Platform
Stitch also greatly extends the programmability of the MongoDB database, by allowing you to code scripts that can run in any copy of your database - even on Atlas.
- Stitch Functions = allows you to embed custom code within the database, which include calling external APIs like Twilio and Slack.
- Stitch Triggers = allows you to have data changes trigger events. Such as a running a function to trigger a Twilio text or email notice when a new customer record is added.
#### Stitch is the Thread Binding Cloud to Mobile
I found an interesting tidbit on MDB Mobile features page: "MongoDB Mobile uses SQLite as a simple key-value store behind the scenes due to its stability and prevalence on devices."
### There Can Be Only One
