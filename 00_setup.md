## Setting up the conda environment
1. Initialisation
```
conda create -n cellpose pytorch=1.8.2 cudatoolkit=10.2 -c pytorch-lts
conda activate cellpose
pip install cellpose
```
2. Create kernel for Jupyter Notebook
```
conda install ipykernel
python -m ipykernel install --user --name=cellpose
```
