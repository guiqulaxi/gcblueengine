import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK165'
    dbObj.xSpeed_kts=[0.000000,3.570000,12.495000,17.850000]
    dbObj.ySL_dB=[95.620003,100.932159,138.117279,148.741592]
    dbObj.speedMinNL_kts=5.985000
    dbObj.NL_min=51.500000
    dbObj.speedMaxNL_kts=17.850000
    dbObj.NL_max=104.500000
    dbObj.cavitationOffset_kts=8.550000
    dbObj.cavitationSlope_ktsperft=0.003500
    dbObj.cavitationSL_dB=166.741592
    dbObj.snorkelingSL_dB=160.741592
    dbObj.BuildSLTable()
    return dbObj