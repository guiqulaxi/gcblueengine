import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK185'
    dbObj.xSpeed_kts=[0.000000,4.496000,15.736000,22.480000]
    dbObj.ySL_dB=[84.199997,88.308838,117.070694,125.288361]
    dbObj.speedMinNL_kts=9.660000
    dbObj.NL_min=47.240002
    dbObj.speedMaxNL_kts=22.480000
    dbObj.NL_max=90.199997
    dbObj.cavitationOffset_kts=13.800000
    dbObj.cavitationSlope_ktsperft=0.012440
    dbObj.cavitationSL_dB=143.288361
    dbObj.snorkelingSL_dB=137.288361
    dbObj.BuildSLTable()
    return dbObj