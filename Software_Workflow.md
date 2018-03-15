# Functional Design of AFM Image Segmentation Software

1. Image preprocessing and Segmentation:
  - Background drift removal: using python packages Scikit-Image and OpenCV, we morphologically open the image based on user input structures to approximate and cancel out tip drift
  - Texture based segmentation based on a random walk method to separate regions of different textures (random 
walker in skimage).
  - Grayscale normalized version of the corrected image is output.
  - Percentile filter from Scipy.ndimage module is used to separate the segmented images into ordered and 
disordered regions.

2. Quantitative analysis:
  - Find the number of unique regions based on textures
  - Calculate the absolute and relative coverage percentage by each unique regions
  - Evaluate the overall level of disorder-ness using a numeric label

3. Training:
  - We provide the training set for the user upon request:
    - The training set contains 75% of fifty five pre-processed 512x512 pixelsize images
    - Each image is assigned a numeric label to indicate the level of disorder, and is associated with a set of 
two parameters (pH, concentration of solute-buffer solution)
    - We only require the user to cite the required sources provided by us
  - User can also use self designed training sets

4. Testing:
  - The testing set contains 25% of 55 pre-processed 512x512 pixelsize images
    - The fraction of correct prediction is calculated to evaluate training.
  - User can also use self designed test sets

5. Prediction of order to disorder ratio based on an input image:
  - The user inputs an AFM image in txt format (may or may not be preprocessed. <span style = "color:blue"> Please see use-cases for further details </span> )
  - Using K-nearest neighbors algorithm, the percent surface coverage of each region, percent surface coverage overall and order to disorder ratio is output.

6. Prediction of disorder-ness based on a set of conditions:
  - The user inputs the conditions (pH, concentration. <span style = "color:blue"> For further details please see use-cases </span> )
  - Using multi-dimensional regression analysis, the order:disorder ratio for the pH and peptide concentrations are output.

7. Visualization:
  - When 1 is performed, the algorithm outputs images of noise corrected, texture-segmented, separated and normalized regions in the image.
