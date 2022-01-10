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
The goal of this document is to write down the important elements of the paper ["COIN: COmpression with Implicit Neural representations"](https://arxiv.org/abs/2103.03123), specifically those that are relevant to our project on neural video compression with implicit representations.

It uses the guidelines from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) adapted to the use case of constructing an experimental design for our project.

As such, it is broken down in four parts. The first one contains the relevant four of the "Five C's" from ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) answered, this is then followed by a series of applicable ideas from the paper which could be integrated into our project. Miscellaneous notes serve as the penultimate section. The final part contains excerpts from the paper (e.g the abstract) for easy future checking during development.



# Four/Five C's
## What is the **category** of the paper?
A Neural Image Compression paper advocating the usage of [SIREN](SIREN:%20Implicit%20Neural%20Representations%20with%20Periodic%20Activation%20Functions.md) models to overfit an image with a NN. It takes the ideas of SIREN and focuses on finding the best combination of network size and model compression techniques. 

## What is the **context** of the paper?
The success of implicit neural representation using sinusoidal positional encodings in modelling high-frequency signals such as pixel coordinate->RGB mappings. 

## Is the paper **correct** in it's assumptions?
COIN proved that very small networks in terms of parameter count can fit images very well, and that model compression techniques like using half-precision weights do not greatly harm the model. As such, it did show the promise of using SIRENS in image compressions.

## What are the main **contributions**?

- Constructing very small models, when compared to the 5x1024 MLPs used by [SIREN](SIREN:%20Implicit%20Neural%20Representations%20with%20Periodic%20Activation%20Functions.md), capable of fitting an image with acceptable PSNR and good bits-per-pixel.
- Showing that simple model compression is applicable and sufficient.
- Paving the way for systems using the same techniques which are [competitive](https://arxiv.org/abs/2112.04267) with the state of the art.

# Relevant Ideas

- **SIREN MLP for video compression:** instead of image compression. This is the inspiration for the entire project
- **Progressive decoding:** by evaluating the network using progressively higher resolutions. Same principles could be applied to video.
  - The other version of progressive decoding simply runs over parts of the image/video first
- Have a long appendix with examples of video frames.
- Have a link to compressed video files that can be easily played during evaluation. 
- Network structure:
  - 0.07bpp. Number of layers: 5, width of layers: 20.
  - 0.15bpp. Number of layers: 5, width of layers: 30.
  - 0.3bpp. Number of layers: 10, width of layers: 28.
  - 0.6bpp. Number of layers: 10, width of layers: 40.
  - 1.2bpp. Number of layers: 13, width of layers: 49.
  - Coordinates normalized to [-1,1]
  - RGB normalized to [0,1]
  - Learning rate: 2e-4
  - 

# Notes

- They can fit 393k pixel images with NNs having only 8k params
- Outperforms JPEG at low bit-rate without entropy-coding or learning distributions over weights
- They apply two methods for reducing the size of the models
  - Neural architecture search to find the best length/width of an NLP within a given param budget.
  - Weight Quantization going from 32-bit to 16-bit. 
- Importantly, they find that 8-bit quantization is too harsh
- They essentially transform data compression to model compression
- 


# Excerpts

## Abstract 

"We propose a new simple approach for image compression: instead of storing the
RGB values for each pixel of an image, we store the weights of a neural network
overfitted to the image. Specifically, to encode an image, we fit it with an MLP
which maps pixel locations to RGB values. We then quantize and store the weights
of this MLP as a code for the image. To decode the image, we simply evaluate
the MLP at every pixel location. We found that this simple approach outperforms
JPEG at low bit-rates, even without entropy coding or learning a distribution over
weights. While our framework is not yet competitive with state of the art compression methods, we show that it has various attractive properties which could
make it a viable alternative to other neural data compression approaches."