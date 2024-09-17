# MPI Example

![MPI example Image](https://topology-tool-kit.github.io/img/gallery/mpiExample.jpg)

This toy example illustrates the usage of TTK in a distributed-memory context with MPI. For this example, the original data set is small. Thus, the pipeline first resamples it to $256^3$ but this dimension can be changed to fit the capabilities of your distributed system.

For more information about how to run a pipeline in parallel in ParaView with MPI, please refer to the [ParaView documentation](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html).

Please note both ParaView and TTK need to be compiled with MPI to allow for parallel execution in a distributed context (by setting the following CMake flags `-DPARAVIEW_USE_MPI=ON` and `-DTTK_ENABLE_MPI=ON` for ParaView and TTK respectively).

## Pipeline description

The produced visualization captures the covalent and hydrogen bonds within the molecule complex as well as shows where the electronic density experiences rapid changes, indicating transition points occurring within the bond.

First, the magnitude of the scalar field is computed and the data set is resampled to $256^3$. This dimension can be changed (see the commands below).

Then, both the scalar field and its magnitude are smoothed via [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html) and normalized via [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html).

Next, the critical points of the scalar field are computed via [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) and used as seeds of the [IntegralLines](https://topology-tool-kit.github.io/doc/html/classttkIntegralLines.html).

Next, the geometry of the integral lines is smoothed using the [GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html). 

Finally, the critical points of the magnitude are computed on the smoothed geometry of the integral lines.

## ParaView
To reproduce the above screenshot on 4 processes and 2 threads, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:

``` bash
OMP_NUM_THREADS=2 mpirun -n 4 pvserver 
``` 
In another command line enter the following command:
``` bash
paraview 
```
Now, follow the procedure described in paragraph $7.2.2$ of the following [ParaView documentation](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html#configuring-a-server-connection) to connect your ParaView server to your client. Once that is done, you can open the state file `state/mpiExample.pvsm` in the ParaView GUI through `File` > `Load State`. 


## Python code

``` python  linenums="1"
--8<-- "python/mpiExample.py"
```

To run the above Python script using 2 threads and 4 processes, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
OMP_NUM_THREADS=2 mpirun -n 4 pvbatch python/mpiExample.py 
```

By default, the dataset is resampled to $256^3$. To resample to a higher dimension, for example $2048^3$, enter the following command:

```bash
OMP_NUM_THREADS=2 mpirun -n 4 pvbatch pipeline.py 2048
```
Be aware that this will require a lot of memory to execute and will most likely not be possible on a regular laptop.



## Inputs
- [at.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/at.vti): A molecular dataset: a three-dimensional regular grid with one scalar field, the electronic density in the Adenine Thymine complex.

## Outputs
- `integralLines.pvtu`: the geometry of the smoothed integral lines capturing the covalent and hydrogen bonds of the molecule, as extracted by the analysis pipeline.
- `criticalPoints.pvtu`: the critical points computed on the geometry of the integral lines, showing the rapid changes in the bonds.

## C++/Python API

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[IntegralLines](https://topology-tool-kit.github.io/doc/html/classttkIntegralLines.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

