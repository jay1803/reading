---
title: "On Genetic Algorithms: Why Novelty Search is important"
date: 2023-07-18T20:36:53Z
category: reading
description: "Before discussing Novelty Search, let us have a quick overview of what Genetic Algorithms currently mean."
source: "https://medium.com/@nniranjhana/on-genetic-algorithms-why-novelty-search-is-important-6d2879d3ed81"
---

Before discussing Novelty Search, let us have a quick overview of what Genetic Algorithms currently mean.
### Heuristics and Evolutionary Algorithms
<<<Heuristics>>> are techniques that use shortcuts to solve time-limited and complex problems quickly, yielding a good enough solution, that may not be optimal. In Computer Sciences and related fields, this means algorithms trade complete, accurate or precise results for speed.

<<<Metaheuristics>>>s are higher level frameworks or procedures designed to find, develop or select a heuristic based on the optimization problem. Genetic/Evolutionary Algorithms are metaheuristics - they are strategies that guide the heuristic search process, inspired by the subtler processes like natural selection.

A typical Genetic Algorithm implementation would require —
1. a genetic description of the solution space, and
2. a fitness function to evaluate it.

The <<<solution space>>> is the initial population. The genetic description involves representing each member of the population as a set of parameters with binary string encoding, called a gene.

The <<<fitness function>>> is what is applied on the members, or on the solution space to rank how close the member iss to solving the original problem.

Members are selected based on their fitness functions (more fit, more probability of getting selected), and their parameters or genes are made to crossover to generate an offspring, and this next generation member is also added to the solution space.
### How is this a heuristic? Where is the shortcut?
### The importance of Novelty Search
From approaches in Machine Learning to defining the fitness function of GAs, one can identify something fundamental — that all of them are objective-based.

Kenneth Stanley, a pioneer of Novelty Search, gives solid explanations with proofs of why objective-based search will doom us in the long run: https://www.youtube.com/watch?v=dXQPL9GooyI

Novelty search does not reward progress as defined by objectives or performance, rather it rewards being different.
Novelty search mitigates deception — in which seemingly promising fitness candidates fall into local maxima
It is important to note that novelty is not a random walk kind of situation — novelty rewards diverging behaviors, thus creating a constant pressure to do something new.

Fitness creates a gradient towards the objective — maximizing fitness is done with the intent of bringing the search towards a goal.
Novelty creates a gradient of behavioral differences — maximizing is done without any intent of search termination or direction.

You can read Ken’s full paper here — https://pdfs.semanticscholar.org/e49d/1ee1bddea0922faca358f3fd42474baad300.pdf
You can even use few implementations from the NEAT software catalog here — http://eplex.cs.ucf.edu/neat_software/#novelty
### Different kinds of Novelty Search algorithms
Two of them are named Minimal Criteria Novelty Search (MCNS) and Novelty Search with Local Competetion (NSLC), where both focus on maximizing novelty through different approaches.

Well, if you made it this far without getting bored, here’s something cool to watch — https://www.youtube.com/watch?v=pgaEE27nsQw

-----

“Abandoning objectives is often the only way to outperform the direct search for the objective.” — Kenneth Stanley
