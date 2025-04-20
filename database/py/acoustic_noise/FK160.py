import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK160'
    dbObj.xSpeed_kts=[0.000000,3.336000,11.676000,16.680000]
    dbObj.ySL_dB=[91.919998,96.521111,128.728882,137.931107]
    dbObj.speedMinNL_kts=7.420000
    dbObj.NL_min=50.369999
    dbObj.speedMaxNL_kts=16.680000
    dbObj.NL_max=96.660004
    dbObj.cavitationOffset_kts=10.600000
    dbObj.cavitationSlope_ktsperft=0.006470
    dbObj.cavitationSL_dB=155.931107
    dbObj.snorkelingSL_dB=149.931107
    dbObj.BuildSLTable()
    return dbObj