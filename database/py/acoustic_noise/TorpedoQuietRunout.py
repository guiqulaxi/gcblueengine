import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='TorpedoQuietRunout'
    dbObj.xSpeed_kts=[0.000000,35.000000,50.000000,99.000000]
    dbObj.ySL_dB=[85.000000,100.000000,135.000000,135.000000]
    dbObj.speedMinNL_kts=20.000000
    dbObj.NL_min=70.000000
    dbObj.speedMaxNL_kts=50.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=99.000000
    dbObj.cavitationSlope_ktsperft=0.050000
    dbObj.cavitationSL_dB=100.000000
    dbObj.snorkelingSL_dB=100.000000
    dbObj.BuildSLTable()
    return dbObj