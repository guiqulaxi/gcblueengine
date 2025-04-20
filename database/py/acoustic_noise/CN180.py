import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN180'
    dbObj.xSpeed_kts=[0.000000,5.980000,20.930000,29.900000]
    dbObj.ySL_dB=[93.300003,101.702042,160.516312,177.320389]
    dbObj.speedMinNL_kts=6.930000
    dbObj.NL_min=50.000000
    dbObj.speedMaxNL_kts=29.900000
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=9.900000
    dbObj.cavitationSlope_ktsperft=0.005000
    dbObj.cavitationSL_dB=195.320389
    dbObj.snorkelingSL_dB=189.320389
    dbObj.BuildSLTable()
    return dbObj