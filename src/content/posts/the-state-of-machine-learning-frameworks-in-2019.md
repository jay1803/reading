---
title: "The State of Machine Learning Frameworks in 2019"
date: 2023-06-13T15:10:25Z
category: reading
description: "Why do researchers love PyTorch?"
source: "https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/"
---

Why do researchers love PyTorch?
- Simplicity. It’s similar to numpy, very pythonic, and integrates easily with the rest of the Python ecosystem. For example, you can simply throw in a pdb breakpoint anywhere into your PyTorch model and it’ll work. In TensorFlow, debugging the model requires an active session and ends up being much trickier.
- Great API. Most researchers prefer PyTorch’s API to TensorFlow’s API. This is partially because PyTorch is better designed and partially because TensorFlow has handicapped itself by switching APIs so many times (e.g. ‘layers’ -> ‘slim’ -> ‘estimators’ -> ‘tf.keras’).
- Performance. Despite the fact that PyTorch’s dynamic graphs give strictly less opportunity for optimization, there have been many anecdotal reports that PyTorch is as fast if not faster than TensorFlow. It's not clear if this is really true, but at the very least, TensorFlow hasn't gained a decisive advantage in this area.
## By BingChat
The state of machine learning frameworks in 2019 is the topic of this web article, which compares PyTorch and TensorFlow, the two dominant frameworks in research and industry. The article uses graphs, data, and examples to show that:

- PyTorch has surpassed TensorFlow in the number of papers, conferences, and job listings, especially in vision and language domains.
- PyTorch has improved its performance, simplicity, and API over TensorFlow, and has gained more adoption and support from researchers.
- TensorFlow has maintained its edge in production, and has solutions for mobile, serving, and other requirements that PyTorch lacks.
- TensorFlow has introduced eager mode to address its weaknesses, but this also forces a choice between ease of use and deployment.

The article also discusses the challenges and opportunities for both frameworks, such as:

- The influence of researcher preference on industry adoption, and the potential of PyTorch to attract new talent and startups.
- The transition from TensorFlow 1.0 to 2.0, which may offer a chance for companies to evaluate PyTorch.
- The uncertainty of Google’s role in industry, and how it may affect the competition and innovation in machine learning.

The article concludes that PyTorch and TensorFlow are both auto-differentiation frameworks, but they have different strengths and weaknesses, and that the future of machine learning will depend on how well they can address the needs of researchers and industry.
