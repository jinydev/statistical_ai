---
layout: default
title: "index"
---

[< 2.1.1 Why Estimate F](../index.html) | [2.1.2 How Do We Estimate F >](../../2_1_2_how_do_we_estimate_f/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Prediction

In many situations, a set of inputs _X_ are readily available, but the output _Y_ cannot be easily obtained. In this setting, since the error term averages to zero, we can predict _Y_ using 
$$ \hat{Y} = \hat{f}(X) \tag{2.2} $$

where $\hat{f}$ represents our estimate for _f_, and $\hat{Y}$ represents the resulting prediction for _Y_.

In this setting, $\hat{f}$ is often treated as a _black box_, in the sense that one is not typically concerned with the exact form of $\hat{f}$, provided that it yields accurate predictions for _Y_.

As an example, suppose that $X_1, \dots, X_p$ are characteristics of a patient’s blood sample that can be easily measured in a lab, and _Y_ is a variable encoding the patient’s risk for a severe adverse reaction to a particular drug. It is natural to seek to predict _Y_ using _X_, since we can then avoid giving the drug in question to patients who are at high risk of an adverse reaction—that is, patients for whom the estimate of _Y_ is high.

The accuracy of $\hat{Y}$ as a prediction for _Y_ depends on two quantities, which we will call the _reducible error_ and the _irreducible error_. In general, $\hat{f}$ will not be a perfect estimate for _f_, and this inaccuracy will introduce some error. This error is _reducible_ because we can potentially improve the accuracy of $\hat{f}$ by using the most appropriate statistical learning technique to estimate _f_. However, even if it were possible to form a perfect estimate for _f_, so that our estimated response took the form $\hat{Y} = f(X)$, our prediction would still have some error in it! This is because _Y_ is also a function of $\epsilon$, which, by definition, cannot be predicted using _X_. Therefore, variability associated with $\epsilon$ also affects the accuracy of our predictions.

This is known as the _irreducible_ error, because no matter how well we estimate _f_, we cannot reduce the error introduced by $\epsilon$.

Why is the irreducible error larger than zero? The quantity $\epsilon$ may contain unmeasured variables that are useful in predicting _Y_: since we don't measure them, _f_ cannot use them for its prediction. ![Figure 2.3](./img/Image_017.png)

**FIGURE 2.3.** _The plot displays_ `income` _as a function of_ `years of education` _and_ `seniority` _in the_ `Income` _data set. The blue surface represents the true underlying relationship between_ `income` _and_ `years of education` _and_ `seniority`, _which is known since the data are simulated. The red dots indicate the observed values of these quantities for 30 individuals._

The quantity $\epsilon$ may also contain unmeasurable variation. For example, the risk of an adverse reaction might vary for a given patient on a given day, depending on manufacturing variation in the drug itself or the patient’s general feeling of well-being on that day.

Consider a given estimate $\hat{f}$ and a set of predictors _X_, which yields the prediction $\hat{Y} = \hat{f}(X)$. Assume for a moment that both $\hat{f}$ and _X_ are fixed, so that the only variability comes from $\epsilon$. Then, it is easy to show that $$

\begin{align*}
E(Y - \hat{Y})^2 &= E[f(X) + \epsilon - \hat{f}(X)]^2 \\
&= [f(X) - \hat{f}(X)]^2 + \text{Var}(\epsilon)
\end{align*} \tag{2.3}

$$

where $E(Y - \hat{Y})^2$ represents the average, or _expected value_, of the squared difference between the predicted and actual value of _Y_, and $\text{Var}(\epsilon)$ represents the _variance_ associated with the error term $\epsilon$.

The focus of this book is on techniques for estimating _f_ with the aim of minimizing the reducible error. It is important to keep in mind that the irreducible error will always provide an upper bound on the accuracy of our prediction for _Y_.

This bound is almost always unknown in practice.

# Inference

We are often interested in understanding the association between _Y_ and $X_1, \dots, X_p$. In this situation we wish to estimate _f_, but our goal is not necessarily to make predictions for _Y_.

Now $\hat{f}$ cannot be treated as a black box, because we need to know its exact form.

In this setting, one may be interested in answering the following questions:

- _Which predictors are associated with the response?_

It is often the case that only a small fraction of the available predictors are substantially associated with _Y_. Identifying the few _important_ predictors among a large set of possible variables can be extremely useful, depending on the application.

- _What is the relationship between the response and each predictor?_

Some predictors may have a positive relationship with _Y_, in the sense that larger values of the predictor are associated with larger values of _Y_. Other predictors may have the opposite relationship. Depending on the complexity of _f_, the relationship between the response and a given predictor may also depend on the values of the other predictors.

- _Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?_

Historically, most methods for estimating _f_ have taken a linear form. In some situations, such an assumption is reasonable or even desirable. But often the true relationship is more complicated, in which case a linear model may not provide an accurate representation of the relationship between the input and output variables.

In this book, we will see a number of examples that fall into the prediction setting, the inference setting, or a combination of the two.

For instance, consider a company that is interested in conducting a direct-marketing campaign. The goal is to identify individuals who are likely to respond positively to a mailing, based on observations of demographic variables measured on each individual. In this case, the demographic variables serve as predictors, and response to the marketing campaign (either positive or negative) serves as the outcome. The company is not interested in obtaining a deep understanding of the relationships between each individual predictor and the response; instead, the company simply wants to accurately predict the response using the predictors. This is an example of modeling for prediction.

In contrast, consider the `Advertising` data illustrated in Figure 2.1. One may be interested in answering questions such as:

- _Which media are associated with sales?_

- _Which media generate the biggest boost in sales?_ or

- _How large of an increase in sales is associated with a given increase in TV advertising?_

This situation falls into the inference paradigm.

Another example involves modeling the brand of a product that a customer might purchase based on variables such as price, store location, discount levels, competition price, and so forth. In this situation one might really be most interested in the association between each variable and the probability of purchase. For instance, _to what extent is the product’s price associated with sales?_ This is an example of modeling for inference.

Finally, some modeling could be conducted both for prediction and inference. For example, in a real estate setting, one may seek to relate values of homes to inputs such as crime rate, zoning, distance from a river, air quality, schools, income level of community, size of houses, and so forth. In this case one might be interested in the association between each individual input variable and housing price—for instance, _how much extra will a house be worth if it has a view of the river?_ This is an inference problem.

Alternatively, one may simply be interested in predicting the value of a home given its characteristics: _is this house under- or over-valued?_ This is a prediction problem.

Depending on whether our ultimate goal is prediction, inference, or a combination of the two, different methods for estimating _f_ may be appropriate. For example, _linear models_ allow for relatively simple and interpretable inference, but may not yield as accurate predictions as some other approaches. In contrast, some of the highly non-linear approaches that we discuss in the later chapters of this book can potentially provide quite accurate predictions for _Y_, but this comes at the expense of a less interpretable model for which inference is more challenging.

---

## Sub-Chapters


[< 2.1.1 Why Estimate F](../index.html) | [2.1.2 How Do We Estimate F >](../../2_1_2_how_do_we_estimate_f/index.html)
