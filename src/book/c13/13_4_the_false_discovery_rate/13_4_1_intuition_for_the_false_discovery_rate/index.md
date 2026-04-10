---
layout: default
title: "index"
---

# _13.4.1 Intuition for the False Discovery Rate_ 

As we just discussed, when _m_ is large, then trying to prevent _any_ false positives (as in FWER control) is simply too stringent. Instead, we might try to make sure that the ratio of false positives ( _V_ ) to total positives ( _V_ + _S_ = _R_ ) is sufficiently low, so that most of the rejected null hypotheses are not false positives. The ratio _V/R_ is known as the _false discovery proportion_ false (FDP). 

discovery proportion 

It might be tempting to ask the data analyst to control the FDP: to make sure that no more than, say, 20% of the rejected null hypotheses are false positives. However, in practice, controlling the FDP is an impossible task for the data analyst, since she has no way to be certain, on any particular dataset, which hypotheses are true and which are false. This is very similar to the fact that the data analyst can control the FWER, i.e. she can guarantee that Pr( _V ≥_ 1) _≤ α_ for any pre-specified _α_ , but she cannot guarantee that _V_ = 0 on any particular dataset (short of failing to reject any null hypotheses, i.e. setting _R_ = 0). 

574 13. Multiple Testing 

Therefore, we instead control the _false discovery rate_ (FDR)[15] , defined false as 

discovery rate 

FDR = E(FDP) = E( _V/R_ ) _._ (13.9) 

When we control the FDR at (say) level _q_ = 20%, we are rejecting as many null hypotheses as possible while guaranteeing that no more than 20% of those rejected null hypotheses are false positives, _on average_ . 

In the definition of the FDR in (13.9), the expectation is taken over the population from which the data are generated. For instance, suppose we control the FDR for _m_ null hypotheses at _q_ = 0 _._ 2. This means that if we repeat this experiment a huge number of times, and each time control the FDR at _q_ = 0 _._ 2, then we should expect that, on average, 20% of the rejected null hypotheses will be false positives. On a given dataset, the fraction of false positives among the rejected hypotheses may be greater than or less than 20%. 

Thus far, we have motivated the use of the FDR from a pragmatic perspective, by arguing that when _m_ is large, controlling the FWER is simply too stringent, and will not lead to “enough” discoveries. An additional motivation for the use of the FDR is that it aligns well with the way that data are often collected in contemporary applications. As datasets continue to grow in size across a variety of fields, it is increasingly common to conduct a huge number of hypothesis tests for exploratory, rather than confirmatory, purposes. For instance, a genomic researcher might sequence the genomes of individuals with and without some particular medical condition, and then, for each of 20,000 genes, test whether sequence variants in that gene are associated with the medical condition of interest. This amounts to performing _m_ = 20 _,_ 000 hypothesis tests. The analysis is exploratory in nature, in the sense that the researcher does not have any particular hypothesis in mind; instead she wishes to see whether there is modest evidence for the association between each gene and the disease, with a plan to further investigate any genes for which there is such evidence. She is likely willing to tolerate some number of false positives in the set of genes that she will investigate further; thus, the FWER is not an appropriate choice. However, some correction for multiple testing is required: it would not be a good idea for her to simply investigate _all_ genes with _p_ -values less than (say) 0.05, since we would expect 1,000 genes to have such small _p_ -values simply by chance, even if no genes are associated with the disease (since 0 _._ 05 _×_ 20 _,_ 000 = 1 _,_ 000). Controlling the FDR for her exploratory analysis at 20% guarantees that — on average — no more than 20% of the genes that she investigates further are false positives. 

It is worth noting that unlike _p_ -values, for which a threshold of 0.05 is typically viewed as the minimum standard of evidence for a “positive” result, and a threshold of 0.01 or even 0.001 is viewed as much more compelling, there is no standard accepted threshold for FDR control. Instead, the choice of FDR threshold is typically context-dependent, or even datasetdependent. For instance, the genomic researcher in the previous example might seek to control the FDR at a threshold of 10% if the planned follow- 

> 15If _R_ = 0, then we replace the ratio _V/R_ with 0, to avoid computing 0 _/_ 0. Formally, FDR = E( _V/R|R >_ 0) Pr( _R >_ 0). 

13.4 The False Discovery Rate 575 

up analysis is time-consuming or expensive. Alternatively, a much larger threshold of 30% might be suitable if she plans an inexpensive follow-up analysis. 
