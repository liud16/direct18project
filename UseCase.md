<span style="color=red">
# Use Case
</span>
<span style="color:blue">
## Based on the type of user input, our software performs the following tasks:
</span>

1. When the user provides a raw AFM image (of self assembled biomolecules on atomically flat surfaces) that contains regions of different textures, our software provides the following use cases:

* If necessary, convert the **colored** image to **grayscale** image
* Remove background caused by natural drift of the AFM tip
* Remove noise from the AFM image
* Segment the image to separate *ordered* phases or textures from *disordered* phases or textures
* Visualize the ordered and disordered regions separately
* Provide a quantitative evaluation of the order to disorder ratio of the input image


2. When the user provides a set of experimental conditions, our software predicts the disorder-ness of the sample.

* Based on unique sets of experimental conditions comprising mostly of **pH** and **concentration of the peptide-buffer solution**
  our software provides an estimate of the numerical ordered to disordered region ratio and percent surface coverage expected for those conditions.
