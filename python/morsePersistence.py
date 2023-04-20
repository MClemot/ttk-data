#!/usr/bin/env python

from paraview.simple import *

# create a new 'Plane'
plane1 = Plane()
plane1.XResolution = 300
plane1.YResolution = 300

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=plane1)

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(Input=tetrahedralize2)
randomAttributes1.DataType = "Float"
randomAttributes1.ComponentRange = [0.0, 1.0]
randomAttributes1.GeneratePointScalars = 1

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=randomAttributes1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "RandomPointScalars"]
tTKScalarFieldSmoother1.IterationNumber = 7

# create a new 'Calculator'
sine = Calculator(Input=tTKScalarFieldSmoother1)
sine.ResultArrayName = "Sine"
sine.Function = "sin(20*coordsX+1.5)+sin(20*coordsY+1.5)"

# create a new 'Calculator'
distanceField = Calculator(Input=sine)
distanceField.ResultArrayName = "DistanceField"
distanceField.Function = "-sqrt(coordsX*coordsX+coordsY*coordsY)"

# create a new 'Calculator'
calculator1 = Calculator(Input=distanceField)
calculator1.ResultArrayName = "Blend"
calculator1.Function = "Sine+5*DistanceField+5*RandomPointScalars"

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=calculator1)

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=extractSurface6)
warpByScalar1.Scalars = ["POINTS", "Blend"]
warpByScalar1.ScaleFactor = 0.05

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=warpByScalar1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "Blend"]
tTKPersistenceDiagram1.IgnoreBoundary = False

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tTKPersistenceDiagram1)

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = 0.0
threshold1.UpperThreshold = 100000.0

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 0.7
persistenceThreshold.UpperThreshold = 10000.0

# create a new 'Tetrehedralize'
tetrahedralize1 = Tetrahedralize(Input=warpByScalar1)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tetrahedralize1, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "Blend"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "Blend"]

# save the ouput
SaveData("PersistenceDiagram.vtu", tTKPersistenceDiagram1)
SaveData("PersistenceCurve.csv", OutputPort(tTKPersistenceCurve1, 3))
SaveData("MorseComplexeCriticalPoints.vtp", OutputPort(tTKMorseSmaleComplex1, 0))
SaveData("MorseComplexe1Separatrices.vtp", OutputPort(tTKMorseSmaleComplex1, 1))
SaveData("MorseComplexeSegmentation.vtu", OutputPort(tTKMorseSmaleComplex1, 3))
