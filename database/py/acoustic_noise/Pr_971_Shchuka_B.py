import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 971 Shchuka-B'
    dbObj.xSpeed_kts=[0.000000,10.500000,28.000000,35.000000]
    dbObj.ySL_dB=[89.900002,97.430000,112.000000,132.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=51.500000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=101.500000
    dbObj.cavitationOffset_kts=11.120000
    dbObj.cavitationSlope_ktsperft=0.024000
    dbObj.cavitationSL_dB=164.199997
    dbObj.snorkelingSL_dB=144.000000
    dbObj.BuildSLTable()
    return dbObj