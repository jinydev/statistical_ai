---
layout: default
title: "index"
---

# **`Out[17]:`** `0.6074` 

This process can be generalized to create a simple function `boot_SE()` for computing the bootstrap standard error for arbitrary functions that take only a data frame as an argument. 

```
In [18]:defboot_SE(func,
D,
n=None,
B=1000,
seed=0):
rng=np.random.default_rng(seed)
first_,second_=0,0
n=norD.shape[0]
for_inrange(B):
idx=rng.choice(D.index,
n,
replace=True)
value=func(D,idx)
first_+=value
second_+=value**2
returnnp.sqrt(second_/B-(first_/B)**2)
```

Notice the use of `_` as a loop variable in `for _ in range(B)` . This is often used if the value of the counter is unimportant and simply makes sure the loop is executed `B` times. 

Let’s use our function to evaluate the accuracy of our estimate of _α_ using _B_ = 1 _,_ 000 bootstrap replications. 

```
In [19]:alpha_SE=boot_SE(alpha_func,
Portfolio,
B=1000,
seed=0)
alpha_SE
```
