import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK190'
    dbObj.xSpeed_kts=[0.000000,4.708000,16.478001,23.540001]
    dbObj.ySL_dB=[82.849998,86.885818,115.136566,123.208206]
    dbObj.speedMinNL_kts=9.905000
    dbObj.NL_min=46.619999
    dbObj.speedMaxNL_kts=23.540001
    dbObj.NL_max=88.949997
    dbObj.cavitationOffset_kts=14.150000
    dbObj.cavitationSlope_ktsperft=0.013120
    dbObj.cavitationSL_dB=141.208206
    dbObj.snorkelingSL_dB=135.208206
    dbObj.BuildSLTable()
    return dbObj