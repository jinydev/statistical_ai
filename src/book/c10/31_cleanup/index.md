---
layout: default
title: "index"
---

# Cleanup 

In setting up our data module, we had initiated several worker processes that will remain running. We delete all references to the torch objects to ensure these processes will be killed. 

444 10. Deep Learning 

```
In [32]:del(Hitters,
```

```
hit_model,hit_dm,
hit_logger,
hit_test,hit_train,
X,Y,
X_test,X_train,
Y_test,Y_train,
X_test_t,Y_test_t,
hit_trainer ,hit_module)
```
