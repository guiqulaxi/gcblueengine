import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK155'
    dbObj.xSpeed_kts=[0.000000,3.124000,10.934000,15.620000]
    dbObj.ySL_dB=[93.279999,97.854004,129.872055,139.020065]
    dbObj.speedMinNL_kts=7.280000
    dbObj.NL_min=50.980000
    dbObj.speedMaxNL_kts=15.620000
    dbObj.NL_max=97.839996
    dbObj.cavitationOffset_kts=10.400000
    dbObj.cavitationSlope_ktsperft=0.005980
    dbObj.cavitationSL_dB=157.020065
    dbObj.snorkelingSL_dB=151.020065
    dbObj.BuildSLTable()
    return dbObj