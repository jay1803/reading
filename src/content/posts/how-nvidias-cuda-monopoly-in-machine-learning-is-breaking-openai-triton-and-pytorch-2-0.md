---
title: "How Nvidia’s CUDA Monopoly In Machine Learning Is Breaking - OpenAI Triton And PyTorch 2.0"
date: 2023-06-13T11:19:32Z
category: reading
description: "with the arrival of PyTorch 2.0 and OpenAI's Triton, Nvidia's dominant position in this field, mainly due to its software moat, is being disrupted."
source: "https://www.semianalysis.com/p/nvidiaopenaitritonpytorch"
---

with the arrival of PyTorch 2.0 and OpenAI's Triton, Nvidia's dominant position in this field, mainly due to its software moat, is being disrupted.

This report will touch on topics such as
- why Google’s TensorFlow lost out to PyTorch,
- why Google hasn’t been able to capitalize publicly on its early leadership of AI,
- the major components of machine learning model training time,
- the memory capacity/bandwidth/cost wall,
- model optimization,
- why other AI hardware companies haven’t been able to make a dent in Nvidia’s dominance so far,
- why hardware will start to matter more,
- how Nvidia’s competitive advantage in CUDA is wiped away,
- and a major win one of Nvidia’s competitors has at a large cloud for training silicon.
### TensorFlow vs. PyTorch
PyTorch won. Google failed to convert its first mover’s advantage into dominance of the nascent ML industry.

Back to why PyTorch won. While there was an element of wrestling control away from Google, it was primarily due to its increased flexibility and usability of PyTorch versus TensorFlow. If we boil it down to a first principal level, PyTorch differed from TensorFlow in using “Eager mode” rather than "Graph Mode."

Eager mode can be thought of as a standard scripting execution method. The deep learning framework executes each operation immediately, as it is called, line by line, like any other piece of Python code. This makes debugging and understanding your code more accessible, as you can see the results of intermediate operations and see how your model behaves.

In contrast, graph mode has two phases. The first phase is the definition of a computation graph representing the operations to perform. A computation graph is a series of interconnected nodes representing operations or variables, and the edges between nodes represent the data flow between them. The second phase is the deferred execution of an optimized version of the computation graph.
### Machine Learning Training Components
there are two major time components in a machine learning model’s training time.
- Compute (FLOPS):  Running dense matrix multiplication within each layer
- Memory (Bandwidth): Waiting for data or layer weights to get to the compute resources. Common examples of bandwidth-constrained operations are various normalizations, pointwise operations, SoftMax, and ReLU.

Even in 2018, purely compute-bound workloads made up 99.8% of FLOPS but only 61% of the runtime. The normalization and pointwise ops achieve 250x less FLOPS and 700x less FLOPS than matrix multiplications, respectively, yet they consume nearly 40% of the model’s runtime.
#### by BingChat
根据当前网页内容，Machine Learning Training Components 这部分的内容是这样的：

- 机器学习模型的训练时间主要由两个部分组成：计算（FLOPS）和内存（Bandwidth）。
- 计算是指在每一层中进行密集的矩阵乘法等操作，需要大量的浮点运算能力。
- 内存是指等待数据或层权重传输到计算资源的时间，需要大量的内存带宽和容量。
- 以前，机器学习训练的主要瓶颈是计算时间，但随着 Nvidia 的 GPU 的发展，这个问题逐渐得到了解决。Nvidia 的 GPU 通过摩尔定律和架构改进，大幅提高了 FLOPS。
- 然而，内存并没有跟上 GPU 的发展。内存的速度和容量的增长受到了物理和经济的限制，导致了 memory wall 的出现。memory wall 是指内存需求超过了供应，导致模型训练的时间和成本的增加。
- 作者举例说明了在 2018 年，当 BERT 模型是最先进的模型，而 Nvidia V100 是最先进的 GPU 时，矩阵乘法已经不再是提高模型性能的主要因素。作者还指出，从 A100 到 H100，FLOPS 增长了 6 倍以上，但内存带宽只增长了 1.65 倍。这意味着 H100 需要更多的技巧来解决 memory wall 的问题。
### The Memory Wall

The answer is $$$.
The nearest shared memory pool is on the same chip and is generally made of SRAM.
the cost per GB of SRAM memory would still be in the $100s for a fully yielded product.

Nvidia’s architecture has always used a much smaller amount of memory on the die.
DRAM has an order magnitude higher latency than SRAM (~>100 nanoseconds vs. ~10 nanoseconds), but it’s also much cheaper ($1s a GB vs. $100s GB.)
While standard DRAM is only a few dollars per GB today, to get the massive bandwidth machine learning requires, Nvidia uses HBM memory, a device comprised of 3D stacked layers of DRAM that requires more expensive packaging. HBM is in the $10 to $20 a GB range, including packaging and yield costs.
#### By BingChat
根据当前网页内容，The Memory Wall 这部分的内容是这样的：

- memory wall 是指随着模型规模的增长，内存容量和带宽的需求超过了供应，导致模型训练的时间和成本的增加。
- 内存有一个层次结构，从近和快到远和慢。最近的共享内存池是在同一芯片上，通常是 SRAM。SRAM 速度快，但容量小，成本高。一些机器学习 ASIC 试图利用大量的 SRAM 来存储模型权重，但仍然不够。Nvidia 的架构一直使用较少的芯片上内存，而依赖于紧密耦合的片外内存，DRAM。DRAM 速度慢，但容量大，成本低。
- DRAM 也遵循了摩尔定律很多年，但在 2009 年左右停滞了。从 2012 年开始，DRAM 的成本几乎没有改善。内存需求只增加了。DRAM 现在占服务器总成本的 50%。
- 为了获得更高的内存带宽，Nvidia 使用了 HBM 内存，一种由 3D 堆叠层组成的 DRAM 设备，需要更昂贵的封装。HBM 的成本在每 GB 10 到 20 美元之间。
- 内存容量和带宽的成本限制在 Nvidia 的 A100 GPU 中不断显现。A100 需要很多技巧才能绕过 memory wall，并且在没有重度优化的情况下 FLOPS 利用率很低。FLOPS 利用率指的是模型训练所需的计算 FLOPS 与 GPU 理论 FLOPS 的比例。即使经过重度优化，60% 的 FLOPS 利用率也被认为是非常高的。其余的时间是开销、空闲时间或者重新计算结果以减少内存瓶颈。
### Operator Fusion – The Workaround
Instead of writing each intermediate result to memory, operations are fused, so multiple functions are computed in one pass to minimize memory reads/writes. Operator fusion improves operator dispatch, memory bandwidth, and memory size costs.

#### By BingChat
根据当前网页内容，Operator Fusion – The Workaround 这部分的内容是这样的：

- 操作融合是一种优化方法，可以减少内存读写的次数，提高内存利用率和性能。操作融合是指将多个操作合并为一个更复杂的操作，一次性完成计算，而不是将每个中间结果写入内存。
- 操作融合可以改善操作调度、内存带宽和内存大小的成本。操作融合对于那些内存密集型的操作，如归一化、逐点运算等，特别有用。操作融合也可以减少更复杂操作的开销，如 Flash Attention，它包含了矩阵乘法作为一个更大的融合操作的一部分。
- PyTorch 由于使用了 eager mode，每个操作都会立即执行并返回结果，这样会增加内存带宽的需求。因此，操作融合是 PyTorch 中一个重要的优化方法。操作融合通常需要编写自定义的 CUDA 核函数，但这比使用简单的 python 脚本要困难得多。
- 为了折中，PyTorch 逐渐在本身实现了更多的操作。这些操作通常是多个常用操作融合成一个单一的更复杂的函数。增加操作既使得在 PyTorch 中创建模型更容易，也使得 eager mode 的性能更快，因为有更少的内存读写。但缺点是 PyTorch 膨胀到了 2000 多个操作。
- 对于 AI 硬件创业公司来说，为 PyTorch 完全实现一个高性能的后端意味着要支持这 2000 多个操作。这需要很高的人才水平和时间成本。而且，由于开发者习惯了 PyTorch 中的新操作，他们会继续使用它们，而不管它们是否对性能有帮助。
- 此外，并不是所有的操作都可以被融合。很多时间都花在了决定哪些操作要融合，以及哪些操作要分配给特定的计算资源。不同的架构在这方面可能有不同的策略。
### Nvidia Is King
The growth in operators and position as the default has helped Nvidia as each operator was quickly optimized for their architecture but not for any other hardware.

Ease of use is king.

The only way to break the vicious cycle is for the software that runs models on Nvidia GPUs to transfer seamlessly to other hardware with as little effort as possible.

简单来说，软件生态（PyTorch）总某种程度上弥补了硬件（Nvidia）的不足，这也助长了 Nvidia 在 AI 领域的垄断地位。
#### By BingChat
根据当前网页内容，Nvidia Is King 这部分的内容是这样的：

- Nvidia 是机器学习领域的霸主，主要是因为它的软件护城河。它开发了 CUDA 平台，让开发者可以利用 GPU 的并行计算能力进行通用应用，如机器学习。CUDA 提供了高性能和支持多种编程语言。
- Nvidia 的 GPU 也是最适合 PyTorch 的硬件，因为 PyTorch 中的每个操作都被快速地优化了 Nvidia 的架构，但没有针对其他硬件进行优化。如果一个 AI 硬件创业公司想要完全支持 PyTorch，就必须支持 2000 多个操作，并且保证高性能。
- Nvidia 的 GPU 在处理矩阵乘法等计算密集型的操作时表现优异，但在处理归一化、逐点运算等内存密集型的操作时效率低下。因此，要在 GPU 上训练一个大型的模型，需要很高的人才水平和很多技巧，才能提高 FLOPS 利用率。
- FLOPS 利用率指的是模型训练所需的计算 FLOPS 与 GPU 理论 FLOPS 的比例。即使经过重度优化，60% 的 FLOPS 利用率也被认为是非常高的。其余的时间是开销、空闲时间或者重新计算结果以减少内存瓶颈。
- eager mode 执行加上操作融合意味着软件、技术和模型都被推动去适应当前 GPU 的计算和内存的比例。每个开发机器学习芯片的公司都受到同样的 memory wall 的限制。ASIC 都受到支持最常用框架的限制。ASIC 都受到默认开发方法的限制，即使用 GPU 优化的 PyTorch 代码和 Nvidia 和外部库的混合。一个放弃 GPU 的各种非计算包袱，而转向更多 FLOPS 和更严格编程模型的架构，在这种情况下没有多大意义。易用性是王道。
- 打破这个恶性循环的唯一方法是让在 Nvidia GPU 上运行模型的软件能够无缝地转移到其他硬件上，而不需要太多努力。随着模型架构的稳定和 PyTorch 2.0、OpenAI Triton 和 MosaicML 等公司提供的抽象层成为默认，芯片解决方案的架构和经济性开始成为购买决策的最大驱动力，而不是 Nvidia 提供的易用性。
### PyTorch 2.0
PyTorch 2.0...will make properly utilizing various hardware resources much easier.

PyTorch 2.0 brings an 86% performance improvement for training on Nvidia’s A100 and 26% on CPUs for inference! This dramatically reduces the compute time and cost required for training a model. These benefits could extend to other GPUs and accelerators from AMD, Intel, Tenstorrent, Luminous Computing, Tesla, Google, Amazon, Microsoft, Marvell, Meta, Graphcore, Cerebras, SambaNova, etc.
#### By BingChat
根据当前网页内容，PyTorch 2.0 这部分的内容是这样的：

- PyTorch 2.0 是 PyTorch 的最新版本，它引入了一些新的特性，如 TorchDynamo 和 TorchInductor，以及对 eager mode 和 graph mode 的支持。
- TorchDynamo 是一个 JIT 编译器，它可以将 PyTorch 的 eager mode 代码转换为 graph mode 代码，从而提高性能和可移植性。TorchDynamo 可以自动检测代码中的热点，并将它们编译成优化的计算图。TorchDynamo 还可以将多个操作融合成一个更复杂的操作，减少内存读写的次数。
- TorchInductor 是一个代码生成器，它可以将 PyTorch 的 graph mode 代码转换为不同硬件架构的专用代码，从而提高效率和兼容性。TorchInductor 可以根据硬件的特点和限制，生成最佳的代码。TorchInductor 还可以支持自定义的硬件加速器，只需要提供一些基本的信息和接口。
- eager mode 和 graph mode 是两种执行机器学习模型的方式。eager mode 是一种即时执行的方式，每个操作都会立即计算并返回结果，这样可以方便调试和理解代码。graph mode 是一种延迟执行的方式，需要先定义一个计算图，然后再优化和执行，这样可以提高性能和并行度，但也增加了复杂度和难度。
- PyTorch 2.0 支持两种模式的混合使用，让开发者可以根据需要选择最适合的模式。PyTorch 2.0 还提供了一些工具和库，如 TorchScript、torch.fx、torch.nn、torch.utils、torch.distributed 等，来帮助开发者创建、优化、部署和扩展机器学习模型。
### OpenAI Triton
OpenAI Triton only officially supports Nvidia GPUs today, but that is changing in the near future.
#### By BingChat
根据当前网页内容，OpenAI Triton 这部分的内容是这样的：
- OpenAI Triton 是一个开源的软件，它可以让开发者在并行计算硬件上训练大规模的机器学习模型，如 GPU、TPU 或 FPGA。Triton 是一种新的编程语言，它可以自动生成优化的代码，适应不同的硬件架构和内存层次结构。
- Triton 的设计目标是简单、可移植和高效。Triton 的语法类似于 Python，但是更加简洁和强大。Triton 可以处理内存管理和同步问题，让开发者可以专注于算法逻辑。Triton 还可以利用硬件的特性，如共享内存、缓存、寄存器等，来提高性能和降低内存需求。
- Triton 可以与 PyTorch 无缝集成，让开发者可以在 PyTorch 中使用 Triton 编写自定义的操作。Triton 还可以支持其他框架和硬件，只需要提供一些基本的接口和信息。Triton 的目标是成为一个通用的并行计算平台，让开发者可以在任何硬件上运行任何模型。
- Triton 已经被用于实现一些先进的机器学习模型，如 DeepSpeed、Megatron-LM、GPT-3 等。Triton 在这些模型中显示了显著的性能提升和内存节省。Triton 还可以用于实现一些新颖的算法，如 Flash Attention、Sparse Transformers 等。

也就是说 Nvidia 的优势并非完全由自己的技术带来，更多的原因在于软件生态，自然 Nvidia 在硬件驱动方面的优势也帮助了软件生态的构建，相比 AMD 来说。
如果 AMD 在驱动方面表现得更好，同时 PyTorch 这样的软件框架可以支持 AMD 的显卡的上线，那么对于 Nvidia 来说确实会构成不小的威胁。
但是从收益上来说，对于机器学习的科学家来说，GPU 是 AMD 还是 Nvidia 并不会有什么不同，或者对于 PyTorch 来说，移植到 AMD 的 GPU 会有更大的优势吗？也很难说，唯一的收益方是 AMD，或者说当 Nvidia 自己作死的时候。
这样看来，AMD 短期也不会获得什么优势。
## Summarized by BingChat
This web page is an article that discusses how Nvidia's CUDA monopoly in machine learning is breaking due to the arrival of PyTorch 2.0 and OpenAI's Triton. The article explains why PyTorch became the dominant framework for machine learning, why memory bandwidth and capacity are the major bottlenecks for model training, and how PyTorch 2.0 and Triton enable more efficient and portable code generation for various hardware accelerators. The article also hints at a major win for one of Nvidia's competitors at Microsoft and provides a link to a paid report for more details.
### how CUDA is monopoly in machine learning
简单来说，Tesor
CUDA is a platform developed by Nvidia that enables developers to use the parallel computing power of GPUs for general-purpose applications, such as machine learning. CUDA has been the dominant platform for machine learning, as it offers superior performance and supports a wide range of programming languages²³. However, this monopoly is starting to break as more and more people are switching to OpenAI's Triton and PyTorch 2.0¹³.

Triton is a software that allows for the training of large-scale machine learning models on parallel computing hardware, such as GPUs, TPUs, or FPGAs. Triton is designed to be easy to use, portable, and efficient. It automatically generates optimized code for different hardware architectures and handles memory management and synchronization issues¹³.

PyTorch 2.0 is the latest version of the popular machine learning framework PyTorch, which is widely used by researchers and practitioners. PyTorch 2.0 introduces several new features, such as TorchDynamo and TorchInductor, that enable more efficient and portable code generation for various hardware accelerators. PyTorch 2.0 also supports both eager mode and graph mode, which are two ways of executing machine learning models¹.

These two software tools are disrupting Nvidia's CUDA monopoly in machine learning by providing more flexibility, portability, and performance for machine learning developers. They also enable the use of other hardware accelerators besides Nvidia's GPUs, which could increase the competition and innovation in the machine learning industry¹³.

Source: Conversation with Bing, 6/13/2023(1) SemiAnalysis on LinkedIn: How Nvidia’s CUDA Monopoly In Machine .... https://www.linkedin.com/posts/semianalysis_how-nvidias-cuda-monopoly-in-machine-learning-activity-7020688520637804544-XZTe Accessed 6/13/2023.
(2) How OpenAI and PyTorch Are Disrupting Machine Learning With NVidia’s CUDA. https://jackieomotalade.com/how-openai-and-pytorch-are-disrupting-machine-learning-with-nvidias-cuda/ Accessed 6/13/2023.
(3) How Nvidia’s CUDA Monopoly In Machine Learning Is Breaking - SemiAnalysis. https://www.semianalysis.com/p/nvidiaopenaitritonpytorch Accessed 6/13/2023.
