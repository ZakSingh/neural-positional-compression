- [Topic Selection](#topic-selection)
- [Research Methodology](#research-methodology)
- [Model Construction](#model-construction)
- [Experimental Design](#experimental-design)
- [Deciding on Figures for Report](#deciding-on-figures-for-report)

#Decision-Making Process Documentation
This document is being written with the benefit of hindsight, however, some of its ideas can be traced to the "Relevant Ideas" section of the research documents on [SIREN](Research_Docs/SIREN:%20Implicit%20Neural%20Representations%20with%20Periodic%20Activation%20Functions.md), [COIN](Research_Docs/COIN:%20COmpression%20with%20Implicit%20Neural%20representations.md), and [Implicit Neural Representations for Image Compression](Research_Docs/Implicit%20Neural%20Representations%20for%20Image%20Compression.md). 


We will now document our decision-making process regarding topic selection, research methodology, model construction and experimental design.

# Topic Selection
- We decided to explore Implicit Neural Representations For Video after we came across [COIN](Research_Docs/COIN:%20COmpression%20with%20Implicit%20Neural%20representations.md), specifically, it was clear to us that a Neural Network design should be able to learn how to take advantage of frame sequentiality. This was of interest since in the image representation application all similarity is purely spatial in nature, we were curious about how well the NN could capture movement and fine-details in non-static scenes.
- Another factor that influenced our choice of topic was our restricted computational resources. We only had access to one shared medium-power EC2 instance and wanted a topic where we could obtain significant results within this restriction. Video representation was ideal since we could choose the resolution, number of frames and number of iterations. Other topics we considered largely involved Neural Architecture Search, however, they were deemed infeasible
# Research Methodology
- We began with a literature sweep during which we wrote down the most relevant papers we found, i.e those in the [Research_Docs](Research_Docs/), alongside notes on their relevant content as well as ideas which could be adapted sucessfuly to the video domain. During this process we followed the guidlines outlined in ["How to Read a Paper"](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458) in order to optimise the reading process. 
- After we identified the above core set of papers, we searched for any related work that built upon either positional encodings or SIRENs. The results of this are evident in the background section of our report. 
- Following the inspection of all relevant prior work, we began  constructing the model. Initial development began with a very small and noisy 68x68 video. We moved onto the 128x128 videos shown in the report after reaching a satisfying base architecture.
# Model Construction
- We began with the simplest model structure that had proven sucessful, the ReLU+Sinusoidal Encoding of [NeRF](https://arxiv.org/abs/2003.08934). This was severely limited as it could not learn high-frequency features for even 5 frames of the 68x68 video without large amount of vertical stripes and artifacting.
- The first attempt at fixing this was to employ progressive chunking where we kept expanding the size of the chunk during training. This greatly improved quality in terms of PSNR, however, the unbalanced number of times we showed earlier vs later frames resulted in temporal inconsistencies. I.e a person could move their leg forward and then back in the next frame.
- After this initial failure we changed out the model for a SIREN with the exact parameters specified in the above paper. Because [Implicit Neural Representations for Image Compression](Research_Docs/Implicit%20Neural%20Representations%20for%20Image%20Compression.md) had already found that positional encodings and SIRENs are, to some extent, additive we immediately combined the SIREN model with a uniform sinusoidal encoding.
- This resulted in a near-perfect fit to the 68x68 video. After this point we moved onto the 128x128.
- Given that we could not hope to fit the 500 frames in one MLP, keeping the limitations on hidden layer count that [Implicit Neural Representations for Image Compression](Research_Docs/Implicit%20Neural%20Representations%20for%20Image%20Compression.md) had found in mind, we employed static chunking to ensure that the entire video could be encoded.
- At this point we began to have the specific goal of ilustrating our project on video compression, which is why we included the l1 regularisation into the loss function. To ensure that the weights remain small and behave well under future entropy coding.
- Observing that we get better and better results as we increase the positional encoding dimension, a question arose on which of the dimensions was less or more important for final image quality. As such we decided to decouple the encoding dimension sizes
- To make sure our comparisons between uniform vs non-uniform encoding dimensions were as fair as possible we imposed a strict ordering on the encoding components. The goal was to have it so if we do decide to use the same value across dimensions it should be no different then we were encoding all of them simultaneously.
- Surprisingly, decreasing the time dimension encoding size and increasing the others led to better results than a uniform distribution. We tested the limits of this and found that the proportion does matter, dropping the time dimension size below 1/3 of the spatial size seemed to hurt performance
- After we could fit 15 frames with decent PSNR we looked into up-to-date NN compression systems. We decided to use [DeepCABAC](https://arxiv.org/abs/1905.08318) since it offered a tailored quantization mechanisms alongside the arithmetic entropy coding we had anticipated when we introduced l1 regularisation
# Experimental Design
- We decided on a representative set of NN model and positional encoding combinations to compare against INVR. ReLU+Sin, INVR-None and INVR-Even were obvious as they showcased the specific strengths of our system, however, we were also quite curious abouut trying out the Gaussian encoding which is how INVR-Gaussian entered our model set.
- We researched classical encoding standards to compare against, fianlly landing on H.264 (Because of its usage of the original CABAC) and MPEG
- The graphs were chosen to showcase the image quality benefits of our system as well as its convergence properties. We were specifically looking to see what the probability density function looked like since during training the mean and median were almost always identical which puzzeled us.




# Deciding on Figures for Report
- Image Comparison
	- INVR Uncompressed
	- INVR Compressed
	- Gaussian
	- MPEG
	- H264
	- Original

- Per-Frame PSNR graph
	- INVR Uncompressed
	- INVR Compressed
	- MPEG
	- H264

- PSNR histogram

- Single chunk training PSNR
	- ENVR
	- Even frequency encoding
	- No frequency encoding?
	- Gaussian?
	- Dotted line bars for MPEG and H264?

Log every 500 iterations,  train for 20k
