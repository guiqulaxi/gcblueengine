import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Harushio'
    dbObj.xSpeed_kts=[0.000000,6.000000,16.000000,20.000000]
    dbObj.ySL_dB=[90.900002,99.209999,115.599998,123.800003]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=46.500000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=96.500000
    dbObj.cavitationOffset_kts=13.540000
    dbObj.cavitationSlope_ktsperft=0.026000
    dbObj.cavitationSL_dB=162.500000
    dbObj.snorkelingSL_dB=135.800003
    dbObj.BuildSLTable()
    return dbObj