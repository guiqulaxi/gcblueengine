import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK160'
    dbObj.xSpeed_kts=[0.000000,3.336000,11.676000,16.680000]
    dbObj.ySL_dB=[91.980003,96.344055,126.892433,135.620544]
    dbObj.speedMinNL_kts=8.204000
    dbObj.NL_min=50.369999
    dbObj.speedMaxNL_kts=16.680000
    dbObj.NL_max=96.570000
    dbObj.cavitationOffset_kts=11.720000
    dbObj.cavitationSlope_ktsperft=0.006710
    dbObj.cavitationSL_dB=153.620544
    dbObj.snorkelingSL_dB=147.620544
    dbObj.BuildSLTable()
    return dbObj