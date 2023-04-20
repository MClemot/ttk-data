# Persistence Clustering 2 

<!--[![Dragon example video tutorial](https://topology-tool-kit.github.io/img/gallery/dragon.jpg)](https://youtu.be/YVk9vRKIEX8)-->

<!--iframe width="100%" height="420"
src="https://www.youtube.com/embed/YVk9vRKIEX8" frameborder="0"
allowfullscreen></iframe-->

![Persistence Clustering 2 Image](https://topology-tool-kit.github.io/img/gallery/persistenceClustering2.jpeg)

## Pipeline description
<!--This example first loads a triangle mesh from disk.-->
This pipeline is similar to the previous examples of persistence clustering and performs a clustering by persistence on a 2D data set taken from the [scikit-learn examples](https://scikit-learn.org/stable/modules/clustering.html). Please check out the [Karhunen-Love Digits 64-Dimensions](https://topology-tool-kit.github.io/examples/karhunenLoveDigits64Dimensions/) example for an application of this pipeline on a real-life data set..

First, this example loads a point cloud from disk (top left view in the above screenshot), then it computes a mesh on which a density field is obtained with a Gaussian Resampling on the points (top right view in the above screenshot). This density field will be considered as the input scalar data.
<!--In a pre-processing, the mesh is smoothed and an elevation function is computed on top of it.-->
<!--Then an elevation function is computed on it, and will be considered as the input scalar data for ou.-->

Next, a [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the features with a persistence above a certain value. The result is a simplified persistence diagram (bottom left view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data, giving us a simplified data.

From there a [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed (bottom right view in the above screenshot). Finally, by using the identifier of the 2-dimension cell of the Morse Smale complex where one point lands, a cluster identifier, encoded in the AscendingManifold field in the ouput, is given to it.


<!--This simplified data is then used as the input of the computation of [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) (top left view, above screenshot) and the [ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html) (bottom left view, above screenshot).-->

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview --state=states/persistenceClustering2.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceClustering2.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering2.py
```


## Inputs
- [clustering2.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/clustering2.csv): a table of 2 dimension points.

## Outputs
- `data2Resampled.csv`: the output is the data resampled in CSV file format, the cluster identifier of a point is given in the AscendingManifold field.
<!-- `Segmentation.vtp`: the output Morse Smale complex in VTK file format (bottom right view, above screenshot).-->


## C++/Python API

<!--[ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html)-->

<!--[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)-->

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

<!--[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)-->

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
