"""------------------QSWAT Workflow v1.5.2 Settings File---------------"""
# Project Identification
Project_Name     = "blue_nile_qswat"
Model_2_namelist = False        # True = get settings from existing model 
                                # False = get model from current settings

"""---------------------------   File Names  --------------------------"""
# Raster files (Should be projected with the same projection)
Topography         = "dem.tif"
Soils              = "blue_nile_300_soil.tif"
Land_Use           = "blue_nile_300_land_use.tif"


# LookUp Files
soil_lookup        = "soil_lookup.csv"
landuse_lookup     = "landuse_lookup.csv"
# Database table files
Usersoil           = "usersoil.csv"
WGEN_user          = "WGEN_user.csv"


# Shape Files
Outlet             = "outlet.shp" # it should have same format as in the example


# Weather stationinformation files
Precipitation      = "pcp.txt"
Temperature        = "tmp.txt"
Rel_Humidity       = "hmd.txt"
Solar_Radiation    = "slr.txt"
Wind               = "wnd.txt"


"""---------------------------  Project Options  ----------------------"""
# Watershed Deliniation (1 = Cells)
WS_thresholds_type    = 1            
WS_threshold          = 50000
OUT_Snap_threshold    = 300                # metres 
Burn_in_shape         = ""                 # leave as "" if none


#  -------------------  HRU Definition  ------------------
Slope_classes         = "0, 7, 50, 9999"

# HRU creation method   (1 = Dominant landuse, soil, slope , 2 = Dominant HRU,
#                        3 = Filter by Area,                 4 = Target Number of HRUs,
#                        5 = Filter by landuse, soil, slope)

HRU_creation_method   = 5


# Thresholds           (1 = Total Area , 2 = Percent)
HRU_thresholds_type   = 2

HRU_thres_LandUse     = 12             # Only used if HRU_creation_method 5 is selected
HRU_thres_Soil        = 10             #        can be set to "" if 5 is not selected
HRU_thres_Slope       = 7

Target_Value          = None           # used if HRU_creation_method 3 and 4 are selected


# Routing and ET and infiltration
ET_method             = 2           # 1 = Priestley-Taylor, 2 = Penman-Monteith,   3 = Hargreaves,        (4 = Observed - Not supported Currently)
Routing_method        = 2           # 1 = Muskingum,        2 = Variable Storage
Routing_timestep      = 1           # 1 = Daily,            2 = Hourly
Rainfall_timestep     = 1           # 1 = Daily,            2 = Sub-hourly timestep (works with Green & Ampt infiltration)
Run_off_method        = 1           # 1 = SCS Curve Number, 2 = Green & Ampt

# model run settings
cal_file              = ""           # a model.in file (format of swatcup) with parameters for the callibrated model
                                     # leave as "" if there is no file to be used.
Model_Run_period      = "1979 - 2013"# e.g. "1975 - 1980". period to run the simulation from file.cio,
                                     # leave as "" to run whole period where weather data is available
Warm_up_period        = 2            # the number of years for running the model without printing output


# Log progress or not? If yes, you will not see updates
log                   = False        # True or False
"""---------------------------  Settings End  -----------------------"""