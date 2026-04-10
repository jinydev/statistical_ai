---
layout: default
title: "index"
---

# _10.9.4 Using Pretrained CNN Models_ 

We now show how to use a CNN pretrained on the `imagenet` database to classify natural images, and demonstrate how we produced Figure 10.10. We copied six JPEG images from a digital photo album into the directory `book_images` . These images are available from the data section of `www. statlearning.com` , the ISLP book website. Download `book_images.zip` ; when clicked it creates the `book_images` directory. 

The pretrained network we use is called `resnet50` ; specification details can be found on the web. We will read in the images, and convert them into the array format expected by the `torch` software to match the specifications in `resnet50` . The conversion involves a resize, a crop and then a predefined standardization for each of the three channels. We now read in the images and preprocess them. 

10.9 Lab: Deep Learning 453 

```
In [61]:resize=Resize((232,232))
crop=CenterCrop(224)
normalize=Normalize([0.485,0.456,0.406],
[0.229,0.224,0.225])
imgfiles=sorted([fforfinglob('book_images/*')])
imgs=torch.stack([torch.div(crop(resize(read_image(f))),255)
forfinimgfiles])
imgs=normalize(imgs)
imgs.size()
```

```
Out[61]:torch.Size([6,3,224,224])
```

We now set up the trained network with the weights we read in code block 6. The model has 50 layers, with a fair bit of complexity. 

```
In [62]:resnet_model=resnet50(weights=ResNet50_Weights.DEFAULT)
summary(resnet_model ,
input_data=imgs,
col_names=['input_size',
'output_size',
'num_params'])
```

We set the mode to `eval()` to ensure that the model is ready to predict on new data. 

```
In [63]:resnet_model.eval()
```

Inspecting the output above, we see that when setting up the `resnet_model` , the authors defined a `Bottleneck` , much like our `BuildingBlock` module. We now feed our six images through the fitted network. 

```
In [64]:img_preds=resnet_model(imgs)
```

Let’s look at the predicted probabilities for each of the top 3 choices. First we compute the probabilities by applying the softmax to the logits in `img_preds` . Note that we have had to call the `detach()` method on the tensor `img_preds` in order to convert it to our a more familiar `ndarray` . 

```
In [65]:img_probs=np.exp(np.asarray(img_preds.detach()))
img_probs/=img_probs.sum(1)[:,None]
```

In order to see the class labels, we must download the index file associated with `imagenet` .[27] **`In [66]:`** `labs = json.load(open('imagenet_class_index.json')) class_labels = pd.DataFrame([(int(k), v[1]) for k, v in labs.items()], columns=['idx', 'label']) class_labels = class_labels.set_index('idx') class_labels = class_labels.sort_index()` 

We’ll now construct a data frame for each image file with the labels with the three highest probabilities as estimated by the model above. 

> 27This is avalable from the book website and s3.amazonaws.com/deep-learningmodels/image-models/imagenet_class_index.json. 

454 10. Deep Learning 

```
In [67]:fori,imgfileinenumerate(imgfiles):
```

```
img_df=class_labels.copy()
img_df['prob']=img_probs[i]
img_df=img_df.sort_values(by='prob',ascending=False)[:3]
print(f'Image:{imgfile}')
print(img_df.reset_index().drop(columns=['idx']))
```

```
Image:book_images/Cape_Weaver.jpg
labelprob
0jacamar0.287283
1bee_eater0.046768
2bulbul0.037507
Image:book_images/Flamingo.jpg
labelprob
0flamingo0.591761
1spoonbill0.012386
2American_egret0.002105
Image:book_images/Hawk_Fountain.jpg
labelprob
0great_grey_owl0.287959
1kite0.039478
2fountain0.029384
Image:book_images/Hawk_cropped.jpg
labelprob
0kite0.301830
1jay0.121674
2magpie0.015513
Image:book_images/Lhasa_Apso.jpg
labelprob
0Lhasa0.151143
1Shih-Tzu0.129850
2Tibetan_terrier0.102358
Image:book_images/Sleeping_Cat.jpg
labelprob
0tabby0.173627
1tiger_cat0.110414
2doormat0.093447
```

We see that the model is quite confident about `Flamingo.jpg` , but a little less so for the other images. We end this section with our usual cleanup. 

```
In [68]:del(cifar_test,
cifar_train ,
cifar_dm,
cifar_module ,
cifar_logger ,
cifar_optimizer ,
cifar_trainer)
```
