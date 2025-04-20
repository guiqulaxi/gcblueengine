import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK215'
    dbObj.xSpeed_kts=[0.000000,6.224000,21.784000,31.120001]
    dbObj.ySL_dB=[75.440002,78.810486,102.403870,109.144836]
    dbObj.speedMinNL_kts=12.110000
    dbObj.NL_min=43.099998
    dbObj.speedMaxNL_kts=31.120001
    dbObj.NL_max=82.000000
    dbObj.cavitationOffset_kts=17.299999
    dbObj.cavitationSlope_ktsperft=0.015960
    dbObj.cavitationSL_dB=127.144836
    dbObj.snorkelingSL_dB=121.144836
    dbObj.BuildSLTable()
    return dbObj