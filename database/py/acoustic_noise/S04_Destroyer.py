import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S04.Destroyer'
    dbObj.xSpeed_kts=[5.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[106.500000,110.680000,123.220001,127.400002]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=53.500000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=93.500000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj