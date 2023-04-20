#! /usr/bin/env/python

from paraview.simple import *

import numpy as np

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="Isabel.cdb")

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=tTKCinemaProductReader1)
extractBlock1.Selectors = ["/Root/Block0", "/Root/Block10"]

# create a new 'Calculator'
calculator1 = Calculator(Input=extractBlock1)
calculator1.ResultArrayName = "velocityMag"
calculator1.Function = "-velocityMag"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram3.ScalarField = ["POINTS", "velocityMag"]
tTKPersistenceDiagram3.InputOffsetField = ["POINTS", "velocityMag"]
tTKPersistenceDiagram3.IgnoreBoundary = False

# create a new 'Threshold'
threshold7 = Threshold(Input=tTKPersistenceDiagram3)
threshold7.Scalars = ["CELLS", "Persistence"]
threshold7.LowerThreshold = 1.2
threshold7.UpperThreshold = 136.490955383565

# create a new 'TTK PersistenceDiagramClustering'
tTKPersistenceDiagramClustering1 = TTKPersistenceDiagramClustering(Input=threshold7)
UpdatePipeline()

# Get the data
matchings_data = FetchData(OutputPort(tTKPersistenceDiagramClustering1, 2))[0]

# Get field data
field_data = matchings_data.GetBlock(0).GetFieldData()

# Display the Wasserstein distance
wasserstein_distance = field_data.GetArray("WassersteinDistance").GetValue(0)

# Save the Wasserstein distance in a csv file
np.savetxt("WassersteinDistance.csv", [wasserstein_distance])
