# <placeholder name> RetinAnalysis
> Author: Vina My Pham<br>
Project supervisor: Robin van der Weide<br><br>
MSc Bioinformatics internship - Kind group, Hubrecht Institute<br>
 January 15, 2024 to July 26, 2024

## Project description
Framework to perform 3D quantitative analyses on confocal microscopy stacks. 

This repository contains all Python code for pre-processing images, 3D instance segmentations, quality control, quantification and data visualisation.

## Contents
- [Colab](./colab): directory containing Google Colab notebooks.
- [Conda environment .yaml](./cellpose-env_mac.yml): cellpose conda yaml for Mac env
- [Pip req .txt](./colab_requirements.txt): pypi modules used in Colab notebooks

## Author's notes
The workflow was developed for analysing samples from mouse retinal organoid tissue (hence the name 'RetinAnalysis'), but the general set-up is suited for any 3D analysis.

Each notebook serves its own function, though some code redundancy present.

> e.g. finding overlap in Z-direction follows similar logic as comparing two distinct 2D label matrices.

The modular structure can provide a basis for if the notebooks are translated into scripts to run from the CLI.
