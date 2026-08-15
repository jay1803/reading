---
title: "Clouded Judgement 10.18.24 - From Systems of Record to Systems of Intelligence"
date: 2024-10-22T15:25:20Z
category: reading
description: "There’s a long-held belief in enterprise software that building a lasting moat requires a system of record. Salesforce is the system of record for customer d..."
source: "https://cloudedjudgement.substack.com/p/clouded-judgement-101824-from-systems"
---

There’s a long-held belief in enterprise software that building a lasting moat requires a system of record. Salesforce is the system of record for customer data, Workday for employee data, and ServiceNow for IT data, to name a few. The idea is that the central repository of critical business data forms the core value. But while this central database is important, it's not the whole story.

The real value—and the true lock-in—comes from the workflows and integrations that are built around these systems of record. These applications are not just repositories; they are tools designed for humans to input and manage data. At their core, they’re interfaces built to help employees take information from one source and enter it into another, often manually. These systems rely on people sitting in front of screens, navigating the user interface (UI) to input, process, and move data through various workflows. This human-centered design has made these systems essential for companies, and replacing not only the data but the workflows tied to them is where the true switching cost lies.

With AI, however, this dynamic could radically change. One of AI’s greatest strengths, particularly with large foundation models, is its ability to process unstructured data—data that humans today manually enter into systems of record. Sales reps, for instance, hate entering data into Salesforce after every call, and managers often find this data inaccurate or incomplete, making forecasting a challenge. But what if an AI could do that work instead? Imagine an AI that listens in on a sales call, identifies the person on the other end, extracts relevant details like company size, pain points, competitors, deal size, and then automatically enters that data into the system. The role of the human UI disappears, replaced by an AI agent seamlessly interacting with the system of record.

This shift means that the emphasis moves away from the UI or front-end application, which was historically designed to help humans enter and manipulate data. Instead, the focus shifts to the database and making it as efficient and flexible as possible for AI agents to work with. In the AI-first future, the real value won't lie in complex interfaces for human users, but in how well the system can gather, store, and process data autonomously.

As a result, we may see a fundamental change in how enterprise applications are built. The traditional model of a front-end application tied to a database like Oracle and a series of manual workflows might give way to AI-native applications built on AI native databases, where the database takes center stage. These AI applications will be designed to operate on top of centralized data repositories— like a data lakes or lakehouse —where AI agents gather and process information from a wide array of unstructured sources. This will make the underlying database even more critical, as workflows will be automated, reducing the need for humans to manually move data from system to system.

In this new AI-driven world, the traditional moats built by systems of record could weaken. The reliance on human-driven UIs and manual processes will fade, and the value will shift to how efficiently AI can gather and act on data - data apps will emerge. Companies that embrace this shift could build more flexible, AI-powered systems that are more scalable and less reliant on manual workflows, fundamentally changing the way enterprise software operates. The world needs an AI database to power AI native apps.

We’ll also need an entirely new set of tools and infrastructure to process and manage these workflows. What happens if a long running workflow with many steps times out or runs into a processing error? Do you start over at the beginning or go back to the last step pre failure? How do you monitor all of these workflows running in parallel? How do you evaluate their output? In short - we’ll need an explosion of new infra to support AI native apps.

If you’re building any kind of AI native application to disrupt cloud based systems of record, I’d love to speak with you!
