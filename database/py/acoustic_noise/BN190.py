import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN190'
    dbObj.xSpeed_kts=[0.000000,7.860000,27.510000,39.299999]
    dbObj.ySL_dB=[84.699997,90.231125,128.949005,140.011261]
    dbObj.speedMinNL_kts=9.590000
    dbObj.NL_min=46.619999
    dbObj.speedMaxNL_kts=39.299999
    dbObj.NL_max=91.500000
    dbObj.cavitationOffset_kts=13.700000
    dbObj.cavitationSlope_ktsperft=0.011580
    dbObj.cavitationSL_dB=158.011261
    dbObj.snorkelingSL_dB=152.011261
    dbObj.BuildSLTable()
    return dbObj