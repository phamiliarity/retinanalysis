*Legend*<br>
<img src="../.imgs/legend.svg" alt="Legend for the flowchart" width="250"/>
<hr>

# 01_run_cellpose_pretrained_models.ipynb
Notebook to run pre-trained Cellpose models (v2.2.2) [1] on a 2D microscopy slice.

Useful for determining the best performing model out-of-the-box for further finetuning.

![Flowchart of the notebook for running all pre-trained models](../.imgs/flowchart_run-2Dcellpose_modelzoo.png)

# 02_HITL_finetuning.ipynb
Notebook to finetune a pre-trained Cellpose model using a human-in-the-loop approach.

![Flowchart of the notebook for finetuning a pre-trained model.](../.imgs/flowchart_HITL_model_finetuning.png)

# 03_run_cellpose_single_model.ipynb
- Notebook to run a (finetuned) Cellpose model on one or more microscopy stacks.