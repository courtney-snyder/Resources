stk.v.11.0
WrittenBy    STK_v11.3.0

BEGIN Facility

    Name		 Brewster_Station

    BEGIN CentroidPosition

        CentralBody		 Earth
        DisplayCoords		 Geodetic
        EcfLatitude		 4.8146999999999998e+01
        EcfLongitude		 -1.1969200000000001e+02
        EcfAltitude		 3.6100000000000000e+02
        HeightAboveGround		 0.0000000000000000e+00
        ComputeTrnMaskAsNeeded		 Off
        AzElMask		 AzElMaskFile: Brewster_Station.aem
        DisplayAltRef		 Ellipsoid
        UseTerrainInfo		 Off
        NumAzRaysInMask		 360
        TerrainNormalMode		 UseCbShape

    END CentroidPosition

    BEGIN Extensions

        BEGIN LaserCAT
        END LaserCAT

        BEGIN ExternData
        END ExternData

        BEGIN RFI
        END RFI

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals
            AzElMask IncludeIntervals
        END AccessConstraints

        BEGIN ObjectCoverage
        END ObjectCoverage

        BEGIN Desc
            BEGIN ShortText
Brewster Station
Name:           Brewster Station
Country:        UnitedStates
Location:       Brewster, Washington
Status:         Active
Type:           GroundStation
Notes:          
Sources:                       http://licensing.fcc.gov/prod/ib/forms/help/GrandFatherList.pdf
Last updated:   2010-02-23
            END ShortText
            BEGIN LongText
Name:           Brewster Station
Country:        UnitedStates
Location:       Brewster, Washington
Status:         Active
Type:           GroundStation
Notes:          
Sources:                       http://licensing.fcc.gov/prod/ib/forms/help/GrandFatherList.pdf
Last updated:   2010-02-23
            END LongText
        END Desc

        BEGIN Atmosphere
<?xml version = "1.0" standalone = "yes"?>
<VAR name = "STK_Atmosphere_Extension">
    <SCOPE Class = "AtmosphereExtension">
        <VAR name = "Version">
            <STRING>&quot;1.0.0 a&quot;</STRING>
        </VAR>
        <VAR name = "ComponentName">
            <STRING>&quot;STK_Atmosphere_Extension&quot;</STRING>
        </VAR>
        <VAR name = "Description">
            <STRING>&quot;STK Atmosphere Extension&quot;</STRING>
        </VAR>
        <VAR name = "Type">
            <STRING>&quot;STK Atmosphere Extension&quot;</STRING>
        </VAR>
        <VAR name = "UserComment">
            <STRING>&quot;STK Atmosphere Extension&quot;</STRING>
        </VAR>
        <VAR name = "ReadOnly">
            <BOOL>false</BOOL>
        </VAR>
        <VAR name = "Clonable">
            <BOOL>true</BOOL>
        </VAR>
        <VAR name = "Category">
            <STRING>&quot;&quot;</STRING>
        </VAR>
        <VAR name = "InheritAtmosAbsorptionModel">
            <BOOL>true</BOOL>
        </VAR>
        <VAR name = "AtmosAbsorptionModel">
            <VAR name = "Simple_Satcom">
                <SCOPE Class = "AtmosphericAbsorptionModel">
                    <VAR name = "Version">
                        <STRING>&quot;1.0.1 a&quot;</STRING>
                    </VAR>
                    <VAR name = "ComponentName">
                        <STRING>&quot;Simple_Satcom&quot;</STRING>
                    </VAR>
                    <VAR name = "Description">
                        <STRING>&quot;Simple Satcom gaseous absorption model&quot;</STRING>
                    </VAR>
                    <VAR name = "Type">
                        <STRING>&quot;Simple Satcom&quot;</STRING>
                    </VAR>
                    <VAR name = "UserComment">
                        <STRING>&quot;Simple Satcom gaseous absorption model&quot;</STRING>
                    </VAR>
                    <VAR name = "ReadOnly">
                        <BOOL>false</BOOL>
                    </VAR>
                    <VAR name = "Clonable">
                        <BOOL>true</BOOL>
                    </VAR>
                    <VAR name = "Category">
                        <STRING>&quot;&quot;</STRING>
                    </VAR>
                    <VAR name = "SurfaceTemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>293.15</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "WaterVaporConcentration">
                        <QUANTITY Dimension = "Density" Unit = "g*m^-3">
                            <REAL>7.5</REAL>
                        </QUANTITY>
                    </VAR>
                </SCOPE>
            </VAR>
        </VAR>
        <VAR name = "EnableLocalRainData">
            <BOOL>false</BOOL>
        </VAR>
        <VAR name = "LocalRainIsoHeight">
            <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                <REAL>2000</REAL>
            </QUANTITY>
        </VAR>
        <VAR name = "LocalRainRate">
            <QUANTITY Dimension = "SlowRate" Unit = "mm*hr^-1">
                <REAL>1</REAL>
            </QUANTITY>
        </VAR>
        <VAR name = "LocalSurfaceTemp">
            <QUANTITY Dimension = "Temperature" Unit = "K">
                <REAL>293.15</REAL>
            </QUANTITY>
        </VAR>
    </SCOPE>
</VAR>        END Atmosphere

        BEGIN Identification
        END Identification

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #00ff00
                LabelColor		 #00ff00
                LineStyle		 0
                MarkerStyle		 5
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 Off
                Inherit		 On
                IsDynamic		 Off
                ShowLabel		 On
                ShowAzElMask		 Off
                ShowAzElFill		 Off
                AzElFillStyle		 7
                AzElFillAltTranslucency		 0.5
                UseAzElColor		 Off
                AzElColor		 #ffffff
                MinDisplayAlt		 0
                MaxDisplayAlt		 10000000
                NumAzElMaskSteps		 1
                ShowAzElAtRangeMask		 On
                ShowAzElAtRangeFill		 Off
                AzElFillRangeTranslucency		 0.5
                AzElAtRangeFillStyle		 7
                UseAzElAtRangeColor		 Off
                AzElAtRangeColor		 #ffffff
                MinDisplayRange		 0
                MaxDisplayRange		 1000000
                NumAzElAtRangeMaskSteps		 10

            END Graphics

            BEGIN DisplayTimes
                DisplayType		 AlwaysOn
            END DisplayTimes
        END Graphics

        BEGIN VO
        END VO

    END Extensions

    BEGIN SubObjects

    END SubObjects

END Facility
