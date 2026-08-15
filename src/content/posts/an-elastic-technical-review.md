---
title: "An Elastic technical review"
date: 2023-12-28T16:12:32Z
category: reading
description: "As I said before, EVERY COMPANY MUST be a tech-driven company."
source: "https://hhhypergrowth.com/an-elastic-technical-review/"
---

As I said before, EVERY COMPANY MUST be a tech-driven company.

MDB started by making an open-source NoSQL database, then it sold support and tooling for that database to enterprises that were using it for either their internal database or as an embedded database within their products. Once cloud computing took hold, MDB then started providing a managed, vendor-neutral, cloud hosting service for its core database... one that its customers flocked to, for its scale, high availability (HA), ease of use, and the fact it completely saves them money by eliminating costs around infrastructure and ongoing maintenance.
### Elastic Overview
Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real time. It is generally used as the underlying engine/technology that powers applications that have complex search features and requirements.

Elastic Stack is:
- Elasticsearch, the search and analytics database at the core.
- Logstash, the data processing and transformation pipeline, for data ingestion into Elasticsearch.
- Kibana, the visual interface over Elasticsearch, with data visualization dashboards and a cluster & data management interface.
- Beats, light-weight data shippers utilized for transmitting monitoring data from network and systems, and ingesting them into Elasticsearch.
- "Features" (formerly X-Pack), plug-ins that are modules for enhancing the capabilities of ELK stack, such as adding cluster monitoring, alerting, data security, reporting, machine learning (ML), and a visual presentation app called Canvas.

Elasticsearch (ES) is the open-source NoSQL database at the heart of the stack, which provides search and analytic capabilities over your data.

Alternate open-source search-based databases on the market are:
- Apache Solr, which is also based on Lucene. But it pales in comparison, having only 2.5k vs 40k stars for ES on Github as a sign of its popularity, and #16 on DB Engine ratings.
- Apache Druid, a OLAP/BI analytics engine, which has 8k stars on Github. It's also a clustered data engine but is a lot more convoluted & complex to run.

Kibana is the visual interface over Elasticsearch. At it's core, it's a visualization dashboard app that allows you to rapidly graph ad-hoc queries against your ES data, and create persistent visualization dashboards.
It is pretty similar to another open-source visualization dashboard, Grafana, but is more closely tied to having ES as the underlying database, and, unlike Grafana, provides a mgmt interface over your ES cluster and its data. One great feature of Kibana is its "out-of-the-box" dashboards for specific server apps you are monitoring with Beats, that are curated by Elastic

Logstash is the ingestion piece, that allows for continuously reading in logs from various servers, transforming log entries into JSON objects and ingest them into ES. It has a rich system of data pipeline steps, where you can convert, enrich, filter and transform log data prior to ingestion.

Beats is a collection of light-weight "data shippers", each specific to collecting a type of data feed from remote servers or devices. This includes a log file shipper, metric shipper, network traffic monitoring and more.

Features/X-Pack is a system of modules within the Elastic Stack to enhance the platform and help apply Elastic Stack to specific use cases.
#### Getting Support
There are 4 tiers of support subscriptions.
### Comparison to MongoDB (MDB)
- Both are focused around a core open-source NoSQL document store, accessed via JSON-based REST APIs or native libraries.
- Both founders created companies around that open-source database engine that provided enterprise support and continued adding features, tools and eventually platforms around their core database.
- Both provide platforms containing tools around that core database.

Differences:
- MDB has wide variety of use cases, as an all-purpose document store. Elastic has narrower set of more specific use cases - however it is expanding. If you manage a collection of data objects that has infrequent search or analytics needs, you pick MDB.
- Given this more limited set of use cases, Elastic has had to fight harder. They have mostly expanded their product line by acquisition, adding tools and services that helped build their core database into a platform. MDB is building its platform itself, and IMHO is subsequently moving way slower.
- Both have an "Open Source" focus, and both try to address having competitors use their software against them.
### Strengths, in Haiku
#### Multiple indexes and aliases
One big strength of Elasticsearch is the ability to search over multiple indexes in a single query, including the use of wildcard.
#### Filters
First thing you set up in your query is what is the overall data you want to view.

There are 2 overall modes of searching:
- Full-text searches attempt to match the most relevant documents to your filter.
- Structured searches make a boolean determination (a yea or a nea) per document.
### Acquisitions
Elastic's acquisitions that added tools or SaaS services in their ecosystem:
- Kibana (2012)
- Logstash (2012)
- Found (2015) - A cloud-neutral managed Elastic Stack hosting SaaS service. Now is same named Elastic Cloud service and also the Elastic Cloud Enterprise "on-premise cloud" version.
- Packetbeat (2015) - real-time network packet analytics library, built ELK stack, to monitor distributed systems. Now is Beats product.
- Prelect (2016) - predictive behavioral analytics firm, focused on cybersecurity, fraud detection, and IT operations analytics. Now likely drives ML modules in Kibana.
- OpBeat (2017) - APM system for Javascript apps. Now an APM module in Kibana and the APM Server app.
- Swiftype (2017) - Startup providing hosted SaaS search service for enterprises to easily add search capabilities to their website or app.
- Insight.io (2018) - Startup with a developer-focused SaaS tool for creating a search interface over your source code.
I am way more impressed with Elastic than MDB here.

MDB is trying to move into the same ecosystem - enterprise plugins with a premium cost, mgmt interfaces, and (finally) a viz dashboard and improving analytical capabilities. But they are moving way slower than Elastic, and are never going to catch up to start stealing business from Elastic for search & analytical use cases. I think they are playing it safe & conservative, as they already have a wide set of use cases. Any collection of data in a modern web or mobile app can use MongoDB.

MDB had an acquisition to buy customers (mLab). They already had their own mobile database product and had a mobile sync service in beta -- yet they NOW decide, after that development effort, to purchase Realm as a bolt-on (and, I'm guessing, scrapping their efforts thus far towards mobile and sync). I can't tell why MDB is moving so slow - they keep building everything themselves!

Elastic on the other hand, is expanding their platform to help them find more and more appropriate use cases for Elastic Stack ... OR ... to find new successful SaaS services built on top of Elasticsearch. Either way, they expand use cases and expand the potential TAM. There is nothing stopping them from making a competing services to Splunk or New Relic -- but for now they are focused more on enabling others to do that.
#### ... That Can Scale Up to Infinity, and Beyond
We live in a technological world where datasets are ever-growing, as you pull in time-series data feeds from monitoring IoT sensors or infrastructure.

comprised of one or more nodes (individual systems), you can horizontally scale, which is increasing the number of nodes in that cluster. Each additional node added to the cluster increases capacity and capabilities. Both MongoDB and Elasticsearch are clustered data engines that utilize replicated shards.

Sharding (also called partitioning) is a way to split up a data set across a cluster, to allow you to 1) horizontally split your data, to be able to scale the performance and size of your cluster, and 2) allows you to distribute and parallelize operations across shards located across cluster nodes, to improve performance & throughput.
### Use Cases
Elastic Stack excels at search & analytics over:
- Full text data (ie articles, blog posts, tweets, comments)
- Terms data (ie tags, usernames, locations)
- System logs & real-time metrics (ie systems, network devices)
- Application logs & real-time metrics (ie server-side apps, databases, APIs, microservices)
- Security/Audit logs (ie firewall logs, app audit logs)
- Numerical data (ie financial tx analytics)
- Time-series data (ie metrics, events, devices, IoT sensors)
- Geospatial data (lat/long points, geo-regions, location beacons)
- IP data (network traffic, routing logs)
#### Infrastructure Monitoring
- Logs
- Metrics
- Application Performance Monitoring (APM)
- Uptime
#### Search services
- App Search
- Site Search
- Enterprise Search
#### Analytics
- Security Analytics
- Audit
- Business Analytics
- Mapping

Competition to the data engine is MongoDB, Cassandra, and other scalable NoSQL stores. Developers may prefer and pick those.

Amazon is a competitor to hosting Elasticsearch. Unlike MDB, Elastic isn't combating it via licensing, but instead are combating it with their proprietary XPack plugins.

AWS comparison, from Elastic marketing, says they are missing:
- premium modules for ML, Security, Canvas
- free modules for alerting, monitoring, SQL, Canvas
- curated UI plugins for monitoring/APM
- Index curation & rollup features (Hot/Warm/Frozen indexes)
- Elastic Map Service
- Logstash/Beats management UI
### Final Takeaways
Elastic knew early that they needed a complete ecosystem.

MDB has a much wider use case. But for search and analytics, there is really no alternative to Elasticsearch outside the way-less-used Solr. The choice for a company is really, does a search engine apply to our use case? If so, you go Elastic Stack.

MongoDB is solely used by software development companies. Elastic Stack can be used without code! That means that, unlike MongoDB, it's not just for software developer companies -- any company can benefit.

Simply put, companies with large infrastructure can save big bucks by taking a DO-IT-YOURSELF attitude with monitoring and security. Elastic directly competes with Splunk and New Relic here.
