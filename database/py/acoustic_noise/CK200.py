import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK200'
    dbObj.xSpeed_kts=[0.000000,5.180000,18.129999,25.900000]
    dbObj.ySL_dB=[87.779999,92.172035,122.916298,131.700363]
    dbObj.speedMinNL_kts=8.190000
    dbObj.NL_min=48.000000
    dbObj.speedMaxNL_kts=25.900000
    dbObj.NL_max=90.500000
    dbObj.cavitationOffset_kts=11.700000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=149.700363
    dbObj.snorkelingSL_dB=143.700363
    dbObj.BuildSLTable()
    return dbObj