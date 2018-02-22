# Components 

### Convert colored image to grayscale

* Input - Colored AFM image
* If already grayscale, proceed to the next step.
* Output - Grayscale AFM image

### Background correction from Natural drift from AFM tip

* Input - Grayscale AFM image
* Output - Background corrected Grayscale AFM image

### Noise filtering - corrects the image for random noise

* Input - Background corrected Grayscale AFM image
* Output - Noise filtered background corrected grayscale AFM image

### Image segmentation into two images - ordered and disordered image and vizualize the images

* Input - Noise filtered background corrected grayscale AFM image
* Output - Show input image alongside two segmented images showing ordered and disordered regions

### Quantification of order and disorder using segmented images

* Input - Segmeted images - ordered and disordered images
* Orderness = Ordered pixels/Total pixels
* Disorderness = Disordered pixels/Total pixels
* Output - Orderness and Disorderness of the image 
