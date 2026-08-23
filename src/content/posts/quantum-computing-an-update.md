---
title: "Quantum Computing – An Update"
date: 2024-11-25T15:32:08Z
category: reading
author: "Steve Blank"
description: "Summary:"
source: "https://steveblank.com/2024/10/22/quantum-computing-an-update/"
---

Summary:
- There’s been incremental technical progress in making physical qubits
- There is no clear winner yet between the seven approaches in building qubits
- Reminder – why build a quantum computer?
- How many physical qubits do you need?
- Advances in materials science will drive down error rates
- Regional research consortiums
- Venture capital investment FOMO and financial engineering
## Quantum Computing – An Update
qubit – is short for a quantum bit.
### Incremental Technical Progress
As of 2024 there are seven different approaches being explored to build physical qubits for a quantum computer. The most mature currently are
- Superconducting
- Photonics
- Cold Atoms
- Trapped Ions

Other approaches include
- Quantum Dots
- Nitrogen Vacancy in Diamond Centers
- Topological

All these approaches have incrementally increased the number of physical qubits.

Every company currently hypes the number of physical qubits they have working. By itself this is a meaningless number to indicate progress to a working quantum computer. What matters is the number of logical qubits.
### Reminder – Why Build a Quantum Computer?
key misunderstandings about quantum computers is that they are faster than current classical computers on all applications. That’s wrong. They are not. They are faster on a small set of specialized algorithms.
These special algorithms are what make quantum computers potentially valuable. For example, running Grover’s algorithm on a quantum computer can search unstructured data faster than a classical computer.

It’s possible that quantum computers will be treated as “accelerators” to the overall compute workflows – much like GPUs today.

However, while all of these algorithms might have commercial potential one day, no one has yet to come up with a use for them that would radically transform any business or military application. Except for one – and that one keeps people awake at night. It’s Shor’s algorithm for integer factorization – an algorithm that underlies much of existing public cryptography systems.
### How many physical qubits do you need for one logical qubit?
Unlike traditional transistors in a microprocessor that once manufactured always work, qubits are unstable and fragile. They can pop out of a quantum state due to noise, decoherence (when a qubit interacts with the environment,) crosstalk (when a qubit interacts with a physically adjacent qubit,) and imperfections in the materials making up the quantum gates. When that happens errors will occur in quantum calculations. So to correct for those error you need lots of physical qubits to make one logical qubit.

So how do you figure out how many physical qubits you need?
Different quantum algorithms require different numbers of qubits. Some algorithms (e.g., Shor’s prime factoring algorithm) may need >5,000  logical qubits

Seven approaches are being explored to build physical qubits for quantum computers, with no clear winner yet. While the number of physical qubits is increasing, the focus is on logical qubits, which require thousands of physical qubits due to their instability and error-prone nature. Advancements in materials science are crucial to reducing error rates and making quantum computers a reality.

Thousands of logical qubits are needed to create a quantum computer that can run these specialized applications. Each logical qubit is constructed out of many physical qubits. The question is, how many physical qubits are needed? Herein lies the problem.
