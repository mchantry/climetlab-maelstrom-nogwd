## maelstrom-nogwd

A dataset plugin for climetlab for the dataset maelstrom-nogwd/nogwd.


Features
--------

In this README is a description of how to get the maelstrom-nogwd.

## Datasets description

There are two datasets: 

### 1 : `nogwd`


### 2
TODO


## Using climetlab to access the data (supports grib, netcdf and zarr)

See the demo notebooks here (https://github.com/ecmwf-lab/climetlab_maelstrom_nogwd/notebooks

https://github.com/ecmwf-lab/climetlab_maelstrom_nogwd/notebooks/demo_nogwd.ipynb
[nbviewer] (https://nbviewer.jupyter.org/github/climetlab_maelstrom_nogwd/blob/main/notebooks/demo_nogwd.ipynb) 
[colab] (https://colab.research.google.com/github/climetlab_maelstrom_nogwd/blob/main/notebooks/demo_nogwd.ipynb) 

The climetlab python package allows easy access to the data with a few lines of code such as:
```

!pip install climetlab climetlab_maelstrom_nogwd
import climetlab as cml
ds = cml.load_dataset(""maelstrom-nogwd-nogwd", date='20201231',)
ds.to_xarray()
```
