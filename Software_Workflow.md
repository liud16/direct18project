# Functional Design of AFM Image Segmentation Software

1. Image preprocessing:
  - Background drift removal: using python packages similar to *"Strel"* in Matlab
  - Edge identification and segmentation: using edge-based segmentation (Canny detector in skimage) and/or region-based segmentation (watershed in skimage)
  - texture based segmentation based on a random walk method to separate regions of different textures (random walker in skimage)

2. Quantitative analysis:
  - Find the number of unique regions based on textures
  - Calculate the absolute and relative coverage percentage by each unique regions
  - Evaluate the overall level of disorder-ness using a numeric label

3. Training:
  - We provide the training set for the user upon request:
    - the training set contains a fraction of 6400 pre-processed images
    - each image is assigned a numeric label to indicate the level of disorder, and is associated with a set of two parameters (pH, concentration of solute-buffer solution)
    - we only require the user to cite the required sources provided by us
  - User can also use self designed training sets
4. Testing:
  - The testing set contains the fraction of 6400 pre-processed images that is not used in training
  - The fraction of correct prediction is calculated to evaluate training.
  - User can also use self designed test sets

5. Prediction of order to disorder ratio based on an input image:
  - The user inputs an AFM image in txt format (may or may not be preprocessed. <span style = "color:blue"> Please see use-cases for further details </span> )
  - Using K-nearest neighbors or K-means algorithm, the percent surface coverage of each region, percent surface coverage overall and order to disorder ratio is output.

6. Prediction of disorder-ness based on a set of conditions:
  - The user inputs the conditions (pH, concentration. <span style = "color:blue"> For further details please see use-cases </span> )
  - Using multi-dimensional regression analysis, the order:disorder ratio, percent surface coverage of a phase, or percent surface coverage of the surface by the solute for the given set of conditions is output.

7. Visualization:
  - When 1 is performed, the algorithm outputs images of noise corrected, texture-segmented, separated and normalized regions in the image.
