import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN190'
    dbObj.xSpeed_kts=[0.000000,7.680000,26.879999,38.400002]
    dbObj.ySL_dB=[86.300003,92.582329,136.558640,149.123306]
    dbObj.speedMinNL_kts=8.260000
    dbObj.NL_min=46.709999
    dbObj.speedMaxNL_kts=38.400002
    dbObj.NL_max=91.949997
    dbObj.cavitationOffset_kts=11.800000
    dbObj.cavitationSlope_ktsperft=0.009410
    dbObj.cavitationSL_dB=167.123306
    dbObj.snorkelingSL_dB=161.123306
    dbObj.BuildSLTable()
    return dbObj