# Components

### Convert colored image to grayscale

* Input - Colored AFM image of self assembled structures on flat substrates
* If already grayscale, proceed to the next step.
* Output - Grayscale AFM image
* Primitive Components- Scikit-image

### Background correction from Natural drift from AFM tip

* Input - Grayscale AFM image
* Output - Background corrected and normalized Grayscale AFM image
* Primitive Components- Scikit-image

### Noise filtering - corrects the image for random noise

* Input - Background corrected normalized Grayscale AFM image
* Output - Noise filtered background corrected normalized grayscale AFM image
* Primitive Components- Scikit-image

### Image segmentation into two images - ordered and disordered image and visualize the images

* Input - Noise filtered background corrected normalized grayscale AFM image
* Output - Show input image alongside two segmented images showing ordered and disordered regions
* Primitive Components- Scikit-image

### Quantification of order and disorder using segmented images

* Input - segmented images - ordered and disordered images
* Orderedness = Ordered pixels/Total pixels
* Disorderedness = Disordered pixels/Total pixels
* Order:Disorder ratio = Ordered pixels/Disordered pixels
* Output - Order:Disorder ratio, Orderedness and Disorderedness of the image
* Primitive Components- numpy, pandas, Scikit-image, math, stats

### Clustering and Prediction

* Input - processing parameters (pH, Concentration)
* clustering of Orderedness, Disorderedness, Order:Disorder ratio parameters from training sets, validated with test sets.
* Prediction of Orderedness, Disorderedness and Order:Disorder ratio for input parameters, by regression of training and test cases.
