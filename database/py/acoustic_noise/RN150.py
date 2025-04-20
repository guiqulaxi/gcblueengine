import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN150'
    dbObj.xSpeed_kts=[0.000000,5.760000,20.160000,28.799999]
    dbObj.ySL_dB=[102.199997,110.494400,168.555206,185.143997]
    dbObj.speedMinNL_kts=5.915000
    dbObj.NL_min=51.700001
    dbObj.speedMaxNL_kts=28.799999
    dbObj.NL_max=110.199997
    dbObj.cavitationOffset_kts=8.450000
    dbObj.cavitationSlope_ktsperft=0.003325
    dbObj.cavitationSL_dB=203.143997
    dbObj.snorkelingSL_dB=197.143997
    dbObj.BuildSLTable()
    return dbObj