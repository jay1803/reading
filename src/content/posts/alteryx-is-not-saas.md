---
title: "Alteryx is not SaaS"
date: 2023-12-28T16:10:37Z
category: reading
description: "Software-as-a-Service is TYPICALLY defined as both a licensing model (subscription) AND a delivery method (they host the service, so there is no installation..."
source: "https://hhhypergrowth.com/alteryx-is-not-saas/"
---

Software-as-a-Service is TYPICALLY defined as both a licensing model (subscription) AND a delivery method (they host the service, so there is no installation or management of that service by the customer).

Alteryx does have the oh-so important recurring revenue needed to obtain hypergrowth -- but it is NOT SaaS.

First a few terms...

- Software-as-a-Service (SaaS) = a software application being made available ON THE CLOUD, so that you don't have to install it locally on your computer then manage and upgrade it from there. For end-user applications, this means the software is entirely accessed via a web or mobile application, having most/all data stored in the cloud. For server-side applications like databases, SaaS can mean managed hosting of that application (see MongoDB Atlas).
- Single-tenancy = traditional method of installing software into your own system, where your company is the only "tenant" (customer of the application) accessing it. Every instance is its own install and is their "own island" (isolated from others). Hosted applications can be single-tenant, but requires separate infrastructure be utilized per customer.
- Multi-tenancy = SaaS term that means you can support multiple customers on the same hosted instance of the application, each user being secured to see only their own data. Vast majority of SaaS applications are architected to be multi-tenant.
- Data bleed = when security of a multi-tenant application is not implemented correctly, and a user can accidentally see another user's data or data becomes co-mingled. This is a big no-no.
- Tenant isolation = intentionally keeping application as single-tenant for security purposes. In cloud hosting, it means renting your own set of infrastructure, instead of using shared instances.
- Vertical scaling = buying a more powerful server to make it more responsive and performant. This is typically the only option for server-side installed software that isn't cluster-based.
- Horizontal scaling = being able to scale up more instances to make a cluster-based server-side application more responsive and performant.

Alteryx is not a SaaS company. Every product is a software you download from them, then install on your system. However, unlike the days of old with boxed software that you bought at the store, access to these softwares is sold on an annual subscription basis - so it IS recurring revenue. But they are not hosting anything for you in the cloud, nor providing their products "as-a-service".

The vast majority of Alteryx products are WINDOWS-based. Not every company utilizes Windows, so they are limiting their market potential somewhat with this choice.
