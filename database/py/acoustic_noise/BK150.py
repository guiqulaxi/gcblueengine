import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK150'
    dbObj.xSpeed_kts=[0.000000,3.014000,10.549000,15.070000]
    dbObj.ySL_dB=[93.680000,98.071396,128.811188,137.593979]
    dbObj.speedMinNL_kts=7.910000
    dbObj.NL_min=51.580002
    dbObj.speedMaxNL_kts=15.070000
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=11.300000
    dbObj.cavitationSlope_ktsperft=0.007620
    dbObj.cavitationSL_dB=155.593979
    dbObj.snorkelingSL_dB=149.593979
    dbObj.BuildSLTable()
    return dbObj