# Description
Modules containing code developed for the pipeline.

# Overview
**Data storage**
- Slice Object
- Stack Object
> input: custom name, img_path, label_path

**Foci segmentation**

Pre-processing
- Increase contrast between pixels by clipping extremes.
- Smooth edges using erosion and dilation

Segmentation
- Binarize an image matrix using Otsu's thresholding method.
- Convert a 2D binary matrix into a label matrix.
- Convert a 3D binary matrix into a label matrix. 

**Segmentation quality control**
- Merge heavily overlapping masks with optional gap in the z direction

**Quantification**
- Find overlapping masks between two 2D matrices

**Statistics**
- Calculate Jaccard index between two sets of coordinates.


**Utils**

Coordinate retrieval
- Get planes in which the mask id is present in a 3D matrix
- Get pixel coordinates with specified mask ID in a 2D/3D matrix
- Get unique mask IDs from specified pixel coordinates in a 2D matrix

Size 
- Get the number of planes for each mask ID in a 3D mask matrix.

**Plot**

Pre-processing
- Stack the channels of a image matrix

Visualisation
- Show individual plane(s) with mask outlines
- Show the planes of a stack and their masks (optional)

**IO**

- Write settings to a JSON file
