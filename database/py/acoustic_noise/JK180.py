import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK180'
    dbObj.xSpeed_kts=[0.000000,4.698000,16.443001,23.490000]
    dbObj.ySL_dB=[85.849998,89.658188,116.315475,123.931847]
    dbObj.speedMinNL_kts=9.170000
    dbObj.NL_min=47.860001
    dbObj.speedMaxNL_kts=23.490000
    dbObj.NL_max=91.800003
    dbObj.cavitationOffset_kts=13.100000
    dbObj.cavitationSlope_ktsperft=0.011340
    dbObj.cavitationSL_dB=141.931854
    dbObj.snorkelingSL_dB=135.931854
    dbObj.BuildSLTable()
    return dbObj