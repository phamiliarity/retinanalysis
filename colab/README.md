# Description
Interactive Python Notebooks for quantitative confocal microscopy analyses. Detailed descriptions can be found in the subdirectories.

*Note: Developed in Google Colab with Colab-specific functionalities:
    - Ability to connect to GPU.
    - Forms functionality for easy user input.

## Overview
### [Initialise](./00_init)
Notebooks for optional pre-processing.
- [**get_subsection.ipynb**](./00_init/get_subsection.ipynb): get x-y subsection(s) of stacks.

### [Segmentation](./01_segmentation)
Notebooks for segmentation of nuclei and foci in (confocal) microscopy data.
- [**01_run_2Dcellpose_pretrained_models.ipynb**](./01_segmentation/01_run_2Dcellpose_pretrained_models.ipynb): segment a 2D TIFF file with all available Cellpose models (v2.2.2)
- [**02_HITL_model_finetuning.ipynb**](./01_segmentation/02_HITL_model_finetuning.ipynb): finetune a pre-trained Cellpose model using 2D TIFFs and manually-refined annotations.
- [**03_run_cellpose_on_stack**](./01_segmentation/03_run_cellpose_on_stack.ipynb): segment a multiplane TIFF file using a pre-trained or custom Cellpose model.
- [**foci_segmentation**](./01_segmentation/foci_segmentation.ipynb): segment foci in a multiplane TIFF file using heuristic intensity-based methods (otsu, watershed)

### [Quality control](./02_quality_control/)
Notebooks for filtering/refining masks.
- [**merging_masks_in_Z**](./02_quality_control/merging_masks_in_Z.ipynb):  merging masks in Z-direction
- [**placeholder**](): removing masks based on mask statistics (e.g., size, overlap)

### [Quantification](./03_quantification/)
Notebooks for quantitative analyses.
- [**model_output_comparison.ipynb**](./03_quantification): comparison between overlap of two 2D label matrices. (precision, recall, F1-score, Jaccard Indices)
    - [**model_comparison_plots.ipynb**](./03_quantification) : Visualising the output.

- [**3D_segmentations_stats.ipynb**](./03_quantification/): report statistics for each label in a 3D label matrix.
- [**placeholder**](./03_quantification):  Signal intensities: *soon..*

# References
1. Pachitariu, M., Stringer, C. Cellpose 2.0: how to train your own model. Nat Methods 19, 1634–1641 (2022). https://doi.org/10.1038/s41592-022-01663-4
