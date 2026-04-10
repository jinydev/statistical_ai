---
layout: default
title: "index"
---

# **`In [3]:`** `from torchmetrics import (MeanAbsoluteError ,` 

```
R2Score)
```

```
fromtorchinfoimportsummary
fromtorchvision.ioimportread_image
```

The package `pytorch_lightning` is a somewhat higher-level interface to `torch` that simplifies the specification and fitting of models by reducing the amount of boilerplate code needed (compared to using `torch` alone). 

```
In [4]:frompytorch_lightningimportTrainer
frompytorch_lightning.loggersimportCSVLogger
```

In order to reproduce results we use `seed_everything()` . We will also `seed_` instruct `torch` to use deterministic algorithms where possible. 

```
everything()
```

```
In [5]:frompytorch_lightning.utilities.seedimportseed_everything
seed_everything(0,workers=True)
```

```
torch.use_deterministic_algorithms(True,warn_only=True)
```

We will use several datasets shipped with `torchvision` for our examples: `torchvision` a pretrained network for image classification, as well as some transforms used for preprocessing. 
