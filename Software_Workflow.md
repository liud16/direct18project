# Functional Design of AFM Image Segmentation Software

1. Image preprocessing:
  - Background drift removal: using python packages similar to Strel in Matlab
  - Edge identification and segmentation: using edge-based segmentation (Canny detector in skimage) and/or region-based segmentation (watershed in skimage)

2. Quantitative analysis:
  - Find the number of unique regions
  - Calculate the absolute and relative coverage percentage by each unique regions
  - Evaluate the overall level of disorder-ness using a numeric label

3. Training:
  - We provide the training set for the user:
    - the training set contains a fraction of 6400 pre-processed images
    - each image is assigned a numeric label to indicate the level of disorder, and is associated with a set of three parameters (pH, concentration, incubation time)

4. Testing:
  - The testing set contains the fraction of 6400 pre-processed images that is not used in training
  - The fraction of correct prediction is calculated to evaluate training.

5. Prediction of disorder-ness based on an input image:
  - The user inputs an AFM image
  - Using K-nearest neighbors or K-mean algorithm, the disorder-ness of the image is determined.

6. Prediction of disorder-ness based on a set of conditions:
  - The user inputs the conditions (pH, concentration, incubation time)
  - Using multi-dimensional regression analysis, the disorder-ness of the peptide in the given set of conditions is determined

7. Visualization:
  - When 4 is performed, the algorithm outputs images of individual regions in the image
