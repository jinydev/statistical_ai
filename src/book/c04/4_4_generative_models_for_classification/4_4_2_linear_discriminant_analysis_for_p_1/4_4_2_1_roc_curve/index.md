---
layout: default
title: "index"
---

[< 4.4.2 Linear Discriminant Analysis For P 1](../index.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/index.html)


# **ROC Curve** 

![Figure 4.8](./img/4_8.png)

**FIGURE 4.8.** _A ROC curve for the LDA classifier on the_ `Default` _data. It traces out two types of error as we vary the threshold value for the posterior probability of default. The actual thresholds are not shown. The true positive rate is the sensitivity: the fraction of defaulters that are correctly identified, using a given threshold value. The false positive rate is 1-specificity: the fraction of non-defaulters that we classify incorrectly as defaulters, using that same threshold value. The ideal ROC curve hugs the top left corner, indicating a high true positive rate and a low false positive rate. The dotted line represents the “no information” classifier; this is what we would expect if student status and credit card balance are not associated with probability of default._ 

marized over all possible thresholds, is given by the _area under the (ROC) curve_ (AUC). An ideal ROC curve will hug the top left corner, so the larger area under the AUC the better the classifier. For this data the AUC is 0 _._ 95, which is the (ROC) close to the maximum of 1 _._ 0, so would be considered very good. We expect curve a classifier that performs no better than chance to have an AUC of 0.5 (when evaluated on an independent test set not used in model training). ROC curves are useful for comparing different classifiers, since they take into account all possible thresholds. It turns out that the ROC curve for the logistic regression model of Section 4.3.4 fit to these data is virtually indistinguishable from this one for the LDA model, so we do not display it here. 

the (ROC) curve 

As we have seen above, varying the classifier threshold changes its true positive and false positive rate. These are also called the _sensitivity_ and one sensitivity minus the _specificity_ of our classifier. Since there is an almost bewildering specificity array of terms used in this context, we now give a summary. Table 4.6 shows the possible results when applying a classifier (or diagnostic test) to a population. To make the connection with the epidemiology literature, we think of “+” as the “disease” that we are trying to detect, and “ _−_ ” as the “non-disease” state. To make the connection to the classical hypothesis testing literature, we think of “ _−_ ” as the null hypothesis and “+” as the 

4. Classification 

156 

|_Predicted_<br>_class_||_True class_<br>_−_or Null<br>+ or Non-null<br>Total|_True class_<br>_−_or Null<br>+ or Non-null<br>Total|_True class_<br>_−_or Null<br>+ or Non-null<br>Total|
|---|---|---|---|---|
||_−_or Null<br>+ or Non-null|True Neg. (TN)<br>False Pos. (FP)|False Neg. (FN)<br>True Pos. (TP)|N~~_∗_~~<br>P_∗_|
||Total|N|P||

**TABLE 4.6.** _Possible results when applying a classifier or diagnostic test to a population._ 

|**ABLE 4.6.** _Possib_<br>_opulation._|_le results wh_<br>|_en applying a classifer or diagnostic test to _|
|---|---|---|
|Name|Defnition|Synonyms<br>|
|False Pos. rate<br>True Pos. rate<br>Pos. Pred. value<br>Neg. Pred. value|FP_/_N<br>TP_/_P<br>TP_/_P_∗_<br>TN_/_N_∗_|Type I error, 1_−_Specifcity<br>1_−_Type II error, power, sensitivity, recall<br>Precision, 1_−_false discovery proportion|

**TABLE 4.7.** _Important measures for classification and diagnostic testing, derived from quantities in Table 4.6._ 

alternative (non-null) hypothesis. In the context of the `Default` data, “+” indicates an individual who defaults, and “ _−_ ” indicates one who does not. 

Table 4.7 lists many of the popular performance measures that are used in this context. The denominators for the false positive and true positive rates are the actual population counts in each class. In contrast, the denominators for the positive predictive value and the negative predictive value are the total predicted counts for each class.

---

## Sub-Chapters


[< 4.4.2 Linear Discriminant Analysis For P 1](../index.html) | [4.4.3 Quadratic Discriminant Analysis >](../../4_4_3_quadratic_discriminant_analysis/index.html)
