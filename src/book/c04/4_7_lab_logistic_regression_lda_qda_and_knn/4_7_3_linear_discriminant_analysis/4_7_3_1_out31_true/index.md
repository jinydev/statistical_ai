---
layout: default
title: "index"
---

[< 4.7.3 Linear Discriminant Analysis](../index.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/index.html)


# **`Out[31]:`** `True` 

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so. For instance, suppose that we wish to predict a market decrease only if we are very certain that the market will indeed decrease on that day — say, if the posterior probability is at least 90%. We know that the first column of `lda_prob` corresponds to the label `Down` after having checked the `classes_` attribute, hence we use the column index 0 rather than 1 as we did above. 

```python
In [32]: np.sum(lda_prob[:,0] > 0.9)
```

```python
Out[32]: 0
```

No days in 2005 meet that threshold! In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%. 

The LDA classifier above is the first classifier from the `sklearn` library. We will use several other objects from this library. The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5. Specifically, the methods first create a generic classifier without referring to any data. This classifier is then fit to data with the `fit()` method and predictions are always produced with the `predict()` method. This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of `sklearn`. This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation. This standard pattern also allows for a predictable formation of workflows.

---

## Sub-Chapters


[< 4.7.3 Linear Discriminant Analysis](../index.html) | [4.7.4 Quadratic Discriminant Analysis >](../../4_7_4_quadratic_discriminant_analysis/index.html)
