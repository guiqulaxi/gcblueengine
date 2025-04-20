import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 636'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[90.599998,98.610001,114.300003,122.599998]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=48.040001
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=98.040001
    dbObj.cavitationOffset_kts=11.820000
    dbObj.cavitationSlope_ktsperft=0.025000
    dbObj.cavitationSL_dB=162.300003
    dbObj.snorkelingSL_dB=134.600006
    dbObj.BuildSLTable()
    return dbObj