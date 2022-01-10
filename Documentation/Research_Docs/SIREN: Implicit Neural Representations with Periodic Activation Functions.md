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
The goal of this document is to write down the important elements of the paper ["Implicit Neural Representations with Periodic Activation Functions"](https://arxiv.org/pdf/2006.09661.pdf), specifically those that are relevant to our project on neural video compression with implicit representations.

It uses the guidelines from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) adapted to the use case of constructing an experimental design for our project.

As such, it is broken down in four parts. The first one contains the relevant four of the "Five C's" from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) answered, this is then followed by a series of applicable ideas from the paper which could be integrated into our project. Miscellaneous notes serve as the penultimate section. The final part contains excerpts from the paper (e.g the abstract) for easy future checking during development.



# Four/Five C's
## What is the **category** of the paper?
A Neural Architecture paper advocating for the usage of periodic activation functions in neural models to allow for the capture of high-frequency information (e.g image pixel values).

Specifically, they are interested in functions which map coordinates and satisfy constraints based on the coordinates, the function and all the potential derivatives of the function. A neural network is meant to implicitly represent such a function in a more compact manner when compared to discrete representations.

## What is the **context** of the paper?
The general trend towards applying implicit neural representations to model signals and the failure of standard MLPs to capture fine-grained information.

## Is the paper **correct** in it's assumptions?
Yes, their sin-activation-based MLP outperforms standard NN designs using conventional activation functions for signal processing tasks showing that they are indeed capable of capturing high-frequency information.

## What are the main **contributions**?

- Sin activations in NNs making them capable of representing high-frequency signals/functions.
- Experimental proof of their superiority for a variety of tasks.

# Relevant Ideas

- Potentially: find the exact video they use and compare against our model. Since our model would be focused on compression we should see if we can match their quality with a very small MLP. They get ~30db PSNR.
  - 5-layer MLPs with 1024 neurons per layer lr = 1x10^{-4}, batch_size=GPU_mem, iter_count = 100,000, hardware= Titan X
  - [Github](https://github.com/vsitzmann/siren)
  - [Data](https://drive.google.com/drive/folders/1_iq__37-hw7FJOEUK1tX7mdp8SKB368K), including the video they test on
  - Video Quality Metric: avg PSNR
- They recommend using weight initialisation in the first layer such that sin(w_0 . Wx+b) spans multiple periods over [-1,1]. They find a w_0 value of 30 to work quite well, this is repeated across future works such as COIN.
- In their supplementary material they mentions that using the same w_0 in all layers speeds up SIREN training and boosts gradients by a factor of w_0. Might be relevant if gradient values tend to vanish.



# Notes

- ReLU networks cannot process signals effectively because they require modelling information contained in higher-order derivatives. ReLU networks have zero-derivatives everywhere for any derivative order greater or equal to 2.
- Other activation types, tanh/softplus, are not as well behaved as sin. This is expected given that decomposition into periodic functions (sin/cos) is standard in signal processing because of domain-fit.
- Because the derivative of sine is cosine---which is itself equal to sqrt(1-sin^2) i.e sinusoidal in nature---and the derivative of cosine is -sin, any derivative of a SIREN is also a SIREN
- They do an early experiment on fitting a SIREN to a short 300x512x512 video and show that it outperforms ReLU-MLPs. The intent of their work was not to test video-compression, merely to show a better PSNR than standard MLP solutions. 



# Excerpts

## Abstract 

"Implicitly defined, continuous, differentiable signal representations parameterized
by neural networks have emerged as a powerful paradigm, offering many possible
benefits over conventional representations. However, current network architectures
for such implicit neural representations are incapable of modeling signals with
fine detail, and fail to represent a signal’s spatial and temporal derivatives, despite
the fact that these are essential to many physical signals defined implicitly as the
solution to partial differential equations. We propose to leverage periodic activation
functions for implicit neural representations and demonstrate that these networks,
dubbed sinusoidal representation networks or SIRENs, are ideally suited for representing complex natural signals and their derivatives. We analyze SIREN activation
statistics to propose a principled initialization scheme and demonstrate the representation of images, wavefields, video, sound, and their derivatives. Further, we show
how SIRENs can be leveraged to solve challenging boundary value problems, such
as particular Eikonal equations (yielding signed distance functions), the Poisson
equation, and the Helmholtz and wave equations. Lastly, we combine SIRENs with
hypernetworks to learn priors over the space of SIREN functions. Please see the
project website for a video overview of the proposed method and all applications."


"
Finally, we propose to initialize the first layer of the sine network with weights so that the
sine function sin(ω0 · Wx + b) spans multiple periods over [−1, 1]. We found ω0 = 30 to work
well for all the applications in this work. The proposed initialization scheme yielded fast and robust
convergence using the ADAM optimizer for all experiments in this work"

