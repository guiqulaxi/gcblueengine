import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK170'
    dbObj.xSpeed_kts=[0.000000,3.760000,13.160000,18.799999]
    dbObj.ySL_dB=[89.199997,93.801788,126.014275,135.217850]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=49.150002
    dbObj.speedMaxNL_kts=18.799999
    dbObj.NL_max=94.300003
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.007450
    dbObj.cavitationSL_dB=153.217850
    dbObj.snorkelingSL_dB=147.217850
    dbObj.BuildSLTable()
    return dbObj