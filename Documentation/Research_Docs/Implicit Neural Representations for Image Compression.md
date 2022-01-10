# Table of contents:
- [Table of contents:](#table-of-contents)
- [Introduction](#introduction)
- [Four/Five C's](#fourfive-cs)
  - [What is the **category** of the paper?](#what-is-the-category-of-the-paper)
  - [What is the **context** of the paper?](#what-is-the-context-of-the-paper)
  - [Is the paper **correct** in it's assumptions?](#is-the-paper-correct-in-its-assumptions)
  - [What are the main **contributions**?](#what-are-the-main-contributions)
- [Relevant Ideas](#relevant-ideas)
- [Notes](#notes)
- [Excerpts](#excerpts)
  - [Abstract](#abstract)

# Introduction
The goal of this document is to write down the important elements of the paper ["Implicit Neural Representations for Image Compression"](https://arxiv.org/pdf/2112.04267.pdf), specifically those that are relevant to our project on neural video compression with implicit representations.

It uses the guidelines from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) adapted to the use case of constructing an experimental design for our project.

As such, it is broken down in four parts. The first one contains the relevant four of the "Five C's" from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) answered, this is then followed by a series of applicable ideas from the paper which could be integrated into our project. Miscellaneous notes serve as the penultimate section. The final part contains excerpts from the paper (e.g the abstract) for easy future checking during development.



# Four/Five C's
## What is the **category** of the paper?
A Neural Image Compression paper advocating for a design similar to [COIN](COIN:%20COmpression%20with%20Implicit%20Neural%20representations.md) yet more complex and competitive with the state-of-the-art

## What is the **context** of the paper?
The relative lack of competitive image compression systems based on implicit neural representations as well as the simplicity of those that did exist. 

## Is the paper **correct** in it's assumptions?
The paper is correct to assume that the base SIREN-model based technique is capable of producing superior results to those seen up until that point via the application of a few additional techniques 

## What are the main **contributions**?

- Combining SIREN MLPs with:
  - Meta-learning initialization based on MAML (Model-Agnostic Meta-Learning) to improve performance
  - Quantization-aware retraining
  - Entropy coding
- Being competitive with common image compressions algorithms and closer to the state-of-the-art

# Relevant Ideas

- **Important:** improved input positional encoding when compared to nerf: f(p)=(p, sin(a^0*pi*p), cos(a^0*pi*p),...,sin(a^{l-1}*pi*p), cos(a^{l-1}*pi*p)). 
  - This draws heavily upon "Fourier features let networks learn high frequency functions in low dimensional domains" by introducing a scale parameter "a".
  - It concatenates the original coordinate so that can be picked up by the first hidden layer as well, the authors do this so that the SIREN model does not lose any previously available information (if you think of the first hidden layer as embedding layer then it still has access to the original coordinate info).
  - The scale parameter is essentially the standard deviation
- **Important:** Regularization: they optimise MSE + p*L_1(model_weights) in order to reduce entropy
- **Important:** Better quantization with the AI Model Efficiency Toolkit (AIMET)
  - The authors apply quantization specific to each weight tensor 
  - They use bitwidths between 7 and 8
- **Important:**  Post-Quantization Optimization: 
  - They do AdaRound to round weights up or down after model training
  - Afterwards they do Quantization Aware Training using the Straight Through Estimator for gradient computation.
- **Important:**  Entropy Coding: 
  - They do not give the exact algorithm they use, they merely mention it is a "binarized arithmetic coding algorithm to losslessly compress the quantized weights"
  - Based on google search it is probably similar to [DeepCABAC](https://github.com/fraunhoferhhi/DeepCABAC) or 
- The authors find that improving training time is a major component in making implicit neural representations viable, improve training and inference time by using **TinyCUDA**, potentially in conjunction with their methods.
- Updates require less storage than a full weight tensor, if we break up a video into chunks we can keep the same architecture and just send the diff---influenced by sec.3.3.2
- **Important:** Parameter Values For different datasets and resolutions:
  - Default values unless stated otherwise:
    - 3 hidden layers
    - std_dev/scale = 1.4
    - L1_reg_weight = 10^{-5}
  - Freq_bands:
    - High_res = 16
    - Low_res = 12
  - Num hidden units per layer:
    - High_res = {24,32,48,64}
    - Low_res = {32,48,64,128}
  - Optimal bidwith for quantization:
    - 7 when using meta learning
    - 8 generally
  - Uses mixed precision training through
- **Metrics**:
  - Bitrate[bpp], should adapt to video
  - PSNR, use avg PSNR for video


- They keep the w_0 set to 30, potentially worth tuning 
- Meta-learning initialization based on MAML (Model-Agnostic Meta-Learning) to improve performance
  - Probably **infeasible** given the fact that it must be trained on a lot of videos and we do not have that much computation at our disposition




# Notes

- The authors hypothesize two main reasons for the paucity of implicit neural representations applied to image compression: 
  - It is difficult to make them competitive with standard video compression algorithms
  - High encoding time
- THeir work vastly outperforms COIN
- Their weight initialization diverges from that of the traditional [SIREN](SIREN:%20Implicit%20Neural%20Representations%20with%20Periodic%20Activation%20Functions.md) models



# Excerpts

## Abstract 

"Recently Implicit Neural Representations (INRs) gained
attention as a novel and effective representation for various
data types. Thus far, prior work mostly focused on optimizing their reconstruction performance. This work investigates INRs from a novel perspective, i.e., as a tool for image
compression. To this end, we propose the first comprehensive image compression pipeline based on INRs including
quantization, quantization-aware retraining and entropy
coding. Encoding with INRs, i.e., overfitting to a data sample, is typically orders of magnitude slower. To mitigate this
drawback, we leverage meta-learned initializations based
on MAML to reach the encoding in fewer gradient updates
which also generally improves rate-distortion performance
of INRs. We find that our approach to source compression with INRs vastly outperforms similar prior work, is
competitive with common compression algorithms designed
specifically for images and closes the gap to state-of-theart learned approaches based on Rate-Distortion Autoencoders. Moreover, we provide an extensive ablation study
on the importance of individual components of our method
which we hope facilitates future research on this novel approach to image compression."