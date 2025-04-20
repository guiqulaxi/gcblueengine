import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN190'
    dbObj.xSpeed_kts=[0.000000,7.680000,26.879999,38.400002]
    dbObj.ySL_dB=[84.699997,90.139297,128.214386,139.092987]
    dbObj.speedMinNL_kts=10.220000
    dbObj.NL_min=46.799999
    dbObj.speedMaxNL_kts=38.400002
    dbObj.NL_max=92.400002
    dbObj.cavitationOffset_kts=14.600000
    dbObj.cavitationSlope_ktsperft=0.010950
    dbObj.cavitationSL_dB=157.092987
    dbObj.snorkelingSL_dB=151.092987
    dbObj.BuildSLTable()
    return dbObj