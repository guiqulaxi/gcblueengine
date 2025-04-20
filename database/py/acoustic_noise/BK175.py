import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK175'
    dbObj.xSpeed_kts=[0.000000,4.084000,14.294000,20.420000]
    dbObj.ySL_dB=[87.080002,91.447014,122.016113,130.750137]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=48.480000
    dbObj.speedMaxNL_kts=20.420000
    dbObj.NL_max=93.000000
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.010720
    dbObj.cavitationSL_dB=148.750137
    dbObj.snorkelingSL_dB=142.750137
    dbObj.BuildSLTable()
    return dbObj