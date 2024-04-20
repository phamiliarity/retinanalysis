# Overview
*Legend*<br>
<img alt="Legend for the flowchart" src=".imgs/legend.svg"/>

*note: each notebook can be converted into a python script to run from the CLI*


## Categories
### Initialise
Notebooks for optional pre-processing.
- [**get_subsection.ipynb**](./00_init/get_subsection.ipynb): get x-y subsection(s) of stacks.

### Segmentation
Notebooks for segmentation of nuclei and foci in (confocal) microscopy data.
- [**01_run_2Dcellpose_pretrained_models.ipynb**](./01_segmentation/01_run_2Dcellpose_pretrained_models.ipynb): segment a 2D TIFF file with all available Cellpose models (v2.2.2)
- [**02_HITL_model_finetuning.ipynb**](./01_segmentation/02_HITL_model_finetuning.ipynb): finetune a pre-trained Cellpose model using 2D TIFFs and manually-refined annotations.
- [**03_run_cellpose_on_stack**](./01_segmentation/03_run_cellpose_on_stack.ipynb): segment a multiplane TIFF file using a pre-trained or custom Cellpose model.
- [**foci_segmentation**](./01_segmentation/foci_segmentation.ipynb): segment foci in a multiplane TIFF file using heuristic intensity-based methods (otsu, watershed)

### Quality control
Notebooks for filtering/refining masks.
- [**placeholder**]():  merging masks in Z-direction
- [**placeholder**](): removing masks based on mask statistics (e.g., size, overlap)

### Quantification
Notebooks for quantitative analyses.
- [**model_output_comparison.ipynb**](./03_quantification): comparison between overlap of 2D labels. 
    - [**model_comparison_plots.ipynb**](./03_quantification) : Visualising the output.
- [**placeholder**](./03_quantification):  Signal intensities: *soon..*

## Description


### 04_merge_3d_masks.ipynb
- Notebook to detect and merge 3D masks that are fragmented in the z-direction.

### 05_filter_3d_masks.ipynb
- Notebook to perform quality control on the 3D masks for downstream processes.


### model_output_comparison.ipynb
- Notebook to compare manual and predicted segmentations (precision, recall, F1-score, Jaccard Indices)


# References
1. Pachitariu, M., Stringer, C. Cellpose 2.0: how to train your own model. Nat Methods 19, 1634–1641 (2022). https://doi.org/10.1038/s41592-022-01663-4
