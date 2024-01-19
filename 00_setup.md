note: can be run from jupyter notebook as well if preferred.
# Windows
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

# Mac
https://forum.image.sc/t/cellpose-on-macos-m1-pro-apple-silicon-arm64/68018/4
```
conda create -y -n cellpose-env python=3.9 pyqt imagecodecs pyqtgraph
conda activate cellpose-env
pip install cellpose

```
