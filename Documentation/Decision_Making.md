- [Topic Selection](#topic-selection)
- [Research Methodology](#research-methodology)
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
- Following the inspection of all relevant prior work, we began construc



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
