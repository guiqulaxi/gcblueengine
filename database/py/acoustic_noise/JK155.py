import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK155'
    dbObj.xSpeed_kts=[0.000000,3.628000,12.698000,18.139999]
    dbObj.ySL_dB=[93.099998,97.107124,125.157005,133.171265]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=50.959999
    dbObj.speedMaxNL_kts=18.139999
    dbObj.NL_max=97.800003
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.008240
    dbObj.cavitationSL_dB=151.171265
    dbObj.snorkelingSL_dB=145.171265
    dbObj.BuildSLTable()
    return dbObj