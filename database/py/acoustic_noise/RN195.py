import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN195'
    dbObj.xSpeed_kts=[0.000000,7.920000,27.719999,39.599998]
    dbObj.ySL_dB=[86.000000,91.198746,127.589981,137.987473]
    dbObj.speedMinNL_kts=8.750000
    dbObj.NL_min=47.200001
    dbObj.speedMaxNL_kts=39.599998
    dbObj.NL_max=92.199997
    dbObj.cavitationOffset_kts=12.500000
    dbObj.cavitationSlope_ktsperft=0.009175
    dbObj.cavitationSL_dB=155.987473
    dbObj.snorkelingSL_dB=149.987473
    dbObj.BuildSLTable()
    return dbObj