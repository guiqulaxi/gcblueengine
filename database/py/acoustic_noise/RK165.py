import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK165'
    dbObj.xSpeed_kts=[0.000000,3.760000,13.160000,18.799999]
    dbObj.ySL_dB=[93.599998,98.390312,131.922516,141.503143]
    dbObj.speedMinNL_kts=6.860000
    dbObj.NL_min=50.200001
    dbObj.speedMaxNL_kts=18.799999
    dbObj.NL_max=92.199997
    dbObj.cavitationOffset_kts=9.800000
    dbObj.cavitationSlope_ktsperft=0.004300
    dbObj.cavitationSL_dB=159.503143
    dbObj.snorkelingSL_dB=153.503143
    dbObj.BuildSLTable()
    return dbObj