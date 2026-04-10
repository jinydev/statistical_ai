---
layout: default
title: "index"
---

# Forward Stepwise Selection 

_Forward stepwise selection_ is a computationally efficient alternative to best forward subset selection. While the best subset selection procedure considers all stepwise 2 _[p]_ possible models containing subsets of the _p_ predictors, forward stepselection wise considers a much smaller set of models. Forward stepwise selection begins with a model containing no predictors, and then adds predictors to the model, one-at-a-time, until all of the predictors are in the model. In particular, at each step the variable that gives the greatest _additional_ improvement to the fit is added to the model. More formally, the forward stepwise selection procedure is given in Algorithm 6.2. 

stepwise selection 

Unlike best subset selection, which involved fitting 2 _[p]_ models, forward stepwise selection involves fitting one null model, along with _p − k_ models in the _k_ th iteration, for _k_ = 0 _, . . . , p −_ 1. This amounts to a total of 1 + � _kp−_ =01[(] _[p][−][k]_[) = 1+] _[p]_[(] _[p]_[+1)] _[/]_[2][ models. This is a substantial difference: when] 

234 6. Linear Model Selection and Regularization 

|# Variables|Best subset<br>Forward stepwise|
|---|---|
|One<br>Two<br>Three<br>Four|`rating`<br>`rating`<br>`rating`, `income`<br>`rating`, `income`<br>`rating`, `income`, `student`<br>`rating`, `income`, `student`<br>`cards`, `income`<br>`rating`, `income`,<br>`student`, `limit`<br>`student`, `limit`|



**TABLE 6.1.** _The first four selected models for best subset selection and forward stepwise selection on the_ `Credit` _data set. The first three models are identical but the fourth models differ._ 

_p_ = 20, best subset selection requires fitting 1 _,_ 048 _,_ 576 models, whereas forward stepwise selection requires fitting only 211 models.[2] 

In Step 2(b) of Algorithm 6.2, we must identify the _best_ model from among those _p−k_ that augment _Mk_ with one additional predictor. We can do this by simply choosing the model with the lowest RSS or the highest _R_[2] . However, in Step 3, we must identify the best model among a set of models with different numbers of variables. This is more challenging, and is discussed in Section 6.1.3. 

Forward stepwise selection’s computational advantage over best subset selection is clear. Though forward stepwise tends to do well in practice, it is not guaranteed to find the best possible model out of all 2 _[p]_ models containing subsets of the _p_ predictors. For instance, suppose that in a given data set with _p_ = 3 predictors, the best possible one-variable model contains _X_ 1, and the best possible two-variable model instead contains _X_ 2 and _X_ 3. Then forward stepwise selection will fail to select the best possible two-variable model, because _M_ 1 will contain _X_ 1, so _M_ 2 must also contain _X_ 1 together with one additional variable. 

Table 6.1, which shows the first four selected models for best subset and forward stepwise selection on the `Credit` data set, illustrates this phenomenon. Both best subset selection and forward stepwise selection choose `rating` for the best one-variable model and then include `income` and `student` for the two- and three-variable models. However, best subset selection replaces `rating` by `cards` in the four-variable model, while forward stepwise selection must maintain `rating` in its four-variable model. In this example, Figure 6.1 indicates that there is not much difference between the threeand four-variable models in terms of RSS, so either of the four-variable models will likely be adequate. 

Forward stepwise selection can be applied even in the high-dimensional setting where _n < p_ ; however, in this case, it is possible to construct submodels _M_ 0 _, . . . , Mn−_ 1 only, since each submodel is fit using least squares, which will not yield a unique solution if _p ≥ n_ . 

Backward Stepwise Selection 

Like forward stepwise selection, _backward stepwise selection_ provides an backward 

> 2Though forward stepwise selection considers _p_ ( _p_ + 1) _/_ 2 + 1 models, it performs a _guided_ search over model space, and so the _effective_ model space considered contains substantially more than _p_ ( _p_ + 1) _/_ 2 + 1 models. 

stepwise selection 

6.1 Subset Selection 235 

efficient alternative to best subset selection. However, unlike forward stepwise selection, it begins with the full least squares model containing all _p_ predictors, and then iteratively removes the least useful predictor, one-ata-time. Details are given in Algorithm 6.3. 

**Algorithm 6.3** _Backward stepwise selection_ 

1. Let _Mp_ denote the _full_ model, which contains all _p_ predictors. 

2. For _k_ = _p, p −_ 1 _, . . . ,_ 1: 

   - (a) Consider all _k_ models that contain all but one of the predictors in _Mk_ , for a total of _k −_ 1 predictors. 

   - (b) Choose the _best_ among these _k_ models, and call it _Mk−_ 1. Here _best_ is defined as having smallest RSS or highest _R_[2] . 

3. Select a single best model from among _M_ 0 _, . . . , Mp_ using the prediction error on a validation set, _Cp_ (AIC), BIC, or adjusted _R_[2] . Or use the cross-validation method. 

Like forward stepwise selection, the backward selection approach searches through only 1+ _p_ ( _p_ +1) _/_ 2 models, and so can be applied in settings where _p_ is too large to apply best subset selection.[3] Also like forward stepwise selection, backward stepwise selection is not guaranteed to yield the _best_ model containing a subset of the _p_ predictors. 

Backward selection requires that the number of samples _n_ is larger than the number of variables _p_ (so that the full model can be fit). In contrast, forward stepwise can be used even when _n < p_ , and so is the only viable subset method when _p_ is very large. 
