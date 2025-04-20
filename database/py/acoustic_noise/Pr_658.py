import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 658'
    dbObj.xSpeed_kts=[0.000000,7.800000,20.799999,26.000000]
    dbObj.ySL_dB=[99.500000,120.769997,167.399994,172.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=57.000000
    dbObj.speedMaxNL_kts=26.000000
    dbObj.NL_max=104.000000
    dbObj.cavitationOffset_kts=11.170000
    dbObj.cavitationSlope_ktsperft=0.016000
    dbObj.cavitationSL_dB=177.800003
    dbObj.snorkelingSL_dB=184.000000
    dbObj.BuildSLTable()
    return dbObj