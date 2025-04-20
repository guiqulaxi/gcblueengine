import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Noisemaker 140'
    dbObj.xSpeed_kts=[0.000000,5.000000,20.000000,30.000000]
    dbObj.ySL_dB=[140.000000,140.000000,140.000000,140.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=60.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=60.000000
    dbObj.cavitationOffset_kts=0.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=140.000000
    dbObj.snorkelingSL_dB=140.000000
    dbObj.BuildSLTable()
    return dbObj