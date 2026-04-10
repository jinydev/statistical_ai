---
layout: default
title: "index"
---

# _10.7.3 Dropout Learning_ 

The second row in Table 10.1 is labeled _dropout_ . This is a relatively new dropout and efficient form of regularization, similar in some respects to ridge regularization. Inspired by random forests (Section 8.2), the idea is to randomly remove a fraction _φ_ of the units in a layer when fitting the model. Figure 10.19 illustrates this. This is done separately each time a training observation is processed. The surviving units stand in for those missing, and their weights are scaled up by a factor of 1 _/_ (1 _− φ_ ) to compensate. This prevents nodes from becoming over-specialized, and can be seen as a form of regularization. In practice dropout is achieved by randomly setting the activations for the “dropped out” units to zero, while keeping the architecture intact. 
