import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Torpedo2'
    dbObj.xSpeed_kts=[0.000000,5.000000,10.000000,50.000000]
    dbObj.ySL_dB=[135.000000,135.000000,137.000000,157.000000]
    dbObj.speedMinNL_kts=20.000000
    dbObj.NL_min=75.000000
    dbObj.speedMaxNL_kts=50.000000
    dbObj.NL_max=95.000000
    dbObj.cavitationOffset_kts=99.000000
    dbObj.cavitationSlope_ktsperft=0.050000
    dbObj.cavitationSL_dB=105.000000
    dbObj.snorkelingSL_dB=105.000000
    dbObj.BuildSLTable()
    return dbObj