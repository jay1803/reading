---
title: "The New Language Model Stack"
date: 2023-06-15T11:16:44Z
category: reading
description: "1. Nearly every company in the Sequoia network is building language models into their products."
source: "https://www.sequoiacap.com/article/llm-stack-perspective/"
---

1. Nearly every company in the Sequoia network is building language models into their products.
2. The new stack for these applications centers on language model APIs, retrieval, and orchestration, but open source usage is also growing.
   1. 65% had applications in production, up from 50% two months ago, while the remainder are still experimenting.
   2. 94% are using a foundation model API. OpenAI’s GPT was the clear favorite in our sample at 91%, however Anthropic interest grew over the last quarter to 15%. (Some companies are using multiple models).
   3. 88% believe a retrieval mechanism, such as a vector database, would remain a key part of their stack.
   4. 38% were interested in an LLM orchestration and application development framework like LangChain.
   5. Sub-10% were looking for tools to monitor LLM outputs, cost, or performance and A/B test prompts.
   6. A handful of companies are looking into complementary generative technologies, such as combining generative text and voice. We also believe this is an exciting growth area.
   7. 15% built custom language models from scratch or open source, often in addition to using LLM APIs.

LLM APIs
- OpenAI
- Anthropic PBC
- Cohere Inc.

Vector Database
- AWS
- PGVector

Frameworks
- LangChain
-----

3. Companies want to customize language models to their unique context.

Right now, there are three main ways to customize language models (for a deeper technical explanation, see [Andrej’s recent State of GPT talk at Microsoft Build](https://build.microsoft.com/en-US/sessions/db3f4859-cd30-4445-a0cd-553c3304f8e2)):
    - Train a custom model from scratch. Highest degree of difficulty.
    - Fine-tune a base model. Medium degree of difficulty.
    - Use a pre-trained model and retrieve relevant context. Lowest degree of difficulty.

4. Today, the stack for LLM APIs can feel separate from the custom model training stack, but these are blending together over time.
5. The stack is becoming increasingly developer-friendly.
6. Language models need to become more trustworthy (output quality, data privacy, security) for full adoption.
7. Language model applications will become increasingly multi-modal.
8. It’s still early.
