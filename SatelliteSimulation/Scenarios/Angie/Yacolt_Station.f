STK.V.9.0
WrittenBy    StandardObjectCatalog
BEGIN Facility
Name        Yacolt_Station
	BEGIN CentroidPosition
		DisplayCoords         Geodetic
		EcfLatitude           45.863
		EcfLongitude          -122.396
		EcfAltitude           197
		DisplayAltRef         Ellipsoid
		AzElMask              AzElMaskFile: Yacolt_Station.aem
	END CentroidPosition
BEGIN Extensions
	BEGIN Graphics
		BEGIN Graphics
			ShowAzElAtRangeMask       On
			MinDisplayRange           0.0
			MaxDisplayRange           1000000.0
			NumAzElAtRangeMaskSteps   10
		END Graphics
	END Graphics
	BEGIN AccessConstraints
			LineOfSight     IncludeIntervals
			AzElMask        IncludeIntervals
	END AccessConstraints
	BEGIN Desc
		ShortText    14
Yacolt Station
		LongText    293
Name:           Yacolt Station
Country:        UnitedStates
Location:       Yacolt, Washington
Status:         Active
Type:           GroundStation
Notes:          

Sources:                       http://licensing.fcc.gov/prod/ib/forms/help/GrandFatherList.pdf
Last updated:   2010-02-23
	END Desc
END Extensions
END Facility
