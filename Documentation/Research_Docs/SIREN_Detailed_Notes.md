# Table of contents:
- [Table of contents:](#table-of-contents)
- [Introduction](#introduction)
- [Four/Five C's](#fourfive-cs)
  - [What is the **category** of the paper?](#what-is-the-category-of-the-paper)
  - [What is the **context** of the paper?](#what-is-the-context-of-the-paper)
  - [Is the paper **correct** in it's assumptions](#is-the-paper-correct-in-its-assumptions)
  - [What are the main **contributions**?](#what-are-the-main-contributions)
- [Relevant Ideas](#relevant-ideas)
- [Excerpts](#excerpts)
  - [Abstract](#abstract)

# Introduction
The goal of this document is to write down the important elements of the paper ["Implicit Neural Representations with Periodic Activation Functions"](https://arxiv.org/pdf/2006.09661.pdf), specifically those that are relevant to our project on neural video compression with implicit representations.

It uses the guidelines from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) adapted to the use case of constructing an experimental design for our project.

As such, it is broken down in four parts parts. The first one contains the relevant four of the "Five C's" from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) answered, this is then followed by a series of applicable ideas from the paper which could be integrated into our project. The final section contains excerpts from the paper (e.g the abstract) for easy future checking during development.



# Four/Five C's
## What is the **category** of the paper?

## What is the **context** of the paper?

## Is the paper **correct** in it's assumptions

## What are the main **contributions**?


# Relevant Ideas

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




