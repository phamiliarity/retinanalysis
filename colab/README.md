# Overview
[complete flowchart]

# Main
## 01_run_cellpose_pretrained_models.ipynb
- Notebook to run pre-trained Cellpose models (v2.2.2) on a single microscopy slice.

<img alt="Flowchart of the notebook: A test slice and model parameters are used to run pre-trained models. The output is .tiff files of the predictions." src="retinanalysis/colab/.imgs/01_flowchart.svg"/>

## 02_HITL_finetuning.ipynb
- Notebook to finetune a pre-trained Cellpose model using a human-in-the-loop approach.

## 03_run_cellpose_single_model.ipynb
- Notebook to run a (finetuned) Cellpose model on one or more microscopy stacks.

## 04_merge_3d_masks.ipynb
- Notebook to detect and merge 3D masks that are fragmented in the z-direction.

## 05_filter_3d_masks.ipynb
- Notebook to perform quality control on the 3D masks for downstream processes.

# Additional

## 01x_model_output_comparison

